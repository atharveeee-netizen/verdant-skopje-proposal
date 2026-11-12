# Macedonian Urban Dendrometry Taxonomy & Local Linguistic Normalization

> **Document Intelligence Reference Table for Cyrillic Extraction**  
> **Challenge:** Track 3 – Safeguarding Green Infrastructure in Skopje  

---

## 1. Urban Tree Species Normalization Table

Archival felling permits across Skopje typically use Macedonian common names, vernacular colloquialisms, or abbreviated Latin names. The table below provides the standardized mapping used by Project VERDANT's entity normalizer:

| Macedonian Cyrillic Name | Latin Botanical Name | English Common Name | Typical Compensatory Ratio | Cadastral Category |
|:---|:---|:---|:---:|:---|
| **Јавор** / Платан (*Javor*) | *Platanus orientalis* / *Platanus acerifolia* | Oriental Plane / London Plane | 5:1 | High-Canopy Shade |
| **Липа** (*Lipa*) | *Tilia cordata* / *Tilia tomentosa* | Small-leaved Lime / Silver Linden | 4:1 | High-Canopy Biofilter |
| **Костен** (*Kosten*) | *Aesculus hippocastanum* | Horse Chestnut | 3:1 | Urban Boulevard |
| **Јасен** (*Jasen*) | *Fraxinus excelsior* / *Fraxinus ornus* | European Ash / Manna Ash | 3:1 | Park Corridor |
| **Брест** (*Brest*) | *Ulmus minor* / *Ulmus pumila* | Field Elm / Siberian Elm | 4:1 | Native Canopy |
| **Бреза** (*Breza*) | *Betula pendula* | Silver Birch | 3:1 | Ornamental Greenery |
| **Даб** (*Dab*) | *Quercus robur* / *Quercus petraea* | Pedunculate Oak / Sessile Oak | 5:1 | Protected Native |
| **Топола** (*Topola*) | *Populus nigra* / *Populus alba* | Black Poplar / White Poplar | 3:1 | Riparian Corridor |
| **Врба** (*Vrba*) | *Salix alba* / *Salix babylonica* | White Willow / Weeping Willow | 3:1 | Vardar River Bank |
| **Бор** (*Bor*) | *Pinus nigra* / *Pinus sylvestris* | European Black Pine / Scots Pine | 3:1 | Coniferous Buffer |
| **Чемпрес** (*Chempres*) | *Cupressus sempervirens* | Mediterranean Cypress | 3:1 | Urban Buffer |
| **Акација** (*Akacija*) | *Robinia pseudoacacia* | Black Locust | 2:1 | Fast-Growing Fill |

---

## 2. Common Cyrillic OCR Character Confusions

Macedonian Cyrillic documents (especially historical typewriter and low-contrast copies) exhibit specific character confusion pairs that standard off-the-shelf OCR engines misidentify:

| Cyrillic Glyph | Visual Confusion | Typical OCR Failure | Normalization Rule |
|:---:|:---:|:---|:---|
| **Ѓ** (Gje) | **Г** or **Б** | Read as Latin `G` or Cyrillic `Г` | If preceding `орче Петров` (Gjorche Petrov), map to `Ѓ`. |
| **Ќ** (Kje) | **К** or **Ћ** | Misidentified as Serbian `Ћ` or Latin `K'` | Validate against Macedonian morphological dictionary. |
| **Ж** (Zhe) | **Ж** / **X** / **III** | Split into three vertical strokes `III` | Post-process known stems (e.g. `Животна средина`). |
| **Џ** (Dzhe) | **Ц** with descender | Conflated with `Ц` (Tse) | Contextual disambiguation on cadastral placenames. |
| **З** (Ze) | **3** (Numeral Three) | Digit `3` read as letter `З` or vice-versa | In parcel numbers (e.g. `КП 1408/3`), enforce numeric typing. |
| **О** (O) | **0** (Numeral Zero) | Letter `О` substituted for `0` in parcel IDs | Regex validation of cadastral parcel patterns (`^\d+(/\d+)?$`). |

---

## 3. Date & Numeric Conventions

- **Macedonian Date Formats:** Standard administrative format is `DD.MM.YYYY` (e.g., `14.11.2018` or `14.XI.2018` using Roman numerals for months). The regex parser extracts both variants into ISO 8601 (`YYYY-MM-DD`).
- **Cadastral Parcel Notation:** Parcels are designated as `КП <Main_Number>/<Sub_Number>` (e.g., `КП 1408/2`), accompanied by the Cadastral Municipality (*Катастарска општина* - КО, e.g., `КО Центар 1`).
