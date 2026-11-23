/**
 * Pendiente (Fase 1): renderizar un documento validado a HTML estático.
 *
 * Plan:
 * 1. Compilar @opzy/renderer y @opzy/sections con Vite en modo SSR (los .vue no corren en Node sin compilar).
 * 2. createSSRApp(PageRenderer, { document }) + renderToString de vue/server-renderer.
 * 3. Extraer el CSS de las secciones usadas y armar el HTML con pageShell().
 * 4. Subir a s3://$PUBLISH_BUCKET/sites/<subdominio>/v<versión>/ y mover el puntero "live".
 */
import { readFileSync } from "node:fs";
import { pageDocumentSchema } from "@opzy/sections";

const path = process.argv[2];
if (!path) {
  console.error("Uso: pnpm render <documento.json>");
  process.exit(1);
}

const result = pageDocumentSchema.safeParse(JSON.parse(readFileSync(path, "utf8")));
if (!result.success) {
  console.error(result.error.format());
  process.exit(1);
}
console.log(`Documento válido: ${result.data.sections.length} secciones. Render SSR pendiente.`);
