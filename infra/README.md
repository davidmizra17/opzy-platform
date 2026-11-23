# Infraestructura

Infraestructura como código para AWS. Pendiente de la tarea de infraestructura de la Fase 1.

Recursos previstos:

- ECS Fargate: servicio `api`, servicio `worker` (Celery) y `scheduler` (Celery beat), misma imagen.
- RDS PostgreSQL y ElastiCache Redis.
- S3 + CloudFront: widget, landing y sitios publicados de clientes (un subdominio por sitio).
- Secrets Manager para claves (LLM, pagos).
- Dos entornos idénticos: `staging` y `production`.
