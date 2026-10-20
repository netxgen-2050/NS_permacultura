# 🌱 Agente de Regeneración · Lighthouse VRN

**Un agente de IA experto en permacultura para diseñar la regeneración de Lighthouse** (~1.000 ha sobre el río Negro, Mainqué, Patagonia, dentro de BioPueblo).

Este repo es su "cerebro": un vault de documentos en Markdown, en español, que cualquier IA puede leer para trabajar como el agente. Se puede abrir también con Obsidian.

---

## Qué hace

El agente **observa, informa, pregunta y marca. Nunca decide.** Revisa lo que le muestres (un masterplan, una idea, un presupuesto, una foto del campo) como lo haría un diseñador de permacultura y te dice:

- qué está bien y por qué;
- qué rompe alguna de las reglas del proyecto;
- qué dato falta medir antes de afirmar algo;
- qué preguntas conviene llevarle al equipo o a un experto.

Las decisiones son del equipo.

## Las 8 reglas que no se negocian

1. **El agua primero.** Nada se diseña sin saber de dónde viene y adónde va el agua.
2. **La franja del río y el cauce son un bien común.** No se lotean.
3. **Sin pérdida de suelo.**
4. **Nativas, sin invasoras.** Nunca tamarisco (*Tamarix*) ni olivillo (*Elaeagnus*).
5. **Sin biocidas ni vertidos.** Nada llega al río.
6. **Proporción ecológica de 10% a 50%, con trinquete.** Arranca en 10%, sube hasta 50% y nunca baja.
7. **Medir antes de afirmar.** *El dato que falta no es cero.*
8. **Coherencia con la tokenomics de NetX Gen y la Ordenanza 173.** No se comercializa nada antes de la aprobación municipal.

## Qué sabe

| Tema | Dónde |
|---|---|
| El sitio: suelo, clima, agua, el cono, la barda, la planicie | `01` |
| Fundamentos y método de diseño en permacultura | `02`, `03`, `10` |
| Agua en zonas áridas (~200 mm de lluvia por año) | `04` |
| Ecología del Monte: especies nativas y hábitats | `05` |
| Suelo y técnicas de revegetación | `06` |
| Masterplan preliminar de Martín (presentación, zonas, etapa 1, clima) y su revisión | `07`, `14`, `sources/martin/` |
| Rewilding y proporción ecológica | `08` |
| Monitoreo (el Libro C) | `09` |
| Expertos a contratar y términos de referencia | `11` |
| Glosario español-inglés | `12` |
| Preguntas abiertas y backlog | `13` |
| Diseño regional y estrategia fractal | `15`, `16`, `17` |
| Biblioteca del curso de permacultura (PDC) | `18`, `sources/biblioteca-pdc/` |

### La biblioteca del PDC
El agente tiene catalogada la biblioteca completa de un curso de diseño en permacultura: ~7.500 archivos con manuales, libros y fichas. Leyó unos 150 de esos documentos y los resumió en cinco notas: **agua**, **suelo, compost y carbono**, **núcleo y método de diseño**, **animales y pastoreo**, y **diseño social y biorregión**. Algunos aprendizajes que aplica:

- **En 200 mm, el agua se concentra**: el escurrimiento de un área grande se lleva a un área ~10 veces más chica.
- **Los caminos son la primera obra de agua.**
- **El pastoreo holístico no tiene evidencia con ~200 mm.** Va como experimento con parcelas testigo, no como receta.
- Las fuentes clásicas a veces chocan con las reglas (Mollison recomienda *Tamarix* para zonas secas). Cuando pasa, el agente lo marca.

### La mirada regional
Una conversación con Maurício Umann (Fractal, Portugal), diseñador y docente de permacultura, sumó ideas que hoy son centrales en el vault:

- **Es un diseño regional, no de un terreno.** Para diseñar bien las 120 ha hay que entender las 1.000 ha de Lighthouse, y para eso las ~10.000 ha de BioPueblo y todo el valle.
- **Se diseña todo, pero se implementa 1 ha.** Después se crece siguiendo la secuencia de Fibonacci (1, 1, 2, 3, 5, 8…) y aprendiendo cada año: unas 34 ha en ~7 años, con un oasis que se puede recorrer.
- **La fertilidad se trae del valle:** poda de frutales que hoy se quema, descarte de fruta, orujo, estiércol y restos de comida.
- **Se vende en clusters de ~16 familias.** Cada cluster financia su propia regeneración y aporta a un fondo común del ecosistema.
- **Regenerar es rendimiento, no costo.** Un lote con "100 razones" pasa a tener "300 razones".

## Cómo se lee lo que dice

Cada afirmación lleva una marca de confianza:

| Marca | Significa |
|---|---|
| **[C]** | Confirmado (medido o documentado) |
| **[S]** | Tiene fuente citada |
| **[NC]** | No confirmado: estimación o dicho en una reunión |
| **[criterio]** | Juicio del agente o de un experto |
| **[verificar]** | Hay que chequearlo antes de usarlo |

## Cómo usarlo con tu IA

**Claude Code, Codex, Cursor u otro agente que trabaje sobre carpetas:** cloná el repo y abrí la carpeta. El agente lee solo `CLAUDE.md` o `AGENTS.md` y entra en el rol.

```bash
git clone https://github.com/netxgen-2050/NS_permacultura.git
```

**ChatGPT, Claude.ai, Gemini u otro chat:** conectá este repo de GitHub a un proyecto, o subí `AGENTS.md`, `00 - Léeme.md` y los docs que te interesen. Empezá con:

> Leé AGENTS.md y actuá como el Agente de Regeneración de Lighthouse.

**Preguntas para arrancar:**
- "Revisá este sector del masterplan contra las 8 reglas."
- "¿Dónde pondrías la primera hectárea y por qué?"
- "¿Qué datos faltan para dimensionar el escurrimiento del cono?"
- "¿Qué especies nativas usarías para un rompevientos en la barda?"

## Cómo aportar

- Para orientarte, empezá por `00 - Léeme.md`: es el mapa del vault.
- En `templates/` hay fichas para observaciones de campo, intervenciones, especies y revisiones de diseño.
- Los datos nuevos (presentaciones, capas GIS, fotos, análisis de suelo o agua) van en `sources/`. Después se le pide al agente que actualice los docs que correspondan.
- Las preguntas y los pendientes viven en `13 - Preguntas abiertas y backlog.md`.

---

*Parte del ecosistema NetX Gen. Repo privado; no compartir fuera del equipo.*
