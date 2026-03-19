<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

const textoBusqueda = ref('')
const tipoSeleccionado = ref('Todos')
const equiposExpandidos = ref([])

// Variables para el Documento
const modalVisible = ref(false)
const documentoActual = ref({
  equipoId: '', equipoNombre: '', equipoSn: '',
  desde: '', hasta: '', proyecto: '', fechaGeneracion: ''
})

const toggleDetalles = (id) => {
  const index = equiposExpandidos.value.indexOf(id)
  if (index > -1) {
    equiposExpandidos.value.splice(index, 1)
  } else {
    equiposExpandidos.value.push(id)
  }
}

// 🗄️ Base de datos: Preparada para subida de archivos
const inventario = ref([
  { 
    id: 'SNS-001', nombre: 'SBE 5 Pressure Sensor', tipo: 'Sensores de Presión', 
    desc: 'Sensor de presión de alta precisión para aplicaciones oceanográficas.',
    fabricante: 'Sea-Bird Scientific', numeroSerie: '11599',
    rango: '0 a 10.000 psia', precision: '±0.015% del rango', voltaje: '8-18 V DC', salida: '0-5 V DC',
    ultimaCalibracion: '05 de mayo de 2023', periodicidad: '12 a 24 meses',

    reservas: [
      // Reserva completada con archivo subido
      { 
        desde: '2026-04-10', hasta: '2026-04-25', proyecto: 'Campaña Costa Brava', 
        estado: 'Aprobada', archivo: 'Responsabilidad_SBE5_Firmado_Ribas.pdf' 
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
    reservas: [], nuevaReserva: { desde: '', hasta: '', proyecto: '' }, wiki: null
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

// 1. Generar la reserva inicial (Estado: Pendiente) y abrir el documento para descargar
const solicitarReserva = (equipo) => {
  if (!equipo.nuevaReserva.desde || !equipo.nuevaReserva.hasta || !equipo.nuevaReserva.proyecto) {
    alert("⚠️ Por favor, rellena las fechas y el proyecto de la campaña.")
    return
  }
  
  // Guardamos la reserva como pendiente
  equipo.reservas.push({
    desde: equipo.nuevaReserva.desde,
    hasta: equipo.nuevaReserva.hasta,
    proyecto: equipo.nuevaReserva.proyecto,
    estado: 'Pendiente',
    archivo: null
  })

  // Preparamos el documento para visualizar y descargar
  documentoActual.value = {
    equipoId: equipo.id,
    equipoNombre: equipo.nombre,
    equipoSn: equipo.numeroSerie,
    desde: equipo.nuevaReserva.desde,
    hasta: equipo.nuevaReserva.hasta,
    proyecto: equipo.nuevaReserva.proyecto,
    fechaGeneracion: new Date().toLocaleDateString('es-ES')
  }
  
  equipo.nuevaReserva = { desde: '', hasta: '', proyecto: '' }
  modalVisible.value = true
}

// 2. Función para imprimir/guardar como PDF (Usa el sistema nativo del navegador)
const descargarPDF = () => {
  window.print()
}

// 3. Función para simular la subida del archivo firmado
const subirDocumento = (event, reserva) => {
  const archivo = event.target.files[0]
  if (archivo) {
    reserva.estado = 'Aprobada'
    reserva.archivo = archivo.name
    alert(`✅ Documento "${archivo.name}" subido con éxito. La reserva ha sido validada institucionalmente.`)
  }
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
      <p>Explora el catálogo, bloquea fechas y gestiona la subida de documentos de custodia.</p>
    </div>

    <div class="caja-filtros">
      <div class="grupo-filtro">
        <label>🔍 Buscar por palabra clave o ID:</label>
        <input v-model="textoBusqueda" type="text" placeholder="Ej. SBE 5, presión...">
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
            <span v-if="equipo.reservas.some(r => r.estado === 'Pendiente')" class="badge-pendiente-top">⏳ Pendiente Subir PDF</span>
            <span v-else-if="equipo.reservas.length > 0" class="badge-ocupado">🗓️ Ocupado</span>
            <span v-else class="badge-libre">✅ Disponible</span>
          </div>
          
          <h4>{{ equipo.nombre }} <span class="id-equipo">({{ equipo.id }})</span></h4>
          <p class="descripcion">{{ equipo.desc }}</p>
          
          <button @click="toggleDetalles(equipo.id)" class="btn-desplegar">
            {{ equiposExpandidos.includes(equipo.id) ? '▲ Ocultar Ficha y Reservas' : '▼ Ver Ficha Técnica y Gestor de Cesión' }}
          </button>

          <div v-if="equiposExpandidos.includes(equipo.id)" class="ficha-tecnica-desplegada">
            
            <div class="bloque-reservas">
              <h5>📅 Calendario y Gestor de Documentación</h5>
              
              <div v-if="equipo.reservas.length > 0" class="lista-reservas">
                <ul>
                  <li v-for="(res, index) in equipo.reservas" :key="index" class="item-reserva">
                    <div class="datos-reserva">
                      <strong>Del {{ res.desde }} al {{ res.hasta }}</strong> - {{ res.proyecto }}
                    </div>
                    
                    <div class="acciones-reserva">
                      <span v-if="res.estado === 'Aprobada'" class="estado-ok" :title="res.archivo">
                        ✅ Validado: {{ res.archivo.length > 15 ? res.archivo.substring(0, 15) + '...' : res.archivo }}
                      </span>
                      
                      <label v-if="res.estado === 'Pendiente'" class="btn-subir">
                        📤 Subir PDF Firmado
                        <input type="file" accept=".pdf" @change="subirDocumento($event, res)" style="display: none;">
                      </label>
                    </div>
                  </li>
                </ul>
              </div>
              <div v-else class="lista-reservas libre">
                <p>El equipo está libre. No hay campañas programadas.</p>
              </div>

<div class="formulario-reserva">
                <h6>1. Nueva solicitud de cesión:</h6>
                <div class="inputs-reserva">
                  
                  <div class="campo-etiquetado">
                    <label>📅 Fecha de Inicio:</label>
                    <input type="date" v-model="equipo.nuevaReserva.desde">
                  </div>
                  
                  <div class="campo-etiquetado">
                    <label>📅 Fecha de Fin:</label>
                    <input type="date" v-model="equipo.nuevaReserva.hasta">
                  </div>
                  
                  <div class="campo-etiquetado">
                    <label>🔬 Campaña o Proyecto:</label>
                    <input type="text" v-model="equipo.nuevaReserva.proyecto" placeholder="Ej. Mareas 2026">
                  </div>

                </div>

                <button @click="solicitarReserva(equipo)" class="btn-generar-doc">
                  Crear Solicitud y Descargar Documento
                </button>
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
        
        <div class="area-impresion">
          <div class="cabecera-papel">
            <h3>🏛️ DOCUMENTO DE RESPONSABILIDAD DE PRÉSTAMO</h3>
            <p>Instituto de Ciencias del Mar (ICM-CSIC) - Servicio de Ingeniería Oceanográfica</p>
          </div>

          <div class="cuerpo-papel">
            <p>Por la presente, se genera la solicitud de cesión temporal del siguiente equipamiento científico:</p>
            
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
              <p><strong>Fecha de expedición:</strong> {{ documentoActual.fechaGeneracion }}</p>
              <div class="caja-firma-vacia">
                <p>Firma del Responsable (Certificado Digital o Manuscrita)</p>
              </div>
            </div>
          </div>
        </div>

        <div class="pie-papel no-imprimir">
          <div class="instrucciones-descarga">
            <p><strong>Siguiente paso:</strong> Descarga este documento, fírmalo con AutoFirma/FNMT y súbelo de vuelta en el panel de reservas.</p>
          </div>
          <div class="botones-modal">
            <button @click="cerrarModal" class="btn-cancelar">Cerrar</button>
            <button @click="descargarPDF" class="btn-imprimir">🖨️ Descargar como PDF</button>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<style scoped>
/* ESTILOS BASE Y GRID MANTENIDOS */
.pagina-catalogo { animation: fadeIn 0.4s ease; }
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
.badge-pendiente-top { background: #f8d7da; color: #721c24; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 0.85rem; border: 1px solid #f5c6cb; }

.tarjeta-equipo h4 { margin: 0 0 10px 0; color: #333; font-size: 1.4rem; }
.descripcion { font-size: 1rem; color: #555; line-height: 1.5; margin-top: 0; margin-bottom: 20px; }
.btn-desplegar { background: #005596; color: white; border: none; padding: 10px 15px; border-radius: 4px; font-weight: bold; cursor: pointer; }
.ficha-tecnica-desplegada { background: #fdfdfd; border: 1px solid #eee; border-radius: 8px; margin-top: 15px; overflow: hidden; }

/* BLOQUE RESERVAS Y BOTÓN SUBIR */
.bloque-reservas { background-color: #f0f7ff; padding: 20px; border-bottom: 1px solid #cce0f0; }
.bloque-reservas h5 { margin: 0 0 15px 0; color: #005596; font-size: 1.1rem; }
.lista-reservas { background: white; padding: 15px; border-radius: 6px; border: 1px solid #cce0f0; margin-bottom: 15px; }
.item-reserva { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; padding: 12px 0; font-size: 0.95rem; }
.acciones-reserva { display: flex; align-items: center; gap: 10px; }
.estado-ok { background: #d4edda; color: #155724; padding: 5px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold; border: 1px solid #c3e6cb; cursor: help; }

.btn-subir { background: #ffc107; color: #856404; border: 1px solid #ffeeba; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-size: 0.85rem; font-weight: bold; display: inline-block; transition: background 0.2s; }
.btn-subir:hover { background: #e0a800; }

.inputs-reserva { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 15px; }
.inputs-reserva input { padding: 10px; border: 1px solid #ccc; border-radius: 4px; flex: 1; min-width: 130px; }
.btn-generar-doc { background: #005596; color: white; border: none; padding: 12px 20px; border-radius: 4px; font-weight: bold; font-size: 1rem; cursor: pointer; width: 100%; }
.btn-generar-doc:hover { background: #00447a; }

.bloque-resumen { padding: 20px; background-color: #fff; }
.wiki-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.seccion-wiki h6 { margin: 0 0 8px 0; color: #005596; }
.seccion-wiki ul { padding-left: 15px; margin: 0; font-size: 0.9rem; color: #444; }

/* MODAL Y DOCUMENTO DE IMPRESIÓN */
.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.7); display: flex; justify-content: center; align-items: center; z-index: 1000; padding: 20px; }
.modal-papel { background: white; width: 100%; max-width: 750px; border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); display: flex; flex-direction: column; max-height: 90vh; overflow-y: auto; }
.area-impresion { font-family: 'Times New Roman', serif; padding: 40px; }

.cabecera-papel { text-align: center; border-bottom: 2px solid #333; padding-bottom: 15px; margin-bottom: 25px; }
.cabecera-papel h3 { margin: 0 0 5px 0; font-size: 1.3rem; color: #000; letter-spacing: 1px; }
.cabecera-papel p { margin: 0; font-size: 0.95rem; color: #333; }

.cuerpo-papel { font-size: 1.05rem; line-height: 1.6; color: #000; }
.datos-papel { border: 1px solid #333; padding: 15px; margin: 20px 0; background: #fff; }
.datos-papel p { margin: 5px 0; }
.texto-legal-papel { text-align: justify; margin-bottom: 40px; }

.zona-firma { border-top: 1px dashed #999; padding-top: 20px; display: flex; flex-direction: column; gap: 30px; }
.caja-firma-vacia { width: 300px; height: 100px; border: 1px solid #ccc; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 10px; color: #666; font-size: 0.85rem; }

.pie-papel { display: flex; flex-direction: column; gap: 15px; padding: 20px; border-top: 1px solid #eee; background: #f5f5f5; font-family: Arial, sans-serif; }
.instrucciones-descarga { background: #e2eef7; padding: 10px; border-left: 4px solid #005596; font-size: 0.9rem; color: #005596; }
.botones-modal { display: flex; justify-content: flex-end; gap: 15px; }
.btn-cancelar { background: #ddd; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; }
.btn-imprimir { background: #28a745; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; }
.btn-imprimir:hover { background: #218838; }

/* TRUCO DE MAGIA: CSS PARA IMPRIMIR COMO PDF */
@media print {
  body * { visibility: hidden; }
  .modal-overlay { position: absolute; left: 0; top: 0; background: white; width: 100%; }
  .modal-papel { box-shadow: none; max-width: 100%; border: none; overflow: visible; }
  .area-impresion, .area-impresion * { visibility: visible; }
  .no-imprimir { display: none !important; }
}
</style>