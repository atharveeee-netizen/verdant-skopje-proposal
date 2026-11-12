# Project VERDANT: Automated Green Cadastre Modernization for Skopje

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Track](https://img.shields.io/badge/Challenge-IEEE%20HT%20%26%20UNDP%20GenAI%20for%20Good-green.svg)](https://www.ieee.org/)
[![Track Category](https://img.shields.io/badge/Track-Track%203%3A%20Safeguarding%20Green%20Infrastructure-success.svg)](https://www.undp.org/)
[![Architecture v2](https://img.shields.io/badge/Architecture-Two--Zone%20(v2.0)-darkgreen.svg)](docs/ARCHITECTURE_v2.md)
[![Document Length](https://img.shields.io/badge/Proposal-Strictly%208%20Pages%20XeLaTeX-black.svg)](verdant_proposal.pdf)
[![Budget](https://img.shields.io/badge/Budget-USD%2040%2C000%20(Direct%20Materials)-darkgreen.svg)](verdant_proposal.pdf)

> **Master IEEE Humanitarian Technologies & UNDP GenAI for Good (Cities Edition) Proposal**  
> **Track 3: Safeguarding Green Infrastructure in Skopje, North Macedonia**  
> *A sovereign document intelligence and cadastral reconciliation system for municipal green infrastructure protection and compensatory reforestation.*

---

## 1. Executive Summary

In Skopje, winter particulate pollution ($\text{PM}_{2.5}$) regularly exceeds the World Health Organization 24-hour limit by **5.5 to 11.2 times** ($82.4 \text{ to } 168.0\text{ }\mu\text{g/m}^3$), while the urban tree canopy has faced persistent contraction from commercial and infrastructure clearings. Although municipal regulations mandate compensatory replanting (typically 3 to 5 saplings per mature tree felled), thousands of archival felling permits sit trapped in municipal paper storage, occluded by circular purple rubber stamps and decoupled from the digital *Zelen Katastar* (Green Cadastre).

**Project VERDANT** delivers an end-to-end, two-zone system that reconciles archival tree felling permits with the municipal *Zelen Katastar* via calibrated document intelligence, deterministic validation against the Agency for Real Estate Cadastre (**AREC** / *AKN*), human-in-the-loop staff verification, and a unified Q&A retrieval engine.

---

## 2. Core Architecture: Two-Zone Model

To resolve the conflict between municipal data sovereignty and open-source reproducibility, VERDANT operates across two distinct zones:

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

### Zone 1: City Enclave (Offline-Capable, Municipal Sovereign Boundary)
- **Data Residency:** All raw paper scans, digitised PDF permits, unredacted names, citizen national ID numbers (*ЕМБГ*), and municipal notes remain strictly inside the municipal enclave.
- **Offline Reliability:** Zero external cloud dependencies. Ingestion, OCR, and database updates function reliably on-premise.
- **Workflow:**
  1. **Intake:** Ingests raw files, computes SHA-256 hashes for tamper-evident provenance, and archives original scans non-destructively.
  2. **Read:** Local Cyrillic OCR (PaddleOCR / Tesseract 5) retaining word-level bounding box coordinates.
  3. **Extract:** South Slavic **CLASSLA** NLP pipeline extracts structured dates, species, tree counts, parcel IDs, and obligations.
  4. **Verify:** Validates parcels against AREC records, enforces structural sum checks, and checks statutory replanting ratios.
  5. **Staff Review:** Displays candidate mutations as side-by-side diffs with highlighted source text. Approving or rejecting takes one click.
  6. **Cadastre Update:** Writes only staff-approved mutations into the PostgreSQL/PostGIS *Zelen Katastar* database.
  7. **Q&A Layer:** Executes natural language queries via parameterised SQL/PostGIS tools, providing exact document citations or abstaining when evidence is insufficient.

### Zone 2: Open Zone (Public Repository & Benchmark Suite)
- **Open Source:** Permissive Apache-2.0 codebase, schemas, and container specifications.
- **Synthetic Permit Generator:** Procedural generation engine creating realistic synthetic Macedonian felling permits (varying typography, simulated typewriter ink, Cyrillic handwriting, and circular purple municipal stamp overlays).
- **Evaluation Benchmark:** A curated, fully anonymised, and de-identified real permit sample released with the City of Skopje's consent for reproducible academic benchmarking.

---

## 3. The Five Operational Rules

1. **Staff Authority:** Nothing enters the Cadastre without a staff decision. Every AI output is a proposed diff against a record, displayed with the source page, highlighted bounding box, and confidence score. One-click approve; one-click reject.
2. **Two Zones, Not "100% Air-Gapped":** Real citizen data (*ЕМБГ*) and city archives stay in the enclave. The open-source repository houses code, models, synthetic data, and the de-identified evaluation benchmark.
3. **Calibrated Abstention:** Conformal risk control (Learn-then-Test) guarantees bounded error rates (e.g., $\le 2.0\%$ error among auto-proposed fields at a $15\%$ human review rate). Stratified calibration accounts for distinct document eras (1970s handwritten vs. 2020s laser-printed). Deterministic structural checks catch arithmetic anomalies; spatial context filters catch valid-but-wrong parcel matches.
4. **Explicit Relational Data Model:** A disambiguated schema connects permits to individual felling lines, parcel references, proposed cadastre trees, replanting obligations, and verification events.
5. **Unified Engine:** The same core PostgreSQL/PostGIS store powers both extraction ingestion and the Phase 1 (Zindi) Q&A query engine (NL-to-SQL, spatial predicates, document citations, and calibrated abstention).

*For the complete technical specification, formal SQL DDL, and statistical proofs, see [`docs/ARCHITECTURE_v2.md`](docs/ARCHITECTURE_v2.md).*

---

## 4. Itemized Budget & Funding Allocation ($40,000 USD)

In compliance with IEEE Humanitarian Technologies financial guidelines, **100% of the requested USD 40,000 (INR 37,20,000 at INR 93/USD)** is allocated exclusively to direct materials, hardware testbeds, mobile audit kits, tree tagging consumables, and local municipal transit. **Zero grant funds are requested for personnel salaries, student stipends, computers, overhead, or unitemised contingency.**

### Master Budget Summary

| Line | Category | Description | USD | INR (₹) |
|:---:|:---|:---|---:|---:|
| **1** | Testbeds & Optical Bench | Prototype iteration, multi-spectral bench, calibration rigs | \$6,022 | ₹5,60,000 |
| **2** | Archival Intake Station | Heavy-duty A3 scanner, polarizing backlights, acid-free trays | \$3,011 | ₹2,80,000 |
| **3** | Survey Consumables | 3,000 anodized QR tags, laser dendrometers, calipers, borers | \$9,462 | ₹8,80,000 |
| **4** | Arborist Field Kits | 10 IP68 rugged tablets + external GNSS receivers (QField/ODK) | \$6,075 | ₹5,65,000 |
| **5** | Local Field Travel | 58 local field visits across 10 Skopje municipalities | \$6,237 | ₹5,80,000 |
| **6** | Training & Safety | Bilingual MK/SQ manuals, PPE gear, stakeholder seminars | \$4,409 | ₹4,10,000 |
| **7** | Deployment Tooling | Air-gapped server enclosure, NVMe offline mirror arrays, HSM | \$2,473 | ₹2,30,000 |
| **8** | Spares Pool & Logistics | 2 reserve tablet kits, scanner consumables, customs | \$2,311 | ₹2,15,000 |
| **Total** | **Direct Project Allocation** | **All lines direct implementation $\cdot$ GST & Customs Included** | **\$40,000** | **₹37,20,000** |

### Geographic Partnership Model
- **International Travel Policy:** In accordance with IEEE Humanitarian Technologies rules, **no grant funds are allocated to international airfares or student travel abroad**.
- **Collaborative Structure:** Core software engineering, containerization, algorithm calibration, and synthetic data generation are conducted by the university engineering student team. On-ground archival digitization, physical inspections, and field travel are conducted **domestically within the Skopje Valley** by the local municipal community partner (**PE "Parks and Greenery"** field crews and City of Skopje inspectors).

---

## 5. Administrative & Geographic Grounding

- **Cadastral Authority:** Agency for Real Estate Cadastre (**AREC** / *Агенција за катастар на недвижности* - AKN). Spatial data is referenced to **MGI Balkans Zone 7** (EPSG:31277).
- **The 10 Municipalities of Skopje:**
  1. Aerodrom (*Аеродром*)
  2. Butel (*Бутел*)
  3. Gazi Baba (*Гази Баба*)
  4. Gjorče Petrov (*Ѓорче Петров*)
  5. Karpoš (*Карпош*)
  6. Kisela Voda (*Кисела Вода*)
  7. Saraj (*Сарај*)
  8. Centar (*Центар*)
  9. Čair (*Чаир*)
  10. Šuto Orizari (*Шуто Оризари*)
  *(Note: Vodno is a protected mountain forest park, not a municipality).*
- **Data Protection Law:** North Macedonia's *Law on Personal Data Protection* (*Official Gazette No. 42/20*) transposes EU GDPR principles. Enclave isolation is grounded in administrative risk reduction and citizen identity protection (*ЕМБГ*).
- **Green Cadastre Baseline:** Developed under the City of Skopje with UNDP/REC support within the "Resilient Skopje" framework (2020–2021).

---

## 6. Repository Structure

```
verdant-skopje-proposal/
├── verdant_proposal.tex       # Master XeLaTeX source (8 pages, SHWAS layout)
├── verdant_proposal.pdf       # Compiled submission PDF
├── README.md                  # System overview, two-zone topology, budget summary
├── .gitignore                 # LaTeX auxiliary and cache filter
├── docs/                      # Architectural specifications & deep research
│   ├── ARCHITECTURE_v2.md     # Master Architecture v2 (Data model, 5 rules, throughput)
│   ├── Skopje_Green_Cadastre_Master_Proposal.md
│   ├── Skopje_Green_Cadastre_Perfected_Architecture.md
│   ├── Track3_Deep_Research_100_Works.md
│   └── Track3_Top_50_Git_Repositories.md
├── figures/                   # High-resolution monochrome publication figures
│   ├── fig1_canopy_loss.png
│   ├── fig2_intervention_node.png
│   ├── fig3_permit_sample.png
│   ├── fig4_system_block_diagram.png
│   ├── fig5_conformal_curve.png
│   ├── fig6_swimlanes.png
│   ├── fig7_principle_operation.png
│   ├── fig_gantt_timeline.png
│   └── fig8_engineering_loop.png
└── scripts/                   # Tooling & automated build verification
    ├── generate_figures.py    # Python Matplotlib figure generator
    └── compile_proposal.py    # Automated XeLaTeX 2-pass compilation & verification
```

---

## 7. How to Compile

To recompile the proposal PDF from source:

```bash
# Ensure XeLaTeX and required fonts (Cambria, Segoe UI) are installed
xelatex -interaction=nonstopmode -halt-on-error verdant_proposal.tex
xelatex -interaction=nonstopmode -halt-on-error verdant_proposal.tex
```

Or run the automated compilation script:
```bash
python scripts/compile_proposal.py
```
