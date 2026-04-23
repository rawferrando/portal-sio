<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

// Lógica de Instrumentos
const categoriaActiva = ref('Física')
const categorias = ['Física', 'Biogeoquímica', 'Geología', 'Laboratorio']

const instrumentos = ref([
  { id: 1, nombre: 'CTD SeaBird 911plus', tipo: 'Física', ultimaCalibracion: '2025-11-15', estado: 'Disponible', descripcion: 'Medida de conductividad, temperatura y presión.' },
  { id: 2, nombre: 'ADCP Teledyne Workhorse', tipo: 'Física', ultimaCalibracion: '2026-01-20', estado: 'En Uso', descripcion: 'Perfilador de corrientes por efecto Doppler.' },
  { id: 3, nombre: 'Sensor de Oxígeno SBE 43', tipo: 'Biogeoquímica', ultimaCalibracion: '2025-09-10', estado: 'Disponible', descripcion: 'Sensor de oxígeno para rosetas.' }
])

const instrumentosFiltrados = computed(() => {
  return instrumentos.value.filter(inst => inst.tipo === categoriaActiva.value)
})

const equipoSeleccionado = ref(null)
const mostrarCalendario = (equipo) => {
  equipoSeleccionado.value = equipo
}
</script>

<template>
  <div class="servicios-hub">
    <div class="fondo-servicios"></div>

    <div class="contenedor-ancho contenido-hub">
      <div class="migas-pan" @click="$emit('volver')" style="cursor: pointer; color: #8cc63f; font-weight: bold; margin-bottom: 20px; display: inline-block;">
        &larr; Volver a Servicios
      </div>

      <h1 class="titulo-seccion">Instrumentación Oceanográfica</h1>
      <p class="subtitulo">Gestión integral, calibración y préstamo de equipamiento científico del SIO.</p>

      <div class="tabs-sio">
        <button v-for="cat in categorias" :key="cat" :class="['tab-btn', { activa: categoriaActiva === cat }]" @click="categoriaActiva = cat">
          {{ cat }}
        </button>
      </div>

      <div class="grid-principal">
        <div class="seccion-bloque">
          <h2 class="titulo-fija">Equipamiento: {{ categoriaActiva }}</h2>
          <div class="tabla-scroll">
            <table class="tabla-sio">
              <thead>
                <tr>
                  <th>Equipo</th>
                  <th>Calibración</th>
                  <th>Estado</th>
                  <th>Acción</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="inst in instrumentosFiltrados" :key="inst.id">
                  <td><strong>{{ inst.nombre }}</strong></td>
                  <td>{{ inst.ultimaCalibracion }}</td>
                  <td><span :class="['badge', inst.estado.toLowerCase()]">{{ inst.estado }}</span></td>
                  <td><button class="btn-mini" @click="mostrarCalendario(inst)">Ver</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="seccion-bloque">
          <h2 class="titulo-fija">Préstamos</h2>
          <p class="p-compacto">Descargue y suba el documento de responsabilidad firmado.</p>
          <div class="doc-box">
            <span>📄 Responsabilidad_SIO.pdf</span>
            <a href="#" class="link-sio">Descargar</a>
          </div>
          <button class="btn-sio">📤 Subir Documento</button>
          
          <div v-if="equipoSeleccionado" class="cal-mini">
            <h3 class="titulo-mini">{{ equipoSeleccionado.nombre }}</h3>
            <div class="grid-dias">
              <div v-for="n in 21" :key="n" :class="['dia', { ocupado: n > 12 && n < 16 }]">{{ n }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.servicios-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }
.fondo-servicios { 
  position: absolute; top: 0; left: 0; width: 100%; height: 550px; 
  background-image: linear-gradient(rgba(1, 33, 105, 0.75), rgba(1, 33, 105, 0.9)), url('/instrumentacion.jpg');
  background-size: cover; background-position: center; z-index: 0; 
}
.contenido-hub { position: relative; z-index: 10; padding-top: 120px; }
.titulo-seccion { color: white; font-size: 2.2rem; font-weight: bold; position: relative; display: inline-block; padding-bottom: 8px; margin-bottom: 15px; }
.titulo-seccion::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 4px; background-color: #8cc63f; }
.subtitulo { color: #e0e6ed; font-size: 1.1rem; margin-bottom: 30px; max-width: 800px; }

.tabs-sio { display: flex; gap: 10px; margin-bottom: 20px; }
.tab-btn { padding: 8px 15px; background: rgba(255,255,255,0.1); border: 1px solid white; color: white; border-radius: 5px; cursor: pointer; }
.tab-btn.activa { background: #8cc63f; border-color: #8cc63f; color: #012169; }

.grid-principal { display: grid; grid-template-columns: 1.5fr 1fr; gap: 25px; }
.seccion-bloque { background: white; border-radius: 12px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); }
.titulo-fija { color: #012169; margin-bottom: 15px; font-size: 1.4rem; border-bottom: 2px solid #eee; padding-bottom: 8px; }

.tabla-sio { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
.tabla-sio th { text-align: left; padding: 10px; border-bottom: 2px solid #f0f0f0; }
.tabla-sio td { padding: 12px 10px; border-bottom: 1px solid #f9f9f9; }

.badge { padding: 3px 8px; border-radius: 10px; font-weight: bold; font-size: 0.7rem; }
.badge.disponible { background: #e6f4ea; color: #1e7e34; }
.badge.en-uso { background: #fff4e5; color: #b45d00; }

.doc-box { background: #f8f9fa; padding: 10px; border: 1px dashed #ccc; margin: 15px 0; display: flex; justify-content: space-between; font-size: 0.8rem; }
.btn-sio { width: 100%; background: #012169; color: white; border: none; padding: 10px; border-radius: 5px; font-weight: bold; cursor: pointer; }
.btn-mini { background: #f0f7ff; color: #0086c0; border: 1px solid #0086c0; padding: 4px 8px; border-radius: 4px; cursor: pointer; }

.cal-mini { margin-top: 20px; padding-top: 15px; border-top: 1px solid #eee; }
.grid-dias { display: grid; grid-template-columns: repeat(7, 1fr); gap: 3px; }
.dia { background: #f0f0f0; padding: 5px; text-align: center; font-size: 0.7rem; border-radius: 2px; }
.dia.ocupado { background: #0086c0; color: white; }

@media (max-width: 992px) { .grid-principal { grid-template-columns: 1fr; } }
</style>