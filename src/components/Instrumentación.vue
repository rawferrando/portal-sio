<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

// 1. LÓGICA DE CATEGORÍAS
const categoriaActiva = ref('Física')
const categorias = ['Física', 'Biogeoquímica', 'Geología', 'Laboratorio']

// 2. DATOS DE LOS INSTRUMENTOS (WikiSIO)
const instrumentos = ref([
  { 
    id: 1, 
    nombre: 'CTD SeaBird 911plus', 
    tipo: 'Física', 
    ultimaCalibracion: '2025-11-15', 
    estado: 'Disponible',
    descripcion: 'Medida de conductividad, temperatura y presión en perfiles.'
  },
  { 
    id: 2, 
    nombre: 'ADCP Teledyne Workhorse', 
    tipo: 'Física', 
    ultimaCalibracion: '2026-01-20', 
    estado: 'En Uso',
    descripcion: 'Perfilador de corrientes por efecto Doppler (300 kHz).'
  },
  { 
    id: 3, 
    nombre: 'Sensor de Oxígeno SBE 43', 
    tipo: 'Biogeoquímica', 
    ultimaCalibracion: '2025-09-10', 
    estado: 'Disponible',
    descripcion: 'Sensor de oxígeno disuelto para integración en rosetas.'
  }
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
  <div class="instrumentacion-hub">
    <div class="fondo-instrumentacion"></div>

    <div class="contenedor-ancho contenido-hub">
      
      <div class="migas-pan" @click="$emit('volver')" style="cursor: pointer; color: #8cc63f; font-weight: bold; margin-bottom: 20px; display: inline-block;">
        &larr; Volver a Servicios
      </div>

      <h1 class="titulo-seccion">Instrumentación Oceanográfica</h1>
      <p class="subtitulo">Gestión integral, calibración y préstamo de equipamiento científico del SIO.</p>

      <div class="tabs-categorias">
        <button 
          v-for="cat in categorias" 
          :key="cat" 
          :class="['tab-btn', { activa: categoriaActiva === cat }]"
          @click="categoriaActiva = cat"
        >
          {{ cat }}
        </button>
      </div>

      <div class="grid-principal">
        
        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Equipamiento: {{ categoriaActiva }}</h2>
          </div>
          <div class="tabla-scroll">
            <table class="tabla-sio">
              <thead>
                <tr>
                  <th>Equipo</th>
                  <th>Última Calibración</th>
                  <th>Estado</th>
                  <th>Acción</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="inst in instrumentosFiltrados" :key="inst.id">
                  <td class="info-principal">
                    <strong>{{ inst.nombre }}</strong>
                    <span class="mini-desc">{{ inst.descripcion }}</span>
                  </td>
                  <td>{{ inst.ultimaCalibracion }}</td>
                  <td>
                    <span :class="['status-badge', inst.estado.replace(' ', '-').toLowerCase()]">
                      {{ inst.estado }}
                    </span>
                  </td>
                  <td>
                    <button class="btn-check" @click="mostrarCalendario(inst)">📅 Disponibilidad</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="columna-derecha">
          
          <div class="seccion-bloque">
            <h2 class="titulo-fija">Préstamos</h2>
            <p class="txt-p">Es obligatorio el documento de responsabilidad firmado para solicitar equipos.</p>
            
            <div class="descarga-box">
              <span class="icon">📄</span>
              <div class="text">
                <strong>Responsabilidad_SIO.pdf</strong>
                <a href="#" class="link-download">Descargar formulario</a>
              </div>
            </div>

            <label class="btn-upload">
              📤 Subir documento firmado
              <input type="file" style="display: none;">
            </label>
          </div>

          <div v-if="equipoSeleccionado" class="seccion-bloque card-cal">
            <h3 class="titulo-mini">{{ equipoSeleccionado.nombre }}</h3>
            <div class="mini-grid">
              <div v-for="n in 28" :key="n" :class="['dia', { ocupado: n > 10 && n < 14 }]">
                {{ n }}
              </div>
            </div>
            <p class="legend">* Días en azul: equipo reservado.</p>
          </div>

        </div>

      </div> 
    </div>
  </div>
</template>

<style scoped>
.instrumentacion-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

/* 🖼️ FONDO IGUAL QUE SERVICIOS */
.fondo-instrumentacion { 
  position: absolute; 
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 550px; 
  background-image: linear-gradient(rgba(1, 33, 105, 0.75), rgba(1, 33, 105, 0.9)), 
                    url('/instrumentacion.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: 0; 
}

.contenido-hub { position: relative; z-index: 10; padding-top: 120px; }

.titulo-seccion { 
  color: white; 
  font-size: 2.2rem; 
  margin-bottom: 15px; 
  font-weight: bold; 
  position: relative;
  display: inline-block;
  padding-bottom: 8px;
}

.titulo-seccion::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background-color: #8cc63f; 
}

.subtitulo { color: #e0e6ed; font-size: 1.1rem; margin-bottom: 35px; max-width: 800px; }

/* TABS ESTILO PORTAL */
.tabs-categorias { display: flex; gap: 8px; margin-bottom: 25px; }
.tab-btn { 
  padding: 10px 18px; 
  background: rgba(255, 255, 255, 0.1); 
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white; 
  border-radius: 6px; 
  cursor: pointer; 
  font-weight: bold; 
  transition: 0.3s;
}
.tab-btn.activa { background: #8cc63f; color: #012169; border-color: #8cc63f; }

/* GRID PRINCIPAL */
.grid-principal { display: grid; grid-template-columns: 1.6fr 1fr; gap: 25px; }

.seccion-bloque { 
  background: white; 
  border-radius: 12px; 
  padding: 30px; 
  box-shadow: 0 10px 30px rgba(0,0,0,0.15); 
  display: flex;
  flex-direction: column; 
  min-height: auto;
}

.titulo-fija { color: #012169; margin-top: 0; font-size: 1.4rem; margin-bottom: 15px; border-bottom: 2px solid #f0f0f0; padding-bottom: 10px;}

/* TABLAS */
.tabla-scroll { overflow-x: auto; }
.tabla-sio { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.tabla-sio th { text-align: left; padding: 12px; color: #777; border-bottom: 2px solid #f5f5f5; }
.tabla-sio td { padding: 15px 12px; border-bottom: 1px solid #f9f9f9; }
.info-principal strong { display: block; color: #012169; font-size: 0.95rem; }
.mini-desc { font-size: 0.8rem; color: #999; }

/* BADGES DE ESTADO */
.status-badge { padding: 4px 10px; border-radius: 20px; font-size: 0.7rem; font-weight: bold; text-transform: uppercase; }
.status-badge.disponible { background: #e8f5e9; color: #2e7d32; }
.status-badge.en-uso { background: #fff3e0; color: #ef6c00; }

.btn-check { background: #f0f7ff; color: #0086c0; border: 1px solid #0086c0; padding: 6px 10px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; font-weight: bold; }

/* COLUMNA DERECHA */
.columna-derecha { display: flex; flex-direction: column; gap: 25px; }
.txt-p { font-size: 0.9rem; color: #666; line-height: 1.4; margin-bottom: 15px; }
.descarga-box { display: flex; gap: 12px; align-items: center; background: #f8f9fa; padding: 15px; border-radius: 8px; border: 1px dashed #ccc; margin-bottom: 15px;}
.link-download { display: block; font-size: 0.8rem; color: #0086c0; font-weight: bold; }
.btn-upload { display: block; text-align: center; padding: 12px; background: #012169; color: white; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.9rem; }

/* CALENDARIO */
.card-cal { border-top: 4px solid #8cc63f; }
.mini-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px; }
.dia { background: #f0f0f0; padding: 6px; text-align: center; font-size: 0.7rem; border-radius: 3px; color: #999; }
.dia.ocupado { background: #0086c0; color: white; font-weight: bold; }
.legend { font-size: 0.7rem; color: #999; margin-top: 10px; font-style: italic; }

@media (max-width: 1100px) { .grid-principal { grid-template-columns: 1fr; } }
</style>