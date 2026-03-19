<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

const textoBusqueda = ref('')
const tipoSeleccionado = ref('Todos')

// Controla qué equipos están "desplegados"
const equiposExpandidos = ref([])

const toggleDetalles = (id) => {
  const index = equiposExpandidos.value.indexOf(id)
  if (index > -1) {
    equiposExpandidos.value.splice(index, 1)
  } else {
    equiposExpandidos.value.push(id)
  }
}

// 🗄️ Base de datos con el nivel de detalle de la Wiki SIO
const inventario = ref([
  { 
    id: 'SNS-001', 
    nombre: 'SBE 5 Pressure Sensor', 
    tipo: 'Sensores de Presión', 
    desc: 'Sensor de presión de alta precisión diseñado específicamente para aplicaciones oceanográficas y de investigación marina.',
    fabricante: 'Sea-Bird Scientific',
    numeroSerie: '11599',
    
    // 👇 AQUÍ VOLCAMOS TODA LA WIKI SIO DEL SBE 5 👇
    wiki: {
      descripcionGeneral: "El SBE 5 Pressure Sensor es un sensor de presión de alta precisión fabricado por Sea-Bird Scientific, diseñado específicamente para aplicaciones oceanográficas y de investigación marina. Este sensor se utiliza para determinar la profundidad mediante la medición de la presión absoluta en el agua. La profundidad es un parámetro fundamental en oceanografía, ya que permite localizar espacialmente las medidas de otros parámetros (como temperatura y salinidad) del agua, siendo esencial para el análisis de la estructura vertical de la columna de agua.",
      caracteristicasMedicion: [
        "Rango de Presión: 0 a 10.000 psia (aproximadamente 0 a 6.800 metros de profundidad)",
        "Precisión: ±0.015% del rango completo",
        "Resolución: 0.001% del rango completo",
        "Estabilidad: ±0.005% del rango completo por año",
        "Tiempo de Respuesta: <100 ms"
      ],
      caracteristicasFisicas: [
        "Diámetro: Aproximadamente 19 mm",
        "Longitud: Aproximadamente 76 mm"
      ],
      especificacionesElectricas: [
        "Voltaje de Alimentación: 8-18 V DC",
        "Consumo de Corriente: <5 mA",
        "Señal de Salida: 0-5 V DC (proporcional a la presión)",
        "Impedancia de Salida: <1000 ohms",
        "Aislamiento: >100 MΩ a 50 V DC"
      ],
      principioFuncionamiento: "El sensor SBE 5 utiliza un transductor de presión de alta precisión basado en tecnología de galgas extensiométricas (strain gauge). La presión del agua actúa sobre un diafragma de titanio, que se deforma proporcionalmente. Las galgas convierten esta deformación en una señal eléctrica que se amplifica y lineariza electrónicamente.",
      mantenimientoPreventivo: [
        "Inspección visual: Verificar ausencia de daños en diafragma y conectores",
        "Limpieza: Enjuague con agua destilada después de cada uso",
        "Almacenamiento: En ambiente seco, protegido de golpes",
        "Verificación funcional: Chequeo de respuesta antes de cada campaña"
      ],
      aplicaciones: [
        "Perfiles CTD: Medición continua de profundidad durante perfiles verticales",
        "Fondeos fijos: Monitoreo de presión en estaciones fijas",
        "Estudios de mareas: Registro de variaciones de presión por efecto de mareas"
      ],
      documentacion: "https://www.seabird.com/support"
    }
  },
  { 
    id: 'SNS-002', 
    nombre: 'Salinómetro Guildline Portasal', 
    tipo: 'Laboratorio', 
    desc: 'Análisis de salinidad en muestras de agua con altísima precisión paramétrica.',
    fabricante: 'Guildline Instruments',
    numeroSerie: '67890',
    wiki: null // (Los demás los dejamos sencillos por ahora para no hacer el código infinito)
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
  const asunto = encodeURIComponent(`Consulta: ${equipo.nombre} (ID: ${equipo.id})`)
  return `mailto:${email}?subject=${asunto}`
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
        <input v-model="textoBusqueda" type="text" placeholder="Ej. SBE 5, presión, SNS-001...">
      </div>
      <div class="grupo-filtro">
        <label>📂 Filtrar por categoría:</label>
        <select v-model="tipoSeleccionado">
          <option value="Todos">Todas las categorías</option>
          <option value="Sensores de Presión">Sensores de Presión</option>
          <option value="Laboratorio">Equipos de Laboratorio</option>
        </select>
      </div>
    </div>

    <div class="resultados">
      <p class="contador-resultados">Mostrando {{ equiposFiltrados.length }} equipos</p>
      
      <div class="grid-equipos">
        <div v-for="equipo in equiposFiltrados" :key="equipo.id" class="tarjeta-equipo">
          
          <div class="cabecera-tarjeta">
            <div class="etiqueta-tipo">{{ equipo.tipo }}</div>
            <span class="id-equipo">{{ equipo.id }}</span>
          </div>
          
          <h4>{{ equipo.nombre }}</h4>
          <p class="descripcion">{{ equipo.desc }}</p>
          
          <button @click="toggleDetalles(equipo.id)" class="btn-desplegar">
            {{ equiposExpandidos.includes(equipo.id) ? '▲ Ocultar Ficha Técnica de la Wiki' : '▼ Ver Ficha Técnica Completa' }}
          </button>

          <div v-if="equiposExpandidos.includes(equipo.id)" class="ficha-tecnica-desplegada">
            
            <div v-if="equipo.wiki">
              
              <div class="seccion-wiki">
                <h5>📖 Descripción General</h5>
                <p>{{ equipo.wiki.descripcionGeneral }}</p>
              </div>

              <div class="wiki-grid-2">
                <div class="seccion-wiki">
                  <h5>📏 Características de Medición</h5>
                  <ul>
                    <li v-for="(item, index) in equipo.wiki.caracteristicasMedicion" :key="index">{{ item }}</li>
                  </ul>
                </div>
                
                <div class="seccion-wiki">
                  <h5>⚡ Especificaciones Eléctricas</h5>
                  <ul>
                    <li v-for="(item, index) in equipo.wiki.especificacionesElectricas" :key="index">{{ item }}</li>
                  </ul>
                </div>
              </div>

              <div class="seccion-wiki">
                <h5>⚙️ Principio de Funcionamiento</h5>
                <p>{{ equipo.wiki.principioFuncionamiento }}</p>
              </div>

              <div class="wiki-grid-2">
                <div class="seccion-wiki">
                  <h5>🛠️ Mantenimiento Preventivo</h5>
                  <ul>
                    <li v-for="(item, index) in equipo.wiki.mantenimientoPreventivo" :key="index">{{ item }}</li>
                  </ul>
                </div>

                <div class="seccion-wiki">
                  <h5>🌊 Aplicaciones Oceanográficas</h5>
                  <ul>
                    <li v-for="(item, index) in equipo.wiki.aplicaciones" :key="index">{{ item }}</li>
                  </ul>
                </div>
              </div>
              
              <div class="seccion-wiki doc-link">
                <h5>📚 Documentación Técnica</h5>
                <a :href="equipo.wiki.documentacion" target="_blank">Abrir manuales y soporte del fabricante ➔</a>
              </div>

            </div>
            
            <div v-else class="aviso-vacio">
              <p>Ficha técnica en proceso de migración desde la Wiki SIO.</p>
            </div>

          </div>

          <a :href="generarEnlaceCorreo(equipo)" class="btn-solicitar">✉️ Solicitar Disponibilidad</a>
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

.caja-filtros { background: #f8f9fa; padding: 25px; border-radius: 8px; border: 1px solid #ddd; display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 30px; }
.grupo-filtro { flex: 1; min-width: 250px; display: flex; flex-direction: column; gap: 8px; }
.grupo-filtro label { font-weight: bold; color: #333; font-size: 0.95rem; }
.grupo-filtro input, .grupo-filtro select { padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 1rem; width: 100%; box-sizing: border-box; }

.contador-resultados { font-weight: bold; color: #666; margin-bottom: 15px; }
.grid-equipos { display: flex; flex-direction: column; gap: 25px; } /* Cambiado a columna para que la ficha grande se vea bien */

.tarjeta-equipo { background: white; border: 1px solid #e0e0e0; border-radius: 8px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); display: flex; flex-direction: column; }
.cabecera-tarjeta { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
.etiqueta-tipo { background: #e2eef7; color: #005596; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; }
.id-equipo { font-size: 0.85rem; color: #888; font-family: monospace; font-weight: bold; background: #f0f0f0; padding: 3px 6px; border-radius: 4px; }

.tarjeta-equipo h4 { margin: 0 0 10px 0; color: #333; font-size: 1.4rem; }
.descripcion { font-size: 1rem; color: #555; line-height: 1.5; margin-top: 0; margin-bottom: 20px; }

.btn-desplegar { background: #005596; color: white; border: none; padding: 10px 15px; border-radius: 4px; font-weight: bold; cursor: pointer; font-size: 0.95rem; transition: background 0.2s; margin-bottom: 15px; text-align: center; }
.btn-desplegar:hover { background: #00447a; }

/* ESTILOS DE LA WIKI DESPLEGADA */
.ficha-tecnica-desplegada { background: #f8fbff; border: 1px solid #cce0f0; border-radius: 8px; padding: 25px; margin-bottom: 20px; animation: slideDown 0.3s ease-out; }
@keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }

.seccion-wiki { margin-bottom: 20px; }
.seccion-wiki h5 { margin: 0 0 10px 0; color: #003d6b; font-size: 1.1rem; border-bottom: 2px solid #cce0f0; padding-bottom: 5px; }
.seccion-wiki p { font-size: 0.95rem; color: #444; line-height: 1.6; margin: 0; }
.seccion-wiki ul { padding-left: 20px; margin: 0; }
.seccion-wiki li { font-size: 0.9rem; color: #444; margin-bottom: 6px; line-height: 1.4; }

.wiki-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
@media (max-width: 768px) { .wiki-grid-2 { grid-template-columns: 1fr; gap: 10px; } }

.doc-link a { color: #005596; font-weight: bold; text-decoration: none; }
.doc-link a:hover { text-decoration: underline; }
.aviso-vacio { text-align: center; color: #888; font-style: italic; padding: 20px; }

.btn-solicitar { display: block; text-align: center; text-decoration: none; background: transparent; border: 2px solid #005596; color: #005596; padding: 12px; border-radius: 4px; font-weight: bold; cursor: pointer; transition: all 0.2s; margin-top: auto; }
.btn-solicitar:hover { background: #005596; color: white; }
</style>