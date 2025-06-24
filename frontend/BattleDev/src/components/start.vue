<template>
    <div class="grid grid-cols-2 gap-6 bg-gray-800 rounded-2xl p-8 w-4/5 max-w-6xl shadow-lg">
      
      <!-- Coluna 1 - Personagem -->
      <div class="flex flex-col items-center justify-center">
        <img src="../assets/image-removebg-preview (15).png" alt="Personagem" class="w-lg" />
      </div>

      <!-- Coluna 2 - Info + Botões -->
      <div class="flex flex-col justify-center space-y-6 text-white">
        
        <!-- Seletor de linguagem -->
        <div  class="flex justify-center" style="width: 100%;">
          <dropdown />
        </div>

        <!-- Botões -->
        <div class="flex space-x-4 gap-3 justify-center">
          <button class="btn btn-secondary px-5" style="border-radius: 100px;">Ranked</button>
          <button class="btn btn-secondary px-5" style="border-radius: 100px;">Train</button>
        </div>

        <!-- Rank Progress -->
        <div class="flex items-center space-x-4">
          <img src="../assets/image-removebg-preview (16).png" alt="Rank" class="w-72 h-72" />
          <span>2 matches to new rank</span>
        </div>

      </div>
    </div>
</template>

<script setup>
// vazio por enquanto
import Dropdown from './Dropdown.vue'
</script>

<style scoped>
/* Estilo adicional se quiser */
/* Exemplo: ajustar o select caso queira mais bonito */
</style>
