"""Compara último dato de cada indicador España 2050 con senda lineal base(2019) -> meta 2030."""
import json, glob, os

BASE_YEAR, TARGET_YEAR = 2019, 2030
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

rows = []
for f in sorted(glob.glob(os.path.join(HERE, "datos_*.json"))):
    with open(f, encoding="utf-8") as fh:
        rows += json.load(fh)


def num(x):
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    s = str(x).replace("%", "").replace("*", "").strip()
    # "330.640" (miles ES) o "1,2" (decimal ES); "13.0" sin coma se deja como decimal
    if "," in s or (s.count(".") == 1 and len(s.split(".")[1]) == 3):
        s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


out = []
for r in rows:
    # si la serie actual no casa con la base del informe, usar valor reescalado a la base
    v_raw = r.get("ultimo_valor_ajustado_a_base", r.get("ultimo_valor"))
    b, t, v = num(r.get("base")), num(r.get("meta2030")), num(v_raw)
    y = r.get("anio_dato")
    try:
        y = int(str(y)[:4])
    except (TypeError, ValueError):
        y = None
    estado, prog, esperado = "sin dato", None, None
    if None not in (b, t, v, y) and t != b:
        prog = (v - b) / (t - b)
        esperado = max(0.0, min(1.0, (y - BASE_YEAR) / (TARGET_YEAR - BASE_YEAR)))
        if prog >= 1:
            estado = "meta 2030 en linea"
        elif prog >= esperado:
            estado = "en senda"
        elif prog > 0:
            estado = "avanza, por debajo de senda"
        else:
            estado = "estancado o retroceso"
    out.append({**r, "progreso": prog, "esperado": esperado, "estado": estado})

out.sort(key=lambda r: (int(r["id"]), str(r.get("sub") or "")))
with open(os.path.join(HERE, "resultado.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)

from collections import Counter
print(Counter(r["estado"] for r in out))
for r in out:
    p = "  -  " if r["progreso"] is None else f"{r['progreso']*100:5.0f}%"
    e = "  -  " if r["esperado"] is None else f"{r['esperado']*100:3.0f}%"
    print(f"{r['id']:>2} {str(r.get('sub') or '')[:12]:12} {str(r['indicador'])[:45]:45} base={r.get('base')!s:>8} "
          f"meta={r.get('meta2030')!s:>8} ult={r.get('ultimo_valor')!s:>8} ({r.get('anio_dato')}) prog={p} esp={e} {r['estado']} [{r.get('comparabilidad')}]")
