# Senda España 2050

Seguimiento independiente de los 50 objetivos del informe [*España 2050: Fundamentos y propuestas para una Estrategia Nacional de Largo Plazo*](https://www.lamoncloa.gob.es/presidente/actividades/Documents/2021/200521-Estrategia_Espana_2050.pdf) (mayo de 2021).

Para cada indicador, la web compara el último dato oficial con una senda recta que va del punto de partida del informe (tomado en 2019) a su meta de 2030, y prolonga la tendencia real para responder: *a este ritmo, ¿cuándo llegamos?*

**Web:** https://searchingalpha.github.io/espana-2050/

> Proyecto independiente. No está afiliado al Gobierno de España ni a la Oficina Nacional de Prospectiva y Estrategia.

## Estados

| Estado | Significado |
|---|---|
| Meta 2030 en línea | El indicador ya está en el nivel fijado para 2030 (no es un objetivo cumplido: hay que mantenerlo y seguir hacia 2050) |
| Al ritmo previsto | Ha recorrido al menos lo que pide la senda para el año del dato |
| Por debajo del ritmo | Avanza, pero menos de lo necesario |
| Estancado o retroceso | No avanza o empeora |

Progreso = (último dato − punto de partida) ÷ (meta 2030 − punto de partida).

## Datos

- `data/datos_A.json` … `datos_D.json`: último dato de cada indicador, con año, URL de la fuente, grado de comparabilidad y notas. Recogidos el 4 de octubre de 2026 de Eurostat, INE, OCDE (incl. PISA 2025), MITECO, REE, IMSERSO, FUNDAE, Ministerio de Vivienda y Eurobarómetro.
- `scripts/analisis.py`: calcula progreso y estado → `data/resultado.json`.
- `scripts/build_data.py`: añade nombres, metas 2040/2050 y la proyección "a este ritmo" → `src/data/e2050.json`.

Para actualizar con datos nuevos, edita los `datos_*.json` y ejecuta:

```sh
npm run data
git commit -am "Actualiza datos" && git push
```

## Desarrollo

```sh
npm install
npm run dev
```

Cada push a `main` se publica automáticamente en GitHub Pages (GitHub Actions).

¿Has visto un error o un dato más reciente? Abre una [issue](https://github.com/SearchingAlpha/espana-2050/issues).
