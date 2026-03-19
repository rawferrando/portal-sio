<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

const textoBusqueda = ref('')
const tipoSeleccionado = ref('Todos')
const equiposExpandidos = ref([])

// Variables para el Modal (El Documento Simulado)
const modalVisible = ref(false)
const docSoloLectura = ref(false)
const documentoActual = ref({
  equipoId: '', equipoNombre: '', equipoSn: '',
  desde: '', hasta: '', proyecto: '',
  firmante: '', fechaFirma: ''
})

const toggleDetalles = (id) => {
  const index = equiposExpandidos.value.indexOf(id)
  if (index > -1) {
    equiposExpandidos.value.splice(index, 1)
  } else {
    equiposExpandidos.value.push(id)
  }
}

// Base de datos
const inventario = ref([
  { 
    id: 'SNS-001', nombre: 'SBE 5 Pressure Sensor', tipo: 'Sensores de Presión', 
    desc: 'Sensor de presión de alta precisión para aplicaciones oceanográficas.',
    fabricante: 'Sea-Bird Scientific', numeroSerie: '11599',
    rango: '0 a 10.000 psia', precision: '±0.015% del rango', voltaje: '8-18 V DC', salida: '0-5 V DC',
    ultimaCalibracion: '05 de mayo de 2023', periodicidad: '12 a 24 meses',

    // Lista de reservas (Añadimos datos de la firma para poder verlos después)
    reservas: [
      { 
        desde: '2026-04-10', hasta: '2026-04-25', proyecto: 'Campaña Costa Brava', 
        estado: 'Firmado', firmante: 'Dr. Joan Ribas', fechaFirma: '2026-03-15' 
      }
    ],
    nuevaReserva: { desde: '', hasta: '', proyecto: '' },
    
    wiki: {
      descripcionGeneral: "El SBE 5 Pressure Sensor es un sensor de presión de alta precisión...",
      caracteristicasMedicion: ["Rango: 0 a 10.000 psia", "Precisión: ±0.015%"],
      caracteristicasFisicas: ["Diámetro: 19 mm", "Longitud: 76 mm"],
      especificacionesElectricas: ["Voltaje: 8-18 V DC", "Salida: 0-5 V DC"],
      principioFuncionamiento: "Utiliza un transductor basado en galgas extensiométricas.",
      mantenimientoPreventivo: ["Enjuague con agua destilada", "Verificación funcional"],
      aplicaciones: ["Perfiles CTD", "Fondeos fijos"],
      documentacion: "https://www.seabird.com/support"
    }
  },
  { 
    id: 'SNS-002', nombre: 'Salinómetro Guildline Portasal', tipo: 'Laboratorio', 
    desc: 'Análisis de salinidad en muestras de agua con altísima precisión.',
    fabricante: 'Guildline Instruments', numeroSerie: '67890',
    rango: '0.005 a 42 PSU', precision: '±0.003 PSU', voltaje: '110/220 V AC', salida: 'RS-232',
    ultimaCalibracion: '12 de enero de 2024', periodicidad: '12 meses',
    reservas: [],
    nuevaReserva: { desde: '', hasta: '', proyecto: '' },
    wiki: null
  }
])

const equiposFiltrados = computed(() => {
  return inventario.value.filter(equipo => {
    const texto = textoBusqueda.value.toLowerCase()
    const coincideTexto = equipo.nombre.toLowerCase().includes(texto) || equipo.id.toLowerCase().includes(texto)
    const coincideTipo = tipoSeleccionado.value === 'Todos' || equipo.tipo === tipoSeleccionado.value
    return coincideTexto && coincideTipo
  })
})

// Paso 1: Abrir el documento en blanco para rellenar
const prepararDocumento = (equipo) => {
  if (!equipo.nuevaReserva.desde || !equipo.nuevaReserva.hasta || !equipo.nuevaReserva.proyecto) {
    alert("⚠️ Por favor, rellena las fechas y el proyecto antes de generar el documento.")
    return
  }
  
  // Preparamos los datos para mostrarlos en el papel
  documentoActual.value = {
    equipoId: equipo.id,
    equipoNombre: equipo.nombre,
    equipoSn: equipo.numeroSerie,
    desde: equipo.nuevaReserva.desde,
    hasta: equipo.nuevaReserva.hasta,
    proyecto: equipo.nuevaReserva.proyecto,
    firmante: '', // Estará en blanco para que lo firme
    fechaFirma: new Date().toLocaleDateString('es-ES')
  }
  
  docSoloLectura.value = false
  modalVisible.value = true
}

// Paso 2: Guardar la firma y cerrar el documento
const firmarYGuardar = () => {
  if (!documentoActual.value.firmante) {
    alert("✍️ Debes escribir tu nombre y DNI como firma de conformidad.")
    return
  }

  // Buscamos el equipo y le añadimos la reserva firmada
  const equipo = inventario.value.find(e => e.id === documentoActual.value.equipoId)
  if (equipo) {
    equipo.reservas.push({
      desde: documentoActual.value.desde,
      hasta: documentoActual.value.hasta,
      proyecto: documentoActual.value.proyecto,
      estado: 'Firmado',
      firmante: documentoActual.value.firmante,
      fechaFirma: documentoActual.value.fechaFirma
    })
    // Limpiamos el formulario base
    equipo.nuevaReserva = { desde: '', hasta: '', proyecto: '' }
  }

  modalVisible.value = false
}

// Abrir un documento que ya estaba firmado para verlo
const verDocumentoGuardado = (reserva, equipo) => {
  documentoActual.value = {
    equipoId: equipo.id,
    equipoNombre: equipo.nombre,
    equipoSn: equipo.numeroSerie,
    desde: reserva.desde,
    hasta: reserva.hasta,
    proyecto: reserva.proyecto,
    firmante: reserva.firmante,
    fechaFirma: reserva.fechaFirma
  }
  docSoloLectura.value = true
  modalVisible.value = true
}

const cerrarModal = () => {
  modalVisible.value = false
}
</script>

<template>
  <div class="pagina-catalogo">
    
    <div class="cabecera-catalogo">
      <button @click="$emit('volver')" class="btn-volver">⬅ Volver al Inicio</button>
      <h2>Buscador de Instrumentación Científica</h2>
      <p>Explora nuestro catálogo y gestiona los documentos de responsabilidad de tus campañas.</p>
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
            {{ equiposExpandidos.includes(equipo.id) ? '▲ Ocultar Ficha y Reservas' : '▼ Ver Ficha Técnica y Calendario' }}
          </button>

          <div v-if="equiposExpandidos.includes(equipo.id)" class="ficha-tecnica-desplegada">
            
            <div class="bloque-reservas">
              <h5>📅 Calendario y Custodia de Documentos</h5>
              
              <div v-if="equipo.reservas.length > 0" class="lista-reservas">
                <ul>
                  <li v-for="(res, index) in equipo.reservas" :key="index" class="item-reserva">
                    <div class="datos-reserva">
                      <strong>Del {{ res.desde }} al {{ res.hasta }}</strong> - {{ res.proyecto }}
                    </div>
                    <div class="acciones-reserva">
                      <span class="estado-ok">✅ Doc. Firmado</span>
                      <button @click="verDocumentoGuardado(res, equipo)" class="btn-ver-doc">👁️ Ver Documento</button>
                    </div>
                  </li>
                </ul>
              </div>
              <div v-else class="lista-reservas libre">
                <p>El equipo está libre. No hay campañas programadas.</p>
              </div>

              <div class="formulario-reserva">
                <h6>1. Configurar nueva reserva:</h6>
                <div class="inputs-reserva">
                  <input type="date" v-model="equipo.nuevaReserva.desde" title="Fecha de inicio">
                  <input type="date" v-model="equipo.nuevaReserva.hasta" title="Fecha de fin">
                  <input type="text" v-model="equipo.nuevaReserva.proyecto" placeholder="Nombre del proyecto (Ej. Mareas 2026)">
                </div>

                <button @click="prepararDocumento(equipo)" class="btn-generar-doc">
                  📄 Generar Documento para Firmar
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

          </div>
        </div>
      </div>
    </div>

    <div v-if="modalVisible" class="modal-overlay">
      <div class="modal-papel">
        
        <div class="cabecera-papel">
          <h3>🏛️ DOCUMENTO DE RESPONSABILIDAD DE PRÉSTAMO</h3>
          <p>Instituto de Ciencias del Mar (ICM-CSIC) - Servicio de Ingeniería Oceanográfica</p>
        </div>

        <div class="cuerpo-papel">
          <p>Por la presente, se formaliza la cesión temporal del siguiente equipamiento científico para su uso exclusivo en la campaña detallada a continuación:</p>
          
          <div class="datos-papel">
            <p><strong>Instrumento:</strong> {{ documentoActual.equipoNombre }} (ID: {{ documentoActual.equipoId }})</p>
            <p><strong>Número de Serie:</strong> {{ documentoActual.equipoSn }}</p>
            <p><strong>Proyecto/Campaña:</strong> {{ documentoActual.proyecto }}</p>
            <p><strong>Periodo de Cesión:</strong> Del {{ documentoActual.desde }} al {{ documentoActual.hasta }}</p>
          </div>

          <p class="texto-legal-papel">
            <strong>CLÁUSULA DE RESPONSABILIDAD:</strong> El abajo firmante, actuando como Investigador Principal o Responsable de Campaña, asume la responsabilidad civil e institucional sobre el equipo descrito. Se compromete a garantizar su correcta operación según los manuales del fabricante y a cubrir los costes de reparación o reposición en caso de pérdida, robo o negligencia operativa durante el periodo de cesión estipulado.
          </p>

          <div class="zona-firma">
            <div class="firma-fecha">
              <label>Fecha de la firma:</label>
              <span>{{ documentoActual.fechaFirma }}</span>
            </div>
            
            <div class="firma-input-caja">
              <label>Responsable de Préstamo (Nombre y DNI):</label>
              <input v-if="!docSoloLectura" v-model="documentoActual.firmante" type="text" placeholder="Escribe aquí para firmar digitalmente..." class="input-firma-real">
              <span v-else class="firma-estampada">✍️ {{ documentoActual.firmante }}</span>
            </div>
          </div>
        </div>

        <div class="pie-papel">
          <button @click="cerrarModal" class="btn-cancelar">Cerrar</button>
          <button v-if="!docSoloLectura" @click="firmarYGuardar" class="btn-firmar">Firmar y Guardar Documento</button>
        </div>

      </div>
    </div>

  </div>
</template>

<style scoped>
/* ESTILOS BASE */
.pagina-catalogo { animation: fadeIn 0.4s ease-in-out; position: relative; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
.cabecera-catalogo { margin-bottom: 30px; }
.cabecera-catalogo h2 { color: #005596; margin-bottom: 5px; }
.btn-volver { background: #6c757d; color: white; border: none; padding: 8px 15px; border-radius: 4px; cursor: pointer; font-weight: bold; margin-bottom: 20px; }
.caja-filtros { background: #f8f9fa; padding: 25px; border-radius: 8px; border: 1px solid #ddd; display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 30px; }
.grupo-filtro { flex: 1; min-width: 250px; display: flex; flex-direction: column; gap: 8px; }
.grupo-filtro input, .grupo-filtro select { padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 1rem; }
.grid-equipos { display: flex; flex-direction: column; gap: 25px; }
.tarjeta-equipo { background: white; border: 1px solid #e0e0e0; border-radius: 8px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
.cabecera-tarjeta { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
.etiqueta-tipo { background: #e2eef7; color: #005596; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; }
.id-equipo { font-size: 1.1rem; color: #888; font-family: monospace; }
.badge-libre { background: #d4edda; color: #155724; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 0.85rem; }
.badge-ocupado { background: #fff3cd; color: #856404; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 0.85rem; border: 1px solid #ffeeba; }

.tarjeta-equipo h4 { margin: 0 0 10px 0; color: #333; font-size: 1.4rem; }
.descripcion { font-size: 1rem; color: #555; line-height: 1.5; margin-top: 0; margin-bottom: 20px; }
.btn-desplegar { background: #005596; color: white; border: none; padding: 10px 15px; border-radius: 4px; font-weight: bold; cursor: pointer; }
.ficha-tecnica-desplegada { background: #fdfdfd; border: 1px solid #eee; border-radius: 8px; margin-top: 15px; overflow: hidden; }

/* RESERVAS Y ACCIONES */
.bloque-reservas { background-color: #f0f7ff; padding: 20px; border-bottom: 1px solid #cce0f0; }
.bloque-reservas h5 { margin: 0 0 15px 0; color: #005596; font-size: 1.1rem; }
.lista-reservas { background: white; padding: 15px; border-radius: 6px; border: 1px solid #cce0f0; margin-bottom: 15px; }
.item-reserva { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; padding: 10px 0; font-size: 0.95rem; }
.acciones-reserva { display: flex; align-items: center; gap: 10px; }
.estado-ok { background: #d4edda; color: #155724; padding: 4px 8px; border-radius: 12px; font-size: 0.85rem; font-weight: bold; border: 1px solid #c3e6cb; }
.btn-ver-doc { background: #e2eef7; color: #005596; border: 1px solid #b8daff; padding: 5px 10px; border-radius: 4px; cursor: pointer; font-size: 0.85rem; font-weight: bold; }
.btn-ver-doc:hover { background: #cce5ff; }

.inputs-reserva { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 15px; }
.inputs-reserva input { padding: 10px; border: 1px solid #ccc; border-radius: 4px; flex: 1; min-width: 130px; }
.btn-generar-doc { background: #005596; color: white; border: none; padding: 12px 20px; border-radius: 4px; font-weight: bold; font-size: 1rem; cursor: pointer; width: 100%; transition: background 0.2s; }
.btn-generar-doc:hover { background: #00447a; }

.bloque-resumen { padding: 20px; background-color: #fff; }
.wiki-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.seccion-wiki h6 { margin: 0 0 8px 0; color: #005596; }
.seccion-wiki ul { padding-left: 15px; margin: 0; font-size: 0.9rem; color: #444; }

/* =========================================
   ESTILOS DEL MODAL (EL DOCUMENTO DE PAPEL)
   ========================================= */
.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.6); display: flex; justify-content: center; align-items: center; z-index: 1000; padding: 20px; }
.modal-papel { background: white; width: 100%; max-width: 700px; border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); display: flex; flex-direction: column; max-height: 90vh; overflow-y: auto; font-family: 'Times New Roman', serif; }

.cabecera-papel { text-align: center; border-bottom: 2px solid #333; padding: 25px 20px 15px 20px; background: #fafafa; }
.cabecera-papel h3 { margin: 0 0 5px 0; font-size: 1.3rem; color: #222; letter-spacing: 1px; }
.cabecera-papel p { margin: 0; font-size: 0.95rem; color: #555; }

.cuerpo-papel { padding: 30px; font-size: 1.05rem; line-height: 1.6; color: #333; }
.datos-papel { background: #f9f9f9; border: 1px solid #ddd; padding: 15px; margin: 20px 0; }
.datos-papel p { margin: 5px 0; }
.texto-legal-papel { text-align: justify; margin-bottom: 40px; }

.zona-firma { border-top: 1px dashed #ccc; padding-top: 20px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px; }
.firma-fecha { font-weight: bold; }
.firma-input-caja { display: flex; flex-direction: column; flex: 1; min-width: 250px; }
.firma-input-caja label { font-weight: bold; margin-bottom: 5px; font-size: 0.95rem; }
.input-firma-real { padding: 10px; border: 1px solid #333; font-family: 'Courier New', Courier, monospace; font-size: 1rem; background: #fffdf5; }
.firma-estampada { font-family: 'Brush Script MT', cursive, sans-serif; font-size: 1.5rem; color: #000080; border-bottom: 1px solid #ccc; padding: 5px 0; }

.pie-papel { display: flex; justify-content: flex-end; gap: 15px; padding: 20px; border-top: 1px solid #eee; background: #f5f5f5; font-family: Arial, sans-serif; }
.btn-cancelar { background: #ddd; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; }
.btn-firmar { background: #28a745; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; }
.btn-firmar:hover { background: #218838; }
</style>