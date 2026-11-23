<script setup lang="ts">
import type { HeroSplitProps } from "./definition";

const props = defineProps<HeroSplitProps>();
</script>

<template>
  <section class="hero" :class="props.variant">
    <div class="copy">
      <h1>{{ props.headline || "Tu titular aquí" }}</h1>
      <p v-if="props.subheadline">{{ props.subheadline }}</p>
      <a class="cta" :data-action="props.cta.action">{{ props.cta.label }}</a>
    </div>
    <div class="media" :data-image="props.imageId ?? ''" aria-hidden="true" />
  </section>
</template>

<style scoped>
.hero {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-lg);
  padding: var(--space-xl) var(--space-lg);
  align-items: center;
}
@media (min-width: 768px) {
  .hero { grid-template-columns: 1fr 1fr; }
  .hero.image-left .media { order: -1; }
}
h1 { font: var(--font-display); color: var(--color-ink); margin: 0 0 var(--space-sm); }
p { color: var(--color-ink-soft); margin: 0 0 var(--space-md); }
.cta {
  display: inline-block;
  padding: var(--space-sm) var(--space-md);
  border-radius: var(--radius);
  background: var(--color-brand);
  color: var(--color-on-brand);
  font-weight: 600;
  text-decoration: none;
}
.media {
  aspect-ratio: 4 / 3;
  border-radius: var(--radius);
  background: var(--color-surface-muted);
}
</style>
