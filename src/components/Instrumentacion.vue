<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

const textoBusqueda = ref('')
const tipoSeleccionado = ref('Todos')
const equiposExpandidos = ref([])

const toggleDetalles = (id) => {
  const index = equiposExpandidos.value.indexOf(id)
  if (index > -1) {
    equiposExpandidos.value.splice(index, 1)
  } else {
    equiposExpandidos.value.push(id)
  }
}

// 🗄️ Base de datos: Reservas + Formulario + Wiki Completa
const inventario = ref([
  { 
    id: 'SNS-001', 
    nombre: 'SBE 5 Pressure Sensor', 
    tipo: 'Sensores de Presión', 
    desc: 'Sensor de presión de alta precisión diseñado específicamente para aplicaciones oceanográficas y de investigación marina.',
    
    // DATOS DEL FORMULARIO BÁSICO
    fabricante: 'Sea-Bird Scientific',
    numeroSerie: '11599',
    rango: '0 a 10.000 psia',
    precision: '±0.015% del rango',
    voltaje: '8-18 V DC',
    salida: '0-5 V DC',
    ultimaCalibracion: '05 de mayo de 2023',
    periodicidad: '12 a 24 meses',

    // SISTEMA DE RESERVAS
    reservas: [
      { desde: '2026-04-10', hasta: '2026-04-25', proyecto: 'Campaña Costa Brava (ICATMAR)' }
    ],
    nuevaReserva: { desde: '', hasta: '', proyecto: '' },
    
    // TODA LA WIKI DETALLADA DE LAS CAPTURAS
    wiki: {
      descripcionGeneral: "El SBE 5 Pressure Sensor es un sensor de presión de alta precisión fabricado por Sea-Bird Scientific, diseñado específicamente para aplicaciones oceanográficas y de investigación marina. Este sensor se utiliza para determinar la profundidad mediante la medición de la presión absoluta en el agua. La profundidad es un parámetro fundamental en oceanografía, ya que permite localizar espacialmente las medidas de otros parámetros (como temperatura y salinidad) del agua, siendo esencial para el análisis de la estructura vertical de la columna de agua.",
      caracteristicasMedicion: [
        "Rango de Presión: 0 a 10.000 psia (aprox. 0 a 6.800 metros de profundidad)",
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
      principioFuncionamiento: "El sensor SBE 5 utiliza un transductor de presión de alta precisión basado en tecnología de galgas extensiométricas (strain gauge). La presión del agua actúa sobre un diafragma de titanio, que se deforma proporcionalmente a la presión aplicada. Las galgas extensiométricas convierten la deformación en una señal eléctrica, la cual se amplifica y lineariza electrónicamente.",
      mantenimientoPreventivo: [
        "Inspección visual: Verificar ausencia de daños en diafragma y conectores",
        "Limpieza: Enjuague con agua destilada después de cada uso",
        "Almacenamiento: En ambiente seco, protegido de golpes",
        "Verificación funcional: Chequeo de respuesta antes de cada campaña"
      ],
      aplicaciones: [
        "Perfiles CTD: Medición continua de profundidad durante perfiles verticales",
        "Fondeos fijos: Monitoreo de presión en estaciones fijas",
        "Estudios de mareas: Registro de variaciones de presión por efecto de mareas",
        "Calibración batimétrica: Verificación de profundidades cartográficas"
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
    rango: '0.005 a 42 PSU',
    precision: '±0.003 PSU',
    voltaje: '110/220 V AC',
    salida: 'RS-232',
    ultimaCalibracion: '12 de enero de 2024',
    periodicidad: '12 meses',
    reservas: [],
    nuevaReserva: { desde: '', hasta: '', proyecto: '' },
    wiki: null
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

const confirmarReserva = (equipo) => {
  if (!equipo.nuevaReserva.desde || !equipo.nuevaReserva.hasta) {
    alert("⚠️ Por favor, selecciona la fecha de inicio y fin de la campaña.")
    return
  }
  equipo.reservas.push({
    desde: equipo.nuevaReserva.desde,
    hasta: equipo.nuevaReserva.hasta,
    proyecto: equipo.nuevaReserva.proyecto || 'Reserva Interna SIO'
  })
  equipo.nuevaReserva = { desde: '', hasta: '', proyecto: '' }
  alert(`✅ ¡Fechas bloqueadas con éxito para el equipo ${equipo.id}!`)
}
</script>

<template>
  <div class="pagina-catalogo">
    
    <div class="cabecera-catalogo">
      <button @click="$emit('volver')" class="btn-volver">⬅ Volver al Inicio</button>
      <h2>Buscador de Instrumentación Científica</h2>
      <p>Explora nuestro catálogo, revisa las fichas técnicas y bloquea fechas para tus campañas.</p>
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
      <div class="grid-equipos">
        
        <div v-for="equipo in equiposFiltrados" :key="equipo.id" class="tarjeta-equipo">
          
          <div class="cabecera-tarjeta">
            <div class="etiqueta-tipo">{{ equipo.tipo }}</div>
            <span v-if="equipo.reservas.length > 0" class="badge-ocupado">🗓️ Con Reservas Activas</span>
            <span v-else class="badge-libre">✅ Disponible</span>
          </div>
          
          <h4>{{ equipo.nombre }} <span class="id-equipo">({{ equipo.id }})</span></h4>
          <p class="descripcion">{{ equipo.desc }}</p>
          
          <button @click="toggleDetalles(equipo.id)" class="btn-desplegar">
            {{ equiposExpandidos.includes(equipo.id) ? '▲ Ocultar Detalles y Reservas' : '▼ Ver Ficha Técnica y Calendario' }}
          </button>

          <div v-if="equiposExpandidos.includes(equipo.id)" class="ficha-tecnica-desplegada">
            
            <div class="bloque-reservas">
              <h5>📅 Calendario de Disponibilidad</h5>
              <div v-if="equipo.reservas.length > 0" class="lista-reservas">
                <p class="texto-aviso">Este equipo tiene las siguientes fechas bloqueadas:</p>
                <ul>
                  <li v-for="(res, index) in equipo.reservas" :key="index">
                    <strong>Del {{ res.desde }} al {{ res.hasta }}</strong> - {{ res.proyecto }}
                  </li>
                </ul>
              </div>
              <div v-else class="lista-reservas libre">
                <p>No hay campañas programadas. El equipo está totalmente libre.</p>
              </div>
              <div class="formulario-reserva">
                <h6>Solicitar Bloqueo de Fechas:</h6>
                <div class="inputs-reserva">
                  <input type="date" v-model="equipo.nuevaReserva.desde" title="Fecha de inicio">
                  <input type="date" v-model="equipo.nuevaReserva.hasta" title="Fecha de fin">
                  <input type="text" v-model="equipo.nuevaReserva.proyecto" placeholder="Nombre del proyecto...">
                  <button @click="confirmarReserva(equipo)" class="btn-reservar">Bloquear Fechas</button>
                </div>
              </div>
            </div>

            <div class="bloque-resumen">
              <div class="wiki-grid-2">
                <div class="seccion-wiki">
                  <h6>📋 Identificación</h6>
                  <ul>
                    <li><strong>Fabricante:</strong> {{ equipo.fabricante }}</li>
                    <li><strong>S/N:</strong> {{ equipo.numeroSerie }}</li>
                  </ul>
                </div>
                <div class="seccion-wiki">
                  <h6>🔧 Calibración</h6>
                  <ul>
                    <li><strong>Última:</strong> {{ equipo.ultimaCalibracion }}</li>
                    <li><strong>Periodicidad:</strong> {{ equipo.periodicidad }}</li>
                  </ul>
                </div>
              </div>
            </div>

            <div v-if="equipo.wiki" class="bloque-wiki">
              <h5>📖 Enciclopedia SIO (Wiki)</h5>
              
              <div class="seccion-wiki">
                <h6>Descripción General</h6>
                <p>{{ equipo.wiki.descripcionGeneral }}</p>
              </div>

              <div class="wiki-grid-2">
                <div class="seccion-wiki">
                  <h6>📏 Características de Medición</h6>
                  <ul><li v-for="(item, index) in equipo.wiki.caracteristicasMedicion" :key="index">{{ item }}</li></ul>
                </div>
                <div class="seccion-wiki">
                  <h6>⚡ Especificaciones Eléctricas</h6>
                  <ul><li v-for="(item, index) in equipo.wiki.especificacionesElectricas" :key="index">{{ item }}</li></ul>
                </div>
              </div>

              <div class="wiki-grid-2">
                <div class="seccion-wiki">
                  <h6>📦 Características Físicas</h6>
                  <ul><li v-for="(item, index) in equipo.wiki.caracteristicasFisicas" :key="index">{{ item }}</li></ul>
                </div>
                <div class="seccion-wiki">
                  <h6>🛠️ Mantenimiento Preventivo</h6>
                  <ul><li v-for="(item, index) in equipo.wiki.mantenimientoPreventivo" :key="index">{{ item }}</li></ul>
                </div>
              </div>

              <div class="seccion-wiki">
                <h6>⚙️ Principio de Funcionamiento</h6>
                <p>{{ equipo.wiki.principioFuncionamiento }}</p>
              </div>

              <div class="seccion-wiki">
                <h6>🌊 Aplicaciones Oceanográficas</h6>
                <ul><li v-for="(item, index) in equipo.wiki.aplicaciones" :key="index">{{ item }}</li></ul>
              </div>
              
              <div class="seccion-wiki doc-link">
                <h6>📚 Documentación Técnica</h6>
                <a :href="equipo.wiki.documentacion" target="_blank">Abrir manuales y soporte del fabricante ➔</a>
              </div>
            </div>

          </div>

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

.grid-equipos { display: flex; flex-direction: column; gap: 25px; }

.tarjeta-equipo { background: white; border: 1px solid #e0e0e0; border-radius: 8px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); display: flex; flex-direction: column; }
.cabecera-tarjeta { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
.etiqueta-tipo { background: #e2eef7; color: #005596; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; }
.id-equipo { font-size: 1.1rem; color: #888; font-family: monospace; }

.badge-libre { background: #d4edda; color: #155724; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 0.85rem; }
.badge-ocupado { background: #fff3cd; color: #856404; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 0.85rem; border: 1px solid #ffeeba; }

.tarjeta-equipo h4 { margin: 0 0 10px 0; color: #333; font-size: 1.4rem; }
.descripcion { font-size: 1rem; color: #555; line-height: 1.5; margin-top: 0; margin-bottom: 20px; }

.btn-desplegar { background: #005596; color: white; border: none; padding: 10px 15px; border-radius: 4px; font-weight: bold; cursor: pointer; font-size: 0.95rem; text-align: center; }
.btn-desplegar:hover { background: #00447a; }

.ficha-tecnica-desplegada { background: #fdfdfd; border: 1px solid #eee; border-radius: 8px; padding: 0; margin-top: 15px; animation: slideDown 0.3s ease-out; overflow: hidden; }
@keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }

/* 1. BLOQUE DE RESERVAS */
.bloque-reservas { background-color: #f0f7ff; padding: 20px; border-bottom: 1px solid #cce0f0; }
.bloque-reservas h5 { margin: 0 0 15px 0; color: #005596; font-size: 1.1rem; }
.lista-reservas { background: white; padding: 15px; border-radius: 6px; border: 1px solid #cce0f0; margin-bottom: 15px; }
.lista-reservas.libre { background: #d4edda; border-color: #c3e6cb; color: #155724; font-weight: bold; }
.texto-aviso { margin: 0 0 10px 0; color: #d9534f; font-weight: bold; font-size: 0.9rem; }
.lista-reservas ul { margin: 0; padding-left: 20px; }
.lista-reservas li { font-size: 0.95rem; margin-bottom: 5px; color: #444; }
.formulario-reserva h6 { margin: 0 0 8px 0; color: #333; font-size: 0.95rem; }
.inputs-reserva { display: flex; gap: 10px; flex-wrap: wrap; }
.inputs-reserva input { padding: 8px; border: 1px solid #ccc; border-radius: 4px; flex: 1; min-width: 130px; }
.btn-reservar { background: #28a745; color: white; border: none; padding: 8px 15px; border-radius: 4px; font-weight: bold; cursor: pointer; transition: background 0.2s; white-space: nowrap; }
.btn-reservar:hover { background: #218838; }

/* 2. BLOQUE RESUMEN (IDENTIFICACIÓN BÁSICA) */
.bloque-resumen { padding: 20px; background-color: #fff; border-bottom: 1px solid #eee; }

/* 3. BLOQUE DE LA WIKI */
.bloque-wiki { padding: 20px; background-color: #fafafa; }
.bloque-wiki h5 { margin: 0 0 20px 0; color: #333; font-size: 1.2rem; border-bottom: 2px solid #ddd; padding-bottom: 5px; }
.wiki-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 15px; }
@media (max-width: 768px) { .wiki-grid-2 { grid-template-columns: 1fr; } }

.seccion-wiki { margin-bottom: 15px; }
.seccion-wiki h6 { margin: 0 0 8px 0; color: #005596; font-size: 1rem; }
.seccion-wiki p { font-size: 0.95rem; color: #444; line-height: 1.6; margin: 0; }
.seccion-wiki ul { padding-left: 15px; margin: 0; }
.seccion-wiki li { font-size: 0.9rem; color: #444; margin-bottom: 6px; line-height: 1.4; }

.doc-link a { color: #005596; font-weight: bold; text-decoration: none; display: inline-block; margin-top: 5px; }
.doc-link a:hover { text-decoration: underline; }
</style>