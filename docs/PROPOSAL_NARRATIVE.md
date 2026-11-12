# Project VERDANT: Technical Proposal & Narrative Specification

> **Track:** Track 3 – Safeguarding Green Infrastructure in Skopje, North Macedonia  
> **Challenge:** IEEE Humanitarian Technologies & UNDP GenAI for Good (Cities Edition)  
> **Target Scope:** Phase 1 Prototype (USD 10,000) with Staged Pilot Blueprint (USD 30,000)  
> **Status:** Production Engineering Specification  

---

## 1. Project Framing & Headline Principle

### 1.1 The Operational Problem
The City of Skopje (*Град Скопје*) faces severe air quality challenges, where winter particulate pollution ($\text{PM}_{2.5}$) frequently exceeds international health thresholds due to valley basin temperature inversions. Urban tree canopy provides essential microclimate cooling and particulate bio-filtration. While municipal regulations mandate that any permitted tree removal must be balanced by compensatory replanting (typically 3 to 5 saplings per mature tree felled), thousands of paper felling permits remain stored in municipal archives without digital integration into the city's *Zelen Katastar* (Green Cadastre).

Because these records exist as historical paper files occluded by circular administrative seals, municipal arborists and environmental inspectors cannot systematically verify whether developers have fulfilled their statutory replanting obligations.

### 1.2 The Headline Principle: "The Tool Proposes, Staff Decide"
Project VERDANT does not grant autonomous write access to municipal databases. The system functions as an automated document intelligence assistant that converts unstructured permit files into structured, reviewable *candidate diffs*.

Every proposed modification to the Green Cadastre is presented to municipal staff with:
1. The exact source document page image.
2. The highlighted bounding box coordinates `[x1, y1, x2, y2]` from which the data was extracted.
3. An uncertainty metric derived from distribution-free conformal calibration.
4. A symmetric one-click interface: approving takes one click; rejecting takes one click.

---

## 2. Walkthrough: An End-to-End Worked Example

To demonstrate concrete execution, consider a typical permit scenario processed through VERDANT:

```
[Input Document: Archival Permit Scan]
  │
  ├─ Page 1: Administrative header, reference "14-3821/2", date "14.11.2018"
  ├─ Body: Authorizes removal of 2 Platanus orientalis (Јавор) on parcel "KP 1408/2", KO Centar
  ├─ Condition: Developer must plant 8 replacement saplings (Acer pseudoplatanus)
  └─ Seal: Circular municipal rubber stamp overlapping parcel text
  │
  ▼
[Optical Extraction & Reading (Non-Destructive Multi-Channel)]
  ├─ Dual-stream OCR preserves raw RGB text alongside isolated stamp channel masks
  ├─ Bounding Box Coordinates: [x1: 45, y1: 110, x2: 380, y2: 145]
  │
  ▼
[Entity Extraction & Deterministic Validation]
  ├─ Species normalization: "Јавор" -> Platanus orientalis (Taxonomic ID verified)
  ├─ Count validation: 2 trees felled; replanting obligation extracted as 8 saplings (Ratio: 4:1, PASS)
  ├─ AREC Cadastral Check: Query AREC GIS layer for "КО Centar, KP 1408/2" -> Parcel exists (PASS)
  ├─ Spatial Consistency Check: Street text "Bul. Partizanski Odredi" matches parcel boundary (PASS)
  │
  ▼
[Staff Review Console (City Enclave)]
  ├─ UI displays proposed diff against Green Cadastre parcel layer
  ├─ Source image displayed with green bounding box around extracted text
  ├─ Conformal confidence: 0.96 (Above automated presentation threshold)
  ├─ Municipal Officer clicks [APPROVE]
  │
  ▼
[Cadastre Mutation & Replanting Ledger]
  ├─ Green Cadastre updated: 2 trees flagged as legally removed with archive link
  ├─ Public Compensatory Ledger creates tracking obligation: 8 saplings due by 14.11.2019
```

---

## 3. System Architecture: The Two-Zone Model

To satisfy both municipal data sovereignty and open-source reproducibility, the system enforces a strict boundary between two operational zones:

### 3.1 Zone 1: The City Enclave (Municipal Sovereign Infrastructure)
- **Deployment:** On-premise server or local municipal workstation inside the City of Skopje / PE "Parks and Greenery" network.
- **Privacy & Data Security:** Ingests raw document scans and digital PDFs. Citizen national identification numbers (*ЕМБГ*) and unredacted names remain permanently within this enclave.
- **Components:**
  - *Intake & Provenance:* SHA-256 cryptographic hashing of incoming files.
  - *Optical Ingestion:* Local Cyrillic OCR (PaddleOCR / Tesseract 5) retaining word-level spatial boxes.
  - *Linguistic Processing:* South Slavic CLASSLA pipeline for morphological analysis and entity extraction.
  - *Validation Engine:* Automated SQL queries checking parcel existence against Agency for Real Estate Cadastre (**AREC**) records.
  - *Staff Review Console:* Lightweight web interface for one-click diff approvals.
  - *Enclave Q&A Engine:* Natural language querying with parameterised SQL and direct document citations.

### 3.2 Zone 2: The Open Zone (Public Repository & Community Suite)
- **Deployment:** Public GitHub repository (`atharveeee-netizen/verdant-skopje-proposal`).
- **Components:**
  - Complete Apache-2.0 licensed codebase, Docker containers, and database migration scripts.
  - *Synthetic Permit Engine:* Procedural generation system simulating historical Cyrillic typefaces, paper degradation, and municipal stamp overlays.
  - *De-Identified Benchmark:* Curated gold-standard evaluation dataset published with municipal consent for academic reproducibility.

---

## 4. Technical Methodology & Rigor

### 4.1 Normalized Relational Data Model
The system enforces a clean third-normal-form (3NF) relational and spatial schema in PostgreSQL 16 + PostGIS:

1. `permits`: Immutable archive reference, issue date, cadastral municipality (КО), document hash.
2. `permit_lines`: Specific felling authorizations, species text, tree count, source page, bounding box.
3. `parcel_references`: AREC cadastral parcel identifier, validation status, MGI Balkans Zone 7 geometry.
4. `proposed_cadastre_trees`: Candidate mutations awaiting staff adjudication (pending, approved, rejected).
5. `replanting_obligations`: Mandatory replacement sapling count, species, deadline, compliance state.
6. `verification_events`: Ground inspection logs, planting confirmation, photos, recorded via QField/ODK.

### 4.2 Calibrated Risk Control vs. "0% Hallucination"
Rather than claiming unscientific zero-error performance, VERDANT employs **Distribution-Free Conformal Risk Control**:
- **Marginal Coverage:** Guarantees $\mathbb{P}(Y \in \mathcal{C}(X)) \ge 1 - \alpha$ at significance $\alpha = 0.05$.
- **Finite Sample Accounting:** Acknowledges binomial sampling standard error ($\pm 1.54\%$ on $n = 200$).
- **Era Stratification:** Separates pre-1991 handwritten Yugoslav cursive from post-2010 digital records to prevent non-exchangeability errors.
- **Valid-but-Wrong Parcel Detection:** Catches OCR misreads that form valid parcel numbers by cross-checking extracted street names against spatial parcel polygon boundaries.

### 4.3 Throughput & Operational Bottleneck Analysis
- **GPU Inference Throughput:** At 3.8 seconds per permit on a single modern GPU, 3,000 permits require approximately **3.17 GPU-hours**.
- **Real Operational Bottlenecks:**
  - *Scanning Time:* 12,000 pages at 200 pages/hour requires **60 operator-hours** (eliminated if the city already holds digital PDFs).
  - *Staff Review Time:* Reviewing flagged low-confidence cases (estimated at 20% = 600 cases) at 45 seconds each requires **7.5 staff-hours**.

---

## 5. Staged Budget & Financial Plan

The budget is structured into two separate phases:

### 5.1 Phase 1: Prototype Development (USD 10,000)
The prototype phase builds and validates the core software engine, synthetic data generator, and evaluation benchmark:

| Category | Description | Amount (USD) |
|:---|:---|---:|
| **Compute & Testbeds** | GPU workstation compute instances, local model fine-tuning environments | \$3,200 |
| **Annotation & Linguistics** | Double-annotation of 200 Macedonian permit benchmarks by language specialists | \$2,800 |
| **Enclave & Security** | On-premise Docker container testing, PII masking verification, penetration check | \$2,200 |
| **Documentation & Packaging** | Bilingual user guides, open-source documentation, CI/CD pipelines | \$1,800 |
| **Total Prototype Funding** | **Direct Prototype Implementation Allocation** | **\$10,000** |

### 5.2 Phase 2: Pilot Deployment Blueprint (USD 30,000 - Staged Extension)
If selected for the municipal pilot through December 2027, funding is dedicated to on-site integration:
- **Municipal Integration & Enclave Staging:** Deploying the intake station within the municipal archives office.
- **Staff Workflow Training:** Conducting hands-on verification workshops for municipal arborists and administrative officers.
- **Mobile QField Deployment:** Configuring open-source QField mobile GIS profiles on existing municipal tablets.
- **Sustained System Maintenance:** Software updates, model re-calibration, and administrative support through 2027.

---

## 6. Project Team & Governance

### 6.1 Team Composition
- **Atharve Dahima** (Project Lead & Systems Architect): Student Member, IEEE. Focus on systems architecture, containerization, and PostGIS database integration.
- **Srajan Mishra** (Co-Lead & Document Intelligence Engineer): Student Member, IEEE. Focus on Cyrillic OCR fine-tuning, multi-channel optical processing, and conformal risk calibration.
- **Dr. Vishal Sharma** (Faculty Mentor): Department of Electronics and Communication Engineering, Malaviya National Institute of Technology Jaipur (MNIT Jaipur). Academic supervision, methodology verification, and institutional administration.

### 6.2 Collaborative Partnership Strategy
- **Engineering Hub:** Core algorithms, synthetic generation, and open-source tooling developed by the engineering student team at MNIT Jaipur.
- **Municipal Liaison:** Sector for Environmental Protection, City of Skopje, and Public Enterprise "Parks and Greenery" (*ЈП Паркови и Зеленило*), to be formally onboarded through official challenge matchmaking and the November 19 Q&A session.
