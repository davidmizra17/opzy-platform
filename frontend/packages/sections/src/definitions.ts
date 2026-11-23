import { contact } from "./sections/contact/definition";
import { heroSplit } from "./sections/hero-split/definition";
import { servicesGrid } from "./sections/services-grid/definition";

/** Todas las secciones disponibles. Agregar una nueva aquí y en registry.ts. */
export const sectionDefinitions = [heroSplit, servicesGrid, contact] as const;

export type SectionType = (typeof sectionDefinitions)[number]["type"];

/** Versión de la librería. Subirla al cambiar secciones; los cambios deben ser compatibles. */
export const LIBRARY_VERSION = "0.1.0";
