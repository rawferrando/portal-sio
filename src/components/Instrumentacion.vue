<script setup>
import { ref, computed, watch, onMounted } from 'vue'

const emit = defineEmits(['volver'])

defineProps({
  intranetModoEdicion: {
    type: Boolean,
    default: false
  }
})

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

const LLAVE_ALMACENAMIENTO = 'sio_inventario_persistencia_v4'

const DATOS_MOCK_INICIALES = [
  { 
    id: 'SNS-001', nombre: 'SBE 5 Pressure Sensor', tipo: 'Sensores de Presión', 
    desc: 'Sensor de presión de alta precisión para aplicaciones oceanográficas.',
    fabricante: 'Sea-Bird Scientific', numeroSerie: '11599',
    ultimaCalibracion: '05 de mayo de 2023', periodicidad: '12 a 24 meses',
    reservas: [], nuevaReserva: { desde: '', hasta: '', proyecto: '' },
    wiki: {
      descripcionGeneral: "Sensor de presión de alta precisión basado en la tecnología de galgas extensiométricas.",
      caracteristicasMedicion: ["Rango: 0 a 10.000 psia", "Precisión: ±0.015% FS", "Resolución: 0.001% FS", "Estabilidad: 0.0015% por mes"],
      caracteristicasFisicas: ["Material: Titanio", "Diámetro: 19 mm", "Longitud: 76 mm", "Peso: 0.17 kg"],
      especificacionesElectricas: ["Voltaje: 8-18 V DC", "Consumo: 15 mA", "Salida: Analógica 0-5 V DC", "Respuesta: 10 ms"],
      principioFuncionamiento: "Utiliza un puente de Wheatstone con galgas unidas a un diafragma de titanio.",
      mantenimientoPreventivo: "Limpieza con agua dulce. Inspección del diafragma. Verificación anual.",
      aplicaciones: "Perfiladores CTD, fondeos fijos, robótica submarina."
    }
  },
  { 
    id: 'SNS-002', nombre: 'Salinómetro Guildline Portasal', tipo: 'Equipos de Laboratorio', 
    desc: 'Análisis de salinidad en muestras de agua con altísima precisión.',
    fabricante: 'Guildline Instruments', numeroSerie: '67890',
    ultimaCalibracion: '12 de enero de 2024', periodicidad: '12 meses',
    reservas: [], nuevaReserva: { desde: '', hasta: '', proyecto: '' }, 
    wiki: {
      descripcionGeneral: "Estándar de oro para la determinación de la salinidad en muestras de agua de mar en laboratorio.",
      caracteristicasMedicion: ["Rango: 0.005 a 42 PSU", "Precisión: ±0.003 PSU", "Resolución: 0.0003 PSU", "Estabilidad: ±0.001 PSU por día"],
      caracteristicasFisicas: ["Material: Maletín rígido", "Dimensiones: 53x41x23 cm", "Celda: Vidrio borosilicato", "Peso: 15 kg"],
      especificacionesElectricas: ["Voltaje: 110/220 V AC", "Frecuencia: 50/60 Hz", "Salida: RS-232", "Pantalla: Digital LCD"],
      principioFuncionamiento: "Mide conductividad eléctrica y temperatura simultáneamente bajo el algoritmo PSS-78.",
      mantenimientoPreventivo: "Enjuague de celda. Calibración con Agua de Mar IAPSO.",
      aplicaciones: "Calibración in-situ, estudios masas de agua."
    }
  }
]

const inventario = ref(DATOS_MOCK_INICIALES)

onMounted(() => {
  const datosGuardados = localStorage.getItem(LLAVE_ALMACENAMIENTO)
  if (datosGuardados) {
    try {
      inventario.value = JSON.parse(datosGuardados)
    } catch (error) {
      inventario.value = DATOS_MOCK_INICIALES
    }
  }
})

watch(inventario, (nuevoEstado) => {
  localStorage.setItem(LLAVE_ALMACENAMIENTO, JSON.stringify(nuevoEstado))
}, { deep: true })

const guardarCambiosTecnicos = () => {
  localStorage.setItem(LLAVE_ALMACENAMIENTO, JSON.stringify(inventario.value))
  alert('💾 ✅ Cambios guardados en la base de datos SIO.')
}

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
    alert("⚠️ Rellena las fechas y el proyecto.")
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
    alert(`✅ Documento PDF subido con éxito.`)
  }
}
const cerrarModal = () => { modalVisible.value = false }
</script>

<template>
  <div class="pagina-catalogo">
    
    <div class="cabecera-catalogo">
      <button @click="$emit('volver')" class="btn-volver">⬅ Volver al Inicio</button>
      <h2>Buscador de Instrumentación</h2>
      <p v-if="!intranetModoEdicion">Explora el catálogo, bloquea fechas y gestiona PDF.</p>
      <p v-else class="texto-alerta-intranet">🔓 MODO INTRANET (Formularios Editables)</p>
    </div>

    <div class="caja-filtros">
      <div class="grupo-filtro">
        <label>🔍 Buscar por palabra clave:</label>
        <input v-model="textoBusqueda" type="text" placeholder="Ej. SBE 5..." />
      </div>
      <div class="grupo-filtro">
        <label>📂 Filtrar por categoría:</label>
        <select v-model="tipoSeleccionado">
          <option value="Todos">Todas las categorías</option>
          <option value="Sensores de Presión">Sensores de Presión</option>
          <option value="Equipos de Laboratorio">Equipos de Laboratorio</option>
        </select>
      </div>
    </div>

    <div class="resultados">
      <div class="grid-equipos">
        <div v-for="equipo in equiposFiltrados" :key="equipo.id" class="tarjeta-equipo">
          
          <div class="cabecera-tarjeta">
            <div class="etiqueta-tipo">{{ equipo.tipo }}</div>
            <span v-if="equipo.reservas.some(r => r.estado === 'Pendiente')" class="badge-pendiente-top">⏳ Pendiente PDF</span>
            <span v-else-if="equipo.reservas.length > 0" class="badge-ocupado">🗓️ Ocupado</span>
            <span v-else class="badge-libre">✅ Disponible</span>
          </div>
          
          <h4>{{ equipo.nombre }} <span class="id-equipo">({{ equipo.id }})</span></h4>
          <p class="descripcion">{{ equipo.desc }}</p>
          <button @click="toggleDetalles(equipo.id)" class="btn-desplegar">Ver Ficha Técnica y Gestor</button>

          <div v-if="equiposExpandidos.includes(equipo.id)" class="ficha-tecnica-desplegada">
            
            <div class="bloque-reservas">
              <h5>📅 Calendario y Gestor de PDF</h5>
              <div v-if="equipo.reservas.length > 0" class="lista-reservas">
                <ul>
                  <li v-for="(res, index) in equipo.reservas" :key="index" class="item-reserva">
                    <div class="datos-reserva">Del {{ res.desde }} al {{ res.hasta }} - {{ res.proyecto }}</div>
                    <div class="acciones-reserva">
                      <span v-if="res.estado === 'Aprobada'" class="estado-ok">✅ {{ res.archivo }}</span>
                      <label v-if="res.estado === 'Pendiente'" class="btn-subir">
                        📤 Subir PDF
                        <input type="file" accept=".pdf" @change="subirDocumento($event, res)" style="display: none;" />
                      </label>
                    </div>
                  </li>
                </ul>
              </div>

              <div class="formulario-reserva">
                <h6>1. Nueva solicitud de cesión:</h6>
                <div class="inputs-reserva">
                  <div class="campo-etiquetado"><label>Inicio:</label><input type="date" v-model="equipo.nuevaReserva.desde" /></div>
                  <div class="campo-etiquetado"><label>Fin:</label><input type="date" v-model="equipo.nuevaReserva.hasta" /></div>
                  <div class="campo-etiquetado"><label>Proyecto:</label><input type="text" v-model="equipo.nuevaReserva.proyecto" /></div>
                </div>
                <button @click="solicitarReserva(equipo)" class="btn-generar-doc">Generar PDF</button>
              </div>
            </div>

            <div class="bloque-wiki" :class="{ 'modo-edicion': intranetModoEdicion }">
              <div class="cabecera-wiki-edicion">
                <h5>📋 Ficha Técnica (Wiki SIO)</h5>
              </div>
              
              <div class="wiki-grid">
                <div class="seccion-wiki full-width">
                  <h6>Identificación</h6>
                  <div v-if="intranetModoEdicion" class="grid-inputs-cortos">
                    <label>Fabricante:</label><input v-model="equipo.fabricante" />
                    <label>Nº Serie:</label><input v-model="equipo.numeroSerie" />
                    <label>Última Calibración:</label><input v-model="equipo.ultimaCalibracion" />
                    <label>Periodicidad:</label><input v-model="equipo.periodicidad" />
                  </div>
                  <ul v-else>
                    <li>Fabricante: {{ equipo.fabricante }}</li><li>S/N: {{ equipo.numeroSerie }}</li><li>Última Calib: {{ equipo.ultimaCalibracion }}</li>
                  </ul>
                </div>

                <div class="seccion-wiki full-width">
                  <h6>Descripción</h6>
                  <textarea v-if="intranetModoEdicion" v-model="equipo.wiki.descripcionGeneral" rows="2"></textarea>
                  <p v-else>{{ equipo.wiki.descripcionGeneral }}</p>
                </div>

                <div class="seccion-wiki">
                  <h6>Características de Medición</h6>
                  <div v-if="intranetModoEdicion">
                    <input v-for="(item, i) in equipo.wiki.caracteristicasMedicion" :key="'med'+i" v-model="equipo.wiki.caracteristicasMedicion[i]" class="input-lista" />
                  </div>
                  <ul v-else><li v-for="(item, i) in equipo.wiki.caracteristicasMedicion" :key="'med'+i">{{ item }}</li></ul>
                </div>

                <div class="seccion-wiki">
                  <h6>Características Físicas</h6>
                  <div v-if="intranetModoEdicion">
                    <input v-for="(item, i) in equipo.wiki.caracteristicasFisicas" :key="'fis'+i" v-model="equipo.wiki.caracteristicasFisicas[i]" class="input-lista" />
                  </div>
                  <ul v-else><li v-for="(item, i) in equipo.wiki.caracteristicasFisicas" :key="'fis'+i">{{ item }}</li></ul>
                </div>

                <div class="seccion-wiki">
                  <h6>Mantenimiento Preventivo</h6>
                  <textarea v-if="intranetModoEdicion" v-model="equipo.wiki.mantenimientoPreventivo" rows="2"></textarea>
                  <p v-else>{{ equipo.wiki.mantenimientoPreventivo }}</p>
                </div>

                <div v-if="intranetModoEdicion" class="seccion-wiki full-width zona-guardar-edicion">
                  <button @click="guardarCambiosTecnicos" class="btn-guardar-edicion">💾 Guardar Cambios (Wiki SIO)</button>
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
          </div>
          <div class="cuerpo-papel">
            <div class="datos-papel">
              <p>Instrumento: {{ documentoActual.equipoNombre }} (ID: {{ documentoActual.equipoId }})</p>
              <p>Periodo: {{ documentoActual.desde }} al {{ documentoActual.hasta }}</p>
            </div>
            <div class="zona-firma"><div class="caja-firma-vacia"><p>Firma del Responsable</p></div></div>
          </div>
        </div>
        <div class="pie-papel no-imprimir">
          <div class="botones-modal">
            <button @click="cerrarModal" class="btn-cancelar">Cerrar</button>
            <button @click="descargarPDF" class="btn-imprimir">🖨️ Descargar PDF</button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
.pagina-catalogo { animation: fadeIn 0.4s ease; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
.cabecera-catalogo { margin-bottom: 20px; }
.texto-alerta-intranet { color: #d32f2f; font-weight: bold; background: #ffebee; padding: 10px; border-radius: 4px; display: inline-block; }
.btn-volver { background: #6c757d; color: white; border: none; padding: 8px 15px; border-radius: 4px; cursor: pointer; font-weight: bold; margin-bottom: 20px; }
.caja-filtros { background: #f8f9fa; padding: 20px; border-radius: 8px; display: flex; gap: 20px; margin-bottom: 30px; }
.grupo-filtro { flex: 1; display: flex; flex-direction: column; gap: 8px; }
.grupo-filtro input, .grupo-filtro select { padding: 10px; border: 1px solid #ccc; border-radius: 6px; }
.grid-equipos { display: flex; flex-direction: column; gap: 20px; }
.tarjeta-equipo { background: white; border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; }
.cabecera-tarjeta { display: flex; justify-content: space-between; margin-bottom: 10px; }
.etiqueta-tipo { background: #e2eef7; color: #005596; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; }
.btn-desplegar { background: #005596; color: white; border: none; padding: 10px 15px; border-radius: 4px; cursor: pointer; }
.ficha-tecnica-desplegada { margin-top: 15px; }

.bloque-reservas { background-color: #f0f7ff; padding: 20px; margin-bottom: 15px; border-radius: 6px; }
.lista-reservas { background: white; padding: 10px; margin-bottom: 10px; }
.item-reserva { display: flex; justify-content: space-between; border-bottom: 1px solid #eee; padding: 8px 0; }
.btn-subir { background: #ffc107; padding: 5px 10px; border-radius: 4px; cursor: pointer; font-size: 0.85rem; font-weight: bold; }
.inputs-reserva { display: flex; gap: 10px; margin-bottom: 15px; }
.campo-etiquetado input { padding: 8px; border: 1px solid #ccc; width: 100%; box-sizing: border-box; }
.btn-generar-doc { background: #005596; color: white; border: none; padding: 10px; border-radius: 4px; cursor: pointer; }

.bloque-wiki { padding: 20px; border: 1px solid #eee; }
.bloque-wiki.modo-edicion { border: 2px dashed #005596; background: #f8fbff; }
.wiki-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
.seccion-wiki input, .seccion-wiki textarea { width: 100%; padding: 8px; border: 1px solid #ddd; box-sizing: border-box; margin-bottom: 5px; }
.full-width { grid-column: 1 / -1; }
.grid-inputs-cortos { display: grid; grid-template-columns: auto 1fr; gap: 5px; align-items: center; }
.btn-guardar-edicion { background-color: #28a745; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; }

.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.7); display: flex; justify-content: center; align-items: center; z-index: 1000; padding: 20px; }
.modal-papel { background: white; width: 100%; max-width: 600px; padding: 30px; border-radius: 4px; max-height: 90vh; overflow-y: auto; }
.caja-firma-vacia { width: 250px; height: 80px; border: 1px solid #ccc; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 10px; }
.botones-modal { display: flex; justify-content: flex-end; gap: 10px; margin-top: 20px; }
.btn-cancelar { background: #ddd; border: none; padding: 10px; border-radius: 4px; cursor: pointer; }
.btn-imprimir { background: #28a745; color: white; border: none; padding: 10px; border-radius: 4px; cursor: pointer; }

@media print {
  body * { visibility: hidden; }
  .modal-overlay { position: absolute; left: 0; top: 0; background: white; width: 100%; }
  .modal-papel { box-shadow: none; border: none; }
  .area-impresion, .area-impresion * { visibility: visible; }
  .no-imprimir { display: none !important; }
}
</style>