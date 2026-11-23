# @opzy/sections

La librería de secciones es el producto: cada página de cliente se ve tan bien como estas secciones.

## Agregar una sección

1. Crear `src/sections/<tipo>/definition.ts` con `defineSection` (tipo, descripción para el agente, esquema de props).
2. Crear el componente `src/sections/<tipo>/<Nombre>.vue` usando solo las variables CSS del tema.
3. Registrarla en `src/definitions.ts` y en `src/registry.ts`.
4. Correr `pnpm build:catalog` y commitear también `backend/apps/pages/schema/`.

## Reglas

- Cambios compatibles hacia atrás: agregar variantes o campos opcionales, nunca cambiar el significado de uno existente.
- Subir `LIBRARY_VERSION` en cada cambio de esquema.
- Ningún texto inventado en los componentes: si falta un dato, la sección lo omite o muestra un placeholder neutro.
