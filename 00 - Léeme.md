---
title: NS_permacultura — Léeme (el vault del Agente de Regeneración)
created: 2026-10-15
updated: 2026-10-16 (v0.3, con la reunión con Maurício Umann y la biblioteca del PDC)
status: vault de trabajo (privado) — apoyo al diseño, no es asesoramiento de ingeniería, agronómico ni legal
owners: Gus (diseño, permacultura), Martín (masterplan)
language: español (rioplatense), con nombres científicos y títulos en su idioma original
---

# NS_permacultura — cómo leer esto

Este vault es la base de conocimiento del **Agente de Regeneración** de Lighthouse VRN (Macrolote 7, Mainqué, Río Negro, dentro de BioPueblo). Responde una pregunta:

> **¿Cómo nos aseguramos de que Lighthouse sea un proyecto real de permacultura y regeneración, donde la tierra termine más rica porque estamos ahí?**

Apuntá cualquier asistente de IA (Claude Code, Cursor, ChatGPT…) primero a `AGENTS.md`: lo convierte en el agente (rol, reglas, tono, método de revisión). El agente evalúa, como diseñador experto en permacultura, lo que Gus le va pasando.

## 1. La respuesta en 60 segundos

- **El agua manda**: ~200 mm de lluvia en pocas tormentas, un río grande y una napa poco profunda. El agua del cielo regenera la columna verde del escurrimiento; el agua con permiso del río o la napa alimenta casas y comida ([[04 - Agua en zonas áridas]]).
- **El primer masterplan de Martín va por buen camino**: guiado por el agua, columna verde sobre el escurrimiento principal, etapas desde el cono del río ([[07 - Revisión del masterplan 2026-10-15]]).
- **Los huecos más grandes**: caudales pico, derechos de agua, suelos, línea de base de vegetación.
- **Proporción ecológica con trinquete**: propuesta de Gus (a validar con el equipo): **arrancar en 10% y crecer por etapas hasta un tope de 50%**, sin bajar nunca ([[08 - Rewilding y proporción ecológica]]).
- **Medir antes de afirmar**: línea de base ahora, Libro C todos los años ([[09 - Monitoreo y Libro C]]).
- **Diseño regional, implementación de a una hectárea** (Maurício Umann, 16-oct): entender la región y las 10.000 ha de BioPueblo para diseñar bien las 1.000 y las 120; implementar 1 ha y crecer en Fibonacci; importar la materia orgánica del valle; regenerar como **rendimiento**, no como costo ([[16 - Estrategia fractal (de la región a la primera hectárea)]], [[17 - La regeneración como valor (las 300 razones)]]).
- **El agente marca, nunca decide** (borrador de Constitución, art. 12).

## 2. Mapa del vault

| # | Archivo | Qué te da |
|---|---|---|
| 00 | Léeme (este) | Cómo leer |
| — | `AGENTS.md` / `CLAUDE.md` | Rol, reglas y convenciones del agente |
| 01 | [[01 - Perfil del sitio (Lighthouse 7A)]] | Qué sabemos de la tierra, con qué certeza y qué falta |
| 02 | [[02 - Fundamentos de permacultura]] | Éticas, principios, zonas, sectores, escala de permanencia |
| 03 | [[03 - Método y secuencia de diseño]] | Dos relojes (legal / tierra), orden de diseño, etapas |
| 04 | [[04 - Agua en zonas áridas]] | Las dos aguas, técnicas, riesgos, balance |
| 05 | [[05 - Ecología del Monte (especies y hábitats)]] | Hábitats, paleta nativa, invasoras |
| 06 | [[06 - Suelo y técnicas de revegetación]] | Cómo establecer plantas; ensayos de la primera temporada |
| 07 | [[07 - Revisión del masterplan 2026-10-15]] | Revisión del masterplan preliminar de Martín |
| 08 | [[08 - Rewilding y proporción ecológica]] | Definiciones, referencias, la escalera 10% → 50% |
| 09 | [[09 - Monitoreo y Libro C]] | Protocolo de línea de base, indicadores, plantilla de balance hídrico |
| 10 | [[10 - Guía de revisión regenerativa]] | Los ocho filtros y la plantilla de salida |
| 11 | [[11 - Expertos y términos de referencia]] | A quién contratar, qué pedirle |
| 12 | [[12 - Glosario (ES-EN)]] | Palabras |
| 13 | [[13 - Preguntas abiertas y backlog]] | Decisiones, investigación, preguntas para Martín, respuestas de Gus |
| 14 | [[14 - Llamada 2026-10-15 Masterplanning Preliminar]] | Notas depuradas de la llamada |
| 15 | [[15 - Reunión 2026-10-16 con Maurício Umann (Fractal)]] | La visión regional del profesor del PDC, ordenada |
| 16 | [[16 - Estrategia fractal (de la región a la primera hectárea)]] | Niveles del fractal, secuencia de Fibonacci, primera hectárea, materia orgánica regional, animales |
| 17 | [[17 - La regeneración como valor (las 300 razones)]] | Regenerar como rendimiento; ventas en clusters; qué tiene que ser cierto |
| 18 | [[18 - Biblioteca del PDC]] | Lo aprendido de la biblioteca del curso, por tema, y el catálogo completo |
| 19 | [[19 - Visión regional para BioPueblo (borrador para los dueños)]] | Borrador del documento para los dueños de BioPueblo |
| — | `templates/` | Observación de campo, revisión de diseño, ficha de especie, ficha de intervención |
| — | `sources/` | Presentaciones, exportaciones GIS, datos; `sources/biblioteca-pdc/` tiene el catálogo y las notas destiladas del PDC |
| — | `private/` | Ignorada por git: transcripciones, contenido personal, portafolio confidencial de Fractal 🔒 |

## 3. Recorridos de lectura

| Si sos… | Leé | Tiempo |
|---|---|---|
| **Martín** | 07 → 13 (preguntas para Martín) → 01 → 04 → 08 → 03 | 30 min |
| **Todo el equipo** | Este Léeme → 07 "En un respiro" → 08 §3 → 13 §B | 15 min |
| **Dueños de BioPueblo / inversores** | 19 (borrador para ellos) → 17 → 16 §1–2 | 15 min |
| **Profesional de permacultura** | 01 → 07 → 11 (TdR A) → 05 | 30 min |
| **Nuevo en permacultura** | 02 → 12 → 04 §2 | 20 min |

## 4. Repositorio y colaboración

- Esta carpeta es un **vault de Obsidian** (abrí la carpeta como vault; los `[[links]]` funcionan) y un **repositorio git local**.
- Es un **repo privado en GitHub: `netxgen-2050/NS_permacultura`**. **Por ahora no se comparte** con el resto del equipo; Gus decide cuándo.
- `private/` está ignorada por git.

## 5. Vaults hermanos

- `../NS_Tokenomics/` — diseño de capital, borrador de Constitución y Derechos de la Naturaleza (17), brief RTMM (`sources/`).
- `../NS_platform/` — producto, investigación legal, KMZ/GeoJSON de BioPueblo.
- `../lighthouse-platform/` — la app (mapa del territorio, tribus, bienes comunes, Fogón).

## Fuentes y lógica usada

- Armado el 2026-10-15 a partir de la llamada de masterplanning, los vaults hermanos y bibliografía general de permacultura y zonas áridas; cada doc tiene sus propias fuentes.
- Reunión con Maurício Umann (Fractal), 2026-10-16, y biblioteca del PDC (carpeta «Permaculture to Share» de Drive).
- Respuestas de Gus del 2026-10-15 (idioma, rewilding, rol del agente, repo), registradas en [[13 - Preguntas abiertas y backlog]].
