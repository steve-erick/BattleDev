<template>
  <div class="relative inline-block text-left">
    <!-- Botão de seleção -->
    <button @click="open = !open" class="inline-flex items-center px-4 py-2 bg-white text-black rounded shadow w-64">
      <img :src="selected.image" alt="" class="w-5 h-5 mr-2" />
      {{ selected.name }}
      <svg class="ml-auto w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </button>

    <!-- Dropdown -->
    <div v-if="open" class="absolute z-10 mt-2 w-48 bg-white rounded shadow">
      <ul>
        <li
          v-for="lang in languages"
          :key="lang.name"
          @click="selectLanguage(lang)"
          class="flex items-center px-4 py-2 hover:bg-gray-100 cursor-pointer"
        >
          <img :src="lang.image" alt="" class="w-5 h-5 mr-2" />
          {{ lang.name }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const open = ref(false)

const languages = [
  { name: 'Python', image: new URL('../assets/python.png', import.meta.url).href },
  { name: 'JavaScript', image: new URL('../assets/js.png', import.meta.url).href },
  { name: 'C++', image: new URL('../assets/cpp.png', import.meta.url).href }
]

const selected = ref(languages[0])

function selectLanguage(lang) {
  selected.value = lang
  open.value = false
}
</script>

<style scoped>
/* Estilo extra opcional (se quiser animação ou transições no dropdown) */
</style>
