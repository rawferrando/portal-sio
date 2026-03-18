<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

const textoBusqueda = ref('')
const tipoSeleccionado = ref('Todos')

// 🗄️ Base de datos enriquecida con todas las especificaciones
const inventario = ref([
  { 
    id: 'SNS-001', 
    nombre: 'CTD Sea-Bird 911plus', 
    tipo: 'Perfiladores', 
    desc: 'Medición de alta precisión de conductividad, temperatura y profundidad para campañas en buques oceanográficos.',
    fabricante: 'Sea-Bird Scientific',
    prof_max: '6000m',
    parametros: 'C, T, D, Oxígeno disuelto, Fluorescencia, Turbidez'
  },
  { 
    id: 'SNS-002', 
    nombre: 'Salinómetro Guildline Portasal', 
    tipo: 'Laboratorio', 
    desc: 'Análisis de salinidad en muestras de agua con altísima precisión paramétrica.',
    fabricante: 'Guildline Instruments',
    prof_max: 'N/A (Laboratorio)',
    parametros: 'Salinidad (Ratio de conductividad)'
  },
  { 
    id: 'SNS-003', 
    nombre: 'ADCP Teledyne Workhorse 600kHz', 
    tipo: 'Correntímetros', 
    desc: 'Perfilador de corrientes acústico Doppler, ideal para fondeos costeros y estudios hidrodinámicos.',
    fabricante: 'Teledyne Marine',
    prof_max: '200m',
    parametros: 'Velocidad y dirección de corrientes (Perfil 3D)'
  },
  { 
    id: 'SNS-004', 
    nombre: 'Sensor Oxígeno Aanderaa Optode', 
    tipo: 'Biogeoquímica', 
    desc: 'Sensor óptico de oxígeno disuelto diseñado para despliegues prolongados sin deriva temporal.',
    fabricante: 'Aanderaa Data Instruments',
    prof_max: '6000m',
    parametros: 'Oxígeno disuelto (Concentración y Saturación), Temperatura'
  },
  { 
    id: 'SNS-005', 
    nombre: 'Roseta Oceanográfica 12 Botellas', 
    tipo: 'Muestreo', 
    desc: 'Estructura de muestreo de agua equipada con 12 botellas Niskin de 12 litros y sistema de disparo.',
    fabricante: 'General Oceanics',
    prof_max: '6000m',
    parametros: 'Muestreo físico de agua a distintas profundidades'
  },
  { 
    id: 'SNS-006', 
    nombre: 'Sonda Multiparamétrica EXO2', 
    tipo: 'Perfiladores', 
    desc: 'Plataforma avanzada para monitorización de calidad del agua en estuarios y zonas costeras.',
    fabricante: 'YSI',
    prof_max: '250m',
    parametros: 'pH, ORP, Turbidez, fDOM, Clorofila, Algas'
  }
])

const equiposFiltrados = computed(() => {
  return inventario.value.filter(equipo => {
    const texto = textoBusqueda.value.toLowerCase()
    const coincideTexto = equipo.nombre.toLowerCase().includes(texto) || 
                          equipo.desc.toLowerCase().includes(texto) ||
                          equipo.id.toLowerCase().includes(texto) ||
                          equipo.parametros.toLowerCase().includes(texto)
    
    const coincideTipo = tipoSeleccionado.value === 'Todos' || equipo.tipo === tipoSeleccionado.value
    
    return coincideTexto && coincideTipo
  })
})

// Función que genera el enlace de correo automático
const generarEnlaceCorreo = (equipo) => {
  const email = "sio@icm.csic.es"
  const asunto = encodeURIComponent(`Consulta de disponibilidad: ${equipo.nombre} (${equipo.id})`)
  const cuerpo = encodeURIComponent(`Hola equipo del SIO,\n\nMe gustaría consultar la disponibilidad del siguiente equipo para una futura campaña:\n\n- Equipo: ${equipo.nombre}\n- ID: ${equipo.id}\n\nFechas estimadas de la campaña:\n[Escribe aquí las fechas]\n\nUn saludo,`)
  return `mailto:${email}?subject=${asunto}&body=${cuerpo}`
}
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
        <label>🔍 Buscar por palabra clave, ID o parámetro:</label>
        <input v-model="textoBusqueda" type="text" placeholder="Ej. CTD, oxígeno, SNS-003...">
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
          
          <p class="descripcion">{{ equipo.desc }}</p>
          
          <ul class="ficha-tecnica">
            <li><strong>Fabricante:</strong> {{ equipo.fabricante }}</li>
            <li><strong>Prof. Máxima:</strong> {{ equipo.prof_max }}</li>
            <li><strong>Parámetros:</strong> {{ equipo.parametros }}</li>
          </ul>

          <a :href="generarEnlaceCorreo(equipo)" class="btn-solicitar">
            ✉️ Solicitar Disponibilidad
          </a>
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

.caja-filtros { background: #f8f9fa; padding: 25px; border-radius: 8px; border: 1px solid #ddd; display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 30px; }
.grupo-filtro { flex: 1; min-width: 250px; display: flex; flex-direction: column; gap: 8px; }
.grupo-filtro label { font-weight: bold; color: #333; font-size: 0.95rem; }
.grupo-filtro input, .grupo-filtro select { padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 1rem; width: 100%; box-sizing: border-box; }

.contador-resultados { font-weight: bold; color: #666; margin-bottom: 15px; }
.grid-equipos { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }
.sin-resultados { background: #fff3cd; padding: 20px; border-radius: 6px; color: #856404; text-align: center; font-weight: bold; }

.tarjeta-equipo { background: white; border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); display: flex; flex-direction: column; transition: transform 0.2s; }
.tarjeta-equipo:hover { transform: translateY(-3px); box-shadow: 0 6px 12px rgba(0,0,0,0.1); border-color: #005596; }
.etiqueta-tipo { align-self: flex-start; background: #e2eef7; color: #005596; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; margin-bottom: 10px; }
.tarjeta-equipo h4 { margin: 0 0 5px 0; color: #333; font-size: 1.2rem; }
.id-equipo { font-size: 0.85rem; color: #888; font-family: monospace; margin-bottom: 10px; }

.descripcion { font-size: 0.95rem; color: #555; line-height: 1.5; margin-top: 0; margin-bottom: 15px; }

/* Estilos de la nueva lista técnica */
.ficha-tecnica { background: #fdfdfd; border: 1px solid #eee; padding: 15px; border-radius: 6px; margin: 0 0 20px 0; list-style-type: none; flex: 1; }
.ficha-tecnica li { font-size: 0.85rem; color: #444; margin-bottom: 6px; line-height: 1.4; }
.ficha-tecnica li:last-child { margin-bottom: 0; }

/* Enlace simulando un botón */
.btn-solicitar { display: block; text-align: center; text-decoration: none; background: transparent; border: 2px solid #005596; color: #005596; padding: 10px; border-radius: 4px; font-weight: bold; cursor: pointer; transition: all 0.2s; }
.btn-solicitar:hover { background: #005596; color: white; }
</style>