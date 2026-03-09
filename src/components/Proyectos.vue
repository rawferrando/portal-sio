<script setup>
import { ref, onMounted } from 'vue'

// Estado inicial
const listaProyectos = ref([])
const cargando = ref(true)

onMounted(() => {
  // Simulamos la entrada de datos de la WikiSIO
  setTimeout(() => {
    listaProyectos.value = [
      { id: 1, titulo: "Mantenimiento OBSEA", desc: "Revisión del conector submarino.", responsable: "Ingeniería" },
      { id: 2, titulo: "Radares HF", desc: "Calibración de antenas en tierra.", responsable: "Tecnología" }
    ]
    cargando.value = false
  }, 1000)
})
</script>

<template>
  <div class="wiki-proyectos">
    <button class="btn-v" @click="$emit('volver')">⬅ Volver</button>
    <h1>Registro de Proyectos SIO</h1>

    <div v-if="cargando" class="msg">⌛ Conectando con la base de datos...</div>

    <div v-else class="grid">
      <div v-for="p in listaProyectos" :key="p.id" class="ficha">
        <h3>{{ p.titulo }}</h3>
        <p>{{ p.desc }}</p>
        <small>Dpto: {{ p.responsable }}</small>
      </div>
    </div>
  </div>
</template>

<style scoped>
.wiki-proyectos { padding: 2rem; max-width: 800px; margin: 0 auto; }
.btn-v { padding: 10px; cursor: pointer; margin-bottom: 20px; }
.msg { color: #005596; font-weight: bold; }
.grid { display: grid; gap: 20px; }
.ficha { border-left: 5px solid #005596; background: #f9f9f9; padding: 1.5rem; border-radius: 4px; }
h1 { color: #005596; }
</style>