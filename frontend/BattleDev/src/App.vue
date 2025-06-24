<template >
<div class="min-h-screen flex flex-col"  style="background-color: #1E1E2F">
<Navbar />

<div class="flex justify-center items-center center" style="height: 100vh;">
  <Start />
</div>
  
</div>
</template>
<script setup>
import Start from './components/Start.vue'
import Navbar from './components/Navbar.vue'

</script>