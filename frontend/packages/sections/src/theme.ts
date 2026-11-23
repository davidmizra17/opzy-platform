import { z } from "zod";

export const palettes = {
  default: { brand: "#0F766E", onBrand: "#FFFFFF", ink: "#111827", inkSoft: "#4B5563", surface: "#FFFFFF", surfaceMuted: "#F3F4F6" },
  warm: { brand: "#B45309", onBrand: "#FFFFFF", ink: "#1C1917", inkSoft: "#57534E", surface: "#FFFBF5", surfaceMuted: "#F5EDE3" },
  night: { brand: "#38BDF8", onBrand: "#0B1220", ink: "#F1F5F9", inkSoft: "#94A3B8", surface: "#0B1220", surfaceMuted: "#16213A" },
} as const;

export const fonts = {
  default: { display: "700 2.5rem/1.1 'Inter', system-ui, sans-serif", heading: "600 1.75rem/1.2 'Inter', system-ui, sans-serif", body: "400 1rem/1.6 'Inter', system-ui, sans-serif" },
  serif: { display: "700 2.75rem/1.1 'Fraunces', Georgia, serif", heading: "600 1.875rem/1.2 'Fraunces', Georgia, serif", body: "400 1rem/1.6 'Inter', system-ui, sans-serif" },
} as const;

const radii = { none: "0", sm: "6px", md: "12px", lg: "24px" } as const;

export const themeSchema = z.object({
  palette: z.enum(Object.keys(palettes) as [keyof typeof palettes, ...(keyof typeof palettes)[]]),
  font: z.enum(Object.keys(fonts) as [keyof typeof fonts, ...(keyof typeof fonts)[]]),
  radius: z.enum(["none", "sm", "md", "lg"]),
});

export type Theme = z.infer<typeof themeSchema>;

/** Convierte el tema del documento en variables CSS que usan todas las secciones. */
export function themeVars(theme: Theme): Record<string, string> {
  const p = palettes[theme.palette];
  const f = fonts[theme.font];
  return {
    "--color-brand": p.brand,
    "--color-on-brand": p.onBrand,
    "--color-ink": p.ink,
    "--color-ink-soft": p.inkSoft,
    "--color-surface": p.surface,
    "--color-surface-muted": p.surfaceMuted,
    "--font-display": f.display,
    "--font-heading": f.heading,
    "--font-body": f.body,
    "--radius": radii[theme.radius],
    "--space-xs": "0.25rem",
    "--space-sm": "0.5rem",
    "--space-md": "1rem",
    "--space-lg": "1.5rem",
    "--space-xl": "3rem",
  };
}
