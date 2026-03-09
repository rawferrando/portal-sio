<script setup>
import { ref, onMounted } from 'vue'

// 1. Creamos el almacén vacío y el estado de carga
const listaProyectos = ref([])
const cargando = ref(true)

// 2. Simulamos la conexión a la Base de Datos del ICM
onMounted(() => {
  console.log("Conectando con la base de datos SIO...")
  
  // Simulamos un retraso de red (1.5 segundos)
  setTimeout(() => {
    // Aquí es donde en el futuro irá el 'fetch' real
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
        estado: "En pausa",
        tecnicos: "Ingeniería SIO"
      }
    ]
    cargando.value = false // ¡Datos recibidos!
  }, 1500)
})
</script>

<template>
  <div class="seccion-tecnica">
    <button class="btn-volver" @click="$emit('volver')">⬅ Volver</button>
    
    <h1>Consola de Gestión de Proyectos (Base de Datos)</h1>

    <div v-if="cargando" class="loader">
      <div class="spinner"></div>
      <p>Consultando servidor del SIO... por favor, espere.</p>
    </div>

    <div v-else class="grid-dinamico">
      <div v-for="proyecto in listaProyectos" :key="proyecto.id" class="card-db">
        <div class="badge">{{ proyecto.estado }}</div>
        <h3>{{ proyecto.titulo }}</h3>
        <p>{{ proyecto.desc }}</p>
        <div class="meta">
          <span>👷 Responsables: {{ proyecto.tecnicos }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.seccion-tecnica { max-width: 1000px; margin: 0 auto; padding: 2rem; }
.btn-volver { border: 1px solid #005596; color: #005596; background: white; padding: 8px 16px; cursor: pointer; margin-bottom: 2rem; }

/* Estilo del Cargando */
.loader { text-align: center; padding: 3rem; color: #005596; font-weight: bold; }
.spinner { 
  border: 4px solid #f3f3f3; border-top: 4px solid #005596; 
  border-radius: 50%; width: 40px; height: 40px; 
  animation: spin 1s linear infinite; margin: 0 auto 1rem;
}
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

/* Tarjetas generadas automáticamente */
.grid-dinamico { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; }
.card-db { background: #fff; border: 1px solid #ddd; padding: 1.5rem; border-radius: 8px; position: relative; }
.badge { position: absolute; top: 10px; right: 10px; font-size: 0.7rem; background: #e0f0ff; color: #005596; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
.meta { margin-top: 1rem; font-size: 0.8rem; color: #666; border-top: 1px solid #eee; padding-top: 0.5rem; }
</style>            