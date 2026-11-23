/**
 * Genera, desde las definiciones de secciones:
 *  - dist/catalog.json: lo que el agente puede usar (tipos, descripciones, campos).
 *  - dist/page-document.schema.json: JSON Schema del documento completo.
 * Y copia ambos a backend/apps/pages/schema/, donde el backend valida cada cambio.
 */
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { zodToJsonSchema } from "zod-to-json-schema";
import { LIBRARY_VERSION, sectionDefinitions } from "../src/definitions";
import { pageDocumentSchema } from "../src/document";
import { fonts, palettes } from "../src/theme";

const here = dirname(fileURLToPath(import.meta.url));
const distDir = resolve(here, "../dist");
const backendDir = resolve(here, "../../../../backend/apps/pages/schema");

const catalog = {
  library: LIBRARY_VERSION,
  theme: {
    palettes: Object.keys(palettes),
    fonts: Object.keys(fonts),
    radius: ["none", "sm", "md", "lg"],
  },
  sections: sectionDefinitions.map((def) => ({
    type: def.type,
    description: def.description,
    props: zodToJsonSchema(def.props, { target: "jsonSchema2019-09", $refStrategy: "none" }),
  })),
};

const { $schema: _ignored, ...pageSchema } = zodToJsonSchema(pageDocumentSchema, {
  target: "jsonSchema2019-09",
  $refStrategy: "none",
}) as Record<string, unknown>;
const output = { $schema: "https://json-schema.org/draft/2020-12/schema", ...pageSchema };

for (const dir of [distDir, backendDir]) {
  mkdirSync(dir, { recursive: true });
  writeFileSync(resolve(dir, "catalog.json"), JSON.stringify(catalog, null, 2) + "\n");
  writeFileSync(resolve(dir, "page-document.schema.json"), JSON.stringify(output, null, 2) + "\n");
}

console.log(`Catálogo ${LIBRARY_VERSION}: ${catalog.sections.length} secciones -> dist/ y backend/apps/pages/schema/`);
