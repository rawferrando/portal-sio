<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

const textoBusqueda = ref('')
const tipoSeleccionado = ref('Todos')

// Controla qué equipos están "desplegados" (guardamos sus IDs aquí)
const equiposExpandidos = ref([])

const toggleDetalles = (id) => {
  const index = equiposExpandidos.value.indexOf(id)
  if (index > -1) {
    equiposExpandidos.value.splice(index, 1) // Si estaba abierto, lo cierra
  } else {
    equiposExpandidos.value.push(id) // Si estaba cerrado, lo abre
  }
}

// 🗄️ Base de datos enriquecida con las fichas técnicas completas
const inventario = ref([
  { 
    id: 'SNS-001', 
    nombre: 'SBE 5 Pressure Sensor', 
    tipo: 'Sensores de Presión', 
    desc: 'Sensor de presión de alta precisión diseñado para aplicaciones oceanográficas y determinación de profundidad.',
    fabricante: 'Sea-Bird Scientific',
    numeroSerie: '11599',
    rango: '0 a 10.000 psia',
    precision: '±0.015% del rango',
    voltaje: '8-18 V DC',
    salida: '0-5 V DC',
    ultimaCalibracion: '05 de mayo de 2023',
    periodicidad: '12 a 24 meses'
  },
  { 
    id: 'SNS-002', 
    nombre: 'Salinómetro Guildline Portasal', 
    tipo: 'Laboratorio', 
    desc: 'Análisis de salinidad en muestras de agua con altísima precisión paramétrica.',
    fabricante: 'Guildline Instruments',
    numeroSerie: '67890',
    rango: '0.005 a 42 PSU',
    precision: '±0.003 PSU',
    voltaje: '110/220 V AC',
    salida: 'RS-232 / USB',
    ultimaCalibracion: '12 de enero de 2024',
    periodicidad: '12 meses'
  },
  { 
    id: 'SNS-003', 
    nombre: 'ADCP Teledyne Workhorse 600kHz', 
    tipo: 'Correntímetros', 
    desc: 'Perfilador de corrientes acústico Doppler, ideal para fondeos costeros y estudios hidrodinámicos.',
    fabricante: 'Teledyne Marine',
    numeroSerie: 'WH-5432',
    rango: 'Hasta 50 metros (perfilado)',
    precision: '±0.3% de la velocidad',
    voltaje: '20-50 V DC',
    salida: 'RS-232 / RS-422',
    ultimaCalibracion: '20 de noviembre de 2023',
    periodicidad: '24 meses'
  }
])

const equiposFiltrados = computed(() => {
  return inventario.value.filter(equipo => {
    const texto = textoBusqueda.value.toLowerCase()
    const coincideTexto = equipo.nombre.toLowerCase().includes(texto) || 
                          equipo.desc.toLowerCase().includes(texto) ||
                          equipo.id.toLowerCase().includes(texto)
    
    const coincideTipo = tipoSeleccionado.value === 'Todos' || equipo.tipo === tipoSeleccionado.value
    
    return coincideTexto && coincideTipo
  })
})

const generarEnlaceCorreo = (equipo) => {
  const email = "sio@icm.csic.es"
  const asunto = encodeURIComponent(`Consulta de disponibilidad: ${equipo.nombre} (ID: ${equipo.id})`)
  const cuerpo = encodeURIComponent(`Hola equipo del SIO,\n\nMe gustaría consultar la disponibilidad del siguiente equipo para una futura campaña:\n\n- Equipo: ${equipo.nombre}\n- S/N: ${equipo.numeroSerie}\n- ID interno: ${equipo.id}\n\nFechas estimadas de la campaña:\n[Escribe aquí las fechas]\n\nUn saludo,`)
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
        <label>🔍 Buscar por palabra clave o ID:</label>
        <input v-model="textoBusqueda" type="text" placeholder="Ej. SBE 5, salinidad, SNS-003...">
      </div>
      
      <div class="grupo-filtro">
        <label>📂 Filtrar por categoría:</label>
        <select v-model="tipoSeleccionado">
          <option value="Todos">Todas las categorías</option>
          <option value="Sensores de Presión">Sensores de Presión</option>
          <option value="Correntímetros">Correntímetros</option>
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
          <div class="cabecera-tarjeta">
            <div class="etiqueta-tipo">{{ equipo.tipo }}</div>
            <span class="id-equipo">{{ equipo.id }}</span>
          </div>
          
          <h4>{{ equipo.nombre }}</h4>
          <p class="descripcion">{{ equipo.desc }}</p>
          
          <button @click="toggleDetalles(equipo.id)" class="btn-desplegar">
            {{ equiposExpandidos.includes(equipo.id) ? '▲ Ocultar especificaciones técnicas' : '▼ Ver especificaciones técnicas' }}
          </button>

          <div v-if="equiposExpandidos.includes(equipo.id)" class="ficha-tecnica-desplegada">
            
            <div class="bloque-info">
              <h5>📋 Identificación</h5>
              <ul>
                <li><strong>Fabricante:</strong> {{ equipo.fabricante }}</li>
                <li><strong>S/N:</strong> {{ equipo.numeroSerie }}</li>
              </ul>
            </div>

            <div class="bloque-info">
              <h5>⚙️ Especificaciones</h5>
              <ul>
                <li><strong>Rango:</strong> {{ equipo.rango }}</li>
                <li><strong>Precisión:</strong> {{ equipo.precision }}</li>
                <li><strong>Alimentación:</strong> {{ equipo.voltaje }}</li>
                <li><strong>Señal salida:</strong> {{ equipo.salida }}</li>
              </ul>
            </div>

            <div class="bloque-info">
              <h5>🔧 Calibración</h5>
              <ul>
                <li><strong>Última:</strong> {{ equipo.ultimaCalibracion }}</li>
                <li><strong>Periodicidad:</strong> {{ equipo.periodicidad }}</li>
              </ul>
            </div>

          </div>

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
.grid-equipos { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; align-items: start; }
.sin-resultados { background: #fff3cd; padding: 20px; border-radius: 6px; color: #856404; text-align: center; font-weight: bold; }

.tarjeta-equipo { background: white; border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); display: flex; flex-direction: column; }
.tarjeta-equipo:hover { box-shadow: 0 6px 15px rgba(0,0,0,0.1); border-color: #005596; }

.cabecera-tarjeta { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
.etiqueta-tipo { background: #e2eef7; color: #005596; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; }
.id-equipo { font-size: 0.85rem; color: #888; font-family: monospace; font-weight: bold; background: #f0f0f0; padding: 3px 6px; border-radius: 4px; }

.tarjeta-equipo h4 { margin: 0 0 10px 0; color: #333; font-size: 1.25rem; }
.descripcion { font-size: 0.95rem; color: #555; line-height: 1.5; margin-top: 0; margin-bottom: 15px; }

/* Botón Desplegable */
.btn-desplegar { background: #f1f8ff; color: #005596; border: 1px solid #cce0f0; padding: 8px; border-radius: 4px; font-weight: bold; cursor: pointer; font-size: 0.85rem; transition: background 0.2s; margin-bottom: 15px; text-align: left; }
.btn-desplegar:hover { background: #e2eef7; }

/* Interior de la ficha desplegada */
.ficha-tecnica-desplegada { background: #fafafa; border: 1px solid #eee; border-radius: 6px; padding: 15px; margin-bottom: 15px; display: flex; flex-direction: column; gap: 12px; animation: slideDown 0.3s ease-out; }
@keyframes slideDown { from { opacity: 0; transform: translateY(-5px); } to { opacity: 1; transform: translateY(0); } }

.bloque-info h5 { margin: 0 0 5px 0; color: #333; font-size: 0.9rem; border-bottom: 1px solid #ddd; padding-bottom: 3px; }
.bloque-info ul { list-style: none; padding: 0; margin: 0; }
.bloque-info li { font-size: 0.85rem; color: #555; margin-bottom: 4px; line-height: 1.3; }

/* Enlace simulando un botón */
.btn-solicitar { display: block; text-align: center; text-decoration: none; background: transparent; border: 2px solid #005596; color: #005596; padding: 10px; border-radius: 4px; font-weight: bold; cursor: pointer; transition: all 0.2s; margin-top: auto; }
.btn-solicitar:hover { background: #005596; color: white; }
</style>