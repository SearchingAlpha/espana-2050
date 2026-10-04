"""Genera public/laberinto.svg: un laberinto isométrico propio (no copiado del informe) para la portada.

Laberinto de bloques generado por búsqueda en profundidad con semilla fija, extruido en
proyección isométrica con la paleta del sitio: caras superiores cian, laterales azul y grafito.
"""
import os
import random

SEED, NX, NY = 2050, 30, 9            # celdas del laberinto
CW, CH, HZ = 22, 11, 20               # semiancho de rombo, semialto, altura de muro (px)
TOP, LEFT, RIGHT = "#65b7d9", "#3d7898", "#3c3c3b"

random.seed(SEED)
W, H = 2 * NX + 1, 2 * NY + 1         # rejilla de bloques
wall = [[True] * H for _ in range(W)]
stack, seen = [(0, 0)], {(0, 0)}
wall[1][1] = False
while stack:
    cx, cy = stack[-1]
    nb = [(cx + dx, cy + dy, dx, dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
          if 0 <= cx + dx < NX and 0 <= cy + dy < NY and (cx + dx, cy + dy) not in seen]
    if not nb:
        stack.pop()
        continue
    nx, ny, dx, dy = random.choice(nb)
    wall[2 * cx + 1 + dx][2 * cy + 1 + dy] = False
    wall[2 * nx + 1][2 * ny + 1] = False
    seen.add((nx, ny))
    stack.append((nx, ny))
# salida del laberinto hacia abajo a la izquierda, por donde arranca la senda
wall[1][H - 1] = False


def iso(i, j, z=0):
    return (i - j) * CW, (i + j) * CH - z


polys = []
for s in range(W + H):                 # orden del pintor: de atrás hacia delante
    for i in range(W):
        j = s - i
        if not (0 <= j < H) or not wall[i][j]:
            continue
        a, b = iso(i, j, HZ), iso(i + 1, j, HZ)
        c, d = iso(i + 1, j + 1, HZ), iso(i, j + 1, HZ)
        b0, c0, d0 = iso(i + 1, j), iso(i + 1, j + 1), iso(i, j + 1)
        # cara izquierda (frente sur-oeste) y derecha (frente sur-este), luego la tapa
        polys.append((LEFT, [d, c, c0, d0]))
        polys.append((RIGHT, [c, b, b0, c0]))
        polys.append((TOP, [a, b, c, d]))

xs = [p[0] for _, pts in polys for p in pts]
ys = [p[1] for _, pts in polys for p in pts]
minx, miny = min(xs), min(ys)
vw, vh = max(xs) - minx, max(ys) - miny
out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vw} {vh}" preserveAspectRatio="xMidYMid slice">',
       f"<!-- Laberinto isométrico generado por scripts/maze.py (semilla {SEED}). Ilustración original del proyecto. -->"]
for col, pts in polys:
    out.append(f'<path fill="{col}" d="M' + " ".join(f"{x - minx},{y - miny}" for x, y in pts) + 'Z"/>')
out.append("</svg>")
dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public", "laberinto.svg")
open(dst, "w", encoding="utf-8").write("\n".join(out))
print("laberinto.svg", vw, "x", vh, len(polys), "caras", os.path.getsize(dst) // 1024, "KB")
