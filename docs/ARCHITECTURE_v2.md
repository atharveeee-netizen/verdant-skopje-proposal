# Project VERDANT: Architecture Specification v2

> **System Architecture, Data Model, and Operational Blueprint**  
> **Challenge:** IEEE Humanitarian Technologies & UNDP *GenAI for Good Challenge: Cities Edition*  
> **Track:** Track 3 – Safeguarding Green Infrastructure in Skopje, North Macedonia  
> **Version:** 2.0 (Engineering Baseline)  
> **Date:** November 2026  

---

## 1. Executive Summary & Design Principles

Project VERDANT modernizes the digital green infrastructure registry (*Зелен Катастар*) for the City of Skopje by reconciling historical and active tree felling permits with cadastral parcels and compensatory replanting obligations.

The design is governed by five operational rules:

1. **Staff Authority:** Nothing enters the Cadastre without explicit municipal staff approval. Every AI output is framed as a structured *diff* accompanied by source page coordinates, highlighted text spans, and confidence scores. One click approves; one click rejects.
2. **Two-Zone Topology:** The system separates an offline-capable, PII-isolated **City Enclave** from an open-source **Open Zone**. Real citizen identification numbers (*ЕМБГ*) and unredacted archives remain strictly within the municipal enclave. The public repository contains code, Dockerfiles, synthetic permit generators, and a small, de-identified benchmark dataset published with municipal consent.
3. **Calibrated Abstention:** Claims of "0.0% hallucination" are replaced with formal statistical risk control (Conformal Prediction and Learn-then-Test). Extractions must pass deterministic structural and cadastral integrity checks; ambiguous or low-confidence fields are routed to a human review queue with mathematically bounded error rates.
4. **Normalized Relational Data Model:** A single, disambiguated schema connects permits to individual tree felling lines, parcel references, proposed cadastre updates, compensatory replanting mandates, and field verification events.
5. **Unified Core Engine:** The exact same SQL/PostGIS extraction, validation, and citation store powers both the automated permit ingestion pipeline and the interactive Q&A assistant tested in Phase 1 (Zindi benchmark).

```
+---------------------------------------------------------------------------------------------------+
|  CITY ENCLAVE (Offline-capable, on-premise municipal boundary, PII stays here)                    |
|                                                                                                   |
|  +------------+       +------------+       +------------+       +------------+                    |
|  |   Intake   | ----> |    Read    | ----> |   Extract  | ----> |   Verify   |                    |
|  | Raw files, |       |   OCR +    |       |  Fields +  |       | Checks vs  |                    |
|  |   hashed   |       | page boxes |       |  evidence  |       |  cadastre  |                    |
|  +------------+       +------------+       +------------+       +------------+                    |
|                                                                        |                          |
|                                                                        v                          |
|  +--------------------+                           +--------------------------------------------+  |
|  |   Green Cadastre   | <------------------------ |                Staff Review                |  |
|  |  Approved changes  |   (One-click approve/     |            (Inspect diff, page             |  |
|  |   written here     |        or reject)         |          span, confidence metric)          |  |
|  +--------------------+                           +--------------------------------------------+  |
|                                                                        |                          |
|  ^---------------- staff decisions feed calibration & evaluation <-----+                          |
|                                                                                                   |
|  +---------------------------------------------------------------------------------------------+  |
|  |                                          Q&A Layer                                          |  |
|  |                  (Cited answers, NL-to-SQL, PostGIS tools, can abstain)                     |  |
|  +---------------------------------------------------------------------------------------------+  |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  | One-way, strictly redacted / synthetic
                                                  v
+---------------------------------------------------------------------------------------------------+
|  OPEN ZONE (Public GitHub Repository)                                                             |
|  - Permissive open-source engine (Apache-2.0)                                                     |
|  - Synthetic Macedonian permit generator (procedural text, fonts, stamp overlays)                |
|  - Curated, de-identified evaluation benchmark (released with City consent)                       |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Two-Zone System Topology

### 2.1 Zone 1: The City Enclave (Municipal Sovereign Boundary)
- **Deployment Target:** On-premise server or sovereign municipal infrastructure inside the City of Skopje / PE "Parks and Greenery" network.
- **Data Residency:** All raw paper scans, digitised PDF permits, unredacted names, citizen national ID numbers (*ЕМБГ* - *Единствен матичен број на граѓанинот*), and internal municipal notes remain inside this enclave.
- **Network Profile:** Completely functional offline without external cloud dependencies. No raw document text or PII ever traverses foreign APIs.
- **Enclave Responsibilities:**
  1. **Intake:** Ingests raw document scans or municipal PDFs, computes SHA-256 hashes for tamper-evident provenance, and archives original immutable files.
  2. **Read:** Runs local Cyrillic-capable OCR (PaddleOCR / Tesseract 5 fine-tuned on South Slavic typography), preserving word-level and line-level bounding box coordinates `[x1, y1, x2, y2]`.
  3. **Extract:** Parses entities using the South Slavic **CLASSLA** linguistic pipeline (tokenization, lemmatization, morphological tagging) to extract dates, species, tree quantities, parcel identifiers, and replanting conditions.
  4. **Verify:** Validates extracted parcel IDs against the Agency for Real Estate Cadastre (**AREC** / *AKN*) registry, checks arithmetic consistency (e.g. tree counts vs. species breakdown), and validates statutory replanting ratios.
  5. **Staff Review Console:** A lightweight web UI presenting proposed mutations as side-by-side diffs with source document snippets. Staff can approve, reject, or edit with symmetric operational friction (one click).
  6. **Green Cadastre Synchronization:** Writes approved records into the PostgreSQL/PostGIS *Zelen Katastar* database.
  7. **Q&A Layer:** Executes natural language queries using parameterised SQL and PostGIS tools, accompanied by mandatory citation links back to archived document IDs.

### 2.2 Zone 2: The Open Zone (Public Repository & Benchmark Suite)
- **Deployment Target:** Public GitHub repository (`atharveeee-netizen/verdant-skopje-proposal`).
- **Contents:**
  1. Complete Apache-2.0 licensed Python, PostGIS, and React application code.
  2. **Synthetic Data Engine:** Procedural generation pipeline that outputs realistic synthetic Macedonian felling permits with varying Cyrillic typefaces, simulated typewriter degradation, historical paper textures, and synthetic circular municipal stamp occlusions.
  3. **Evaluation Benchmark:** A small, curated, fully anonymised and de-identified real permit sample released with the explicit written consent of the City of Skopje for model benchmarking and reproducibility.
  4. Automated unit, integration, and conformal calibration test suites.

---

## 3. The Five Operational Rules

### Rule 1: Nothing Reaches the Cadastre Without a Staff Decision
- The AI pipeline is strictly an assistant that proposes structured candidate diffs.
- The review interface displays:
  - The source document page snippet showing the exact text region.
  - The extracted value with its bounding box highlighted.
  - The target Cadastre entity (e.g., updating parcel `KP 1408/2`, felling 3 mature *Platanus orientalis*, flagging 9 compensatory saplings).
  - The conformal prediction set and validation status.
- **Symmetric Friction:** Approving takes one click; rejecting takes one click. Rejection prompts an optional one-click category tag (e.g., `Incorrect Parcel`, `Unclear Text`, `Not a Felling Permit`) which feeds the calibration loop.

### Rule 2: Two Zones, Not "100% Air-Gapped"
- The naive claim of "100% air-gapped" contradicts requirements for open-source reproducibility, public transparency portals, and remote sensor corrections.
- The two-zone model cleanly delineates boundaries:
  - Private data, real citizen identifiers, and official Cadastre write operations live solely within the **City Enclave**.
  - Open-source algorithms, reproducible benchmarks, synthetic evaluation suites, and public analytical code live in the **Open Zone**.

### Rule 3: Calibrated Abstention Instead of "0.0% Hallucination"
- In production machine learning, zero hallucination is an impossible claim. Conformal prediction provides distribution-free marginal coverage guarantees:
  $$\mathbb{P}\left(Y_{n+1} \in \mathcal{C}(X_{n+1})\right) \ge 1 - \alpha$$
- **Finite Sample Realism:** With a calibration set of $n = 200$ permits at significance $\alpha = 0.05$, the empirical coverage has a binomial sampling standard error:
  $$\sigma = \sqrt{\frac{\alpha(1-\alpha)}{n}} = \sqrt{\frac{0.05 \times 0.95}{200}} \approx 1.54\%$$
  The realised coverage naturally fluctuates between $93.5\%$ and $96.5\%$.
- **Stratified Calibration:** Historical handwritten Yugoslav-era permits (1970s–1980s) and modern laser-printed permits (2010s–2020s) violate exchangeability. Calibration must be stratified across document eras and field categories:
  - Era 1: Pre-1991 (Cyrillic cursive / manual typewriter).
  - Era 2: 1991–2010 (Standard typewriter / early dot-matrix).
  - Era 3: 2011–Present (Digital word-processed / scanned PDF).
- **Multi-Tier Deterministic Validation:**
  - *Structural Check:* $\sum \text{species\_counts} = \text{total\_trees\_authorized}$.
  - *Statutory Ratio Check:* $\text{replanting\_saplings} \ge k \times \text{trees\_felled}$ (where $k \in [3, 5]$ as mandated by municipal decree).
  - *Cadastral Referential Check:* Foreign key query against AREC parcel polygons.
- **Conformal Risk Control (Learn-then-Test):** Formally bounds extraction risk:
  $$\text{Target: } \le 2.0\% \text{ error among auto-proposed fields at a } 15\% \text{ human review rate.}$$
- **Valid-but-Wrong Parcel Anomaly:** If a permit cites parcel `1408/1` but OCR misreads `1408/7`, and `1408/7` exists in the Cadastre, deterministic checks will pass. The system implements a spatial context sanity check: flag parcel proposals whose street address text does not spatially intersect the municipal cadastre boundary for that neighborhood.

### Rule 4: Explicit, Disambiguated Data Model
The previous draft conflated permits, trees, and saplings into single integers. The system implements a strict, 3NF relational schema:

```
[Permit] 1 ──── * [PermitLine] 1 ──── 0..1 [ProposedCadastreTree]
   │
   ├───── 1 ──── * [ParcelReference]
   │
   └───── 1 ──── * [ReplantingObligation] 1 ──── * [VerificationEvent]
```

### Rule 5: Unified Engine for Extraction and Q&A
- The Q&A system tested in Phase 1 (Zindi benchmark) is not a standalone chatbot; it is a direct query interface over the normalized PostgreSQL/PostGIS database.
- It employs parameterised NL-to-SQL generation constrained to read-only views, PostGIS spatial predicates (`ST_Contains`, `ST_DWithin`, `ST_Intersects`), and explicit citation generators that point directly to the underlying `permit_id`, archive reference number, and source page span.
- When query ambiguity exceeds threshold or retrieval support is missing, the engine explicitly abstains: `"Nedovolno podatoci vo arhivata" / "Insufficient evidence in records to verify."`

---

## 4. Normalized Data Model (PostgreSQL & PostGIS)

```sql
-- Core Permits Table
CREATE TABLE permits (
    permit_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    archive_reference VARCHAR(64) NOT NULL UNIQUE, -- e.g., '14-3821/2'
    issuing_authority VARCHAR(128) NOT NULL DEFAULT 'City of Skopje - Sector for Environmental Protection',
    issue_date DATE NOT NULL,
    cadastral_municipality VARCHAR(64) NOT NULL, -- e.g., 'Центар', 'Карпош'
    raw_document_hash CHAR(64) NOT NULL,         -- SHA-256 of original file
    document_era VARCHAR(16) NOT NULL,          -- 'pre_1991', '1991_2010', 'post_2010'
    intake_timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(32) NOT NULL DEFAULT 'ingested' -- 'ingested', 'extracted', 'verified', 'reviewed'
);

-- Itemized Felling Lines (One permit can authorize felling multiple distinct trees)
CREATE TABLE permit_lines (
    line_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    permit_id UUID NOT NULL REFERENCES permits(permit_id) ON DELETE CASCADE,
    species_raw VARCHAR(128) NOT NULL,           -- e.g., 'Platanus orientalis (Јавор)'
    species_standardized VARCHAR(128),          -- Botanical taxonomic name
    tree_count INTEGER NOT NULL CHECK (tree_count > 0),
    felling_reason VARCHAR(256),                -- Construction, sanitation, storm damage
    location_description TEXT,                   -- Street or frontage narrative
    evidence_page INTEGER NOT NULL,
    evidence_bbox JSONB NOT NULL,               -- [x1, y1, x2, y2] normalized coordinates
    extraction_confidence NUMERIC(4,3) NOT NULL  -- Conformal non-conformity / model score
);

-- Cadastral Parcel References
CREATE TABLE parcel_references (
    parcel_ref_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    permit_id UUID NOT NULL REFERENCES permits(permit_id) ON DELETE CASCADE,
    parcel_number VARCHAR(32) NOT NULL,         -- e.g., '1408/2'
    cadastral_municipality VARCHAR(64) NOT NULL,
    arec_status VARCHAR(32) NOT NULL,           -- 'valid_exact', 'subdivided', 'not_found'
    matched_parcel_id VARCHAR(64),              -- Official AREC identifier
    spatial_boundary GEOMETRY(Polygon, 31277)   -- MGI Balkans Zone 7 (EPSG:31277)
);

-- Proposed Cadastre Tree Updates (Diff Queue for Municipal Staff)
CREATE TABLE proposed_cadastre_trees (
    proposal_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    permit_line_id UUID NOT NULL REFERENCES permit_lines(line_id) ON DELETE CASCADE,
    parcel_ref_id UUID REFERENCES parcel_references(parcel_ref_id),
    action VARCHAR(32) NOT NULL,                -- 'remove_tree', 'flag_compensatory_planting'
    cadastre_tree_id VARCHAR(64),               -- Nullable if matching against existing GIS layer
    proposed_geometry GEOMETRY(Point, 31277),
    staff_decision VARCHAR(32) NOT NULL DEFAULT 'pending', -- 'pending', 'approved', 'rejected', 'modified'
    staff_reviewer_id VARCHAR(64),
    decision_timestamp TIMESTAMP WITH TIME ZONE,
    decision_notes TEXT
);

-- Compensatory Replanting Obligations
CREATE TABLE replanting_obligations (
    obligation_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    permit_id UUID NOT NULL REFERENCES permits(permit_id) ON DELETE CASCADE,
    required_sapling_count INTEGER NOT NULL CHECK (required_sapling_count >= 0),
    mandated_species VARCHAR(128),
    target_municipality VARCHAR(64) NOT NULL,
    compliance_deadline DATE,
    status VARCHAR(32) NOT NULL DEFAULT 'unfulfilled' -- 'unfulfilled', 'partially_fulfilled', 'fulfilled', 'defaulted'
);

-- Ground Verification Events
CREATE TABLE verification_events (
    event_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    obligation_id UUID NOT NULL REFERENCES replanting_obligations(obligation_id) ON DELETE CASCADE,
    verification_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    inspector_id VARCHAR(64) NOT NULL,
    verified_tree_count INTEGER NOT NULL,
    species_verified VARCHAR(128),
    location_point GEOMETRY(Point, 31277) NOT NULL,
    photo_evidence_hash CHAR(64),
    evidence_uri VARCHAR(512),
    verification_method VARCHAR(32) NOT NULL    -- 'municipal_nursery_log', 'qfield_audit', 'odk_submission'
);
```

---

## 5. Throughput & Bottleneck Sizing

Previous throughput estimates cited contradictory numbers (3.8 seconds per permit vs. 72 hours for 3,000 permits). We establish grounded capacity models:

### 5.1 Computational Inference Throughput
- Ingesting a 4-page PDF or 300 DPI scan through local PaddleOCR and CLASSLA on an NVIDIA RTX 4090 (24GB VRAM) or RTX 3080:
  $$\text{OCR + Entity Extraction Latency} \approx 3.8 \text{ s per permit}$$
- Pure computational processing time for 3,000 permits:
  $$\frac{3,000 \times 3.8\text{ s}}{3,600\text{ s/h}} = 3.17\text{ GPU-hours}$$
- Inference is **not** the operational bottleneck.

### 5.2 Real Operational Bottlenecks
1. **Document Intake (Physical Scanning):**
   - If permits are physically bound in paper archives:
     $$3,000 \text{ permits} \times 4 \text{ pages/permit} = 12,000 \text{ pages}$$
   - At a realistic flatbed/book-edge scan rate of 200 pages per hour:
     $$\text{Total Scanning Time} = \frac{12,000}{200} = 60 \text{ operator hours (approx. 8 full working shifts)}$$
   - *Contingency (Q&A Topic for Nov 19):* If the City of Skopje already holds digital PDFs from prior municipal archiving initiatives, scanning hardware is unnecessary and ingestion proceeds via automated file-drop watchers.
2. **Staff Review Queue:**
   - Assuming a conservative auto-proposal acceptance rate where $20\%$ of fields require human adjudication:
     $$3,000 \text{ permits} \times 0.20 = 600 \text{ flagged permits}$$
   - At an average review time of 45 seconds per flagged case:
     $$\text{Review Time} = \frac{600 \times 45\text{ s}}{3,600\text{ s/h}} = 7.5 \text{ staff hours}$$
   - This fits easily within standard municipal administrative workloads.

---

## 6. Grounded Field Strategy & Hardware Rationalization

The previous draft included unrealistic claims regarding field hardware:
1. **RTK GNSS Under Dense Canopy:** Sub-meter or $\pm 0.15\text{ m}$ accuracy cannot be maintained under wet deciduous leaf canopies; GNSS signals undergo severe multipath interference and cycle slips, dropping RTK receivers to "float" or single-point autonomous mode with errors of $0.5\text{ m to } 2.5\text{ m}$.
2. **Stump Inspection Fallacy:** Trees authorized for felling 5 to 10 years ago leave no stumps; urban building foundations, road expansions, and pavers completely remove or bury them.
3. **Audit Cycle Time:** A 60-second audit cannot realistically encompass locating a site, acquiring a stable satellite fix, measuring DBH, recording bark condition, taking geotagged photos, and affixing a physical tag. A realistic field survey takes 4 to 8 minutes per tree.

### 6.1 Deferred Field Strategy
- **Phase 1 Priority:** Focus 100% of engineering effort on the **Document Intelligence, Cadastral Reconciliation, and Q&A Engine**.
- **Field Auditing (Phase 2 / Pilot Handover):** Rather than writing custom Android software, field validation will leverage industry-standard open-source tools:
  - **QField** (QGIS mobile companion) or **ODK (Open Data Kit)** for standardized geospatial forms.
  - Standard municipal GNSS hardware already operated by PE "Parks and Greenery" crews.
- **Non-Destructive Optical Processing:** Raw scans are preserved immutably. Rather than applying destructive HSV filters that erase underlying strokes, the recognition pipeline feeds multi-channel inputs (raw RGB alongside extracted stamp isolation masks) to ensure no ink data is lost.

---

## 7. Administrative, Geographic & Legal Alignment

### 7.1 Cadastral Authority
- The official land authority is the **Agency for Real Estate Cadastre** (**AREC** / *Агенција за катастар на недвижности* - AKN), not the "State Geodetic Authority". All coordinate references use the national spatial reference system **MGI Balkans Zone 7** (EPSG:31277) with on-the-fly reprojection to WGS84 (EPSG:4326).

### 7.2 The 10 Municipalities of Skopje
The territory of the City of Skopje (*Град Скопје*) comprises exactly ten local self-government municipalities:
1. **Aerodrom** (*Аеродром*)
2. **Butel** (*Бутел*)
3. **Gazi Baba** (*Гази Баба*)
4. **Gjorče Petrov** (*Ѓорче Петров*)
5. **Karpoš** (*Карпош*)
6. **Kisela Voda** (*Кисела Вода*)
7. **Saraj** (*Сарај*)
8. **Centar** (*Центар*)
9. **Čair** (*Чаир*)
10. **Šuto Orizari** (*Шуто Оризари*)

*(Note: Vodno is a mountain and protected forest park managed under PE "Parks and Greenery", not a distinct municipality).*

### 7.3 Data Protection Framework
- North Macedonia's **Law on Personal Data Protection** (*Закон за заштита на личните податоци*, *Official Gazette No. 42/20*) transposes the European Union General Data Protection Regulation (EU GDPR).
- It establishes conditions for lawful processing and cross-border transfers rather than a blanket ban. Project VERDANT's enclave isolation is justified by administrative risk management, municipal IT security policies, and the strict requirement to safeguard citizen national identity numbers (*ЕМБГ*), rather than inaccurate legal claims.

### 7.4 Green Cadastre History
- The initial baseline for the *Zelen Katastar na Grad Skopje* was developed under the City of Skopje with UNDP and REC support within the **"Resilient Skopje"** project framework during **2020–2021** (registering over 65,000 public green objects). Official tree counts and access protocols are confirmed directly with municipal administrators.

---

## 8. Preparation for the November 19 Q&A Session

The following specific questions are prepared for the official challenge Q&A session:
1. **Data Format:** Does the City of Skopje already possess digital PDF scans of historical felling permits, or is physical scanning of paper registers strictly required?
2. **Cadastre Integration:** What API, database export (e.g., GeoPackage, PostGIS dump), or WFS/WMS endpoints exist for the current *Zelen Katastar*?
3. **Labelled Ground Truth:** Will UNDP or the City provide a set of anonymised gold-standard permit extractions to establish a public evaluation baseline for Track 3 participants?
4. **Benchmarking Criteria:** How will the Zindi Phase 1 evaluation score citations, partial field matches, and calibrated abstentions?
