<script setup lang="ts">
import ChatPanel from "./components/ChatPanel.vue";
import PreviewPane from "./components/PreviewPane.vue";
import { demoDocument } from "./demo-document";
</script>

<template>
  <main class="layout">
    <section class="chat-col" aria-label="Chat"><ChatPanel /></section>
    <section class="preview-col" aria-label="Vista previa"><PreviewPane :document="demoDocument" /></section>
  </main>
</template>

<style>
html, body, #app { height: 100%; margin: 0; font-family: system-ui, sans-serif; color: #111827; }
.layout { display: grid; grid-template-columns: 1fr; height: 100%; }
.chat-col { border-right: 1px solid #e5e7eb; min-height: 0; }
.preview-col { padding: 1rem; min-height: 0; background: #fafafa; }
@media (min-width: 900px) { .layout { grid-template-columns: 380px 1fr; } }
@media (max-width: 899px) { .preview-col { display: none; } }
</style>
