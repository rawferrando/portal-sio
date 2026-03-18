<script setup>
import { ref, computed } from 'vue'

// Permite comunicarnos con App.vue para volver al inicio
const emit = defineEmits(['volver'])

// Variables para el buscador
const textoBusqueda = ref('')
const tipoSeleccionado = ref('Todos')

// Base de datos "falsa" de equipos (Aquí pondremos los reales luego)
const inventario = ref([
  { id: 'SNS-001', nombre: 'CTD Sea-Bird 911plus', tipo: 'Perfiladores', desc: 'Medición de alta precisión de conductividad, temperatura y profundidad.' },
  { id: 'SNS-002', nombre: 'Salinómetro Guildline Portasal', tipo: 'Laboratorio', desc: 'Análisis de salinidad en muestras de agua con alta precisión.' },
  { id: 'SNS-003', nombre: 'ADCP Teledyne Workhorse 600kHz', tipo: 'Correntímetros', desc: 'Perfilador de corrientes acústico Doppler para fondeos.' },
  { id: 'SNS-004', nombre: 'Sensor Oxígeno Aanderaa Optode', tipo: 'Biogeoquímica', desc: 'Sensor óptico de oxígeno disuelto para despliegues prolongados.' },
  { id: 'SNS-005', nombre: 'Roseta Oceanográfica 12 Botellas', tipo: 'Muestreo', desc: 'Estructura de muestreo de agua equipada con botellas Niskin.' },
  { id: 'SNS-006', nombre: 'CTD RBRconcerto', tipo: 'Perfiladores', desc: 'Sonda multiparamétrica compacta para despliegues costeros.' }
])

// Motor de búsqueda en tiempo real
const equiposFiltrados = computed(() => {
  return inventario.value.filter(equipo => {
    // 1. Filtro por texto (busca en el nombre, ID o descripción)
    const coincideTexto = equipo.nombre.toLowerCase().includes(textoBusqueda.value.toLowerCase()) || 
                          equipo.desc.toLowerCase().includes(textoBusqueda.value.toLowerCase()) ||
                          equipo.id.toLowerCase().includes(textoBusqueda.value.toLowerCase())
    
    // 2. Filtro por menú desplegable
    const coincideTipo = tipoSeleccionado.value === 'Todos' || equipo.tipo === tipoSeleccionado.value
    
    return coincideTexto && coincideTipo
  })
})
</script>

<template>
  <div class="pagina-catalogo">
    
    <div class="cabecera-catalogo">
      <button @click="$emit('volver')" class="btn-volver">⬅ Volver al Inicio</button>
      <h2>Buscador de Instrumentación Científica</h2>
      <p>Explora nuestro catálogo de equipos, sondas y sensores disponibles para campañas.</p>
    </div>

    <div class="caja-filtros">
      <div class="grupo-filtro">
        <label>🔍 Buscar por palabra clave o ID:</label>
        <input v-model="textoBusqueda" type="text" placeholder="Ej. CTD, salinidad, SNS-003...">
      </div>
      
      <div class="grupo-filtro">
        <label>📂 Filtrar por categoría:</label>
        <select v-model="tipoSeleccionado">
          <option value="Todos">Todas las categorías</option>
          <option value="Perfiladores">Perfiladores (CTD)</option>
          <option value="Correntímetros">Correntímetros</option>
          <option value="Muestreo">Muestreo de Agua</option>
          <option value="Biogeoquímica">Biogeoquímica</option>
          <option value="Laboratorio">Equipos de Laboratorio</option>
        </select>
      </div>
    </div>

    <div class="resultados">
      <p class="contador-resultados">Mostrando {{ equiposFiltrados.length }} equipos</p>
      
      <div v-if="equiposFiltrados.length === 0" class="sin-resultados">
        <p>No se han encontrado equipos que coincidan con tu búsqueda.</p>
      </div>

      <div class="grid-equipos">
        <div v-for="equipo in equiposFiltrados" :key="equipo.id" class="tarjeta-equipo">
          <div class="etiqueta-tipo">{{ equipo.tipo }}</div>
          <h4>{{ equipo.nombre }}</h4>
          <span class="id-equipo">ID: {{ equipo.id }}</span>
          <p>{{ equipo.desc }}</p>
          <button class="btn-solicitar">Solicitar info</button>
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
.pagina-catalogo { animation: fadeIn 0.4s ease-in-out; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

.cabecera-catalogo { margin-bottom: 30px; }
.cabecera-catalogo h2 { color: #005596; margin-bottom: 5px; }
.btn-volver { background: #6c757d; color: white; border: none; padding: 8px 15px; border-radius: 4px; cursor: pointer; font-weight: bold; margin-bottom: 20px; }
.btn-volver:hover { background: #5a6268; }

/* Caja gris del buscador */
.caja-filtros { background: #f8f9fa; padding: 25px; border-radius: 8px; border: 1px solid #ddd; display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 30px; }
.grupo-filtro { flex: 1; min-width: 250px; display: flex; flex-direction: column; gap: 8px; }
.grupo-filtro label { font-weight: bold; color: #333; font-size: 0.95rem; }
.grupo-filtro input, .grupo-filtro select { padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 1rem; width: 100%; box-sizing: border-box; }

/* Grid de Resultados */
.contador-resultados { font-weight: bold; color: #666; margin-bottom: 15px; }
.grid-equipos { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
.sin-resultados { background: #fff3cd; padding: 20px; border-radius: 6px; color: #856404; text-align: center; font-weight: bold; }

/* Tarjetas individuales de cada equipo */
.tarjeta-equipo { background: white; border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); display: flex; flex-direction: column; transition: transform 0.2s; }
.tarjeta-equipo:hover { transform: translateY(-3px); box-shadow: 0 6px 12px rgba(0,0,0,0.1); border-color: #005596; }
.etiqueta-tipo { align-self: flex-start; background: #e2eef7; color: #005596; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; margin-bottom: 10px; }
.tarjeta-equipo h4 { margin: 0 0 5px 0; color: #333; font-size: 1.2rem; }
.id-equipo { font-size: 0.85rem; color: #888; font-family: monospace; margin-bottom: 15px; }
.tarjeta-equipo p { font-size: 0.95rem; color: #555; line-height: 1.5; flex: 1; margin-top: 0; }
.btn-solicitar { background: transparent; border: 2px solid #005596; color: #005596; padding: 8px; border-radius: 4px; font-weight: bold; cursor: pointer; margin-top: 15px; transition: all 0.2s; }
.btn-solicitar:hover { background: #005596; color: white; }
</style>