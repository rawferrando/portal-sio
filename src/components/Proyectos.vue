<script setup>
import { ref, onMounted } from 'vue'

const listaProyectos = ref([])
const cargando = ref(true)

onMounted(() => {
  // Simulamos carga de base de datos
  setTimeout(() => {
    listaProyectos.value = [
      { id: 1, titulo: "Proyecto OBSEA", desc: "Mantenimiento de sensores.", estado: "Activo" },
      { id: 2, titulo: "Campaña NEREIDA", desc: "Fondeos profundos.", estado: "Finalizado" }
    ]
    cargando.value = false
  }, 1000)
})
</script>

<template>
  <div class="seccion-proyectos">
    <button @click="$emit('volver')" class="btn-v">⬅ Volver</button>
    <h1>Proyectos SIO</h1>
    
    <div v-if="cargando">Cargando base de datos...</div>
    
    <div v-else class="grid">
      <div v-for="p in listaProyectos" :key="p.id" class="card">
        <h3>{{ p.titulo }}</h3>
        <p>{{ p.desc }}</p>
        <span>{{ p.estado }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.seccion-proyectos { padding: 20px; color: #333; }
.btn-v { margin-bottom: 20px; cursor: pointer; }
.card { border: 1px solid #ccc; padding: 15px; margin-bottom: 10px; border-radius: 8px; }
</style>