import { z } from "zod";
import { defineSection } from "../../types";

/** Props del componente. El compilador de Vue necesita una interfaz explícita. */
export interface HeroSplitProps {
  variant: "image-left" | "image-right";
  headline: string;
  subheadline?: string;
  imageId?: string;
  cta: { label: string; action: "whatsapp" | "call" | "form" };
}

export const heroSplit = defineSection({
  type: "hero-split",
  description:
    "Titular grande junto a una foto. Ideal para servicios, restaurantes y comercios locales. Va primero en la página.",
  props: z.object({
    variant: z.enum(["image-left", "image-right"]).default("image-right"),
    headline: z.string().max(80).describe("Titular principal. Solo con datos del cliente."),
    subheadline: z.string().max(160).optional(),
    imageId: z.string().optional().describe("ID de un asset subido por el cliente."),
    cta: z.object({
      label: z.string().max(30),
      action: z.enum(["whatsapp", "call", "form"]),
    }),
  }) satisfies z.ZodType<HeroSplitProps, z.ZodTypeDef, unknown>,
});
