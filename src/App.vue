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
  if (index > -1) equiposExpandidos.value.splice(index, 1)
  else equiposExpandidos.value.push(id)
}

const inventario = ref([
  { 
    id: 'SNS-001', nombre: 'SBE 5 Pressure Sensor', tipo: 'Sensores de Presión', 
    desc: 'Sensor de presión de alta precisión para aplicaciones oceanográficas.',
    fabricante: 'Sea-Bird Scientific', numeroSerie: '11599',
    ultimaCalibracion: '05 de mayo de 2023', periodicidad: '12 a 24 meses',
    reservas: [], nuevaReserva: { desde: '', hasta: '', proyecto: '' },
    wiki: {
      descripcionGeneral: "Sensor de presión de alta precisión basado en la tecnología de galgas extensiométricas.",
      caracteristicasMedicion: ["Rango: 0 a 10.000 psia", "Precisión: ±0.015% FS"],
      caracteristicasFisicas: ["Material: Titanio", "Diámetro: 19 mm", "Peso: 0.17 kg"],
      especificacionesElectricas: ["Voltaje: 8-18 V DC", "Consumo: 15 mA"],
      principioFuncionamiento: "Utiliza un puente de Wheatstone con galgas unidas a un diafragma de titanio."
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
  if (!equipo.nuevaReserva.desde || !equipo.nuevaReserva.hasta || !equipo.nuevaReserva.proyecto) return alert("⚠️ Faltan datos.")
  
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
</script>

<template>
  <div class="pagina-catalogo">
    
    <div class="cabecera-catalogo">
      <button @click="$emit('volver')" class="btn-volver">⬅ Volver al Inicio</button>
      <h2>Buscador de Instrumentación Científica</h2>
    </div>

    <div class="caja-filtros">
      <input v-model="textoBusqueda" type="text" placeholder="Buscar por palabra clave..." class="input-filtro" />
      <select v-model="tipoSeleccionado" class="input-filtro">
        <option value="Todos">Todas las categorías</option>
        <option value="Sensores de Presión">Sensores de Presión</option>
      </select>
    </div>

    <div class="resultados">
      <div class="grid-equipos">
        <div v-for="equipo in equiposFiltrados" :key="equipo.id" class="tarjeta-equipo">
          
          <div class="cabecera-tarjeta">
            <span class="etiqueta-tipo">{{ equipo.tipo }}</span>
            <span v-if="equipo.reservas.some(r => r.estado === 'Pendiente')" class="badge-pendiente-top">⏳ PDF Pendiente</span>
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
                  <li v-for="(res, index) in equipo.reservas" :key="index">
                    Del {{ res.desde }} al {{ res.hasta }} - {{ res.proyecto }}
                  </li>
                </ul>
              </div>
              <div class="formulario-reserva">
                <input type="date" v-model="equipo.nuevaReserva.desde" />
                <input type="date" v-model="equipo.nuevaReserva.hasta" />
                <input type="text" v-model="equipo.nuevaReserva.proyecto" placeholder="Proyecto" />
                <button @click="solicitarReserva(equipo)" class="btn-generar">Generar PDF</button>
              </div>
            </div>

            <div class="bloque-wiki">
              <h5>📋 Ficha Técnica Wiki SIO</h5>
              <ul>
                <li>Fabricante: {{ equipo.fabricante }}</li>
                <li>S/N: {{ equipo.numeroSerie }}</li>
              </ul>
              <p>{{ equipo.wiki.descripcionGeneral }}</p>
            </div>

          </div>
        </div>
      </div>
    </div>

    <div v-if="modalVisible" class="modal-overlay">
      <div class="modal-papel">
        <div class="area-impresion">
          <h3>🏛️ DOCUMENTO DE RESPONSABILIDAD</h3>
          <p>Instrumento: {{ documentoActual.equipoNombre }} (ID: {{ documentoActual.equipoId }})</p>
          <p>Periodo: {{ documentoActual.desde }} al {{ documentoActual.hasta }}</p>
          <div class="zona-firma"><p>Firma del Responsable</p></div>
        </div>
        <div class="pie-papel no-imprimir">
          <button @click="cerrarModal" class="btn-cancelar">Cerrar</button>
          <button @click="descargarPDF" class="btn-imprimir">🖨️ Descargar PDF</button>
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
.pagina-catalogo { animation: fadeIn 0.4s ease; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
.cabecera-catalogo { margin-bottom: 30px; }
.btn-volver { background: #6c757d; color: white; border: none; padding: 10px 15px; border-radius: 4px; cursor: pointer; margin-bottom: 20px; }
.caja-filtros { display: flex; gap: 15px; margin-bottom: 30px; }
.input-filtro { padding: 10px; border: 1px solid #ccc; border-radius: 4px; flex: 1; }
.tarjeta-equipo { background: white; border: 1px solid #ddd; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
.cabecera-tarjeta { display: flex; justify-content: space-between; margin-bottom: 10px; }
.etiqueta-tipo { background: #e2eef7; color: #005596; padding: 5px 10px; border-radius: 15px; font-size: 0.85rem; font-weight: bold; }
.badge-libre { background: #d4edda; color: #155724; padding: 5px 10px; border-radius: 4px; font-size: 0.85rem; }
.btn-desplegar { background: #005596; color: white; border: none; padding: 10px 15px; border-radius: 4px; cursor: pointer; }
.ficha-tecnica-desplegada { margin-top: 20px; }
.bloque-reservas { background: #f0f7ff; padding: 15px; margin-bottom: 15px; border-radius: 4px; }
.formulario-reserva { display: flex; gap: 10px; margin-top: 10px; }
.btn-generar { background: #005596; color: white; border: none; padding: 10px; border-radius: 4px; cursor: pointer; }
.bloque-wiki { background: #fff; padding: 15px; border: 1px solid #eee; border-radius: 4px; }

.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.8); display: flex; justify-content: center; align-items: center; z-index: 1000; padding: 20px; }
.modal-papel { background: white; width: 100%; max-width: 600px; padding: 40px; border-radius: 4px; }
.zona-firma { margin-top: 50px; border-top: 1px dashed #ccc; padding-top: 20px; }
.botones-modal { display: flex; justify-content: flex-end; gap: 10px; margin-top: 30px; }
.btn-cancelar { background: #ddd; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; }
.btn-imprimir { background: #28a745; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; }
@media print { body * { visibility: hidden; } .modal-overlay { position: absolute; left:0; top:0; background: white; } .modal-papel { box-shadow: none; border: none; } .area-impresion, .area-impresion * { visibility: visible; } .no-imprimir { display: none; } }
</style>