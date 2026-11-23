import { defineAsyncComponent, type Component } from "vue";
import type { SectionType } from "./definitions";

/**
 * Tipo de sección -> componente Vue, cargado bajo demanda.
 * Una página con 4 secciones descarga solo esos 4 componentes.
 */
const loaders: Record<SectionType, () => Promise<{ default: Component }>> = {
  "hero-split": () => import("./sections/hero-split/HeroSplit.vue"),
  "services-grid": () => import("./sections/services-grid/ServicesGrid.vue"),
  contact: () => import("./sections/contact/Contact.vue"),
};

const cache = new Map<string, Component>();

export function sectionComponent(type: string): Component | undefined {
  if (!(type in loaders)) return undefined;
  if (!cache.has(type)) {
    cache.set(type, defineAsyncComponent(loaders[type as SectionType]));
  }
  return cache.get(type);
}
