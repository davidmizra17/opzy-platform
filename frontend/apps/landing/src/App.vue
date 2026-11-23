<script setup lang="ts">
import { OButton } from "@opzy/ui";
</script>

<template>
  <main class="hero">
    <h1>Cuéntanos qué está frenando tu negocio</h1>
    <p>Descríbelo con tus palabras. En minutos te mostramos cómo resolverlo.</p>
    <!-- TODO(fase-1): abrir el widget embebido. -->
    <OButton>Empezar</OButton>
  </main>
</template>

<style>
body { margin: 0; font-family: system-ui, sans-serif; color: #111827; }
.hero { max-width: 720px; margin: 0 auto; padding: 6rem 1.5rem; }
.hero h1 { font-size: 2.5rem; line-height: 1.1; margin: 0 0 1rem; }
.hero p { color: #4b5563; margin: 0 0 2rem; }
</style>
