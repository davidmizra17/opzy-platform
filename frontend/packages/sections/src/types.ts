import type { z } from "zod";

/**
 * Definición de una sección. No importa el componente Vue: así el script del
 * catálogo y el backend pueden leerla sin compilar SFCs.
 */
export interface SectionDefinition<TType extends string = string, TProps extends z.ZodTypeAny = z.ZodTypeAny> {
  type: TType;
  /** Para el agente: qué es y cuándo usarla. */
  description: string;
  /** Esquema de props. Es el contrato con el agente y con el backend. */
  props: TProps;
}

export function defineSection<TType extends string, TProps extends z.ZodTypeAny>(
  def: SectionDefinition<TType, TProps>,
): SectionDefinition<TType, TProps> {
  return def;
}
