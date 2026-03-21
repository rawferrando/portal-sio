<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

const textoBusqueda = ref('')
const tipoSeleccionado = ref('Todos')
const equiposExpandidos = ref([])

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

// INVENTARIO ESTÁTICO SEGURO
const inventario = ref([
  { 
    id: 'SNS-001', nombre: 'SBE 5 Pressure Sensor', tipo: 'Sensores de Presión', 
    desc: 'Sensor de presión de alta precisión para aplicaciones oceanográficas.',
    fabricante: 'Sea-Bird Scientific', numeroSerie: '11599',
    ultimaCalibracion: '05 de mayo de 2023', periodicidad: '12 a 24 meses',
    reservas: [],
    nuevaReserva: { desde: '', hasta: '', proyecto: '' },
    wiki: {
      descripcionGeneral: "Sensor de presión de alta precisión basado en la tecnología de galgas extensiométricas. Para entornos hostiles.",
      caracteristicasMedicion: ["Rango: 0 a 10.000 psia", "Precisión: ±0.015% FS", "Resolución: 0.001% FS"],
      caracteristicasFisicas: ["Material: Titanio", "Diámetro: 19 mm", "Peso: 0.17 kg"],
      especificacionesElectricas: ["Voltaje: 8-18 V DC", "Consumo: 15 mA"],
      principioFuncionamiento: "Utiliza un puente de Wheatstone con galgas unidas a un diafragma de titanio.",
      mantenimientoPreventivo: "Limpieza con agua dulce. Inspección del diafragma.",
      aplicaciones: "Perfiladores CTD, fondeos fijos."
    }
  },
  { 
    id: 'SNS-002', nombre: 'Salinómetro Guildline Portasal', tipo: 'Laboratorio', 
    desc: 'Análisis de salinidad en muestras de agua con altísima precisión.',
    fabricante: 'Guildline Instruments', numeroSerie: '67890',
    ultimaCalibracion: '12 de enero de 2024', periodicidad: '12 meses',
    reservas: [], 
    nuevaReserva: { desde: '', hasta: '', proyecto: '' }, 
    wiki: {
      descripcionGeneral: "Estándar de oro para la determinación de la salinidad en muestras de agua de mar en laboratorio.",
      caracteristicasMedicion: ["Rango: 0.005 a 42 PSU", "Precisión: ±0.003 PSU"],
      caracteristicasFisicas: ["Material: Maletín rígido", "Peso: 15 kg"],
      especificacionesElectricas: ["Voltaje: 110/220 V AC", "Salida: RS-232"],
      principioFuncionamiento: "Mide conductividad eléctrica y temperatura simultáneamente.",
      mantenimientoPreventivo: "Enjuague de celda. Calibración con Agua de Mar IAPSO.",
      aplicaciones: "Calibración in-situ, estudios masas de agua."
    }
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

const solicitarReserva = (equipo) => {
  if (!equipo.nuevaReserva.desde || !equipo.nuevaReserva.hasta || !equipo.nuevaReserva.proyecto) {
    alert("⚠️ Rellena las fechas y el proyecto de la campaña.")
    return
  }
  
  equipo.reservas.push({ desde: equipo.nuevaReserva.desde, hasta: equipo.nuevaReserva.hasta, proyecto: equipo.nuevaReserva.proyecto, estado: 'Pendiente', archivo: null })

  documentoActual.value = {
    equipoId: equipo.id, equipoNombre: equipo.nombre, equipoSn: equipo.numeroSerie,
    desde: equipo.nuevaReserva.desde, hasta: equipo.nuevaReserva.hasta, proyecto: equipo.nuevaReserva.proyecto,
    fechaGeneracion: new Date().toLocaleDateString('es-ES')
  }
  
  equipo.nuevaReserva = { desde: '', hasta: '', proyecto: '' }
  modalVisible.value = true
}

const descargarPDF = () => { window.print() }

const subirDocumento = (event, reserva) => {
  const archivo = event.target.files[0]
  if (archivo) {
    reserva.estado = 'Aprobada'
    reserva.archivo = archivo.name
    alert(`✅ Documento subido con éxito.`)
  }
}

const cerrarModal = () => { modalVisible.value = false }
</script>

<template>
  <div class="pagina-catalogo">
    
    <div class="cabecera-catalogo">
      <button @click="$emit('volver')" class="btn-volver">⬅ Volver al Inicio</button>
      <h2>Buscador de Instrumentación Científica</h2>
      <p>Explora el catálogo, bloquea fechas y genera el PDF de responsabilidad de custodia.</p>
    </div>

    <div class="caja-filtros">
      <div class="grupo-filtro">
        <label>🔍 Buscar por palabra clave o ID:</label>
        <input v-model="textoBusqueda" type="text" placeholder="Ej. SBE 5, presión..." />
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
            <span v-if="equipo.reservas.some(r => r.estado === 'Pendiente')" class="badge-pendiente-top">⏳ PDF Pendiente</span>
            <span v-else-if="equipo.reservas.length > 0" class="badge-ocupado">🗓️ Ocupado</span>
            <span v-else class="badge-libre">✅ Disponible</span>
          </div>
          
          <h4>{{ equipo.nombre }} <span class="id-equipo">({{ equipo.id }})</span></h4>
          <p class="descripcion">{{ equipo.desc }}</p>
          
          <button @click="toggleDetalles(equipo.id)" class="btn-desplegar">
            {{ equiposExpandidos.includes(equipo.id) ? '▲ Ocultar Ficha y Gestor' : '▼ Ver Ficha Técnica y Gestor de Cesión' }}
          </button>

          <div v-if="equiposExpandidos.includes(equipo.id)" class="ficha-tecnica-desplegada">
            
            <div class="bloque-reservas">
              <h5>📅 Calendario y Gestor de Documentación (PDF)</h5>
              
              <div v-if="equipo.reservas.length > 0" class="lista-reservas">
                <ul>
                  <li v-for="(res, index) in equipo.reservas" :key="index" class="item-reserva">
                    <div class="datos-reserva">
                      <strong>Del {{ res.desde }} al {{ res.hasta }}</strong> - {{ res.proyecto }}
                    </div>
                    <div class="acciones-reserva">
                      <span v-if="res.estado === 'Aprobada'" class="estado-ok">✅ {{ res.archivo }}</span>
                      <label v-if="res.estado === 'Pendiente'" class="btn-subir">
                        📤 Subir PDF Firmado
                        <input type="file" accept=".pdf" @change="subirDocumento($event, res)" style="display: none;" />
                      </label>
                    </div>
                  </li>
                </ul>
              </div>
              <div v-else class="lista-reservas libre"><p>El equipo está libre.</p></div>

              <div class="formulario-reserva">
                <h6>1. Nueva solicitud de cesión:</h6>
                <div class="inputs-reserva">
                  <div class="campo-etiquetado">
                    <label>📅 Fecha Inicio:</label><input type="date" v-model="equipo.nuevaReserva.desde" />
                  </div>
                  <div class="campo-etiquetado">
                    <label>📅 Fecha Fin:</label><input type="date" v-model="equipo.nuevaReserva.hasta" />
                  </div>
                  <div class="campo-etiquetado">
                    <label>🔬 Proyecto:</label><input type="text" v-model="equipo.nuevaReserva.proyecto" placeholder="Ej. Mareas" />
                  </div>
                </div>
                <button @click="solicitarReserva(equipo)" class="btn-generar-doc">Generar Documento PDF</button>
              </div>
            </div>

            <div class="bloque-wiki">
              <h5>📋 Ficha Técnica Wiki SIO</h5>
              <div class="wiki-grid">
                <div class="seccion-wiki full-width">
                  <h6>Identificación</h6>
                  <ul>
                    <li><strong>Fabricante:</strong> {{ equipo.fabricante }}</li>
                    <li><strong>S/N:</strong> {{ equipo.numeroSerie }}</li>
                    <li><strong>Última Calibración:</strong> {{ equipo.ultimaCalibracion }}</li>
                  </ul>
                </div>
                <div class="seccion-wiki full-width">
                  <h6>Descripción General</h6>
                  <p>{{ equipo.wiki.descripcionGeneral }}</p>
                </div>
                <div class="seccion-wiki">
                  <h6>Características de Medición</h6>
                  <ul><li v-for="(item, i) in equipo.wiki.caracteristicasMedicion" :key="'med'+i">{{ item }}</li></ul>
                </div>
                <div class="seccion-wiki">
                  <h6>Características Físicas</h6>
                  <ul><li v-for="(item, i) in equipo.wiki.caracteristicasFisicas" :key="'fis'+i">{{ item }}</li></ul>
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
              <strong>CLÁUSULA DE RESPONSABILIDAD:</strong> El abajo firmante asume la responsabilidad civil e institucional sobre el equipo descrito, comprometiéndose a garantizar su correcta operación y a cubrir los costes de reparación en caso de negligencia.
            </p>
            <div class="zona-firma">
              <p><strong>Fecha de expedición:</strong> {{ documentoActual.fechaGeneracion }}</p>
              <div class="caja-firma-vacia"><p>Firma del Responsable</p></div>
            </div>
          </div>
        </div>
        <div class="pie-papel no-imprimir">
          <div class="botones-modal">
            <button @click="cerrarModal" class="btn-cancelar">Cerrar</button>
            <button @click="descargarPDF" class="btn-imprimir">🖨️ Descargar PDF para Firma</button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
.pagina-catalogo { animation: fadeIn 0.4s ease; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
.cabecera-catalogo { margin-bottom: 30px; }
.cabecera-catalogo h2 { color: #005596; margin-bottom: 5px; font-size: 2rem; }
.btn-volver { background: #6c757d; color: white; border: none; padding: 10px 18px; border-radius: 4px; cursor: pointer; font-weight: bold; margin-bottom: 20px; }
.caja-filtros { background: #f8f9fa; padding: 25px; border-radius: 8px; border: 1px solid #ddd; display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 30px; }
.grupo-filtro { flex: 1; min-width: 250px; display: flex; flex-direction: column; gap: 8px; }
.grupo-filtro input, .grupo-filtro select { padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 1rem; }
.grid-equipos { display: flex; flex-direction: column; gap: 25px; }
.tarjeta-equipo { background: white; border: 1px solid #e0e0e0; border-radius: 8px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
.cabecera-tarjeta { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
.etiqueta-tipo { background: #e2eef7; color: #005596; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: bold; }
.id-equipo { font-size: 1.1rem; color: #888; font-family: monospace; }
.badge-libre { background: #d4edda; color: #155724; padding: 5px 12px; border-radius: 4px; font-weight: bold; font-size: 0.85rem; }
.badge-ocupado { background: #fff3cd; color: #856404; padding: 5px 12px; border-radius: 4px; font-weight: bold; font-size: 0.85rem; }
.badge-pendiente-top { background: #f8d7da; color: #721c24; padding: 5px 12px; border-radius: 4px; font-weight: bold; font-size: 0.85rem; }

.tarjeta-equipo h4 { margin: 0 0 10px 0; color: #333; font-size: 1.5rem; }
.descripcion { font-size: 1.05rem; color: #555; line-height: 1.5; margin-bottom: 20px; }
.btn-desplegar { background: #005596; color: white; border: none; padding: 12px 20px; border-radius: 4px; font-weight: bold; font-size: 1rem; cursor: pointer; transition: background 0.2s; }
.btn-desplegar:hover { background: #00447a; }
.ficha-tecnica-desplegada { background: #fdfdfd; border: 1px solid #eee; border-radius: 8px; margin-top: 20px; overflow: hidden; }

.bloque-reservas { background-color: #f0f7ff; padding: 25px; border-bottom: 1px solid #cce0f0; }
.bloque-reservas h5 { margin: 0 0 20px 0; color: #005596; font-size: 1.2rem; }
.lista-reservas { background: white; padding: 15px; border-radius: 6px; border: 1px solid #cce0f0; margin-bottom: 20px; }
.item-reserva { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; padding: 12px 0; font-size: 1rem; }
.estado-ok { background: #d4edda; color: #155724; padding: 5px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold; }
.btn-subir { background: #ffc107; color: #856404; border: 1px solid #ffeeba; padding: 8px 15px; border-radius: 4px; cursor: pointer; font-size: 0.9rem; font-weight: bold; display: inline-block; }

.inputs-reserva { display: flex; gap: 15px; flex-wrap: wrap; margin-bottom: 20px; }
.campo-etiquetado { display: flex; flex-direction: column; flex: 1; min-width: 150px; }
.campo-etiquetado label { font-size: 0.9rem; font-weight: bold; color: #005596; margin-bottom: 8px; }
.campo-etiquetado input { padding: 12px; border: 1px solid #ccc; border-radius: 4px; font-size: 1rem; }
.btn-generar-doc { background: #005596; color: white; border: none; padding: 15px; border-radius: 4px; font-weight: bold; font-size: 1.1rem; cursor: pointer; width: 100%; transition: background 0.2s; }
.btn-generar-doc:hover { background: #00447a; }

.bloque-wiki { padding: 25px; background-color: #fff; }
.bloque-wiki h5 { margin: 0 0 20px 0; color: #005596; font-size: 1.2rem; }
.wiki-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; }
.seccion-wiki h6 { margin: 0 0 10px 0; color: #005596; font-size: 1.05rem; border-bottom: 1px solid #eee; padding-bottom: 8px; }
.seccion-wiki p { font-size: 1rem; color: #444; line-height: 1.6; margin: 0; }
.seccion-wiki ul { padding-left: 20px; margin: 0; font-size: 1rem; color: #444; line-height: 1.6; }
.full-width { grid-column: 1 / -1; }

.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.8); display: flex; justify-content: center; align-items: center; z-index: 1000; padding: 20px; }
.modal-papel { background: white; width: 100%; max-width: 800px; border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); display: flex; flex-direction: column; max-height: 90vh; overflow-y: auto; }
.area-impresion { font-family: 'Times New Roman', serif; padding: 50px; }
.cabecera-papel { text-align: center; border-bottom: 2px solid #333; padding-bottom: 20px; margin-bottom: 30px; }
.cabecera-papel h3 { margin: 0 0 10px 0; font-size: 1.5rem; color: #000; letter-spacing: 1px; }
.cuerpo-papel { font-size: 1.1rem; line-height: 1.6; color: #000; }
.datos-papel { border: 1px solid #333; padding: 20px; margin: 25px 0; background: #fff; }
.zona-firma { border-top: 1px dashed #999; padding-top: 30px; margin-top: 40px; display: flex; flex-direction: column; gap: 30px; }
.caja-firma-vacia { width: 350px; height: 120px; border: 1px solid #ccc; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 10px; color: #666; }
.pie-papel { padding: 20px; border-top: 1px solid #eee; background: #f8f9fa; }
.botones-modal { display: flex; justify-content: flex-end; gap: 15px; }
.btn-cancelar { background: #ddd; border: none; padding: 12px 25px; border-radius: 4px; cursor: pointer; font-weight: bold; font-size: 1rem; }
.btn-imprimir { background: #28a745; color: white; border: none; padding: 12px 25px; border-radius: 4px; cursor: pointer; font-weight: bold; font-size: 1rem; }

@media print {
  body * { visibility: hidden; }
  .modal-overlay { position: absolute; left: 0; top: 0; background: white; width: 100%; padding: 0; }
  .modal-papel { box-shadow: none; max-width: 100%; border: none; overflow: visible; }
  .area-impresion, .area-impresion * { visibility: visible; }
  .no-imprimir { display: none !important; }
}
</style>