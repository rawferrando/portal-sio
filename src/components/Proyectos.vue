<script setup>
import { ref, onMounted } from 'vue'

// Estado de la "Base de Datos"
const listaProyectos = ref([])
const cargando = ref(true)
const error = ref(null)

onMounted(() => {
  console.log("Iniciando consulta a WikiSIO DB...");
  
  // Simulamos la conexión al servidor del ICM
  setTimeout(() => {
    try {
      listaProyectos.value = [
        { 
          id: 'PRJ-2026-01', 
          titulo: "Mantenimiento Gliders (AUV)", 
          desc: "Preparación y calibración de la flota de planeadores submarinos para la campaña estival.",
          prioridad: "Alta",
          responsable: "Unidad de Tecnología Marina"
        },
        { 
          id: 'PRJ-2026-02', 
          titulo: "Fondeo Profundo Palamós", 
          desc: "Diseño y despliegue de línea de fondeo a 1200m con sensores de corriente y trampas de sedimento.",
          prioridad: "Crítica",
          responsable: "Equipo de Oceanografía Física"
        },
        { 
          id: 'PRJ-2026-03', 
          titulo: "Soporte Antártida (BIO Hespérides)", 
          desc: "Revisión de instrumentación científica para la próxima campaña en la Base Juan Carlos I.",
          prioridad: "Media",
          responsable: "Logística SIO"
        },
        { 
          id: 'PRJ-2026-04', 
          titulo: "Red Radares HF COSMO", 
          desc: "Optimización del procesado de datos en tiempo real de las estaciones terrestres de Cataluña.",
          prioridad: "Alta",
          responsable: "Ingeniería SIO"
        }
      ]
      cargando.value = false
    } catch (e) {
      error.value = "Error al conectar con la WikiSIO. Revisa la red interna."
      cargando.value = false
    }
  }, 1200)
})
</script>

<template>
  <div class="wiki-proyectos">
    <header class="header-interno">
      <button class="btn-retroceder" @click="$emit('volver')">🔙 Volver al Portal</button>
      <h1>🗄️ WikiSIO: Registro de Operaciones</h1>
    </header>

    <div v-if="cargando" class="estado-carga">
      <div class="circulo-proceso"></div>
      <p>Consultando base de datos central...</p>
    </div>

    <div v-else-if="error" class="estado-error">
      <p>❌ {{ error }}</p>
    </div>

    <div v-else class="contenedor-cards">
      <div v-for="proyecto in listaProyectos" :key="proyecto.id" class="ficha-tecnica">
        <div class="cabecera-ficha">
          <span class="id-tag">{{ proyecto.id }}</span>
          <span :class="['prioridad', proyecto.prioridad.toLowerCase()]">{{ proyecto.prioridad }}</span>
        </div>
        <h3>{{ proyecto.titulo }}</h3>
        <p>{{ proyecto.desc }}</p>
        <div class="pie-ficha">
          <strong>🏢 Responsable:</strong> {{ proyecto.responsable }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.wiki-proyectos { max-width: 1200px; margin: 0 auto; padding: 20px; font-family: 'Segoe UI', sans-serif; }
.header-interno { display: flex; align-items: center; gap: 20px; border-bottom: 3px solid #005596; padding-bottom: 15px; margin-bottom: 30px; }
.btn-retroceder { background: #eee; border: none; padding: 8px 15px; border-radius: 5px; cursor: pointer; font-weight: bold; }
h1 { color: #005596; margin: 0; font-size: 1.8rem; }

/* Carga */
.estado-carga { text-align: center; padding: 50px; color: #005596; }
.circulo-proceso { border: 5px solid #f3f3f3; border-top: 5px solid #005596; border-radius: 50%; width: 50px; height: 50px; animation: spin 1s linear infinite; margin: 0 auto 20px; }
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

/* Grid y Fichas */
.contenedor-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 25px; }
.ficha-tecnica { background: white; border: 1px solid #ddd; padding: 20px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
.cabecera-ficha { display: flex; justify-content: space-between; margin-bottom: 15px; }
.id-tag { font-size: 0.75rem; color: #999; font-family: monospace; }
.prioridad { font-size: 0.7rem; padding: 3px 8px; border-radius: 4px; font-weight: bold; text-transform: uppercase; }
.alta { background: #ffdada; color: #cc0000; }
.critica { background: #000; color: #fff; }
.media { background: #e0f0ff; color: #005596; }
h3 { margin: 0 0 10px 0; color: #333; }
p { font-size: 0.95rem; color: #555; line-height: 1.5; }
.pie-ficha { margin-top: 15px; padding-top: 10px; border-top: 1px solid #eee; font-size: 0.85rem; color: #777; }
</style>