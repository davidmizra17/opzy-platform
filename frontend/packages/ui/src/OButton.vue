<script setup lang="ts">
withDefaults(defineProps<{ variant?: "primary" | "secondary"; type?: "button" | "submit" }>(), {
  variant: "primary",
  type: "button",
});
</script>

<template>
  <button :type="type" class="o-button" :class="variant"><slot /></button>
</template>

<style scoped>
.o-button { height: 44px; padding: 0 1rem; border-radius: 12px; font-weight: 600; cursor: pointer; border: 1px solid transparent; }
.primary { background: #0f766e; color: #fff; }
.secondary { background: #fff; color: #111827; border-color: #e5e7eb; }
</style>
