---
title: Monitoreo y Libro C — línea de base e indicadores de salud ecológica
created: 2026-10-15
status: v0.1 — protocolo propuesto; primero lo de bajo costo, después socios científicos
---

# 09 · Monitoreo y Libro C

Volver a [[00 - Léeme]] · Reglas: `AGENTS.md`, regla 7 · Vínculo con tokenomics: `../NS_Tokenomics/01 - Context and Constraints.md` §5 (Ledger C)

## 🌱 En un respiro

"Regenerativo" es una afirmación, y las afirmaciones necesitan evidencia. Antes de tocar nada tomamos una **línea de base** (fotos, suelo, plantas, agua, aves) y después la repetimos todos los años en los mismos puntos. Ese registro es el **Libro C** (*Ledger C*), el libro de capital ecológico que NS_Tokenomics usa para habilitar la liberación de la plata de los bienes comunes. También es el producto principal de un hub de I+D: datos abiertos que muestran un desierto reverdeciendo (o no).

## 1. Línea de base (hacerla antes de las primeras obras)

| Qué | Método | Frecuencia | Quién |
|---|---|---|---|
| **Puntos fotográficos** | Puntos GPS fijos, misma dirección, misma estación; ortofoto de dron de la columna verde | 2 veces/año + después de las tormentas grandes | Equipo |
| **Cobertura vegetal** | Transectas de intercepción por puntos (p. ej. 50 m, un toque cada 50 cm) por unidad de paisaje | Anual, el mismo mes | Equipo + botánico |
| **Análisis de la Función del Paisaje (LFA)** | Método de Tongway para tierras áridas: parches/interparches, estabilidad, infiltración, ciclado de nutrientes | Anual | Equipo capacitado [^lfa] |
| **Suelo** | Calicatas por unidad: textura, profundidad, CE (salinidad), pH, carbono orgánico; prueba de infiltración (anillo simple) | Cada 2–3 años; infiltración anual | Laboratorio (INTA) |
| **Agua** | Pluviómetro(s); reglas limnimétricas / marcadores de cresta en el cauce; profundidad y CE de pozos; calidad del agua en la desembocadura y en el río | Por evento + mensual | Equipo |
| **Biodiversidad** | Proyecto de iNaturalist "Lighthouse VRN"; hotspot de eBird; cámaras trampa; conteos de polinizadores | Continuo | Residentes + visitantes (ciencia ciudadana) |
| **Erosión** | Clavos de erosión y posición de las cabeceras de cárcava | Después de los eventos | Equipo |
| **Registro de plantación** | Cada unidad plantada/sembrada: especie, técnica, fecha, supervivencia | 1, 3, 6, 12, 24 meses | Vivero |

Opcional más adelante: **Ecological Outcome Verification** (Savory Institute) o un convenio con una universidad para un protocolo formal; teledetección (NDVI de Sentinel-2) para tendencias de todo el sitio ✅ gratis.

## 2. Indicadores (Libro C v0)

Tomados de los KPIs del RTMM §13.4 [^rtmm] y de los derechos del borrador de Constitución [^ns17]:

| Indicador | Unidad | Dirección |
|---|---|---|
| Cobertura viva (perenne) por unidad | % | ↑ |
| Largo de interparche de suelo desnudo | m | ↓ |
| Carbono orgánico del suelo (0–10 cm) | % | ↑ |
| Tasa de infiltración | mm/h | ↑ |
| Cabeceras activas / largo de cárcavas | cantidad / m | ↓ |
| Riqueza de especies nativas | n | ↑ |
| Supervivencia de la plantación a los 24 meses | % | ≥ meta |
| Nivel y CE de la napa | m, dS/m | estable / sin salinización |
| Corredor ecológico continuo | % del sitio | ↑ |
| **Proporción silvestre/ecológica del 7A** | % | ↑ (escalera 10% → 50%, [[08 - Rewilding y proporción ecológica]]) |
| NDVI de la columna verde (estación seca) | índice | ↑ |
| Superficie con especies invasoras | ha | ↓ |

Respuesta gradual (Constitución, art. 8): dos períodos de deterioro → explicación → plan de remediación → apoyo → sanción.

## 3. Dónde viven los datos

- Datos crudos en `sources/monitoreo/` (CSV, fotos por fecha) ❓ o en un drive compartido; los resúmenes, en este vault.
- Más adelante: una capa de la plataforma por punto/transecta (modelo GeoJSON de `../lighthouse-platform`), con "sin dato" cuando falte.
- 🧪 **Opcional, a futuro (agregado 2026-10-23): cada registro del Libro C como *atestación*.** La idea viene de la consultoría web3 del 23-oct [^web3]. Quien mide firma la lectura: punto, fecha, indicador, valor o "sin dato", método y foto. Un verificador (laboratorio de suelos de INTA, botánico, hidrólogo; ver [[11 - Expertos y términos de referencia]] §6) firma otra atestación que apunta a esa lectura y dice "revisado, conforme" o "revisado, con observaciones". El estándar candidato es EAS (Ethereum Attestation Service), empezando off-chain [criterio].
  - **Para qué sirve:** cualquiera, incluido un inversor, puede revisar quién midió, quién verificó y cuándo, sin confiar en NetX. Es la prueba que pide [[17 - La regeneración como valor (las 300 razones)]] §2.3 contra el greenwashing, y le da a la invariante J9 (`../NS_Tokenomics/29`) un registro que no se puede editar después.
  - **Límites:** **nunca datos personales on-chain** (Ley 25.326). Las personas se identifican por su rol o con un identificador; las fotos y los CSV quedan en `sources/monitoreo/` y se guarda solo su huella (hash). La atestación no reemplaza al método: un dato mal medido y firmado sigue estando mal medido. Si el registro legal y el libro difieren, manda el legal (`../NS_Tokenomics/29` J10).
  - ❓ Cuándo: no antes de tener línea de base y verificadores con nombre.

## 4. Plantilla de balance hídrico (mensual, m³)

| Mes | Lluvia (mm) | Escurrimiento captado | Napa | Concesión del río | Reúso | **Oferta** | Doméstico | Riego | Vivero | Restauración | Reserva incendios | Pérdidas | **Demanda** | Saldo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ene | sin dato | | | | | | | | | | | | | |

## Fuentes y lógica usada

- Métodos: Tongway y Hindley, *Landscape Function Analysis* (CSIRO, 2004) [^lfa]; monitoreo estándar de pastizales (intercepción por puntos, Herrick et al., *Monitoring Manual for Grassland, Shrubland and Savanna Ecosystems*, USDA-ARS, 2005) [S].
- Elección de indicadores [criterio], alineada con el RTMM y el borrador de Constitución.

[^lfa]: D. Tongway y N. Hindley, *Landscape Function Analysis: Procedures for Monitoring and Assessing Landscapes*, CSIRO, 2004 [S].
[^rtmm]: `../NS_Tokenomics/sources/NetX_Lighthouse_Regenerative_Territorial_Model_AI.md` §13.4.
[^ns17]: `../NS_Tokenomics/17 - Lighthouse Constitution and Rights of Nature (draft).md` §2, §4.
[^web3]: Llamada privada, consultoría web3, 2026-10-23; resumen en `../NS_platform/Documentation/reuniones/2026-10-23 - Consultoría web3 (filtrado plataforma).md` y `../NS_Tokenomics/07` §J.
