"""Genera data.js compacto para la página a partir de resultado.json + metadatos del cuadro original."""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
rows = json.load(open(os.path.join(ROOT, "data", "resultado.json"), encoding="utf-8"))

DESAFIOS = {
    1: "Ser más productivos para crecer mejor",
    2: "Conquistar la vanguardia educativa",
    3: "Mejorar la formación y la recualificación",
    4: "Sociedad neutra en carbono y resiliente al clima",
    5: "Estado de bienestar para una sociedad más longeva",
    6: "Desarrollo territorial equilibrado, justo y sostenible",
    7: "Resolver las deficiencias del mercado de trabajo",
    8: "Reducir la pobreza y la desigualdad",
    9: "Ampliar las bases del bienestar futuro",
}
def desafio(i):
    for lim, d in [(6, 1), (13, 2), (20, 3), (27, 4), (31, 5), (36, 6), (45, 7), (49, 8), (50, 9)]:
        if i <= lim:
            return d

# id -> (nombre corto, unidad, meta2040, meta2050) del cuadro de indicadores (Fig. 6)
META = {
    1: ("Brecha de renta per cápita con la UE-8", "%", -15, -10),
    2: ("Productividad por hora trabajada", "€ PPA", 53, 63),
    3: ("Tasa de empleo (16-64)", "%", 72, 80),
    4: ("Gasto en I+D", "% PIB", 3.5, 4.0),
    5: ("Empleo por tamaño de empresa", "%", None, None),
    6: ("Economía sumergida", "% PIB", 12, 10),
    7: ("Alumnado de 15 años que ha repetido", "%", 10, 5),
    8: ("Abandono escolar temprano", "%", 6, 3),
    9: ("Jóvenes 25-34 con estudios postobligatorios", "%", 86, 93),
    10: ("Peso del origen socioeconómico en la repetición", "odds ratio", 2.0, 1.0),
    11: ("Bajo rendimiento en PISA", "%", 15, 15),
    12: ("Alto rendimiento en PISA", "%", None, None),
    13: ("Gasto público en educación", "% PIB", 5.3, 5.5),
    14: ("Mujeres en carreras STEM", "%", 42, 50),
    15: ("Adultos con competencias digitales básicas", "%", 100, 100),
    16: ("Adultos que no hablan ningún idioma extranjero", "%", 30, 25),
    17: ("Adultos en formación en el último año", "%", 70, 90),
    18: ("Parados con formación reciente", "%", 50, 70),
    19: ("Políticas activas de empleo en formación", "% PIB", 0.30, 0.40),
    20: ("Empresas que forman a su plantilla", "%", None, None),
    21: ("Emisiones de gases de efecto invernadero", "kt CO₂-eq", 126000, 29000),
    22: ("Demanda de agua", "hm³/año", 27885, 26335),
    23: ("Intensidad energética primaria", "kep/miles €", 56, 42),
    24: ("Electricidad de origen renovable", "%", 87, 100),
    25: ("Impuestos ambientales", "% PIB", 4.0, 5.0),
    26: ("Superficie agrícola ecológica", "% SAU", 43, 60),
    27: ("Reforestación anual", "ha/año", 20000, 20000),
    28: ("Tasa de actividad de mayores", "%", None, None),
    29: ("Gasto público en salud", "% PIB", 7.0, 7.0),
    30: ("Gasto en cuidados de larga duración", "% PIB", 2.0, 2.5),
    31: ("Dependientes con derecho reconocido sin prestación", "%", 0, 0),
    32: ("Sobrecarga financiera por vivienda", "%", 6.5, 4.5),
    33: ("Viviendas rehabilitadas al año", "% parque", 1.8, 2.0),
    34: ("Residuos municipales a vertedero", "%", 5, 0),
    35: ("Población expuesta a PM2,5 sobre guía OMS", "%", 15, 2),
    36: ("Pobreza energética", "%", 3.0, 0.0),
    37: ("Tasa de paro", "%", 10, 7),
    38: ("Tasa de empleo de las mujeres", "%", 75, 82),
    39: ("Paro juvenil", "%", 21, 14),
    40: ("Tasa de empleo 55-64", "%", 62, 68),
    41: ("Temporalidad", "%", 18, 15),
    42: ("Parcialidad involuntaria", "%", 5, 3),
    43: ("Horas trabajadas a la semana", "h", 36.0, 35.0),
    44: ("Brecha salarial de género", "%", 5, 0),
    45: ("Satisfacción con la situación laboral", "%", 90, 93),
    46: ("Índice de Gini", "", 31, 29),
    47: ("Población en riesgo de pobreza", "%", 15, 10),
    48: ("Presión fiscal", "% PIB", 40, 43),
    49: ("Gasto en protección social", "% PIB", 19, 20),
    50: ("Personas satisfechas con su vida", "%", 89, 92),
}
SUB_META = {  # (id, sub) -> (etiqueta, meta2040, meta2050)
    (5, "grandes"): ("Grandes (250+)", 33, 35),
    (5, "medianas"): ("Medianas (20-249)", 28, 30),
    (5, "pequenas"): ("Pequeñas (1-19)", 38, 35),
    (11, "lectura"): ("Lectura", 15, 15),
    (11, "matematicas"): ("Matemáticas", 18, 15),
    (11, "ciencia"): ("Ciencias", 15, 15),
    (12, "lectura"): ("Lectura", 8, 10),
    (12, "matematicas"): ("Matemáticas", 13, 16),
    (12, "ciencia"): ("Ciencias", 8, 10),
    (20, "grandes (>249)"): ("Grandes (250+)", 100, 100),
    (20, "medianas (50-249)"): ("Medianas (50-249)", 92, 95),
    (20, "pequeñas (10-49)"): ("Pequeñas (10-49)", 70, 75),
    (28, "55-64"): ("55-64 años", 64, 67),
    (28, "65-74"): ("65-74 años", 9, 11),
    (24, "Eurostat SHARES (RES-E, Directiva)"): (None, 87, 100),
}
# filas que son datos alternativos de otra fila principal
ALT = {(24, "REE (generación nacional)"), (45, "2018_exacto"), (48, "2025_estimado"), (50, "eu_silc_alternativo")}
ESTADO = {"meta 2030 en linea": "enlinea", "en senda": "senda",
          "avanza, por debajo de senda": "lento", "estancado o retroceso": "retroceso", "sin dato": "nodata"}


def f(x):
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return x
    s = str(x).replace("%", "").replace("*", "").strip()
    if "," in s or (s.count(".") == 1 and len(s.split(".")[1]) == 3):
        s = s.replace(".", "").replace(",", ".")
    return float(s)


out, alts = [], {}
for r in rows:
    i, sub = int(r["id"]), r.get("sub")
    item = {
        "valor": f(r["ultimo_valor"]),
        "ajustado": f(r.get("ultimo_valor_ajustado_a_base")),
        "anio": r.get("anio_dato"),
        "fuente": r.get("fuente_url"),
        "comp": r.get("comparabilidad"),
        "nota": r.get("nota"),
    }
    if (i, sub) in ALT:
        alts.setdefault(i, []).append({**item, "etiqueta": sub,
                                        "estado": ESTADO[r["estado"]], "prog": r["progreso"]})
        continue
    nombre, unidad, m40, m50 = META[i]
    etiqueta = None
    if (i, sub) in SUB_META:
        etiqueta, m40, m50 = SUB_META[(i, sub)]
    out.append({
        "id": i, "desafio": desafio(i), "nombre": nombre, "sub": etiqueta, "unidad": unidad,
        "base": f(r["base"]), "meta2030": f(r["meta2030"]), "meta2040": m40, "meta2050": m50,
        **item, "prog": r["progreso"], "esp": r["esperado"], "estado": ESTADO[r["estado"]],
    })
BASE_YEAR = 2019


def llegada(base, valor, anio, meta):
    """Año en que se alcanzaría `meta` prolongando en línea recta la evolución base(2019)->valor(anio)."""
    if None in (base, valor, anio, meta) or meta == base:
        return None
    if (valor - base) / (meta - base) >= 1:
        return "ya"
    rate = (valor - base) / (anio - BASE_YEAR)
    if rate == 0 or (meta - base) / rate <= 0:
        return "nunca"
    return round(BASE_YEAR + (meta - base) / rate, 1)


for o in out:
    o["alt"] = alts.get(o["id"], [])
    v = o["ajustado"] if o["ajustado"] is not None else o["valor"]
    try:
        y = int(str(o["anio"])[:4])
    except (TypeError, ValueError):
        y = None
    o["anio_n"] = y
    o["llega2030"] = llegada(o["base"], v, y, o["meta2030"])
    o["llega2050"] = llegada(o["base"], v, y, o["meta2050"])

data = {"desafios": DESAFIOS, "filas": out}
with open(os.path.join(ROOT, "src", "data", "e2050.json"), "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)

# recuento por indicador (las filas con sub-partes cuentan una vez, por mayoría)
from collections import Counter, defaultdict
by = defaultdict(list)
for o in out:
    by[o["id"]].append(o["estado"])
print(len(by), Counter(Counter(v).most_common(1)[0][0] for v in by.values()))
