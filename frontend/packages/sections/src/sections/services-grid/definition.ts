import { z } from "zod";
import { defineSection } from "../../types";

export interface ServicesGridProps {
  title: string;
  columns: 2 | 3;
  items: { name: string; description?: string }[];
}

export const servicesGrid = defineSection({
  type: "services-grid",
  description: "Lista de servicios o productos en tarjetas. Usar los servicios que nombró el cliente.",
  props: z.object({
    title: z.string().max(60),
    columns: z.union([z.literal(2), z.literal(3)]).default(3),
    items: z
      .array(
        z.object({
          name: z.string().max(50),
          description: z.string().max(140).optional(),
        }),
      )
      .min(1)
      .max(8),
  }) satisfies z.ZodType<ServicesGridProps, z.ZodTypeDef, unknown>,
});
