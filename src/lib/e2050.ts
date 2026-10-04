import data from "../data/e2050.json";

export type Estado = "enlinea" | "senda" | "lento" | "retroceso" | "nodata";
export type Fila = (typeof data.filas)[number];

export const DESAFIOS = data.desafios as Record<string, string>;
export const FILAS = data.filas as Fila[];

export const ESTADOS: Record<Estado, { label: string; short: string; desc: string }> = {
  enlinea: {
    label: "Meta 2030 en línea",
    short: "En línea",
    desc: "Ya está en el nivel fijado para 2030",
  },
  senda: { label: "Al ritmo previsto", short: "Al ritmo", desc: "Avanza al ritmo que pide la senda" },
  lento: { label: "Por debajo del ritmo", short: "Por debajo", desc: "Avanza, pero más despacio de lo necesario" },
  retroceso: { label: "Estancado o retroceso", short: "Retroceso", desc: "No avanza o empeora" },
  nodata: { label: "Sin dato", short: "Sin dato", desc: "No hay dato comparable" },
};
export const ORDEN: Estado[] = ["enlinea", "senda", "lento", "retroceso"];

/** Estado de cada indicador (las partes de un mismo indicador votan; gana la mayoría). */
export function estadoPorId(): Record<number, Estado> {
  const votos: Record<number, Record<string, number>> = {};
  for (const f of FILAS) {
    votos[f.id] ??= {};
    votos[f.id][f.estado] = (votos[f.id][f.estado] ?? 0) + 1;
  }
  const out: Record<number, Estado> = {};
  for (const [id, v] of Object.entries(votos)) {
    out[+id] = Object.entries(v).sort((a, b) => b[1] - a[1])[0][0] as Estado;
  }
  return out;
}

const nfCache = new Map<number, Intl.NumberFormat>();
export function num(v: number | null | undefined): string {
  if (v == null) return "—";
  const a = Math.abs(v);
  const dec = a >= 1000 ? 0 : a < 1 && a !== 0 ? 2 : Number.isInteger(v) ? 0 : 1;
  if (!nfCache.has(dec)) {
    nfCache.set(dec, new Intl.NumberFormat("es-ES", { minimumFractionDigits: dec, maximumFractionDigits: dec, useGrouping: true }));
  }
  // es-ES no agrupa los números de 4 cifras; forzamos el punto de miles para que se lea igual que el informe
  const s = nfCache.get(dec)!.format(v);
  const g = a >= 1000 && a < 10000 ? s.replace(/^(-?\d)(\d{3})/, "$1.$2") : s;
  return g.replace(/^-/, "−");
}

export function unidad(u: string): string {
  if (!u) return "";
  return u === "%" ? "%" : ` ${u}`;
}

export function valorActual(f: Fila): number {
  return (f.ajustado ?? f.valor) as number;
}

/** Texto de "a este ritmo": año en que se llegaría a la meta prolongando la tendencia. */
export function ritmo(f: Fila, meta: "llega2030" | "llega2050"): { big: string; small: string } {
  const v = f[meta] as number | string | null;
  if (v == null) return { big: "—", small: "sin dato" };
  if (v === "ya") return { big: "Ya", small: meta === "llega2030" ? "en el nivel de 2030" : "en el nivel de 2050" };
  if (v === "nunca") return { big: "No llega", small: "la tendencia va en contra" };
  const y = Math.max(Math.ceil(v as number), (f.anio_n ?? 2025) + 1);
  const objetivo = meta === "llega2030" ? 2030 : 2050;
  if (y > 2100) return { big: "+2100", small: "después de 2100" };
  if (y <= objetivo) return { big: String(y), small: `a tiempo para ${objetivo}` };
  const tarde = y - objetivo;
  return { big: String(y), small: `${tarde} ${tarde === 1 ? "año" : "años"} tarde` };
}
