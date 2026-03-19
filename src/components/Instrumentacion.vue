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

// 🗄️ Base de datos: Ahora con "Estado" de los documentos
const inventario = ref([
  { 
    id: 'SNS-001', 
    nombre: 'SBE 5 Pressure Sensor', 
    tipo: 'Sensores de Presión', 
    desc: 'Sensor de presión de alta precisión diseñado específicamente para aplicaciones oceanográficas y de investigación marina.',
    fabricante: 'Sea-Bird Scientific',
    numeroSerie: '11599',
    rango: '0 a 10.000 psia',
    precision: '±0.015% del rango',
    voltaje: '8-18 V DC',
    salida: '0-5 V DC',
    ultimaCalibracion: '05 de mayo de 2023',
    periodicidad: '12 a 24 meses',

    reservas: [
      // Una reserva antigua que ya tiene el documento firmado
      { desde: '2026-04-10', hasta: '2026-04-25', proyecto: 'Campaña Costa Brava (ICATMAR)', estado: 'Aprobada' }
    ],
    nuevaReserva: { desde: '', hasta: '', proyecto: '', aceptaResponsabilidad: false },
    
    wiki: {
      descripcionGeneral: "El SBE 5 Pressure Sensor es un sensor de presión de alta precisión fabricado por Sea-Bird Scientific...",
      caracteristicasMedicion: ["Rango de Presión: 0 a 10.000 psia", "Precisión: ±0.015% del rango completo", "Resolución: 0.001% del rango completo"],
      caracteristicasFisicas: ["Diámetro: Aproximadamente 19 mm", "Longitud: Aproximadamente 76 mm"],
      especificacionesElectricas: ["Voltaje de Alimentación: 8-18 V DC", "Señal de Salida: 0-5 V DC"],
      principioFuncionamiento: "El sensor SBE 5 utiliza un transductor de presión de alta precisión basado en tecnología de galgas extensiométricas.",
      mantenimientoPreventivo: ["Inspección visual", "Enjuague con agua destilada", "Verificación funcional"],
      aplicaciones: ["Perfiles CTD", "Fondeos fijos", "Calibración batimétrica"],
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
    nuevaReserva: { desde: '', hasta: '', proyecto: '', aceptaResponsabilidad: false },
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
  if (!equipo.nuevaReserva.desde || !equipo.nuevaReserva.hasta || !equipo.nuevaReserva.proyecto) {
    alert("⚠️ Por favor, rellena las fechas y el proyecto de la campaña.")
    return
  }
  
  if (!equipo.nuevaReserva.aceptaResponsabilidad) {
    alert("⚖️ Debes aceptar las condiciones previas para procesar la reserva.")
    return
  }
  
  const fechaInicio = equipo.nuevaReserva.desde
  const fechaFin = equipo.nuevaReserva.hasta
  const nombreProyecto = equipo.nuevaReserva.proyecto

  // SE CREA LA RESERVA CON ESTADO PENDIENTE
  equipo.reservas.push({
    desde: fechaInicio,
    hasta: fechaFin,
    proyecto: nombreProyecto,
    estado: 'Pendiente' // 👈 El estado clave para el documento
  })
  
  const email = "sio@icm.csic.es"
  const asunto = encodeURIComponent(`PRE-RESERVA (Pendiente de Firma): ${equipo.nombre} (ID: ${equipo.id})`)
  const cuerpo = encodeURIComponent(`Hola equipo del SIO,\n\nHe registrado una pre-reserva en el portal. Necesito que me generéis el documento de responsabilidad para las siguientes fechas:\n\n- Instrumento: ${equipo.nombre}\n- S/N: ${equipo.numeroSerie}\n- Proyecto: ${nombreProyecto}\n- FECHAS: Del ${fechaInicio} al ${fechaFin}\n\nQuedo a la espera del PDF para devolverlo debidamente firmado.\n\nUn saludo,`)
  
  window.location.href = `mailto:${email}?subject=${asunto}&body=${cuerpo}`

  equipo.nuevaReserva = { desde: '', hasta: '', proyecto: '', aceptaResponsabilidad: false }
  alert(`✅ ¡Pre-reserva registrada en el calendario!\n\nAparecerá como 'Pendiente de Firma' hasta que el SIO reciba y valide tu documento oficial.`)
}
</script>

<template>
  <div class="pagina-catalogo">
    
    <div class="cabecera-catalogo">
      <button @click="$emit('volver')" class="btn-volver">⬅ Volver al Inicio</button>
      <h2>Buscador de Instrumentación Científica</h2>
      <p>Explora nuestro catálogo, revisa las fichas técnicas y gestiona tus campañas.</p>
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
            <span v-if="equipo.reservas.some(r => r.estado === 'Pendiente')" class="badge-pendiente-top">⏳ Pendiente Firma</span>
            <span v-else-if="equipo.reservas.length > 0" class="badge-ocupado">🗓️ Ocupado</span>
            <span v-else class="badge-libre">✅ Disponible</span>
          </div>
          
          <h4>{{ equipo.nombre }} <span class="id-equipo">({{ equipo.id }})</span></h4>
          <p class="descripcion">{{ equipo.desc }}</p>
          
          <button @click="toggleDetalles(equipo.id)" class="btn-desplegar">
            {{ equiposExpandidos.includes(equipo.id) ? '▲ Ocultar Ficha y Reservas' : '▼ Ver Ficha Técnica y Calendario' }}
          </button>

          <div v-if="equiposExpandidos.includes(equipo.id)" class="ficha-tecnica-desplegada">
            
            <div class="bloque-reservas">
              <h5>📅 Calendario y Estado de Firmas</h5>
              
              <div v-if="equipo.reservas.length > 0" class="lista-reservas">
                <p class="texto-aviso">Próximas salidas del equipo:</p>
                <ul>
                  <li v-for="(res, index) in equipo.reservas" :key="index" class="item-reserva">
                    <div class="datos-reserva">
                      <strong>Del {{ res.desde }} al {{ res.hasta }}</strong> - {{ res.proyecto }}
                    </div>
                    <span v-if="res.estado === 'Aprobada'" class="estado-ok">✅ Doc. Firmado</span>
                    <span v-if="res.estado === 'Pendiente'" class="estado-espera">⏳ Pendiente Firma</span>
                  </li>
                </ul>
              </div>
              <div v-else class="lista-reservas libre">
                <p>El equipo está libre. No hay campañas programadas.</p>
              </div>

              <div class="formulario-reserva">
                <h6>1. Iniciar trámite de cesión:</h6>
                <div class="inputs-reserva">
                  <input type="date" v-model="equipo.nuevaReserva.desde" title="Fecha de inicio">
                  <input type="date" v-model="equipo.nuevaReserva.hasta" title="Fecha de fin">
                  <input type="text" v-model="equipo.nuevaReserva.proyecto" placeholder="Nombre del proyecto (Ej. Mareas 2026)">
                </div>

                <div class="caja-legal">
                  <h6>2. Pre-acuerdo de Responsabilidad (ICM-CSIC)</h6>
                  <p class="texto-legal">
                    El equipo quedará bloqueado en estado <strong>"Pendiente de Firma"</strong>. El investigador responsable deberá devolver el PDF oficial firmado para que el SIO apruebe la salida del instrumento.
                  </p>
                  
                  <div class="firma-electronica">
                    <label class="checkbox-legal">
                      <input type="checkbox" v-model="equipo.nuevaReserva.aceptaResponsabilidad">
                      Solicitar documento oficial y añadir pre-reserva al calendario.
                    </label>
                  </div>
                </div>

                <button 
                  @click="confirmarReserva(equipo)" 
                  class="btn-reservar" 
                  :class="{ 'btn-bloqueado': !equipo.nuevaReserva.aceptaResponsabilidad }"
                >
                  Generar Pre-Reserva
                </button>
              </div>
            </div>

            <div class="bloque-resumen">
              <div class="wiki-grid-2">
                <div class="seccion-wiki">
                  <h6>📋 Identificación</h6>
                  <ul><li><strong>Fabricante:</strong> {{ equipo.fabricante }}</li><li><strong>S/N:</strong> {{ equipo.numeroSerie }}</li></ul>
                </div>
                <div class="seccion-wiki">
                  <h6>🔧 Calibración</h6>
                  <ul><li><strong>Última:</strong> {{ equipo.ultimaCalibracion }}</li><li><strong>Periodicidad:</strong> {{ equipo.periodicidad }}</li></ul>
                </div>
              </div>
            </div>

            <div v-if="equipo.wiki" class="bloque-wiki">
              <h5>📖 Enciclopedia SIO (Wiki)</h5>
              <div class="seccion-wiki"><p>{{ equipo.wiki.descripcionGeneral }}</p></div>
              <div class="wiki-grid-2">
                <div class="seccion-wiki"><h6>📏 Medición</h6><ul><li v-for="(item, index) in equipo.wiki.caracteristicasMedicion" :key="index">{{ item }}</li></ul></div>
                <div class="seccion-wiki"><h6>⚡ Eléctricas</h6><ul><li v-for="(item, index) in equipo.wiki.especificacionesElectricas" :key="index">{{ item }}</li></ul></div>
              </div>
              <div class="wiki-grid-2">
                <div class="seccion-wiki"><h6>📦 Físicas</h6><ul><li v-for="(item, index) in equipo.wiki.caracteristicasFisicas" :key="index">{{ item }}</li></ul></div>
                <div class="seccion-wiki"><h6>🛠️ Mantenimiento</h6><ul><li v-for="(item, index) in equipo.wiki.mantenimientoPreventivo" :key="index">{{ item }}</li></ul></div>
              </div>
              <div class="seccion-wiki"><h6>⚙️ Principio</h6><p>{{ equipo.wiki.principioFuncionamiento }}</p></div>
            </div>

          </div>

        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
/* (Estilos Base Mantenidos) */
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
.badge-ocupado { background: #cce5ff; color: #004085; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 0.85rem; border: 1px solid #b8daff; }
.badge-pendiente-top { background: #fff3cd; color: #856404; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 0.85rem; border: 1px solid #ffeeba; }

.tarjeta-equipo h4 { margin: 0 0 10px 0; color: #333; font-size: 1.4rem; }
.descripcion { font-size: 1rem; color: #555; line-height: 1.5; margin-top: 0; margin-bottom: 20px; }
.btn-desplegar { background: #005596; color: white; border: none; padding: 10px 15px; border-radius: 4px; font-weight: bold; cursor: pointer; font-size: 0.95rem; text-align: center; }
.btn-desplegar:hover { background: #00447a; }
.ficha-tecnica-desplegada { background: #fdfdfd; border: 1px solid #eee; border-radius: 8px; padding: 0; margin-top: 15px; animation: slideDown 0.3s ease-out; overflow: hidden; }
@keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }

/* BLOQUE DE RESERVAS Y ESTADOS */
.bloque-reservas { background-color: #f0f7ff; padding: 20px; border-bottom: 1px solid #cce0f0; }
.bloque-reservas h5 { margin: 0 0 15px 0; color: #005596; font-size: 1.1rem; }
.lista-reservas { background: white; padding: 15px; border-radius: 6px; border: 1px solid #cce0f0; margin-bottom: 15px; }
.lista-reservas.libre { background: #d4edda; border-color: #c3e6cb; color: #155724; font-weight: bold; }
.texto-aviso { margin: 0 0 10px 0; color: #005596; font-weight: bold; font-size: 0.9rem; }
.lista-reservas ul { margin: 0; padding-left: 0; list-style: none; }

/* Nuevo diseño para la lista de reservas con el estado a la derecha */
.item-reserva { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; padding: 8px 0; font-size: 0.95rem; color: #444; }
.item-reserva:last-child { border-bottom: none; }
.estado-ok { background: #d4edda; color: #155724; font-size: 0.8rem; padding: 3px 8px; border-radius: 12px; font-weight: bold; }
.estado-espera { background: #fff3cd; color: #856404; font-size: 0.8rem; padding: 3px 8px; border-radius: 12px; font-weight: bold; }

.formulario-reserva h6 { margin: 0 0 8px 0; color: #333; font-size: 0.95rem; font-weight: bold; }
.inputs-reserva { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 15px; }
.inputs-reserva input { padding: 10px; border: 1px solid #ccc; border-radius: 4px; flex: 1; min-width: 130px; }

.caja-legal { background-color: #fffaf0; border: 1px solid #ffeeba; border-left: 4px solid #ffc107; padding: 15px; border-radius: 4px; margin-bottom: 20px; }
.texto-legal { font-size: 0.85rem; color: #665c3e; line-height: 1.5; margin: 0 0 15px 0; }
.firma-electronica { display: flex; flex-direction: column; gap: 10px; }
.checkbox-legal { font-size: 0.9rem; font-weight: bold; color: #333; cursor: pointer; display: flex; align-items: center; gap: 8px; }

.btn-reservar { background: #28a745; color: white; border: none; padding: 12px 20px; border-radius: 4px; font-weight: bold; font-size: 1rem; cursor: pointer; transition: all 0.2s; width: 100%; }
.btn-reservar:hover { background: #218838; }
.btn-bloqueado { background: #6c757d; cursor: not-allowed; opacity: 0.6; }
.btn-bloqueado:hover { background: #6c757d; }

/* WIKI Y RESUMEN */
.bloque-resumen { padding: 20px; background-color: #fff; border-bottom: 1px solid #eee; }
.bloque-wiki { padding: 20px; background-color: #fafafa; }
.bloque-wiki h5 { margin: 0 0 20px 0; color: #333; font-size: 1.2rem; border-bottom: 2px solid #ddd; padding-bottom: 5px; }
.wiki-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 15px; }
@media (max-width: 768px) { .wiki-grid-2 { grid-template-columns: 1fr; } }
.seccion-wiki { margin-bottom: 15px; }
.seccion-wiki h6 { margin: 0 0 8px 0; color: #005596; font-size: 1rem; }
.seccion-wiki p { font-size: 0.95rem; color: #444; line-height: 1.6; margin: 0; }
.seccion-wiki ul { padding-left: 15px; margin: 0; }
.seccion-wiki li { font-size: 0.9rem; color: #444; margin-bottom: 6px; line-height: 1.4; }
</style>