import os
import matplotlib.pyplot as plt
import numpy as np

os.makedirs("img", exist_ok=True)
plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 10})

# -------------------------------------------------------------
# FIGURA EJERCICIO 1: Los 4 casos del robot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
casos_ej1 = [
    ("Caso 1: Antihorario (det = +18)", (1, 2), (5, 3), (3, 7), "green"),
    ("Caso 2: Horario (det = -20)", (2, 1), (6, 5), (8, 2), "crimson"),
    ("Caso 3: Colineal (det = 0)", (1, 1), (3, 3), (6, 6), "darkorange"),
    ("Caso 4: Horario (det = -15)", (0, 4), (5, 4), (3, 1), "crimson")
]

for ax, (titulo, A, B, C, color) in zip(axes.flat, casos_ej1):
    # Vectores AB y BC
    ax.annotate("", xy=B, xytext=A, arrowprops=dict(arrowstyle="->", lw=2, color="blue"))
    ax.annotate("", xy=C, xytext=B, arrowprops=dict(arrowstyle="->", lw=2, color=color, ls="--"))
    
    # Puntos
    for pt, name in [(A, f"A{A}"), (B, f"B{B}"), (C, f"C{C}")]:
        ax.plot(pt[0], pt[1], 'ko', markersize=6)
        ax.text(pt[0] + 0.2, pt[1] + 0.2, name, fontweight='bold', fontsize=10)
        
    ax.set_title(titulo, fontweight='bold', color=color)
    ax.grid(True, linestyle=":", alpha=0.6)
    all_x = [A[0], B[0], C[0]]
    all_y = [A[1], B[1], C[1]]
    ax.set_xlim(min(all_x) - 1, max(all_x) + 2)
    ax.set_ylim(min(all_y) - 1, max(all_y) + 2)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

plt.tight_layout()
plt.savefig("img/ej1_casos.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# FIGURA EJERCICIO 2: Caso Principal (Cruce en X)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 6))
A, B = (1, 1), (7, 5)
C, D = (2, 6), (8, 1)

ax.plot([A[0], B[0]], [A[1], B[1]], 'b-', lw=2.5, label='Segmento AB: (1,1) a (7,5)')
ax.plot([C[0], D[0]], [C[1], D[1]], 'r-', lw=2.5, label='Segmento CD: (2,6) a (8,1)')

# Punto de intersección aproximado (4.89, 3.59)
P_int = (44/9, 32/9)
ax.plot(P_int[0], P_int[1], 'g*', markersize=14, label=f'Intersección P({P_int[0]:.2f}, {P_int[1]:.2f})')

for pt, name in [(A, "A(1,1)"), (B, "B(7,5)"), (C, "C(2,6)"), (D, "D(8,1)")]:
    ax.plot(pt[0], pt[1], 'ko', markersize=6)
    ax.text(pt[0] + 0.2, pt[1] + 0.1, name, fontweight='bold')

ax.set_title("Ejercicio 2 - Caso 1: Cruce transversal (Intersección propia)", fontweight='bold')
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="upper left")
ax.set_xlim(0, 9)
ax.set_ylim(0, 7)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.tight_layout()
plt.savefig("img/ej2_principal.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# FIGURA EJERCICIO 2: Caso 2 (Colineales disjuntos)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 5))
A, B = (1, 1), (3, 3)
C, D = (5, 5), (7, 7)

ax.plot([A[0], B[0]], [A[1], B[1]], 'b-', lw=3, label='Segmento AB: (1,1) a (3,3)')
ax.plot([C[0], D[0]], [C[1], D[1]], 'r-', lw=3, label='Segmento CD: (5,5) a (7,7)')
ax.plot([0, 8], [0, 8], 'k--', alpha=0.3, label='Recta y = x (Colineal)')

for pt, name in [(A, "A(1,1)"), (B, "B(3,3)"), (C, "C(5,5)"), (D, "D(7,7)")]:
    ax.plot(pt[0], pt[1], 'ko', markersize=6)
    ax.text(pt[0] - 0.2, pt[1] + 0.4, name, fontweight='bold')

ax.set_title("Ejercicio 2 - Caso 2: Colineales disjuntos (Sin intersección)", fontweight='bold')
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="upper left")
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.tight_layout()
plt.savefig("img/ej2_caso2.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# FIGURA EJERCICIO 2: Caso 3 (Subcasos)
# -------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 3a: Cruce
ax = axes[0]
A, B = (0, 2), (6, 2)
C, D = (3, 0), (3, 5)
ax.plot([A[0], B[0]], [A[1], B[1]], 'b-', lw=2.5, label='AB')
ax.plot([C[0], D[0]], [C[1], D[1]], 'r-', lw=2.5, label='CD')
ax.plot(3, 2, 'g*', markersize=12, label='Cruce (3,2)')
ax.set_title("3a: Cruce transversal (Sí)", fontweight='bold')
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend()
ax.set_xlim(-1, 7)
ax.set_ylim(-1, 6)

# 3b: Contacto en B
ax = axes[1]
C, D = (6, 2), (9, 5)
ax.plot([A[0], B[0]], [A[1], B[1]], 'b-', lw=2.5, label='AB')
ax.plot([C[0], D[0]], [C[1], D[1]], 'r-', lw=2.5, label='CD')
ax.plot(6, 2, 'go', markersize=10, label='Contacto B=C (6,2)')
ax.set_title("3b: Contacto en extremo (Sí)", fontweight='bold')
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend()
ax.set_xlim(-1, 10)
ax.set_ylim(0, 6)

# 3c: Superposición
ax = axes[2]
C, D = (4, 2), (9, 2)
ax.plot([A[0], B[0]], [A[1], B[1]], 'b-', lw=3, label='AB [0,6]')
ax.plot([C[0], D[0]], [C[1], D[1]], 'r--', lw=3, label='CD [4,9]')
ax.plot([4, 6], [2, 2], 'g-', lw=4, label='Traslape [4,6]')
ax.set_title("3c: Superposición colineal (Sí)", fontweight='bold')
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend()
ax.set_xlim(-1, 10)
ax.set_ylim(0, 4)

for ax in axes:
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

plt.tight_layout()
plt.savefig("img/ej2_caso3.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# FIGURA EJERCICIO 3: Pares de tuberías comprobados
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 6))
N = 8
for i in range(N):
    for j in range(N):
        if j > i:
            ax.plot(j, i, 's', color='navy', markersize=14)
        elif j == i:
            ax.plot(j, i, 'x', color='gray', markersize=10, alpha=0.5)
        else:
            ax.plot(j, i, 'o', color='lightgray', markersize=6, alpha=0.3)

ax.set_xticks(range(N))
ax.set_yticks(range(N))
ax.set_xticklabels([f"T{j}" for j in range(N)])
ax.set_yticklabels([f"T{i}" for i in range(N)])
ax.invert_yaxis()
ax.set_title(f"Matriz de comprobaciones j > i (N={N}) -> Total = 28", fontweight='bold')
ax.set_xlabel("Índice j")
ax.set_ylabel("Índice i")
ax.grid(True, linestyle=":", alpha=0.5)
plt.tight_layout()
plt.savefig("img/ej3_pares.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# FIGURA EJERCICIO 4: Triangulación de polígono
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 6))
poly = np.array([[0,0], [8,0], [8,6], [4,3], [0,6], [0,0]])
ax.plot(poly[:,0], poly[:,1], 'k-', lw=2.5, label='Polígono')
ax.fill(poly[:,0], poly[:,1], color='whitesmoke')

# Diagonales de triangulación: AD y BD
ax.plot([0, 4], [0, 3], 'b--', lw=2, label='Diagonal AD')
ax.plot([8, 4], [0, 3], 'r--', lw=2, label='Diagonal BD')

# Oreja recortada BCD
ax.fill([8, 8, 4], [0, 6, 3], color='peachpuff', alpha=0.5, label='Triángulo BCD (Oreja C)')
ax.fill([0, 8, 4], [0, 0, 3], color='lightcyan', alpha=0.5, label='Triángulo ABD')
ax.fill([0, 4, 0], [0, 3, 6], color='lavender', alpha=0.5, label='Triángulo ADE')

nombres = {'A': (0,0), 'B': (8,0), 'C': (8,6), 'D': (4,3), 'E': (0,6)}
for n, (x, y) in nombres.items():
    ax.plot(x, y, 'ko', markersize=7)
    offset = (0.2, 0.2) if n != 'D' else (0.2, -0.4)
    ax.text(x + offset[0], y + offset[1], f"{n}({x},{y})", fontweight='bold', fontsize=11)

ax.set_title("Ejercicio 4: Triangulación de terreno (3 triángulos, 2 diagonales)", fontweight='bold')
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc='lower center')
ax.set_xlim(-1, 9)
ax.set_ylim(-1, 7)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.tight_layout()
plt.savefig("img/ej4_triangulacion.png", dpi=180)
plt.close()

print("Todas las figuras generadas con éxito en el directorio img/.")
