<script setup lang="ts">
import type { ServicesGridProps } from "./definition";

const props = defineProps<ServicesGridProps>();
</script>

<template>
  <section class="services">
    <h2>{{ props.title }}</h2>
    <ul :style="{ '--cols': props.columns }">
      <li v-for="item in props.items" :key="item.name">
        <h3>{{ item.name }}</h3>
        <p v-if="item.description">{{ item.description }}</p>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.services { padding: var(--space-xl) var(--space-lg); }
h2 { font: var(--font-heading); color: var(--color-ink); margin: 0 0 var(--space-lg); }
ul {
  list-style: none; margin: 0; padding: 0;
  display: grid; gap: var(--space-md);
  grid-template-columns: 1fr;
}
@media (min-width: 768px) { ul { grid-template-columns: repeat(var(--cols), 1fr); } }
li { padding: var(--space-md); border-radius: var(--radius); background: var(--color-surface-muted); }
h3 { margin: 0 0 var(--space-xs); color: var(--color-ink); }
p { margin: 0; color: var(--color-ink-soft); }
</style>
