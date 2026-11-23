import { z } from "zod";
import { sectionDefinitions } from "./definitions";
import { themeSchema } from "./theme";

const sectionInstances = sectionDefinitions.map((def) =>
  z.object({
    id: z.string().min(1).max(40),
    type: z.literal(def.type),
    props: def.props,
  }),
);

/** Esquema del documento de página. El backend valida contra su versión en JSON Schema. */
export const pageDocumentSchema = z.object({
  library: z.string(),
  locale: z.enum(["es", "en"]),
  theme: themeSchema,
  sections: z
    .array(z.discriminatedUnion("type", sectionInstances as unknown as [typeof sectionInstances[number], ...typeof sectionInstances]))
    .max(12),
});

export type PageDocument = z.infer<typeof pageDocumentSchema>;
export type SectionInstance = PageDocument["sections"][number];
