<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

// 1. CATEGORÍAS
const categoriaActiva = ref('Física')
const categorias = ['Física', 'Biogeoquímica', 'Geología', 'Laboratorio']

// 2. DATOS (WikiSIO)
const instrumentos = ref([
  { id: 1, nombre: 'CTD SeaBird 911plus', tipo: 'Física', ultimaCalibracion: '2025-11-15', estado: 'Disponible' },
  { id: 2, nombre: 'ADCP Teledyne Workhorse', tipo: 'Física', ultimaCalibracion: '2026-01-20', estado: 'En Uso' },
  { id: 3, nombre: 'Sensor de Oxígeno SBE 43', tipo: 'Biogeoquímica', ultimaCalibracion: '2025-09-10', estado: 'Disponible' },
  { id: 4, nombre: 'Fluorímetro WetLabs ECO-AFL', tipo: 'Biogeoquímica', ultimaCalibracion: '2025-12-05', estado: 'Mantenimiento' }
])

const instrumentosFiltrados = computed(() => {
  return instrumentos.value.filter(inst => inst.tipo === categoriaActiva.value)
})
</script>

<template>
  <div class="servicios-hub">
    <!-- FONDO UNIFICADO -->
    <div class="fondo-servicios"></div>

    <div class="contenido-hub">
      <!-- BOTÓN VOLVER -->
      <div class="migas-pan" @click="$emit('volver')" style="cursor: pointer; color: #8cc63f; font-weight: bold; margin-bottom: 20px; display: inline-block;">
        &larr; Volver a Servicios
      </div>

      <h1 class="titulo-seccion">Instrumentación Oceanográfica</h1>
      <p class="subtitulo">Gestión integral de equipamiento científico, calibraciones y préstamos del SIO.</p>

      <!-- PESTAÑAS (Estilo I+D+i) -->
      <div class="tabs-sio">
        <button 
          v-for="cat in categorias" 
          :key="cat" 
          :class="['tab-btn', { activa: categoriaActiva === cat }]" 
          @click="categoriaActiva = cat"
        >
          {{ cat }}
        </button>
      </div>

      <div class="grid-layout">
        <!-- FICHA IZQUIERDA: EQUIPOS -->
        <div class="seccion-bloque ficha-tabla">
          <h2 class="titulo-fija">Equipamiento: {{ categoriaActiva }}</h2>
          <div class="tabla-scroll">
            <table class="tabla-sio">
              <thead>
                <tr>
                  <th>Instrumento</th>
                  <th>Calibración</th>
                  <th>Estado</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="inst in instrumentosFiltrados" :key="inst.id">
                  <td><strong>{{ inst.nombre }}</strong></td>
                  <td>{{ inst.ultimaCalibracion }}</td>
                  <td>
                    <span :class="['badge', inst.estado.toLowerCase().replace(' ', '-')]">
                      {{ inst.estado }}
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- FICHA DERECHA: GESTIÓN -->
        <div class="seccion-bloque ficha-gestion">
          <h2 class="titulo-fija">Gestión de Préstamos</h2>
          <p class="txt-p">Descargue el formulario de responsabilidad y súbalo firmado para solicitar material.</p>
          
          <div class="descarga-box">
            <span>📄 Compromiso_Responsabilidad.pdf</span>
            <a href="#" class="link-dl">Descargar</a>
          </div>

          <label class="btn-upload">
            📤 Subir Documento Firmado
            <input type="file" style="display: none;">
          </label>

          <div class="calendario-mini">
            <h3 class="titulo-mini">Disponibilidad General</h3>
            <div class="grid-dias">
              <div v-for="n in 21" :key="n" :class="['dia', { ocupado: n > 12 && n < 17 }]">{{ n }}</div>
            </div>
            <p class="leyenda">* Días en azul: Reservas confirmadas.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* REUTILIZAMOS LAS CLASES DE SERVICIOS PARA COHERENCIA TOTAL */
.servicios-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

.fondo-servicios { 
  position: absolute; top: 0; left: 0; width: 100%; height: 550px; 
  background-image: linear-gradient(rgba(1, 33, 105, 0.75), rgba(1, 33, 105, 0.9)), url('/instrumentacion.jpg');
  background-size: cover; background-position: center; z-index: 0; 
}

.contenido-hub { position: relative; z-index: 10; padding-top: 120px; max-width: 1250px; margin: 0 auto; padding-left: 20px; padding-right: 20px; }

.titulo-seccion { color: white; font-size: 2.2rem; font-weight: bold; position: relative; display: inline-block; padding-bottom: 8px; margin-bottom: 15px; }
.titulo-seccion::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 4px; background-color: #8cc63f; }
.subtitulo { color: #e0e6ed; font-size: 1.1rem; margin-bottom: 35px; max-width: 800px; }

/* TABS */
.tabs-sio { display: flex; gap: 10px; margin-bottom: 25px; }
.tab-btn { padding: 10px 20px; background: rgba(255, 255, 255, 0.1); border: 1px solid white; color: white; border-radius: 8px; cursor: pointer; font-weight: bold; transition: 0.3s; }
.tab-btn.activa { background: #8cc63f; border-color: #8cc63f; color: #012169; }

/* GRID */
.grid-layout { display: grid; grid-template-columns: 1.6fr 1fr; gap: 30px; }
.seccion-bloque { background: white; border-radius: 12px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); min-height: auto; }
.titulo-fija { color: #012169; margin-top: 0; font-size: 1.4rem; margin-bottom: 20px; border-bottom: 2px solid #eee; padding-bottom: 10px; }

/* TABLA */
.tabla-sio { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.tabla-sio th { text-align: left; padding: 12px; color: #666; border-bottom: 2px solid #f0f0f0; }
.tabla-sio td { padding: 15px 12px; border-bottom: 1px solid #f9f9f9; }

.badge { padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; }
.badge.disponible { background: #e6f4ea; color: #1e7e34; }
.badge.en-uso { background: #fff4e5; color: #b45d00; }
.badge.mantenimiento { background: #fdeaea; color: #c53030; }

/* GESTIÓN */
.txt-p { font-size: 0.9rem; color: #666; line-height: 1.4; margin-bottom: 20px; }
.descarga-box { background: #f8f9fa; padding: 15px; border: 1px dashed #ccc; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.link-dl { color: #0086c0; font-weight: bold; text-decoration: none; font-size: 0.85rem; }
.btn-upload { display: block; text-align: center; padding: 12px; background: #012169; color: white; border-radius: 8px; cursor: pointer; font-weight: bold; }

/* CALENDARIO */
.calendario-mini { margin-top: 30px; border-top: 2px solid #f9f9f9; padding-top: 20px; }
.titulo-mini { font-size: 1rem; color: #012169; margin-bottom: 15px; }
.grid-dias { display: grid; grid-template-columns: repeat(7, 1fr); gap: 5px; }
.dia { background: #f0f0f0; padding: 8px; text-align: center; font-size: 0.75rem; border-radius: 4px; color: #999; }
.dia.ocupado { background: #0086c0; color: white; font-weight: bold; }
.leyenda { font-size: 0.7rem; color: #999; margin-top: 10px; font-style: italic; }

@media (max-width: 992px) { .grid-layout { grid-template-columns: 1fr; } }
</style>