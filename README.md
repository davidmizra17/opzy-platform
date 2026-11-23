# OPZY Platform

Widget de IA que diagnostica lo que necesita cada pyme y construye su landing page por chat, a partir de una librería de secciones en Vue.

Monorepo con el backend (Django), los front ends (Vue + TypeScript), el worker de publicación y la infraestructura.

## Estructura

```
backend/      Django + DRF: API pública, agente de triage, páginas, pagos
frontend/     Workspace pnpm
  apps/landing      Landing page de OPZY
  apps/widget       Chat de intake + vista previa en vivo
  packages/sections Librería de secciones (Vue) + catalog.json
  packages/renderer PageRenderer: dibuja un documento de página
  packages/ui       Componentes compartidos
  packages/api-client Cliente TypeScript generado desde OpenAPI
publisher/    Worker Node: documento de página -> HTML estático -> S3
infra/        Infraestructura como código (AWS)
docs/         Decisiones de arquitectura (ADR)
```

## Cómo funciona

1. El cliente describe su negocio en el widget.
2. El agente de triage construye el registro del problema y elige una ruta (construir, resolver, otro).
3. En la ruta "construir", el agente edita un **documento de página** (JSON) usando solo las secciones del catálogo.
4. El backend valida cada cambio contra el esquema y guarda una versión nueva.
5. El widget dibuja el documento en vivo con las mismas secciones Vue.
6. Al aprobar y pagar, el publisher renderiza el documento a HTML estático y lo sube a S3.

El agente nunca escribe HTML: solo JSON validado. Ver `docs/adr/`.

## Requisitos

- Python 3.12 y [uv](https://docs.astral.sh/uv/)
- Node 22 y pnpm 9 (`corepack enable`)
- Docker (Postgres y Redis en local)

## Desarrollo local

```bash
cp .env.example .env
docker compose up -d db redis

# Backend
cd backend
uv sync
uv run python manage.py migrate
uv run python manage.py runserver

# Front ends (otra terminal)
cd frontend
pnpm install
pnpm --filter @opzy/sections build:catalog
pnpm --filter @opzy/widget dev
```

## Comandos útiles

| Comando | Dónde | Qué hace |
| --- | --- | --- |
| `uv run pytest` | backend | Tests |
| `uv run lint-imports` | backend | Verifica los límites entre módulos |
| `uv run ruff check .` | backend | Lint |
| `pnpm -r typecheck` | frontend | Verificación de tipos |
| `pnpm --filter @opzy/sections build:catalog` | frontend | Genera `catalog.json` y el JSON Schema del documento de página |

## Fases

1. **Intake y páginas** (en curso)
2. Portal del cliente
3. CRM para clientes
4. Back office y dashboards
