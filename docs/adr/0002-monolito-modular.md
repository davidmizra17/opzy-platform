# 0002 · Monolito modular en Django

**Estado:** aceptada

## Decisión
Un proyecto Django con una app por módulo (`identity`, `tracking`, `conversations`, `triage`, `catalog`, `billing`, `pages`). Reglas:

- Cada app expone su API interna en `services.py`. Ninguna app importa los modelos de otra.
- Los cambios de estado importantes pasan por casos de uso, sin importar quién los llame (vista, tarea de Celery, acción de admin).
- Los servicios externos (LLM, pagos, almacenamiento) se usan a través de adaptadores.
- `import-linter` verifica los límites en CI (`uv run lint-imports`).

Arquitectura limpia completa (`domain/`, `application/`, `infrastructure/`, `interfaces/`) solo en los módulos con lógica rica: `triage` y `pages`. El resto usa Django directo.

## Procesos
API, workers de Celery y scheduler se ejecutan desde la misma imagen como servicios separados.
