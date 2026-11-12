# November 19 Live Q&A Session: Technical & Operational Checklist

> **Challenge:** IEEE Humanitarian Technologies & UNDP GenAI for Good (Cities Edition)  
> **Target Date:** 19 November 2026 (Official Challenge Q&A)  
> **Team:** Malaviya National Institute of Technology Jaipur (MNIT Jaipur) Consortium  

---

## 1. Permit Archives & Ingestion

1. **Physical Format vs. Digital PDFs:**
   - Does the City of Skopje already possess digitised PDF scans of historical felling permits (e.g. from the 2020--2021 *Resilient Skopje* baseline or municipal digitization drives), or are records exclusively bound paper files in physical archives?
   - *Impact:* If digital PDFs exist, hardware procurement for flatbed scanners can be completely omitted, redirecting resources to higher compute/annotation capacity.
2. **Document Volume & Historical Scope:**
   - What is the estimated total count of un-digitized permits across the 10 municipalities? Is there a designated pilot priority era (e.g., 2018--2024 vs. pre-2000 Yugoslav records)?
3. **Multi-Department Workflow:**
   - Felling authorizations often involve multiple municipal bodies (Sector for Environmental Protection, Sector for Urban Planning, and communal public enterprises). Are permit registers centralized, or will records need de-duplication across sector archives?

---

## 2. Green Cadastre (*Зелен Катастар*) Access & Integration

4. **Cadastre Data Interface:**
   - How will challenge teams access the existing *Zelen Katastar* dataset? Will it be provided as a PostGIS database dump, GeoPackage/Shapefile export, or via a live REST / WFS endpoint?
5. **Cadastral Base Map Resolution:**
   - Is the baseline parcel data linked directly to the Agency for Real Estate Cadastre (**AREC** / *AKN*) coordinate registry in MGI Balkans Zone 7 (EPSG:31277), and what is the typical polygon positional accuracy?
6. **Unique Identifier Scheme:**
   - How are individual trees identified within the current system (e.g., UUID, parcel-relative serial index, or coordinate centroid)?

---

## 3. Evaluation Benchmark & Submission Logistics

7. **Gold Standard Benchmark Data:**
   - Will UNDP or the City of Skopje provide a small, curated set of double-annotated gold-standard permits for local model validation prior to the December 12 technical submission?
8. **November 30 Dataset Window:**
   - The competition schedule lists a November 30 window for dataset contributions. Can teams contribute an open-source synthetic Cyrillic permit dataset to support Track 3 evaluation?
9. **Phase 1 Evaluation Criteria on Zindi:**
   - How will the Phase 1 automated benchmark score structured field accuracy, spatial coordinate matching, and explicit abstentions (e.g., correctly returning "insufficient evidence" when a record lacks parcel data)?

---

## 4. Administrative, Eligibility & Staged Funding Rules

10. **Prototype vs. Pilot Payout Rules:**
    - Can the $10,000 prototype award fund student stipends, linguist annotation time, and remote compute instances, or is it strictly limited to direct materials?
11. **Pilot Award Timeline:**
    - For the subsequent $30,000 pilot award running through 31 December 2027, what are the milestone disbursement gates and reporting intervals?
12. **City Matchmaking & Letter of Support:**
    - How does UNDP facilitate formal collaboration and liaison onboarding with the City of Skopje and PE "Parks and Greenery" for international university teams?
