# 0001 · Monorepo para backend, front ends y publisher

**Estado:** aceptada

## Contexto
El documento de página lo validan el backend, lo dibujan el widget y el publisher, y lo define la librería de secciones. Un cambio de esquema toca las cuatro partes.

## Decisión
Un solo repositorio. Cada parte se construye y despliega por separado; CI decide qué correr según la carpeta que cambió.

## Consecuencias
- Un cambio de esquema es un solo commit.
- El cliente TypeScript se genera desde el OpenAPI del backend en el mismo repo.
- Hay que mantener los workflows de CI filtrados por ruta.
