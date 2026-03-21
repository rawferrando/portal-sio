<script setup>
import { ref, computed, watch, onMounted } from 'vue'

const emit = defineEmits(['volver'])

const props = defineProps({
  intranetModoEdicion: {
    type: Boolean,
    default: false
  }
})

const tipoSeleccionado = ref('Todos')
const modalVisible = ref(false)
const documentoActual = ref({
  equipoId: '', equipoNombre: '', equipoSn: '',
  desde: '', hasta: '', proyecto: '', fechaGeneracion: ''
})

const LLAVE_ALMACENAMIENTO = 'sio_datos_v5'

const DATOS_INICIALES = [
  { 
    id: 'SNS-001', nombre: 'SBE 5 Pressure Sensor', tipo: 'Sensores de Presión', fabricante: 'Sea-Bird', numeroSerie: '11599',
    ultimaCalibracion: '05/2023', periodicidad: '12 meses', reservas: [], nuevaReserva: { desde: '', hasta: '', proyecto: '' },
    wiki: {
      descripcionGeneral: "Sensor de presión de alta precisión.",
      caracteristicasMedicion: ["Rango: 0 a 10.000 psia", "Precisión: ±0.015% FS"],
      caracteristicasFisicas: ["Material: Titanio", "Peso: 0.17 kg"],
      especificacionesElectricas: ["Voltaje: 8-18 V DC"],
      principioFuncionamiento: "Puente de Wheatstone con galgas.",
      mantenimientoPreventivo: "Limpieza con agua dulce.",
      aplicaciones: "Perfiladores CTD."
    }
  },
  { 
    id: 'SNS-002', nombre: 'Salinómetro Portasal', tipo: 'Laboratorio', fabricante: 'Guildline', numeroSerie: '67890',
    ultimaCalibracion: '01/2024', periodicidad: '12 meses', reservas: [], nuevaReserva: { desde: '', hasta: '', proyecto: '' },
    wiki: {
      descripcionGeneral: "Estándar de oro para salinidad.",
      caracteristicasMedicion: ["Rango: 0.005 a 42 PSU"],
      caracteristicasFisicas: ["Material: Maletín rígido"],
      especificacionesElectricas: ["Voltaje: 110/220 V AC"],
      principioFuncionamiento: "Mide conductividad eléctrica.",
      mantenimientoPreventivo: "Enjuague de celda.",
      aplicaciones: "Calibración in-situ."
    }
  }
]

const inventario = ref(DATOS_INICIALES)

onMounted(() => {
  const datos = localStorage.getItem(LLAVE_ALMACENAMIENTO)
  if (datos) {
    try { inventario.value = JSON.parse(datos) } catch (e) { inventario.value = DATOS_INICIALES }
  }
})

watch(inventario, (nuevoValor) => {
  localStorage.setItem(LLAVE_ALMACENAMIENTO, JSON.stringify(nuevoValor))
}, { deep: true })

const guardarCambios = () => {
  localStorage.setItem(LLAVE_ALMACENAMIENTO, JSON.stringify(inventario.value))
  alert('💾 Datos actualizados correctamente en la Intranet.')
}

const equiposFiltrados = computed(() => {
  if (tipoSeleccionado.value === 'Todos') return inventario.value
  return inventario.value.filter(eq => eq.tipo === tipoSeleccionado.value)
})

const solicitarReserva = (equipo) => {
  if (!equipo.nuevaReserva.desde || !equipo.nuevaReserva.hasta || !equipo.nuevaReserva.proyecto) return alert("Faltan datos")
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
const cerrarModal = () => { modalVisible.value = false }
const subirDoc = (e, r) => { if(e.target.files[0]) { r.estado = 'Aprobada'; r.archivo = e.target.files[0].name; alert("Documento subido") } }
</script>

<template>
  <div class="pagina">
    <div class="cabecera">
      <button @click="$emit('volver')" class="btn-volver">⬅ Volver</button>
      <h2>Gestión de Instrumentación</h2>
      <p v-if="props.intranetModoEdicion" class="alerta-intranet">🔓 MODO EDICIÓN ACTIVO</p>
    </div>

    <div class="filtros">
      <label>Filtrar:</label>
      <select v-model="tipoSeleccionado">
        <option value="Todos">Todos</option>
        <option value="Sensores de Presión">Sensores de Presión</option>
        <option value="Laboratorio">Laboratorio</option>
      </select>
    </div>

    <div class="grid-equipos">
      <div v-for="equipo in equiposFiltrados" :key="equipo.id" class="tarjeta-equipo">
        
        <div class="cabecera-tarjeta">
          <span class="tipo">{{ equipo.tipo }}</span>
        </div>
        <h4>{{ equipo.nombre }} ({{ equipo.id }})</h4>

        <div v-if="!props.intranetModoEdicion" class="modo-lectura">
          <p>{{ equipo.wiki.descripcionGeneral }}</p>
          <ul>
            <li>Fabricante: {{ equipo.fabricante }}</li>
            <li>S/N: {{ equipo.numeroSerie }}</li>
            <li v-for="(med, i) in equipo.wiki.caracteristicasMedicion" :key="i">{{ med }}</li>
          </ul>

          <div class="caja-reservas">
            <h5>Reservas:</h5>
            <ul><li v-for="(r, i) in equipo.reservas" :key="i">{{ r.desde }} al {{ r.hasta }} - {{ r.estado }}</li></ul>
            <input type="date" v-model="equipo.nuevaReserva.desde" />
            <input type="date" v-model="equipo.nuevaReserva.hasta" />
            <input type="text" v-model="equipo.nuevaReserva.proyecto" placeholder="Proyecto" />
            <button @click="solicitarReserva(equipo)">Generar PDF</button>
            <input type="file" @change="(e) => subirDoc(e, equipo.reservas[equipo.reservas.length-1])" />
          </div>
        </div>

        <div v-else class="modo-edicion">
          <div class="caja-edicion">
            <label>Nombre:</label><input v-model="equipo.nombre" />
            <label>Fabricante:</label><input v-model="equipo.fabricante" />
            <label>Descripción:</label><textarea v-model="equipo.wiki.descripcionGeneral"></textarea>
            <label>Mantenimiento:</label><textarea v-model="equipo.wiki.mantenimientoPreventivo"></textarea>
            <button @click="guardarCambios" class="btn-guardar">💾 Guardar Cambios</button>
          </div>
        </div>

      </div>
    </div>

    <div v-if="modalVisible" class="modal-overlay">
      <div class="modal-papel">
        <div class="area-impresion">
          <h3>DOCUMENTO DE RESPONSABILIDAD</h3>
          <p>Equipo: {{ documentoActual.equipoNombre }}</p>
          <p>Fechas: {{ documentoActual.desde }} al {{ documentoActual.hasta }}</p>
          <div class="firma"><p>Firma:</p></div>
        </div>
        <div class="no-imprimir">
          <button @click="cerrarModal">Cerrar</button>
          <button @click="descargarPDF">Imprimir</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pagina { padding: 20px; }
.alerta-intranet { color: red; font-weight: bold; }
.btn-volver { margin-bottom: 20px; }
.filtros { margin-bottom: 20px; }
.grid-equipos { display: flex; flex-direction: column; gap: 20px; }
.tarjeta-equipo { border: 1px solid #ccc; padding: 20px; border-radius: 8px; background: #fff; }
.caja-reservas { margin-top: 20px; padding: 10px; background: #f0f8ff; border-radius: 4px; }
.modo-edicion { margin-top: 20px; border: 2px dashed #005596; padding: 15px; }
.caja-edicion { display: flex; flex-direction: column; gap: 10px; }
.caja-edicion input, .caja-edicion textarea { padding: 8px; border: 1px solid #ccc; }
.btn-guardar { background: #28a745; color: white; padding: 10px; border: none; cursor: pointer; }
.modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); display: flex; justify-content: center; align-items: center; }
.modal-papel { background: white; padding: 30px; width: 500px; }
.firma { margin-top: 40px; border-top: 1px solid #000; padding-top: 10px; }
@media print { body * { visibility: hidden; } .modal-overlay { position: absolute; left: 0; top: 0; } .area-impresion, .area-impresion * { visibility: visible; } .no-imprimir { display: none; } }
</style>