import { z } from "zod";
import { defineSection } from "../../types";

export interface ContactProps {
  title: string;
  whatsapp?: string;
  phone?: string;
  address?: string;
  hours?: string;
}

export const contact = defineSection({
  type: "contact",
  description:
    "Datos de contacto y horario. Solo incluir los datos que dio el cliente; los que falten se omiten.",
  props: z.object({
    title: z.string().max(60).default("Contáctanos"),
    whatsapp: z.string().max(32).optional(),
    phone: z.string().max(32).optional(),
    address: z.string().max(160).optional(),
    hours: z.string().max(120).optional(),
  }) satisfies z.ZodType<ContactProps, z.ZodTypeDef, unknown>,
});
