<script setup>
import { ref, onMounted } from 'vue'

// 1. Almacén para los datos y estado de carga
const listaProyectos = ref([])
const cargando = ref(true)

// 2. Simulación de la Base de Datos
onMounted(() => {
  setTimeout(() => {
    listaProyectos.value = [
      { 
        id: 1, 
        titulo: "Proyecto OBSEA 2026", 
        desc: "Mantenimiento preventivo del nodo submarino y sensores de presión.",
        estado: "Activo",
        tecnicos: "R. Ferrando, J. Busquets"
      },
      { 
        id: 2, 
        titulo: "Campaña NEREIDA II", 
        desc: "Recuperación de fondeos profundos en el Mar de Alborán.",
        estado: "Finalizado",
        tecnicos: "Equipo SIO-ICM"
      },
      { 
        id: 3, 
        titulo: "Radares HF Levante", 
        desc: "Calibración anual de antenas y procesado de datos SeaSonde.",
        estado: "Activo",
        tecnicos: "Ingeniería SIO"
      }
    ]
    cargando.value = false
  }, 1500) // 1.5 segundos de "simulación de servidor"
})
</script>

<template>
  <div class="seccion-tecnica">
    <button class="btn-volver" @click="$emit('volver')">⬅ Volver al Inicio</button>
    
    <h1>WikiSIO: Base de Datos de Proyectos</h1>

    <div v-if="cargando" class="loader">
      <div class="spinner"></div>
      <p>Conectando con el servidor del SIO...</p>
    </div>

    <div v-else class="grid-proyectos">
      <div v-for="proyecto in listaProyectos" :key="proyecto.id" class="card-db">
        <span class="badge" :class="proyecto.estado.toLowerCase()">{{ proyecto.estado }}</span>
        <h3>{{ proyecto.titulo }}</h3>
        <p>{{ proyecto.desc }}</p>
        <div class="meta">
          <strong>👷 Técnicos:</strong> {{ proyecto.tecnicos }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.seccion-tecnica { max-width: 1000px; margin: 0 auto; padding: 2rem; }
.btn-volver { border: 1px solid #005596; color: #005596; background: white; padding: 8px 16px; cursor: pointer; margin-bottom: 2rem; font-weight: bold; }

.loader { text-align: center; padding: 4rem; color: #005596; }
.spinner { 
  border: 4px solid #f3f3f3; border-top: 4px solid #005596; 
  border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin: 0 auto 1rem;
}
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

.grid-proyectos { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; }
.card-db { background: white; border: 1px solid #eee; padding: 1.5rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); position: relative; }
.badge { position: absolute; top: 1rem; right: 1rem; font-size: 0.7rem; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
.activo { background: #e6f4ea; color: #1e7e34; }
.finalizado { background: #f1f3f4; color: #5f6368; }
.meta { margin-top: 1rem; font-size: 0.8rem; color: #666; border-top: 1px solid #eee; padding-top: 0.5rem; }
</style>