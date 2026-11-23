<script setup lang="ts">
import { computed } from "vue";
import { themeVars, type PageDocument } from "@opzy/sections";
import { sectionComponent } from "@opzy/sections/registry";

const props = defineProps<{ document: PageDocument }>();

const style = computed(() => ({
  ...themeVars(props.document.theme),
  background: "var(--color-surface)",
  font: "var(--font-body)",
  color: "var(--color-ink)",
  minHeight: "100%",
}));
</script>

<template>
  <div class="opzy-page" :style="style" :lang="props.document.locale">
    <template v-for="section in props.document.sections" :key="section.id">
      <component :is="sectionComponent(section.type)" v-if="sectionComponent(section.type)" v-bind="section.props" />
    </template>
  </div>
</template>
