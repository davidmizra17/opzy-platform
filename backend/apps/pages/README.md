# pages

Documento de página, versiones y publicación. Arquitectura limpia (ver `docs/adr/0002` y `0003`).

```
domain/          Python puro: aplicar cambios, validar contra el esquema, regla de hechos
application/     Casos de uso (create_page, update_page, revert_page) y puertos
infrastructure/  Modelos Django y repositorio
interfaces/      Vistas DRF y la herramienta update_page para el agente
schema/          catalog.json y page-document.schema.json, generados desde frontend/packages/sections
```

Todo cambio de estado de una página pasa por un caso de uso, venga de la vista, del agente o del admin.
