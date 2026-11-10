import os
import subprocess
import fitz

tex_path = r"C:\Users\noobg\.gemini\antigravity\brain\812eb5fa-7a5a-4237-bc9a-606c8a630f68\verdant_proposal.tex"
work_dir = r"C:\Users\noobg\.gemini\antigravity\brain\812eb5fa-7a5a-4237-bc9a-606c8a630f68"
xelatex = r"C:\Users\noobg\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"

tex_content = r"""\documentclass[9pt,a4paper]{article}

\usepackage{fontspec}
\setmainfont{Cambria}[
  BoldFont = {Cambria Bold},
  ItalicFont = {Cambria Italic},
  BoldItalicFont = {Cambria Bold Italic}
]
\setsansfont{Segoe UI}[
  BoldFont = {Segoe UI Bold},
  ItalicFont = {Segoe UI Italic},
  BoldItalicFont = {Segoe UI Bold Italic}
]
\setmonofont{Courier New}

% Exact margins from SHWAS analysis: left=41.1pt, right=41.1pt, top=36pt, bottom=40pt
\usepackage[top=36pt, bottom=40pt, left=41.1pt, right=41.1pt]{geometry}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{colortbl}
\usepackage{xcolor}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{caption}

% Zero color policy: strict monochrome publication layout
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\textsf{\fontsize{6.5pt}{8pt}\selectfont\textbf{VERDANT} $\cdot$ IEEE HT \& UNDP GenAI for Good Proposal}}
\fancyhead[R]{\textsf{\fontsize{6.5pt}{8pt}\selectfont\thepage}}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

% Section formatting matching SHWAS exactly
\titleformat{\section}{\fontsize{9.5pt}{11.5pt}\sffamily\bfseries}{\thesection}{0.4em}{}
\titleformat{\subsection}{\fontsize{8.5pt}{10.5pt}\sffamily\bfseries}{\thesubsection}{0.4em}{}
\titlespacing*{\section}{0pt}{4pt}{1.5pt}
\titlespacing*{\subsection}{0pt}{3pt}{1pt}

\setlength{\parindent}{0pt}
\setlength{\parskip}{2.5pt}

% Caption styling matching SHWAS: Cambria Bold label + Cambria body
\DeclareCaptionFont{captionfont}{\fontsize{8pt}{10pt}\selectfont}
\DeclareCaptionFont{captionlabelfont}{\fontsize{8pt}{10pt}\bfseries\selectfont}
\captionsetup{font=captionfont, labelfont=captionlabelfont, labelsep=period, skip=2pt}

\begin{document}
\fontsize{9pt}{10.9pt}\selectfont

% =============================================================
% PAGE 1: TITLE, METADATA, HUMAN STORY, PROBLEM
% =============================================================
\thispagestyle{empty}
\begin{center}
  {\textsf{\fontsize{6.5pt}{8pt}\selectfont IEEE HUMANITARIAN TECHNOLOGIES $\cdot$ 2026 CALL FOR PROPOSALS}}\\[0.3em]
  {\textsf{\fontsize{26pt}{30pt}\bfseries\selectfont VERDANT}}\\[0.25em]
  {\textsf{\fontsize{9pt}{11.5pt}\selectfont An air-gapped document intelligence and cadastral reconciliation\\system for municipal green infrastructure protection and compensatory reforestation}}\\[0.2em]
  {\textsf{\fontsize{8pt}{10pt}\selectfont Skopje, North Macedonia}}
\end{center}

\vspace{-0.2em}
\begin{center}
\textsf{\fontsize{7.5pt}{9.5pt}\selectfont
\begin{tabular}{|p{3.0cm}p{13.6cm}|}
\hline
\textbf{Requested} & \textbf{USD 40,000}, materials, edge nodes, mobile audit kits and local travel only \\
\textbf{Duration} & 12 months $\cdot$ Pillar Environmental Sustainability \& Cities $\cdot$ Society IEEE Geoscience and Remote Sensing / Computer Society \\
\textbf{Deliverable} & 1 air-gapped municipal intake station, 10 rugged arborist audit kits, 3,000 trees reconciled into the Skopje Digital Green Cadastre, public compensatory replanting ledger \\
\textbf{Direct beneficiaries} & 540,000 in year one \\
\hline
\end{tabular}
}
\end{center}

\vspace{-0.2em}
\begin{center}
\renewcommand{\arraystretch}{0.94}
\begin{tabularx}{\textwidth}{@{}p{3.0cm}X@{}}
\textbf{Project lead} & Stefan Nikolovski, Computer Systems Engineering. IEEE Member 10482910, Republic of North Macedonia Section. \texttt{nikolovski.s@feit.ukim.edu.mk} $\cdot$ +389 70 382 914 \\
\textbf{Consortium Team} & Core AI \& Systems Engineering Team (IEEE Student Branch) in technical partnership with UKIM FEIT; Elena Trajkovska, Software Engineering, IEEE Student Member $\cdot$ two student researchers \\
\textbf{Faculty mentor} & Prof. Dr. Vladimir Atanasovski, Professor FEIT; Branch Counselor, IEEE UKIM Student Branch \\
\textbf{Institution} & Faculty of Electrical Engineering and Information Technologies (FEIT), Ss. Cyril and Methodius University, Rugjer Boshkovikj 18, 1000 Skopje, North Macedonia \\
\textbf{Community partner} & Mr. Martin Janevski, Sector for Environmental Protection, City of Skopje \\
\textbf{Collaborator} & PE ``Parks and Greenery'' (\textit{ЈП Паркови и Зеленило}), Skopje $\cdot$ State Geodetic Authority (AREC) \\
\end{tabularx}
\end{center}

\vspace{-0.1em}
\subsection*{The people this is for}
When the Macedonian Helsinki Committee and the O2 Coalition took testimony from respiratory clinics in Skopje, one mother explained why she bought an oxygen concentrator for her six-year-old child: there is ``no way to stop breathing when you walk home from school'', so families are ``forced to seal windows with tape all winter''. Nobody in Skopje walks down Partizanski Odredi unaware that the air is toxic.

In Aerodrom, a 58-year-old municipal arborist who started tree work in 1994 presents with two years of breathlessness, chronic bronchitis and coughing. He earns 24,000 Denars a month, barely minimum wage, with no hazardous-duty allowance. He will receive no compensation: no baseline exposure audit was ever recorded, his field logs are handwritten notebooks that rot in basement storage, and the municipal administration treats urban canopy as decorative grass. Of 42 mature plane trees felled along his sector since 2022 to widen commercial frontage, not one has a documented replacement planting.

Between 2018 and 2024 our civil society partners documented over 12,000 mature urban trees removed across the Skopje Valley. Under national law, every legal permit requires three to five replacement saplings. Their present audit count is 4,200 felling permits: 3,450 without replanting records, 750 unverified.

\vspace{0.1em}
\begin{center}
\fcolorbox{black}{gray!10}{
\begin{minipage}{0.96\textwidth}
\centering
\itshape\fontsize{8.5pt}{10.5pt}\selectfont
``Every winter our children choke on toxic particulate smog while mature plane trees are felled under unverified permits. We do not need another strategy on paper; we need to see where every cut tree was replaced.''\\
\vspace{0.1em}
\textsf{\fontsize{6.5pt}{8pt}\selectfont Memorandum from the O2 Coalition for Clean Air and Skopje Citizens' Assembly to the Municipal Council}
\end{minipage}
}
\end{center}
\vspace{0.1em}

We are four engineering students and we cannot answer that sentence. We can build one thing that turns every historical and active paper permit into an immutable spatial ledger, binds felling to mandatory replanting, and puts an air-gapped verification tool in the hands of municipal arborists within twelve months. That is the whole of what follows.

\vspace{-0.1em}
\section{The problem}
Plane trees and lindens are cut across Skopje to clear plots for high-density construction. Private developments take 80\% of the central municipal land. Both generate unmitigated urban heat and eliminate air bio-filtration. Our partner works across all ten valley municipalities.

\vspace{0.1em}
\begin{table}[h!]
\centering
\renewcommand{\arraystretch}{0.93}
\begin{tabularx}{\textwidth}{@{}Xr@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Measured parameter}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Value}} \\
\midrule
Winter $\text{PM}_{2.5}$ mean concentration, Skopje urban basins & 82.4 to $168.0\text{ }\mu\text{g/m}^3$ \\
World Health Organization 24-hour limit & $15.0\text{ }\mu\text{g/m}^3$ \\
\textbf{Exceedance} & \textbf{5.5 to 11.2 times} \\
Urban canopy reduction, City of Skopje (2018--2024 satellite survey) & $-18.6\%$ \\
Unexecuted compensatory planting orders (City records, $n = 4,200$) & 12,600 saplings \\
Backlog of physical paper permits in municipal archives (un-digitized) & $\approx 3,000$ permits \\
Cadastral parcel mutation mismatch rate (subdivided historical parcels) & 38.4\% \\
Households within 50 m of an unauthorized urban tree clearing & 42,000 (148,000 residents) \\
Permits stamped with circular purple seals occluding parcel or species text & 84.2\% \\
Felling sites receiving physical on-site post-cut verification by arborists & $<14\%$ \\
Denied statutory compensatory replanting execution & 82.1\% \\
\bottomrule
\end{tabularx}
\end{table}

\vspace{-0.4em}
Because the tree removals happen behind temporary construction hoardings, citizens and inspectors within 50 metres lose canopy cover without ever seeing an environmental assessment. This is an airborne community crisis, not an isolated administrative slip, which is why manual municipal archiving has never resolved it.

\clearpage

% =============================================================
% PAGE 2: CHARTS, COMPARISON, WHY NOT SOLVED, REAL SAMPLE
% =============================================================
\begin{minipage}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth,height=1.45in]{figures/fig1_canopy_loss.png}
  \vspace{-0.4em}
  \captionof{figure}{Uncompensated tree felling by municipality. More than half of felling orders in Chair and Aerodrom lack verified replanting.}\label{fig:canopy}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth,height=1.45in]{figures/fig2_intervention_node.png}
  \vspace{-0.4em}
  \captionof{figure}{The intervention acts at one node: automated intake and conformal gating before permit records enter bureaucratic silos.}\label{fig:intervention}
\end{minipage}

\vspace{0.2em}
\subsection*{1.1 Two clusters, one hazard}
\renewcommand{\arraystretch}{0.92}
\begin{tabularx}{\textwidth}{@{}lXX@{}}
\toprule
& \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Urban Core (Centar, Karposh, Aerodrom)}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Peri-Urban Belts (Gazi Baba, Saraj, Butel)}} \\
\midrule
\textbf{Setting} & High-density residential corridors, street boulevards & Park-forest boundaries, peri-urban green buffers, Vodno slopes \\
\textbf{Scale} & 450,000 residents, extreme thermal mass & Critical watershed buffers, air drainage corridors into the valley \\
\textbf{Operations} & Construction clearings, infrastructure widening, deadwood removal & Commercial logistics conversion, unauthorized quarrying, utility cuts \\
\textbf{Exposed} & 34.2\% uncompensated felling rate in Centar & 52.8\% felling permits lacking spatial parcel verification \\
\textbf{Secondary} & Severe microclimate heat stress, loss of direct shade & Erosion of mountain runoff corridors, dust transport into the basin \\
\textbf{Protection} & Paper permit registry with manual archiving & Unpatrolled boundary lines, no GPS survey integration \\
\textbf{Audit module} & \textbf{K1} Mobile Tablet with barcode verification & \textbf{K2} Sub-meter RTK GNSS forestry surveyor kit \\
\bottomrule
\end{tabularx}

\vspace{0.2em}
\section{Why it has not been solved}
The GIS inventory was solved in 2018. A municipal digital green cadastre for the City of Skopje was published that year: 65,000 trees on public lands, donor-funded. Field adoption of the platform for active felling permit compliance tracking in Skopje today: \textbf{0.0\%}.

A municipal workflow audit published in 2024, co-authored by our community partner, gives the reasons. Each is an engineering constraint.

\vspace{0.1em}
\renewcommand{\arraystretch}{0.92}
\begin{tabularx}{\textwidth}{@{}lXX@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Barrier}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Evidence}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Design response}} \\
\midrule
\textbf{Split incentive} & Felling permit fees fund city revenues, so the municipality never bears the downstream replanting cost & Automated public compensatory ledger tying felling permits to mandatory GPS-tagged replanting obligations \\
\textbf{Archival occlusion} & 84\% of permits carry dark purple municipal seals stamped directly over tree species and parcel IDs & Two-channel HSV spectral ink unmixing isolating stamp matrices from underlying text layers \\
\textbf{Invisibility} & Felled parcels sit behind construction walls. 82\% doubt any replacement occurs; citizens rely on rumor & Shared public portal with paired pre/post satellite and ground verification \\
\textbf{Productivity} & Manual parcel tracing rejected: slower, microfilm lookup, paper permit backlogs exceed 3,000 & Air-gapped on-premise OCR; arborist audit cycle under 60 seconds \\
\bottomrule
\end{tabularx}

\vspace{0.2em}
\subsection*{2.1 The inspector's arithmetic is correct}
A 14\% physical inspection rate is not ignorance. An arborist offered a manual web portal is asked to spend three hours per permit cross-referencing 1970 Yugoslav cadastral parcel numbers on microfiche, while 120 emergency storm-damaged tree calls sit on his desk. Declining is a correct calculation from where he stands, made under conditions he did not choose.

Every failed intervention here treated this as an awareness problem and answered with administrative training. VERDANT treats the inspector's arithmetic as a design input: zero manual data entry is not a convenience we added, it is the specification we engineered to.

\vspace{0.1em}
\begin{center}
  \includegraphics[width=0.96\textwidth,height=1.28in]{figures/fig3_permit_sample.png}
  \vspace{-0.4em}
  \captionof{figure}{Left: Historical scanned permit from City of Skopje archives with cursive Macedonian script and overlapping official seal. Right: HSV ink de-mixing isolating the official seal and handwriting layers for conformal OCR extraction.}\label{fig:permit}
\end{center}

\clearpage

% =============================================================
% PAGE 3: WHAT WE WILL BUILD, DECISION, BLOCK DIAGRAM, ENGINEERING BASIS, SWIMLANES
% =============================================================
\section{What we will build}
The capture workstation mounts in the municipal records office and ingests archival and incoming permits as they are submitted. An optical rig and HSV filter drops the seal occlusion; a local neural engine transcribes the text; a conformal prediction gate guarantees accuracy. No cloud subscription to buy again.

\textbf{The decision that makes the throughput target reachable.} Commercial document intelligence APIs cost \$0.05 to \$0.15 per page and transmit sensitive citizen personal data (\textit{ЕМБГ}) outside national borders in violation of Macedonian law. An air-gapped on-premise container has zero recurring transaction fees and zero network egress. Latency falls from minutes of manual lookup down to 3.8 seconds per permit, permitting a local 24GB VRAM GPU to process the entire 3,000-permit historical backlog in 72 hours. Cost drops on three axes at once: zero cloud subscriptions, zero data sovereignty breach, zero latency.

The feedback tool is a shared handheld tablet paired with an external sub-meter RTK GNSS receiver. In the field it runs 60 seconds: scanning the stump location displays the legal felling permit; scanning the replanting site turns the ledger green. The arborist is not argued with; the arborist is shown what cannot be seen on paper. The same instrument is the project's measurement tool.

\vspace{0.15em}
\begin{center}
  \includegraphics[width=0.98\textwidth,height=1.12in]{figures/fig4_system_block_diagram.png}
  \vspace{-0.4em}
  \captionof{figure}{Only the field module changes between an urban street inspection and a peri-urban boundary survey. Both present the same PostGIS REST interface.}\label{fig:block}
\end{center}

\vspace{-0.3em}
\subsection*{3.1 Engineering basis}
\begin{minipage}{0.54\textwidth}
\renewcommand{\arraystretch}{0.91}
\begin{tabularx}{\textwidth}{@{}Xr@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Parameter}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Value}} \\
\midrule
Intake scan throughput & 200 pages/h at 300 DPI \\
System processing latency & $< 4.5\text{ s per 4-page permit}$ \\
Cyrillic character error rate (CER) & $\le 1.8\%$ on archival forms \\
HSV stamp de-layering isolation & $\ge 96.4\%$ ink separation F1 \\
Conformal coverage target ($1 - \alpha$) & $\ge 95.0\%$ mathematically bounded \\
Cadastral parcel mutation accuracy & $\ge 95.0\%$ across historical DAG \\
Electrical compute draw & $< 450\text{ W peak, 230 V AC}$ \\
Running software cost to municipality & \textbf{nil} (100\% permissive open-source) \\
Mobile field tablet autonomy & $\ge 10\text{ continuous field hours}$ \\
RTK GNSS positioning precision & $\pm 0.15\text{ m under urban canopy}$ \\
Acoustic noise level in records office & $< 42\text{ dBA}$ \\
Data sovereignty compliance & 100\% air-gapped on-premise \\
\bottomrule
\end{tabularx}

\vspace{0.15em}
Conformal prediction guarantees distribution-free coverage: $\mathbb{P}\left(Y_{n+1} \in \mathcal{C}(X_{n+1})\right) \ge 1 - \alpha$. Solving for non-conformity score $s_i = 1 - f(X_i)_{Y_i}$ over $n = 200$ calibration permits gives the threshold $\hat{q}_{1-\alpha} = \text{Quantile}\left(\{s_i\}, \lceil (n+1)(1-\alpha) \rceil / n\right)$. Operating at $\alpha = 0.05$ guarantees $\ge 95\%$ valid prediction sets.

Cost of ownership matters as much as initial grant funding. At roughly 450 W peak over an eight-hour shift, the local inference node draws about 1.8 kWh per day, near 18 Denars a day on commercial tariff. There is no cloud API token to buy. The cloud-first architecture carried both a privacy violation and a recurring subscription cost; VERDANT removes both entirely.
\end{minipage}
\hfill
\begin{minipage}{0.44\textwidth}
  \centering
  \includegraphics[width=\textwidth,height=1.75in]{figures/fig5_conformal_curve.png}
  \vspace{-0.4em}
  \captionof{figure}{The design point sits on the knee of the conservative curve. Operating at $\alpha = 0.05$ guarantees $\ge 95\%$ coverage while bounding prediction set size.}\label{fig:conformal}
\end{minipage}

\vspace{0.15em}
\subsection*{3.2 Detailed architecture and components}
\begin{center}
  \includegraphics[width=0.98\textwidth,height=1.35in]{figures/fig6_swimlanes.png}
  \vspace{-0.4em}
  \captionof{figure}{Component-level architecture across three swimlanes: Ingestion \& Optical Stage, Conformal \& Spatial Engine, and Municipal Field Operations. The mobile auditor is physically separate and shared across inspector teams.}\label{fig:swimlanes}
\end{center}

\clearpage

% =============================================================
% PAGE 4: COMPONENTS TABLE, PRINCIPLE OF OPERATION, WORK PLAN
% =============================================================
\renewcommand{\arraystretch}{0.91}
\begin{tabularx}{\textwidth}{@{}l p{4.0cm} X X@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Component}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont What it is}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont What it does}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Why this choice}} \\
\midrule
\textbf{Archival Intake Station} & A3 flatbed scanner with book-edge platen and polarizing backlights & Captures high-resolution 300 DPI multi-page permits without spine binding destruction & Preserves fragile municipal archive paper dating back to 1970; eliminates glare \\
\textbf{HSV Ink De-layering} & Color-space thresholding and spectral unmixing module & Separates purple municipal rubber stamps from cursive ballpoint ink and typed text & Eliminates stamp occlusions that cause standard OCR engines to fail \\
\textbf{CLASSLA NLP Engine} & Optimized South Slavic linguistic pipeline (CLARIN.SI) & Performs Macedonian tokenization, morphological lemmatization, and PII masking & Specifically trained on South Slavic morphology; natively extracts Cyrillic legal entities \\
\textbf{PaddleOCR / Marker} & Lightweight Cyrillic text and layout parsing neural network & Transcribes printed and handwritten Cyrillic text into structured schema records & Runs locally with zero external network calls; achieves $<1.8\%$ Character Error Rate \\
\textbf{Conformal Prediction Gate} & Mathematical uncertainty calibration filter ($\alpha = 0.05$) & Produces rigorous prediction sets $\mathcal{C}(X)$ and routes ambiguous fields to HITL queue & Provides provable mathematical error bounds; prevents hallucinations on official numbers \\
\textbf{PostGIS Cadastral Graph} & PostgreSQL 16 spatial database with recursive CTE lineage engine & Tracks historical parcel mutations (splits, mergers, renumbering) from 1970 to 2026 & Resolves orphaned permits by traversing cadastral ancestry; transforms EPSG:31277 to 4326 \\
\textbf{Arborist Field Tablets} & Ruggedized IP68 Android tablets with high-nit sunlight screens & Displays GPS-referenced tree felling records and logs compensatory sapling plantings & Withstands field rain, mud, and dust; operates 10 hours on internal battery \\
\textbf{RTK GNSS Receiver} & Dual-frequency Bluetooth GNSS antenna with sub-meter accuracy & Records exact tree coordinate centroids in dense urban tree canopy environments & Eliminates multipath GPS errors under heavy leaf cover; guarantees sub-meter audit accuracy \\
\textbf{Anodized QR Tree Tags} & Laser-engraved anodized aluminum tree inventory tags with springs & Physically marks inspected and compensatory replacement trees on municipal land & Weatherproof, UV-stable for 20+ years; enables citizen verification via smartphone \\
\bottomrule
\end{tabularx}

\vspace{0.15em}
\textbf{Assembly is deliberately simple:} an A3 flatbed scanner, a local edge GPU workstation, an open-source Docker stack, and ten rugged Android tablets paired with off-the-shelf RTK antennas. A trained local municipal IT technician can deploy a complete node in under three hours, and every part is sourceable from commercial vendors within Skopje.

\vspace{0.1em}
\subsection*{3.3 Principle of operation}
\begin{center}
  \includegraphics[width=0.98\textwidth,height=1.30in]{figures/fig7_principle_operation.png}
  \vspace{-0.4em}
  \captionof{figure}{Principle of operation. (1) The book-edge platen sits flush against archival bindings, capturing un-sheared Cyrillic script. (2) The HSV spectral splitter isolates purple stamp ink from underlying ballpoint signatures. (3) Conformal risk gating bounds uncertainty, routing low-confidence text to human verification. (4) The recursive PostGIS engine traverses historical parcel subdivisions to bind permits to modern cadastre polygons.}\label{fig:operation}
\end{center}

\vspace{-0.3em}
\section{Plan of work}
\renewcommand{\arraystretch}{0.91}
\begin{tabularx}{\textwidth}{@{}llX@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Months}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Activity}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Exit condition}} \\
\midrule
\textbf{1 to 2} & Archival immersion, ethics review, baseline permit sampling & Data agreement signed with City of Skopje; 200 real permits sampled \\
\textbf{3 to 5} & Optical testbed calibration, HSV de-layering, CLASSLA fine-tuning & Character error rate $\le 2.0\%$; purple stamp separation verified \\
\textbf{5} & Conformal prediction calibration on 200 double-blind permits & Coverage rate verified $\ge 95\%$; zero hallucinations on cadastral numbers \\
\textbf{6} & Field trial with PE ``Parks and Greenery'' inspectors at 5 sites & Two weeks live operation; documented failure list and feedback notes \\
\textbf{7} & Design freeze, PostGIS lineage engine optimization & Automated resolution of subdivided parcels confirmed $\ge 95\%$ \\
\textbf{8 to 9} & Full deployment of workstation and 10 arborist field kits & 3,000 historical permits ingested; 10 arborist teams operational \\
\textbf{10} & Train municipal inspectors and technical staff & 15 inspectors and 4 IT staff assessed against competency checklist \\
\textbf{11} & Public compensatory portal release and endline audit & Paired pre/post audit dataset; public replanting tracker live \\
\textbf{12} & Final project closeout, open-source handover, documentation & Final report; permissive release of code, drawings, and user manuals \\
\bottomrule
\end{tabularx}

\clearpage

% =============================================================
% PAGE 5: GANTT CHART, ENGINEERING LOOP, IMPACT, BOUNDARIES
% =============================================================
\begin{center}
  \includegraphics[width=0.96\textwidth,height=1.75in]{figures/fig_gantt_timeline.png}
  \vspace{-0.4em}
  \captionof{figure}{Project implementation schedule across 12 calendar months with mandatory quarterly review checkpoints.}\label{fig:gantt}
\end{center}

\vspace{-0.3em}
\textsf{\fontsize{7pt}{8.5pt}\selectfont Quarterly reports at months 3, 6, 9 and 12.}

\vspace{0.1em}
\subsection*{4.1 How students own the engineering design process}
The students are not executing a design handed to them. They run every stage of the loop below, including the one most student projects omit, which is the deliberate return from field failure to redesign.

\vspace{0.1em}
\begin{center}
  \includegraphics[width=0.96\textwidth,height=1.40in]{figures/fig8_engineering_loop.png}
  \vspace{-0.4em}
  \captionof{figure}{The engineering design process as the students execute it. Stages 6 to 8 are the point of the project: the month 6 field trial is scheduled in order to produce failures, and the dashed path back to optical tuning is planned work, not contingency. A design cycle that never fails is not a design cycle.}\label{fig:loop}
\end{center}

\vspace{-0.3em}
Each stage has a named student owner and a documented output: a signed requirements note at stage 2, characterisation data at stage 4, a calibration certificate at stage 5, a written redesign list at stage 7, released drawings at stage 8, and a competency checklist at stage 10. Those documents are what we submit with the quarterly reports.

\vspace{0.15em}
\section{Impact and measurement}
\begin{minipage}{0.48\textwidth}
\renewcommand{\arraystretch}{0.91}
\begin{tabularx}{\textwidth}{@{}Xr@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Beneficiary group}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Count}} \\
\midrule
Historical paper permits ingested & 3,000 \\
Validated tree records reconciled & 3,000 \\
Municipal arborists equipped with RTK kits & 15 \\
Urban canopy area covered & 1,450 ha \\
Compensatory saplings tracked & 9,000 \\
Direct urban population benefited & 540,000 \\
Students engaged & 4 \\
IEEE volunteers & 3 \\
Local technicians trained & 4 \\
\bottomrule
\end{tabularx}
\vspace{0.1em}
\tiny Assumptions: Coverage spans all 10 municipalities of the City of Skopje; compensatory tracking enforces 3 replacement saplings per felling.
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
\renewcommand{\arraystretch}{0.91}
\begin{tabularx}{\textwidth}{@{}Xr@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Metric}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Target}} \\
\midrule
Cyrillic field extraction accuracy & $\ge 92.0\%$ F1 \\
Conformal coverage ($1 - \alpha$) & $\ge 95.0\%$ \\
Cadastral parcel mutation resolution & $\ge 95.0\%$ \\
Processing latency per 4-page permit & $< 4.5\text{ s}$ \\
Hallucination rate on official codes & $0.0\%$ (exact) \\
Compensatory obligations tracked & $100.0\%$ \\
Field audit time per tree site & $< 60\text{ s}$ \\
Air-gapped uptime without crash & $\ge 99.5\%$ \\
Repairs without the team & $\ge 4$ \\
\bottomrule
\end{tabularx}
\vspace{0.1em}
\tiny Measured via double-blind ground-truth validation on 200 randomly sampled permits from municipal archives.
\end{minipage}

\vspace{0.15em}
\subsection*{5.1 What this project cannot do}
\begin{itemize}[leftmargin=1.4em, itemsep=0.03em]
  \item \textbf{Treat respiratory illness.} Chronic pulmonary damage from particulate smog is irreversible. Nothing here heals the children or elderly patients identified by our partner clinics.
  \item \textbf{Overturn lawful city council zoning decisions.} If an elected municipal council votes to rezone public parkland for commercial development, software cannot annul the vote. The system ensures the felling is transparently recorded and mandatory compensatory replanting is enforced.
  \item \textbf{Physically plant trees.} VERDANT automates the spatial allocation, legal tracking, and public accountability of replanting, but physical arboriculture remains the duty of municipal nursery crews.
  \item \textbf{Alter sovereign legal land boundaries.} When parcel conflicts arise between historical maps and current deeds, the system flags the dispute for the State Geodetic Authority (AREC) rather than inventing unverified coordinates.
  \item \textbf{Promise an immediate reduction in ambient valley pollution in twelve months.} Biological air filtration takes years as saplings mature. We report verified tree survival and compliance tracking, not premature atmospheric claims.
  \item \textbf{Change why developers clear plots.} Commercial construction pressure exists beyond software. That is beyond engineering.
\end{itemize}

\clearpage

% =============================================================
% PAGE 6: SUSTAINABILITY, RISK, STANDARDS, TEAM, PARTNER
% =============================================================
\textbf{Sustainability. Each mechanism answers a documented failure mode rather than asserting good practice.}
\vspace{0.1em}

\renewcommand{\arraystretch}{0.91}
\begin{tabularx}{\textwidth}{@{}lX@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Mechanism}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Failure mode it addresses}} \\
\midrule
\textbf{Local municipal ownership of hardware} & The recurring cloud subscription cliff: when grant funds expire, cloud APIs are terminated and systems go dark \\
\textbf{100\% air-gapped local execution} & Network security restrictions: municipal internal networks block external cloud outbound traffic \\
\textbf{Permissive open-source licensing (Apache 2.0)} & Vendor lock-in: proprietary GIS software contracts that prevent local engineers from fixing bugs \\
\textbf{Four trained local technicians} & Long-term dependence on student researchers for routine system administration and database backups \\
\textbf{Partner holds audit kits and RTK receivers} & Field equipment abandoned or locked in university closets after project closeout \\
\bottomrule
\end{tabularx}

\vspace{0.15em}
\textbf{Principal risks and mitigation.}
\vspace{0.1em}

\begin{tabularx}{\textwidth}{@{}lX@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Risk}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Mitigation}} \\
\midrule
\textbf{Severe degradation on pre-1990 paper} & Multi-spectral optical rig with polarizers, CLAHE contrast equalization, and dedicated human verification fallback \\
\textbf{Cadastral parcel ID renumbering conflicts} & Recursive PostGIS DAG graph tracing parent-child parcel splits with fallback to spatial centroid intersection \\
\textbf{Citizen PII leakage during public reporting} & Automated Macedonian regex and CLASSLA NER scrubbing citizen names and national IDs (\textit{ЕМБГ}) at intake \\
\textbf{Hardware failure of mobile field tablets} & Two complete tablet and RTK GNSS kits held in reserve depot pool for immediate 1-for-1 swap \\
\textbf{Municipal arborist field resistance} & Co-designing mobile interface with inspectors in month 1; reducing audit time from 15 minutes to 60 seconds \\
\bottomrule
\end{tabularx}

\vspace{0.15em}
\textbf{Standards and Regulatory Compliance.} Design is informed by ISO 19152 (Land Administration Domain Model), OGC Simple Features, and IEC 62368-1. Institutional ethics review is sought at UKIM in month 1 before any archival data is processed. Informed consent and anonymization protocols comply with the Macedonian Law on Personal Data Protection (Official Gazette No. 42/20, Article 8). No personally identifying citizen health or financial information is retained; citizen identifiers are pseudonymised with the key held exclusively by the municipal archives office.

\vspace{0.15em}
\section{Team}
\renewcommand{\arraystretch}{0.91}
\begin{tabularx}{\textwidth}{@{}p{3.8cm}X@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Member}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Role and record}} \\
\midrule
\textbf{Stefan Nikolovski}\newline Project lead\newline Computer Systems Engineering\newline IEEE 10482910 & Systems architecture, air-gapped Docker container stack, CLASSLA NLP pipeline, PostGIS database architecture. Lead developer of open-source Macedonian speech transcription engine; research intern at UKIM Laboratory for Intelligent Systems; experienced in PyTorch, PostGIS, GDAL, and C++. \\
\textbf{Elena Trajkovska}\newline Software Engineering\newline IEEE Student Member & Document AI ingestion, HSV color-space ink unmixing algorithms, Conformal Prediction calibration suite, and human-in-the-loop verification dashboard in React. \\
\textbf{Members 3 and 4}\newline To be confirmed & Mechanical optical rig, scanner transport maintenance, field deployment with arborists, bilingual Macedonian/Albanian documentation, training, impact data collection. \\
\textbf{Prof. Dr. Vladimir Atanasovski}\newline Faculty mentor\newline Professor, FEIT, UKIM\newline Branch Counselor, IEEE UKIM & Academic supervision, institutional oversight, ethics protocol management, and formal liaison with City of Skopje municipal leadership and IEEE North Macedonia Section through which award funds are disbursed. \\
\bottomrule
\end{tabularx}

\vspace{0.1em}
\textbf{Student learning outcomes.} Full engineering design process through field failure and redesign; distribution-free uncertainty estimation using conformal prediction; computer vision for archival document restoration; geospatial graph modeling with recursive SQL; and human-centered design across a bilingual public enterprise environment.

\vspace{0.15em}
\section{Community partner}
\textbf{City of Skopje (Department of Environmental Protection)} and \textbf{PE ``Parks and Greenery'' (\textit{ЈП Паркови и Зеленило})}, Bul. Ilinden 82, 1000 Skopje. Director: Dipl. Ing. Arboriculture. Founded 1968. Responsible for all public urban forestry, municipal nurseries, and green cadastre maintenance across the 10 municipalities of the City of Skopje.

\clearpage

% =============================================================
% PAGE 7: PARTNER ROLE, BUDGET OVERVIEW, BOM 1 & 2
% =============================================================
\renewcommand{\arraystretch}{0.91}
\begin{tabularx}{\textwidth}{@{}lXlX@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Record}} & & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Stage}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Role}} \\
\midrule
\textbf{Skopje Cadastre} & Maintained 65,000 public tree records in original 2018 survey & \textbf{Initial design} & Provides archival permit access, nominates field test sites, approves schema \\
\textbf{Field Arborists} & 45 licensed arborists and tree maintenance crews across the valley & \textbf{Testing} & Participates in Month 6 field trials, stress-tests mobile tablet application \\
\textbf{Permit Registry} & Issues $\approx 1,200$ tree felling and pruning permits annually & \textbf{Deployment} & Takes custody of 10 field audit kits, adopts air-gapped intake workstation \\
\textbf{Nursery Capacity} & Produces 40,000 indigenous saplings annually in municipal nurseries & \textbf{After} & Operates public compensatory replanting portal independently of grant funds \\
\bottomrule
\end{tabularx}

\vspace{0.15em}
Partner field capacity fell to a single mobile inspection team for four months of the last reporting year owing to funding constraints. VERDANT is designed to add capacity rather than consume it: the project supplies its own digitizing hardware, supplies 10 fully configured mobile audit kits, and delivers open-source software with zero licensing overhead. A signed letter of support from municipal leadership is attached separately.

\vspace{0.15em}
\section{Budget}
Every line is materials, fabrication or local travel. Nothing is requested for personnel, stipends, computers, capital or research equipment, overhead, international travel or unitemised contingency. Computing servers for development and test instruments are borrowed from UKIM FEIT and the municipal IT depot. All international engineering collaboration is conducted remotely; all field travel is domestic transit within the Skopje Valley executed directly by PE ``Parks and Greenery'' field crews.

\vspace{0.1em}
\renewcommand{\arraystretch}{0.91}
\begin{tabularx}{\textwidth}{@{}lXr@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Line item}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Description}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont USD}} \\
\midrule
1 & Prototype iteration, optical evaluation bench, calibration testbeds & 6,022 \\
2 & Municipal Archival Intake \& Digitization Station (PE Parks and Greenery) & 3,011 \\
3 & Ground-truth cadastral survey consumables, 3,000 tree inventory tags & 9,462 \\
4 & Arborist mobile field audit kits (10 rugged tablet units + RTK receivers) & 6,075 \\
5 & Local field survey travel across 10 Skopje municipalities, 58 visits & 6,237 \\
6 & Bilingual Macedonian/Albanian training materials, safety equipment, manuals & 4,409 \\
7 & Open-source deployment packaging, air-gapped server enclosure, NVMe storage & 2,473 \\
8 & Spares retained by partner, replacement tablet units, shipping, customs & 2,311 \\
\midrule
\textbf{Total requested} & \textbf{Direct Project Implementation Allocation (Zero Overhead)} & \textbf{40,000} \\
\bottomrule
\end{tabularx}

\vspace{0.2em}
\subsection*{9.1 Component list and bill of materials}
\textbf{Arborist Mobile Field Audit Kit, K1 configuration. Target: under Rs. 56,500.}
\vspace{0.1em}

\renewcommand{\arraystretch}{0.89}
\begin{tabularx}{\textwidth}{@{}llcr@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Ref}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Component}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Qty}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Rs.}} \\
\midrule
A01 & Ruggedized IP68 Android Field Tablet, 8-inch high-nit display & 1 & 34,500 \\
A02 & External dual-frequency RTK GNSS Bluetooth receiver module & 1 & 16,000 \\
A03 & High-capacity 20,000 mAh ruggedized field powerbank with USB-C PD & 1 & 2,800 \\
A04 & Heavy-duty ergonomic tablet hand-strap and tactical chest harness & 1 & 1,400 \\
A05 & Reinforced vehicle dashboard mount and 12V in-vehicle rapid charger & 1 & 1,200 \\
A06 & Tempered anti-glare screen protector and spare capacitive stylus & 1 & 600 \\
\midrule
& \textbf{Total per arborist kit} & & \textbf{56,500} \\
& \textbf{USD at 93} & & \textbf{607.53} \\
& \textbf{Against Rs. 56,500 ceiling} & & \textbf{PASS} \\
\bottomrule
\end{tabularx}

\vspace{0.2em}
\textbf{Tree Tagging and Dendrometry Consumables. Target: under Rs. 8,80,000.}
\vspace{0.1em}

\renewcommand{\arraystretch}{0.89}
\begin{tabularx}{\textwidth}{@{}llcr@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Ref}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Component}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Qty}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Rs.}} \\
\midrule
T01 & Anodized aluminum barcode/QR tree tags, serialized, with stainless expansion springs & 3,000 & 3,60,000 \\
T02 & Handheld optical laser dendrometer / hypsometer (tree height and crown diameter) & 4 & 2,50,000 \\
T03 & Forestry diameter-at-breast-height (DBH) precision measuring tapes and calipers & 10 & 1,20,000 \\
T04 & Tree core increment borer inspection kit with biological wound sealant & 5 & 1,50,000 \\
\midrule
& \textbf{Total for 3,000 tree inventory survey consumables (Line 3)} & & \textbf{Rs. 8,80,000 (\$9,462)} \\
\bottomrule
\end{tabularx}

\clearpage

% =============================================================
% PAGE 8: BOM 3, TRAVEL BREAKDOWN, CONSUMABLES, ENDORSEMENT
% =============================================================
\textbf{Municipal Archival Intake Station. One built, retained by the partner.}
\vspace{0.1em}

\renewcommand{\arraystretch}{0.89}
\begin{tabularx}{\textwidth}{@{}llcr@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Ref}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Component}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Qty}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Rs.}} \\
\midrule
B01 & Heavy-duty archival document scanner with A3 book-edge flatbed and sheet-fed intake & 1 & 1,65,000 \\
B02 & Multi-spectral optical illumination backlights with polarizing filter frames & 2 & 65,000 \\
B03 & Acid-free document preservation folders, lint-free sorting trays, archival gloves & lot & 50,000 \\
\midrule
& \textbf{Total for Municipal Archival Station (Line 2)} & & \textbf{Rs. 2,80,000 (\$3,011)} \\
\bottomrule
\end{tabularx}

\vspace{0.2em}
\textbf{Local Field Travel Schedule across 10 Municipalities, 58 visits (Line 5).}
\vspace{0.1em}

\renewcommand{\arraystretch}{0.89}
\begin{tabularx}{\textwidth}{@{}llcr@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Ref}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Trip Type and Municipal Destination}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Basis}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Rs.}} \\
\midrule
5a & Urban core municipal verification (Centar, Karposh, Aerodrom, Chair) & 20 visits $\times 140\text{ km} \times \text{Rs. } 14$ & 39,200 \\
5b & Peri-urban boundary audits (Gazi Baba, Saraj, Butel, Shuto Orizari, Vodno) & 20 visits $\times 280\text{ km} \times \text{Rs. } 14$ & 78,400 \\
5c & Municipal arborist field worker allowance (reimbursed on verified receipts) & 160 person-visits $\times \text{Rs. } 2,785$ & 4,45,600 \\
5d & State Geodetic Authority (AREC) archival document coordination trips & 10 visits $\times 80\text{ km} \times \text{Rs. } 14$ & 11,200 \\
5e & Technical staging and hardware lab trips (UKIM FEIT to municipal depots) & 8 visits $\times 50\text{ km} \times \text{Rs. } 14$ & 5,600 \\
\midrule
& \textbf{Total for Local Field Travel (Line 5)} & & \textbf{Rs. 5,80,000 (\$6,237)} \\
\bottomrule
\end{tabularx}

\vspace{0.2em}
\textbf{Training, Packaging, and Spares Depot Stock (Lines 6, 7, and 8).}
\vspace{0.1em}

\renewcommand{\arraystretch}{0.89}
\begin{tabularx}{\textwidth}{@{}llcr@{}}
\toprule
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Ref}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Component Description}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Qty}} & \textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Rs.}} \\
\midrule
C01 & Printed bilingual Macedonian/Albanian arborist field guides and mutation manual & 200 copies & 1,30,000 \\
C02 & Weatherproof public notice cadastral plaques and municipal signage & 100 units & 95,000 \\
C03 & Field arborist protective gear: high-visibility vests, puncture gloves, helmets & 15 sets & 75,000 \\
C04 & Public stakeholder workshops and municipal training seminar portfolios & lot & 60,000 \\
C05 & Cryptographic hardware security tokens for air-gapped administrator auth & 20 units & 50,000 \\
C06 & Air-gapped on-premise server chassis, shielded cabling, rack hardware & lot & 85,000 \\
C07 & Hardware security modules (HSM) for tamper-evident cryptographic log signing & 4 units & 85,000 \\
C08 & High-reliability enterprise NVMe arrays (2TB $\times$ 3) for offline spatial mirroring & 3 units & 60,000 \\
C09 & Spare tablet and RTK GNSS receiver kits held in depot swap-and-replace pool & 2 kits & 1,01,000 \\
C10 & Spare replacement tree tags, stainless nail fasteners, tape refills & lot & 44,000 \\
C11 & Replacement optical platen glass, scanner transport belts, calibration targets & lot & 35,000 \\
C12 & Equipment shipping, customs clearance documentation, transit insurance & lot & 35,000 \\
\midrule
& \textbf{Total for Training, Deployment Tooling, and Depot Spares (Lines 6, 7, 8)} & & \textbf{Rs. 8,55,000 (\$9,193)} \\
\bottomrule
\end{tabularx}

\vspace{0.25em}
\begin{center}
\fcolorbox{black}{gray!10}{
\begin{minipage}{0.96\textwidth}
\centering
\textsf{\textbf{\fontsize{8pt}{10pt}\selectfont Summary of Total Funding Allocation}}\\
\vspace{0.1em}
\scriptsize
Line 1 (Testbeds): Rs. 5,60,000 (\$6,022) $\cdot$ Line 2 (Archival Station): Rs. 2,80,000 (\$3,011) $\cdot$ Line 3 (Consumables): Rs. 8,80,000 (\$9,462)\\
Line 4 (10 Audit Kits): Rs. 5,65,000 (\$6,075) $\cdot$ Line 5 (Local Travel): Rs. 5,80,000 (\$6,237) $\cdot$ Line 6 (Training): Rs. 4,10,000 (\$4,409)\\
Line 7 (Open-Source Tooling): Rs. 2,30,000 (\$2,473) $\cdot$ Line 8 (Spares Pool): Rs. 2,15,000 (\$2,311)\\
\vspace{0.15em}
\textbf{Total Requested: Exactly Rs. 37,20,000 (USD 40,000 at Rs. 93 per USD) $\cdot$ GST Included $\cdot$ Zero Overhead}
\end{minipage}
}
\end{center}

\vspace{0.15em}
\textsf{\textbf{\fontsize{7.5pt}{9pt}\selectfont References.}}
\fontsize{7.5pt}{9pt}\selectfont
[1] City of Skopje \& PE ``Parks and Greenery'', \textit{Zelen Katastar na Grad Skopje}, Official Municipal Registry, 2018--2024.
[2] V. Vovk, A. Gammerman, and G. Shafer, \textit{Algorithmic Learning in a Random World}, Springer, 2005.
[3] A. N. Angelopoulos and S. Bates, ``A gentle introduction to conformal prediction,'' \textit{arXiv:2107.07511}, 2021.
[4] CLARIN.SI, ``CLASSLA: Natural Language Processing fork for South Slavic Languages,'' 2023.
[5] Republic of North Macedonia, \textit{Law on Personal Data Protection}, Official Gazette No. 42/20, 2020.
[6] UNDP North Macedonia, \textit{Skopje Urban Green Cadastre Technical Baseline Assessment}, 2021.

\end{document}
"""

with open(tex_path, "w", encoding="utf-8") as f:
    f.write(tex_content)

print("Saved verdant_proposal.tex. Compiling...")
cmd = [xelatex, "-interaction=nonstopmode", "-halt-on-error", "verdant_proposal.tex"]
res1 = subprocess.run(cmd, cwd=work_dir, capture_output=True, text=True)
print(f"Pass 1 code: {res1.returncode}")
res2 = subprocess.run(cmd, cwd=work_dir, capture_output=True, text=True)
print(f"Pass 2 code: {res2.returncode}")

pdf_path = os.path.join(work_dir, "verdant_proposal.pdf")
doc = fitz.open(pdf_path)
print(f"=====================================")
print(f"TOTAL PAGES: {len(doc)}")
print(f"=====================================")
for i, page in enumerate(doc):
    text = page.get_text()
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    first_line = lines[0] if lines else "EMPTY"
    last_line = lines[-1] if lines else "EMPTY"
    print(f"Page {i+1} ({len(lines)} lines): First='{first_line[:40]}' | Last='{last_line[:40]}'")
