<script setup lang="ts">
import { ref } from "vue";
import { OButton } from "@opzy/ui";

type Msg = { role: "client" | "agent"; text: string };

const messages = ref<Msg[]>([
  { role: "agent", text: "Hola. Cuéntanos qué está frenando tu negocio, con tus palabras." },
]);
const draft = ref("");

function send() {
  const text = draft.value.trim();
  if (!text) return;
  messages.value.push({ role: "client", text });
  draft.value = "";
  // TODO(fase-1): enviar a /api/v1/public/conversations/{id}/messages y leer la respuesta por SSE.
}
</script>

<template>
  <div class="chat">
    <ol class="log" aria-live="polite">
      <li v-for="(m, i) in messages" :key="i" :class="m.role">{{ m.text }}</li>
    </ol>
    <form class="composer" @submit.prevent="send">
      <label class="sr-only" for="msg">Mensaje</label>
      <input id="msg" v-model="draft" placeholder="Escribe tu mensaje…" autocomplete="off" />
      <OButton type="submit">Enviar</OButton>
    </form>
  </div>
</template>

<style scoped>
.chat { display: flex; flex-direction: column; height: 100%; }
.log { flex: 1; overflow: auto; list-style: none; margin: 0; padding: 1rem; display: flex; flex-direction: column; gap: 0.5rem; }
.log li { max-width: 85%; padding: 0.625rem 0.875rem; border-radius: 16px; line-height: 1.4; }
.log li.agent { background: #f3f4f6; align-self: flex-start; border-bottom-left-radius: 4px; }
.log li.client { background: #0f766e; color: #fff; align-self: flex-end; border-bottom-right-radius: 4px; }
.composer { display: flex; gap: 0.5rem; padding: 0.75rem; border-top: 1px solid #e5e7eb; }
.composer input { flex: 1; height: 44px; padding: 0 0.875rem; border-radius: 22px; border: 1px solid #e5e7eb; background: #f3f4f6; }
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
</style>
