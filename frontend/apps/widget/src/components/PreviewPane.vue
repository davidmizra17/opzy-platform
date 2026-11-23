<script setup lang="ts">
import { ref } from "vue";
import { PageRenderer } from "@opzy/renderer";
import type { PageDocument } from "@opzy/sections";

defineProps<{ document: PageDocument }>();
const device = ref<"mobile" | "desktop">("mobile");
</script>

<template>
  <div class="preview">
    <div class="toolbar" role="group" aria-label="Tamaño de la vista previa">
      <button :aria-pressed="device === 'mobile'" @click="device = 'mobile'">Celular</button>
      <button :aria-pressed="device === 'desktop'" @click="device = 'desktop'">Escritorio</button>
    </div>
    <div class="frame" :class="device">
      <!-- TODO(fase-1): renderizar dentro de un iframe para aislar estilos del widget. -->
      <PageRenderer :document="document" />
    </div>
  </div>
</template>

<style scoped>
.preview { display: flex; flex-direction: column; gap: 0.75rem; height: 100%; }
.toolbar { display: flex; gap: 0.5rem; }
.toolbar button { padding: 0.25rem 0.75rem; border-radius: 999px; border: 1px solid #e5e7eb; background: #fff; cursor: pointer; }
.toolbar button[aria-pressed="true"] { background: #111827; color: #fff; }
.frame { flex: 1; overflow: auto; border: 1px solid #e5e7eb; border-radius: 16px; margin: 0 auto; width: 100%; }
.frame.mobile { max-width: 390px; }
.frame.desktop { max-width: 1200px; }
</style>
