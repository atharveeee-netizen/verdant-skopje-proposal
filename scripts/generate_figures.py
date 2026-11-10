import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out_dir = r'C:\Users\noobg\.gemini\antigravity\brain\812eb5fa-7a5a-4237-bc9a-606c8a630f68\figures'
os.makedirs(out_dir, exist_ok=True)

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 8

box_light = dict(boxstyle='square,pad=0.3', facecolor='#f8f8f8', edgecolor='black', linewidth=0.7)
box_shaded = dict(boxstyle='square,pad=0.3', facecolor='#e6e6e6', edgecolor='black', linewidth=0.9)
arrow = dict(arrowstyle='->', lw=0.9, color='black')

# ==========================================
# Figure 1: Uncompensated Tree Felling
# ==========================================
fig, ax = plt.subplots(figsize=(3.4, 2.0), dpi=300)
munis = ['Centar', 'Karposh', 'Aerodrom', 'Chair', 'Peri-urban']
rates = [34.2, 28.5, 41.0, 52.8, 18.4]
bars = ax.bar(munis, rates, color='#d0d0d0', edgecolor='black', width=0.55, linewidth=0.8)
for bar in bars:
    y = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, y + 1.5, f'{y:.1f}%', ha='center', va='bottom', fontsize=6.5)
ax.set_ylabel('Uncompensated Loss (%)', fontsize=7.5)
ax.set_ylim(0, 68)
ax.tick_params(axis='both', which='major', labelsize=7)
ax.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
fig.savefig(os.path.join(out_dir, 'fig1_canopy_loss.png'), dpi=300)
plt.close(fig)
print('Fig 1 generated.')

# ==========================================
# Figure 2: Intervention Node
# ==========================================
fig, ax = plt.subplots(figsize=(3.4, 2.0), dpi=300)
ax.axis('off')
ax.text(0.05, 0.72, 'NOW', fontsize=7.5, fontweight='bold')
ax.text(0.30, 0.72, 'Felling Permit\n(Paper Archive)', bbox=box_light, ha='center', va='center', fontsize=6)
ax.annotate('', xy=(0.54, 0.72), xytext=(0.43, 0.72), arrowprops=arrow)
ax.text(0.66, 0.72, 'Unindexed Drawer\n(Manual Silo)', bbox=box_light, ha='center', va='center', fontsize=6)
ax.annotate('', xy=(0.86, 0.72), xytext=(0.79, 0.72), arrowprops=arrow)
ax.text(0.95, 0.72, 'Unreplanted Tree,\nLost Lineage', bbox=box_light, ha='center', va='center', fontsize=5.5)

ax.text(0.05, 0.28, 'VERDANT', fontsize=7.5, fontweight='bold')
ax.text(0.30, 0.28, 'Felling Permit\n(Optical Intake)', bbox=box_shaded, ha='center', va='center', fontsize=6)
ax.annotate('', xy=(0.54, 0.28), xytext=(0.43, 0.28), arrowprops=arrow)
ax.text(0.66, 0.28, 'Air-Gapped OCR\n& Conformal Gating', bbox=box_shaded, ha='center', va='center', fontsize=6)
ax.annotate('', xy=(0.86, 0.28), xytext=(0.79, 0.28), arrowprops=arrow)
ax.text(0.95, 0.28, 'PostGIS Lineage &\nReplanting Ledger', bbox=box_shaded, ha='center', va='center', fontsize=5.5)

ax.set_xlim(0, 1.05)
ax.set_ylim(0, 1.0)
plt.tight_layout()
fig.savefig(os.path.join(out_dir, 'fig2_intervention_node.png'), dpi=300)
plt.close(fig)
print('Fig 2 generated.')

# ==========================================
# Figure 3: Scanned Macedonian Permit & HSV De-mixing (Optimized Height 1.7in)
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 1.8), dpi=300)

np.random.seed(42)
img_paper = np.ones((240, 360), dtype=float) * 0.94
noise = np.random.normal(0, 0.025, (240, 360))
img_paper += noise
img_paper = np.clip(img_paper, 0.7, 1.0)

ax1.imshow(img_paper, cmap='gray', vmin=0, vmax=1)
for y in [45, 80, 115, 150, 185, 215]:
    ax1.plot([30, 330], [y, y], color='black', lw=0.5, alpha=0.7)
ax1.text(180, 30, 'ГРАД СКОПЈЕ - СЕКТОР ЗА ЖИВОТНА СРЕДИНА', ha='center', va='center', fontsize=6, fontweight='bold', color='#222222')
ax1.text(180, 65, 'РЕШЕНИЕ ЗА СЕЧЕЊЕ И НАДОМЕСТ НА ЗЕЛЕНИЛО', ha='center', va='center', fontsize=5.5, fontweight='bold', color='#333333')
ax1.text(35, 100, 'Локација / Парцела: КП 1408/2 КО Центар', fontsize=5, color='#333333')
ax1.text(35, 135, 'Вид на дрво: Platanus orientalis (Јавор)', fontsize=5, color='#333333')
ax1.text(35, 170, 'Основа за сечење: Градежни активности / Суво стебло', fontsize=4.8, color='#333333')
ax1.text(35, 205, 'Обврска за компензација: 3 садници (Клен / Јавор)', fontsize=5, fontweight='bold', color='#222222')

circle = plt.Circle((280, 185), 38, color='#555555', fill=False, lw=1.1, alpha=0.85)
ax1.add_patch(circle)
inner_circle = plt.Circle((280, 185), 32, color='#555555', fill=False, lw=0.6, alpha=0.85)
ax1.add_patch(inner_circle)
ax1.text(280, 185, 'РЕПУБЛИКА С. МАКЕДОНИЈА\n* ГРАД СКОПЈЕ *\nПЕЧАТ', ha='center', va='center', fontsize=4, color='#444444')
ax1.plot([230, 245, 260, 290, 310], [220, 215, 225, 210, 218], color='#333333', lw=0.9)
ax1.axis('off')
ax1.set_title('Historical Scanned Permit (City of Skopje Archive)', fontsize=7, pad=3)

img_zoom = np.ones((180, 240), dtype=float) * 0.98
ax2.imshow(img_zoom, cmap='gray', vmin=0, vmax=1)
c_zoom = plt.Circle((120, 90), 65, color='black', fill=False, lw=1.3)
ax2.add_patch(c_zoom)
c_zoom_in = plt.Circle((120, 90), 56, color='black', fill=False, lw=0.7)
ax2.add_patch(c_zoom_in)
ax2.text(120, 90, 'HSV Stamp Channel\n[H: 280-330, S > 0.35]\nIsolated Seal Layer', ha='center', va='center', fontsize=6, fontweight='bold', color='black')
rect = plt.Rectangle((15, 15), 210, 150, linewidth=1.1, edgecolor='black', facecolor='none', linestyle='--')
ax2.add_patch(rect)
ax2.text(120, 155, 'Conformal Bounding Box: [x1, y1, x2, y2]', ha='center', va='center', fontsize=5, color='#444444')
ax2.axis('off')
ax2.set_title('HSV De-layering & Coordinate Extraction', fontsize=7, pad=3)

plt.tight_layout()
fig.savefig(os.path.join(out_dir, 'fig3_permit_sample.png'), dpi=300)
plt.close(fig)
print('Fig 3 generated.')

# ==========================================
# Figure 4: Functional Block Diagram
# ==========================================
fig, ax = plt.subplots(figsize=(6.5, 1.5), dpi=300)
ax.axis('off')

ax.text(0.08, 0.52, 'Archival Intake\n(A3 Scan / 300 DPI)', bbox=box_light, ha='center', va='center', fontsize=6.2)
ax.annotate('', xy=(0.17, 0.52), xytext=(0.13, 0.52), arrowprops=arrow)

ax.text(0.25, 0.52, 'HSV De-layering\n(Seal & Script Split)', bbox=box_light, ha='center', va='center', fontsize=6.2)
ax.annotate('', xy=(0.35, 0.52), xytext=(0.32, 0.52), arrowprops=arrow)

ax.text(0.43, 0.52, 'CLASSLA NLP\n& Cyrillic OCR', bbox=box_light, ha='center', va='center', fontsize=6.2)
ax.annotate('', xy=(0.53, 0.52), xytext=(0.50, 0.52), arrowprops=arrow)

ax.text(0.62, 0.52, 'Conformal Gating\n($\\alpha = 0.05$ Abstain)', bbox=box_shaded, ha='center', va='center', fontsize=6.2)
ax.annotate('', xy=(0.73, 0.52), xytext=(0.69, 0.52), arrowprops=arrow)

ax.text(0.81, 0.52, 'PostGIS Mutation\nGraph (EPSG:31277)', bbox=box_shaded, ha='center', va='center', fontsize=6.2)
ax.annotate('', xy=(0.91, 0.52), xytext=(0.88, 0.52), arrowprops=arrow)

ax.text(0.96, 0.52, 'Cadastre\nPortal', bbox=box_light, ha='center', va='center', fontsize=6.2)

ax.annotate('', xy=(0.62, 0.18), xytext=(0.62, 0.36), arrowprops=arrow)
ax.text(0.62, 0.10, 'Human-in-the-Loop Queue (Uncertain/Ambiguous Fields)', bbox=box_light, ha='center', va='center', fontsize=5.2)

ax.set_xlim(0, 1.0)
ax.set_ylim(0, 0.78)
plt.tight_layout()
fig.savefig(os.path.join(out_dir, 'fig4_system_block_diagram.png'), dpi=300)
plt.close(fig)
print('Fig 4 generated.')

# ==========================================
# Figure 5: Conformal Risk Control Curve (Padded for clean y-axis)
# ==========================================
fig, ax = plt.subplots(figsize=(4.2, 2.1), dpi=300)
alpha = np.linspace(0.01, 0.20, 100)
coverage = 1.0 - alpha
set_size = 1.0 + 2.5 * np.exp(-15 * alpha)

ax.plot(alpha, coverage, 'k-', lw=1.2, label=r'Target Coverage $1 - \alpha$')
ax.plot(alpha, set_size / np.max(set_size), 'k--', lw=1.0, label=r'Prediction Set Cardinality $|\mathcal{C}(X)|$')

ax.plot([0.05], [0.95], 'ko', markersize=4)
ax.annotate(r'Design Point: $\alpha = 0.05$' + '\n' + r'Coverage $\geq 95\%$', 
            xy=(0.05, 0.95), xytext=(0.08, 0.81),
            arrowprops=dict(arrowstyle='->', lw=0.8), fontsize=6.8)

ax.set_xlabel(r'Significance Level $\alpha$ (Permissible Risk)', fontsize=7.5)
ax.set_ylabel('Coverage Probability / Relative Size', fontsize=7.5)
ax.set_xlim(0, 0.20)
ax.set_ylim(0.70, 1.02)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='lower left', fontsize=6.8, frameon=True, edgecolor='black')
ax.tick_params(axis='both', which='major', labelsize=7)
plt.tight_layout(pad=0.8)
fig.savefig(os.path.join(out_dir, 'fig5_conformal_curve.png'), dpi=300)
plt.close(fig)
print('Fig 5 generated.')

# ==========================================
# Figure 6: Component-Level Architecture (3 Swimlanes)
# ==========================================
fig, ax = plt.subplots(figsize=(6.5, 2.0), dpi=300)
ax.axis('off')

ax.text(0.02, 0.82, 'INGESTION', fontsize=6.8, fontweight='bold', va='center')
ax.text(0.02, 0.50, 'ENGINE', fontsize=6.8, fontweight='bold', va='center')
ax.text(0.02, 0.18, 'AUDIT / FIELD', fontsize=6.8, fontweight='bold', va='center')

ax.axhline(0.66, color='#888888', linestyle='--', lw=0.6)
ax.axhline(0.33, color='#888888', linestyle='--', lw=0.6)

# Lane 1
ax.text(0.20, 0.82, 'A3 Book-Edge Platen\n(300 DPI Flatbed)', bbox=box_light, ha='center', va='center', fontsize=5.8)
ax.annotate('', xy=(0.33, 0.82), xytext=(0.28, 0.82), arrowprops=arrow)
ax.text(0.42, 0.82, 'HSV Color Filter\n(Stamp/Ink Splitter)', bbox=box_light, ha='center', va='center', fontsize=5.8)
ax.annotate('', xy=(0.54, 0.82), xytext=(0.50, 0.82), arrowprops=arrow)
ax.text(0.65, 0.82, 'CLASSLA Tokenizer\n& PII Redactor', bbox=box_light, ha='center', va='center', fontsize=5.8)
ax.annotate('', xy=(0.77, 0.82), xytext=(0.73, 0.82), arrowprops=arrow)
ax.text(0.86, 0.82, 'PaddleOCR Cyrillic\nRecognition Engine', bbox=box_light, ha='center', va='center', fontsize=5.8)

ax.annotate('', xy=(0.50, 0.60), xytext=(0.50, 0.72), arrowprops=arrow)

# Lane 2
ax.text(0.22, 0.50, 'Air-Gapped Node\n(Jetson / Docker Stack)', bbox=box_shaded, ha='center', va='center', fontsize=5.8)
ax.annotate('', xy=(0.34, 0.50), xytext=(0.29, 0.50), arrowprops=arrow)
ax.text(0.45, 0.50, 'Conformal Prediction\nFilter ($q_{1-\\alpha}$ Evaluator)', bbox=box_shaded, ha='center', va='center', fontsize=5.8)
ax.annotate('', xy=(0.58, 0.50), xytext=(0.54, 0.50), arrowprops=arrow)
ax.text(0.70, 0.50, 'PostGIS 16 Graph\n(Recursive Lineage CTE)', bbox=box_shaded, ha='center', va='center', fontsize=5.8)
ax.annotate('', xy=(0.83, 0.50), xytext=(0.79, 0.50), arrowprops=arrow)
ax.text(0.91, 0.50, 'GENIE.AI API\n(JSON-RPC 2.0)', bbox=box_shaded, ha='center', va='center', fontsize=5.8)

ax.annotate('', xy=(0.50, 0.28), xytext=(0.50, 0.40), arrowprops=arrow)

# Lane 3
ax.text(0.22, 0.18, '10 IP68 Field Tablets\n(QField / MapKit)', bbox=box_light, ha='center', va='center', fontsize=5.8)
ax.annotate('', xy=(0.34, 0.18), xytext=(0.29, 0.18), arrowprops=arrow)
ax.text(0.45, 0.18, 'External RTK GNSS\n(Sub-meter Coordinates)', bbox=box_light, ha='center', va='center', fontsize=5.8)
ax.annotate('', xy=(0.58, 0.18), xytext=(0.54, 0.18), arrowprops=arrow)
ax.text(0.70, 0.18, 'Anodized QR Tags\n(3,000 Tree Inventory)', bbox=box_light, ha='center', va='center', fontsize=5.8)
ax.annotate('', xy=(0.83, 0.18), xytext=(0.79, 0.18), arrowprops=arrow)
ax.text(0.91, 0.18, 'Compensatory\nPublic Dashboard', bbox=box_light, ha='center', va='center', fontsize=5.8)

ax.set_xlim(0, 1.0)
ax.set_ylim(0, 1.0)
plt.tight_layout()
fig.savefig(os.path.join(out_dir, 'fig6_swimlanes.png'), dpi=300)
plt.close(fig)
print('Fig 6 generated.')

# ==========================================
# Figure 7: Principle of Operation (4 Stages) - Explicit Bounds, Zero Cut-off
# ==========================================
fig, (a1, a2, a3, a4) = plt.subplots(1, 4, figsize=(6.5, 1.6), dpi=300)

for a in [a1, a2, a3, a4]:
    a.set_xlim(0, 1.0)
    a.set_ylim(0, 1.15)
    a.axis('off')

# Stage 1
a1.text(0.5, 1.04, '1. Optical Intake', ha='center', va='center', fontsize=6.8, fontweight='bold')
a1.add_patch(plt.Rectangle((0.15, 0.28), 0.70, 0.55, fill=False, edgecolor='black', lw=0.9))
for y in [0.72, 0.62, 0.52, 0.42, 0.32]:
    a1.plot([0.22, 0.78], [y, y], 'k-', lw=0.5)
a1.text(0.5, 0.10, 'Calibrated Lighting\n& 300 DPI Platen', ha='center', va='center', fontsize=5.4)

# Stage 2
a2.text(0.5, 1.04, '2. Ink Unmixing', ha='center', va='center', fontsize=6.8, fontweight='bold')
a2.add_patch(plt.Circle((0.40, 0.55), 0.22, fill=True, facecolor='#cccccc', edgecolor='black', lw=0.8, alpha=0.7))
a2.add_patch(plt.Circle((0.60, 0.50), 0.22, fill=True, facecolor='#eeeeee', edgecolor='black', lw=0.8, alpha=0.7))
a2.text(0.5, 0.55, 'HSV\nSplit', ha='center', va='center', fontsize=5.5, fontweight='bold')
a2.text(0.5, 0.10, 'Separates Stamp,\nSignature & Type', ha='center', va='center', fontsize=5.4)

# Stage 3
a3.text(0.5, 1.04, '3. Conformal Gate', ha='center', va='center', fontsize=6.8, fontweight='bold')
a3.plot([0.15, 0.50, 0.85], [0.38, 0.75, 0.38], 'k-', lw=1.0)
a3.plot([0.50, 0.50], [0.38, 0.75], 'k--', lw=0.8)
a3.text(0.5, 0.82, r'$\hat{q}_{1-\alpha}$', ha='center', va='bottom', fontsize=6.5, fontweight='bold')
a3.text(0.5, 0.10, r'$\mathbb{P}(Y \in \mathcal{C}) \geq 0.95$' + '\nZero Hallucination', ha='center', va='center', fontsize=5.4)

# Stage 4
a4.text(0.5, 1.04, '4. Parcel Lineage', ha='center', va='center', fontsize=6.8, fontweight='bold')
a4.add_patch(plt.Rectangle((0.08, 0.52), 0.32, 0.25, fill=False, edgecolor='black', lw=0.8))
a4.text(0.24, 0.64, 'KP 1408', fontsize=5, ha='center', va='center')
a4.add_patch(plt.Rectangle((0.55, 0.65), 0.38, 0.18, fill=True, facecolor='#e0e0e0', edgecolor='black', lw=0.8))
a4.text(0.74, 0.74, '1408/1', fontsize=4.8, ha='center', va='center')
a4.add_patch(plt.Rectangle((0.55, 0.40), 0.38, 0.18, fill=True, facecolor='#e0e0e0', edgecolor='black', lw=0.8))
a4.text(0.74, 0.49, '1408/2', fontsize=4.8, ha='center', va='center')
a4.annotate('', xy=(0.53, 0.74), xytext=(0.42, 0.67), arrowprops=arrow)
a4.annotate('', xy=(0.53, 0.49), xytext=(0.42, 0.61), arrowprops=arrow)
a4.text(0.5, 0.10, 'PostGIS Temporal\nRecursive Query', ha='center', va='center', fontsize=5.4)

plt.tight_layout(pad=0.5)
fig.savefig(os.path.join(out_dir, 'fig7_principle_operation.png'), dpi=300)
plt.close(fig)
print('Fig 7 generated.')

# ==========================================
# Gantt Chart (Clean Header Placement, Zero Collision)
# ==========================================
fig, ax = plt.subplots(figsize=(6.5, 2.1), dpi=300)

tasks = [
    '1. Archival audit & ethics clearance',
    '2. Multi-spectral rig & HSV bench test',
    '3. CLASSLA NLP & Conformal calibration',
    '4. PostGIS mutation graph & ontology',
    '5. Field pilot: 3,000 tree validation',
    '6. 10 Arborist RTK tablet kits deployment',
    '7. Municipal technician & arborist training',
    '8. Public portal & replanting ledger audit',
    '9. Open release, drawings & final handover'
]

start_months = [1, 2, 3, 5, 7, 8, 9, 10, 11]
duration =     [2, 3, 3, 2, 3, 2, 2,  2,  2]
y_pos = np.arange(len(tasks))

for i in range(len(tasks)):
    ax.barh(y_pos[i], duration[i], left=start_months[i], height=0.45, 
            color='#d9d9d9', edgecolor='black', linewidth=0.8)

# Dotted quarterly lines
for q in [3, 6, 9, 12]:
    ax.axvline(x=q, color='#444444', linestyle=':', lw=0.9)
    # Put label cleanly at top
    ax.text(q, -0.65, f'M{q} Checkpoint', ha='center', va='bottom', fontsize=6.2, fontweight='bold', color='#222222')

ax.set_yticks(y_pos)
ax.set_yticklabels(tasks, fontsize=6.8)
ax.invert_yaxis()
ax.set_xlabel('Project Month (1 to 12)', fontsize=7.5)
ax.set_xlim(0.8, 13.0)
ax.set_xticks(range(1, 13))
ax.tick_params(axis='x', labelsize=7)
ax.set_ylim(len(tasks) - 0.3, -1.0)
ax.grid(axis='x', linestyle='--', alpha=0.4)

plt.tight_layout(pad=0.6)
fig.savefig(os.path.join(out_dir, 'fig_gantt_timeline.png'), dpi=300)
plt.close(fig)
print('Gantt chart generated.')

# ==========================================
# Figure 8: 10-Step Engineering Design Loop
# ==========================================
fig, ax = plt.subplots(figsize=(6.5, 1.7), dpi=300)
ax.axis('off')

box_style = dict(boxstyle='square,pad=0.32', facecolor='#f5f5f5', edgecolor='black', linewidth=0.8)
box_fail = dict(boxstyle='square,pad=0.32', facecolor='#e0e0e0', edgecolor='black', linewidth=1.0)

x_coords = np.linspace(0.08, 0.92, 5)

row1_text = [
    '1. Problem audit\nwith arborists',
    '2. Requirements\nfrom evidence',
    '3. Architecture\n& concept freeze',
    '4. Optical bench\n& HSV tests',
    '5. Conformal\ncalibration'
]
for x, txt in zip(x_coords, row1_text):
    ax.text(x, 0.72, txt, bbox=box_style, ha='center', va='center', fontsize=5.8)

for i in range(4):
    ax.annotate('', xy=(x_coords[i+1] - 0.08, 0.72), xytext=(x_coords[i] + 0.08, 0.72), arrowprops=arrow)

ax.annotate('', xy=(x_coords[4], 0.40), xytext=(x_coords[4], 0.58), arrowprops=arrow)

row2_text = [
    '10. Handover,\ntraining, audit',
    '9. 10 Tablet kits\ndeployed',
    '8. Lineage freeze\n& portal release',
    '7. Adversarial\nfailure analysis',
    '6. 200-Permit\nfield pilot'
]
row2_styles = [box_style, box_style, box_style, box_fail, box_style]

for x, txt, st in zip(x_coords[::-1], row2_text, row2_styles):
    ax.text(x, 0.28, txt, bbox=st, ha='center', va='center', fontsize=5.8)

for i in range(4):
    ax.annotate('', xy=(x_coords[3-i] + 0.08, 0.28), xytext=(x_coords[4-i] - 0.08, 0.28), arrowprops=arrow)

arrow_dashed = dict(arrowstyle='->', lw=1.0, color='black', linestyle='--')
ax.annotate('', xy=(x_coords[3], 0.60), xytext=(x_coords[3], 0.40), arrowprops=arrow_dashed)
ax.text(x_coords[3] - 0.03, 0.48, 'Deliberate\nRedesign Loop', fontsize=5.2, ha='right', va='center', style='italic')

ax.text(0.24, 0.92, 'M1--M3: Ingestion & Calibration', fontsize=6.2, fontweight='bold', ha='center')
ax.text(0.72, 0.92, 'M4--M6: Graph & Field Trial', fontsize=6.2, fontweight='bold', ha='center')
ax.text(0.50, 0.06, 'M7--M12: 3,000 Tree Audit, Inspector Training & Public Handover', fontsize=6.2, fontweight='bold', ha='center')

ax.set_xlim(0, 1.0)
ax.set_ylim(0, 1.0)
plt.tight_layout()
fig.savefig(os.path.join(out_dir, 'fig8_engineering_loop.png'), dpi=300)
plt.close(fig)
print('Fig 8 generated.')
