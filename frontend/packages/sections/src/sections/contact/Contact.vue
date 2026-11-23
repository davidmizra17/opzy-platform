<script setup lang="ts">
import type { ContactProps } from "./definition";

const props = defineProps<ContactProps>();
</script>

<template>
  <section class="contact">
    <h2>{{ props.title }}</h2>
    <dl>
      <template v-if="props.whatsapp"><dt>WhatsApp</dt><dd>{{ props.whatsapp }}</dd></template>
      <template v-if="props.phone"><dt>Teléfono</dt><dd>{{ props.phone }}</dd></template>
      <template v-if="props.address"><dt>Dirección</dt><dd>{{ props.address }}</dd></template>
      <template v-if="props.hours"><dt>Horario</dt><dd>{{ props.hours }}</dd></template>
    </dl>
  </section>
</template>

<style scoped>
.contact { padding: var(--space-xl) var(--space-lg); background: var(--color-surface-muted); }
h2 { font: var(--font-heading); color: var(--color-ink); margin: 0 0 var(--space-md); }
dl { display: grid; grid-template-columns: max-content 1fr; gap: var(--space-xs) var(--space-md); margin: 0; }
dt { color: var(--color-ink-soft); }
dd { margin: 0; color: var(--color-ink); }
</style>
