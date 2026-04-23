<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

// Lógica de datos
const categoriaActiva = ref('Física')
const categorias = ['Física', 'Biogeoquímica', 'Geología', 'Laboratorio']

const instrumentos = ref([
  { id: 1, nombre: 'CTD SeaBird 911plus', tipo: 'Física', ultimaCalibracion: '2025-11-15', estado: 'Disponible' },
  { id: 2, nombre: 'ADCP Teledyne Workhorse', tipo: 'Física', ultimaCalibracion: '2026-01-20', estado: 'En Uso' },
  { id: 3, nombre: 'Sensor de Oxígeno SBE 43', tipo: 'Biogeoquímica', ultimaCalibracion: '2025-09-10', estado: 'Disponible' }
])

const instrumentosFiltrados = computed(() => {
  return instrumentos.value.filter(inst => inst.tipo === categoriaActiva.value)
})

const equipoSeleccionado = ref(null)
</script>

<template>
  <div class="servicios-hub">
    <div class="fondo-servicios"></div>

    <div class="contenido-hub">
      <div class="migas-pan" @click="$emit('volver')" style="cursor: pointer; color: #8cc63f; font-weight: bold; margin-bottom: 20px; display: inline-block;">
        &larr; Volver a Servicios
      </div>

      <h1 class="titulo-seccion">Instrumentación Oceanográfica</h1>
      <p class="subtitulo">Gestión de equipos, calibraciones y préstamos del SIO.</p>

      <div class="tabs-sio">
        <button v-for="cat in categorias" :key="cat" :class="['tab-btn', { activa: categoriaActiva === cat }]" @click="categoriaActiva = cat">
          {{ cat }}
        </button>
      </div>

      <div class="grid-tres-columnas">
        <div class="seccion-bloque" style="grid-column: span 2;">
          <h2 class="titulo-fija">Equipamiento: {{ categoriaActiva }}</h2>
          <table class="tabla-sio">
            <thead>
              <tr>
                <th>Equipo</th>
                <th>Calibración</th>
                <th>Estado</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="inst in instrumentosFiltrados" :key="inst.id">
                <td><strong>{{ inst.nombre }}</strong></td>
                <td>{{ inst.ultimaCalibracion }}</td>
                <td><span :class="['badge', inst.estado.toLowerCase().replace(' ', '-')]">{{ inst.estado }}</span></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="seccion-bloque">
          <h2 class="titulo-fija">Gestión</h2>
          <p style="font-size: 0.9rem; color: #666; margin-bottom: 15px;">Descargue el documento de responsabilidad para solicitar equipos.</p>
          <div class="doc-box">
            <span>📄 Formulario SIO</span>
            <a href="#" style="color: #0086c0; font-weight: bold; text-decoration: none;">Descargar</a>
          </div>
          <button class="btn-sio">📤 Subir Documento</button>

          <div class="calendario-mini" style="margin-top: 25px; border-top: 1px solid #eee; padding-top: 15px;">
             <h3 style="font-size: 1rem; color: #012169; margin-bottom: 10px;">Calendario Disponibilidad</h3>
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
/* COHERENCIA TOTAL CON SERVICIOS */
.servicios-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

.fondo-servicios { 
  position: absolute; top: 0; left: 0; width: 100%; height: 550px; 
  background-image: linear-gradient(rgba(1, 33, 105, 0.7), rgba(1, 33, 105, 0.9)), url('/instrumentacion.jpg');
  background-size: cover; background-position: center; z-index: 0; 
}

.contenido-hub { position: relative; z-index: 10; padding-top: 120px; max-width: 1200px; margin: 0 auto; padding-left: 20px; padding-right: 20px; }

.titulo-seccion { color: white; font-size: 2.2rem; font-weight: bold; position: relative; display: inline-block; padding-bottom: 8px; margin-bottom: 15px; }
.titulo-seccion::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 4px; background-color: #8cc63f; }

.subtitulo { color: #e0e6ed; font-size: 1.1rem; margin-bottom: 40px; }

.tabs-sio { display: flex; gap: 10px; margin-bottom: 25px; }
.tab-btn { padding: 10px 20px; background: rgba(255, 255, 255, 0.1); border: 1px solid white; color: white; border-radius: 8px; cursor: pointer; font-weight: bold; }
.tab-btn.activa { background: #8cc63f; border-color: #8cc63f; color: #012169; }

.grid-tres-columnas { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }

.seccion-bloque { background: white; border-radius: 12px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); min-height: auto; }

.titulo-fija { color: #012169; margin-top: 0; font-size: 1.5rem; margin-bottom: 20px; border-bottom: 2px solid #eee; padding-bottom: 10px; }

.tabla-sio { width: 100%; border-collapse: collapse; }
.tabla-sio th { text-align: left; padding: 10px; color: #666; border-bottom: 2px solid #eee; }
.tabla-sio td { padding: 15px 10px; border-bottom: 1px solid #f0f0f0; }

.badge { padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; }
.badge.disponible { background: #e6f4ea; color: #1e7e34; }
.badge.en-uso { background: #fff4e5; color: #b45d00; }

.doc-box { background: #f8f9fa; padding: 15px; border: 1px dashed #ccc; border-radius: 8px; display: flex; justify-content: space-between; margin-bottom: 15px; }

.btn-sio { width: 100%; background: #012169; color: white; border: none; padding: 12px; border-radius: 8px; font-weight: bold; cursor: pointer; }

.grid-dias { display: grid; grid-template-columns: repeat(7, 1fr); gap: 5px; }
.dia { background: #f0f0f0; padding: 8px; text-align: center; font-size: 0.8rem; border-radius: 4px; color: #999; }
.dia.ocupado { background: #0086c0; color: white; }

@media (max-width: 992px) { .grid-tres-columnas { grid-template-columns: 1fr; } .seccion-bloque { grid-column: span 1 !important; } }
</style>