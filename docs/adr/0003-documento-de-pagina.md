# 0003 · Las páginas son documentos JSON sobre una librería de secciones

**Estado:** aceptada

## Decisión
El agente nunca genera HTML. Edita un documento de página en JSON que solo puede usar las secciones del catálogo.

- `frontend/packages/sections` define cada sección: componente Vue, esquema de props (Zod) y descripción.
- `pnpm --filter @opzy/sections build:catalog` genera:
  - `catalog.json`: lo que el agente puede usar (tipos, campos, variantes, descripciones).
  - `page-document.schema.json`: JSON Schema del documento completo.
- Ambos se copian a `backend/apps/pages/schema/`. El backend valida cada cambio contra ese esquema antes de guardarlo.
- El agente edita con la herramienta `update_page`, que recibe operaciones JSON Patch.
- Cada cambio válido crea una versión nueva e inmutable. Deshacer es volver a una versión anterior.
- El widget dibuja el documento con `@opzy/renderer`; el publisher usa el mismo paquete con el renderizado del servidor de Vue. Lo que el cliente aprueba es lo que se publica.
- Cada documento guarda la versión de la librería con la que se creó (`library`).

## Regla de hechos
El texto que escribe el agente sale solo de datos que dio el cliente. Lo que falta se muestra como placeholder; nunca se inventan horarios, precios ni testimonios.
