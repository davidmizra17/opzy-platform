import { LIBRARY_VERSION, type PageDocument } from "@opzy/sections";

/** Documento de ejemplo mientras se conecta el agente. Solo datos de muestra. */
export const demoDocument: PageDocument = {
  library: LIBRARY_VERSION,
  locale: "es",
  theme: { palette: "warm", font: "serif", radius: "md" },
  sections: [
    {
      id: "hero",
      type: "hero-split",
      props: {
        variant: "image-right",
        headline: "Panadería Sol",
        subheadline: "Pan artesanal en tu barrio",
        cta: { label: "Pedir por WhatsApp", action: "whatsapp" },
      },
    },
    {
      id: "services",
      type: "services-grid",
      props: {
        title: "Lo que hacemos",
        columns: 3,
        items: [{ name: "Pan del día" }, { name: "Tortas por encargo" }, { name: "Desayunos" }],
      },
    },
    { id: "contact", type: "contact", props: { title: "Contáctanos" } },
  ],
};
