<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

// CATEGORÍAS (Igual que en las otras secciones)
const categoriaActiva = ref('Física')
const categorias = ['Física', 'Biogeoquímica', 'Geología', 'Laboratorio']

// DATOS WIKISIO
const instrumentos = ref([
  { 
    id: 1, 
    nombre: 'CTD SeaBird 911plus', 
    tipo: 'Física', 
    ultimaCalibracion: '2025-11-15', 
    estado: 'Disponible',
    descripcion: 'Medida de conductividad, temperatura y presión.',
  },
  { 
    id: 2, 
    nombre: 'ADCP Teledyne Workhorse', 
    tipo: 'Física', 
    ultimaCalibracion: '2026-01-20', 
    estado: 'En Uso',
    descripcion: 'Perfilador de corrientes por efecto Doppler.',
  },
  { 
    id: 3, 
    nombre: 'Sensor de Oxígeno SBE 43', 
    tipo: 'Biogeoquímica', 
    ultimaCalibracion: '2025-09-10', 
    estado: 'Disponible',
    descripcion: 'Sensor de oxígeno disuelto para rosetas.',
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
    <div class="fondo-cabecera"></div>

    <div class="contenedor-ancho contenido-hub">
      <div class="migas-pan" @click="$emit('volver')" style="cursor: pointer; color: #8cc63f; font-weight: bold; margin-bottom: 20px;">
        &larr; Volver a Servicios
      </div>

      <h1 class="titulo-seccion">Instrumentación Oceanográfica</h1>
      <p class="subtitulo">Infraestructura científica del SIO: gestión de equipos, calibraciones y préstamos.</p>

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
          <h2 class="titulo-fija">Equipamiento {{ categoriaActiva }}</h2>
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
                  <td class="info-principal">
                    <strong>{{ inst.nombre }}</strong>
                    <span class="mini-desc">{{ inst.descripcion }}</span>
                  </td>
                  <td class="fecha-celda">{{ inst.ultimaCalibracion }}</td>
                  <td>
                    <span :class="['status-badge', inst.estado.replace(' ', '-').toLowerCase()]">
                      {{ inst.estado }}
                    </span>
                  </td>
                  <td>
                    <button class="btn-check" @click="mostrarCalendario(inst)">📅 Ver Disponibilidad</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="columna-derecha">
          <div class="seccion-bloque">
            <h2 class="titulo-fija">Gestión de Préstamos</h2>
            <p class="instrucciones">Es necesario el documento de responsabilidad firmado para el préstamo de equipos.</p>
            
            <div class="descarga-box">
              <span class="icon">📄</span>
              <div class="text">
                <strong>Responsabilidad_SIO.pdf</strong>
                <a href="#" class="link-download">Descargar formulario</a>
              </div>
            </div>

            <label class="btn-upload">
              📤 Subir Documento Firmado
              <input type="file" style="display: none;">
            </label>
          </div>

          <div v-if="equipoSeleccionado" class="seccion-bloque card-calendario">
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
/* COHERENCIA VISUAL TOTAL CON SERVICIOS / IDI */
.instrumentacion-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

.fondo-cabecera { 
  position: absolute; top: 0; left: 0; width: 100%; height: 520px; 
  background-image: linear-gradient(rgba(1, 33, 105, 0.75), rgba(1, 33, 105, 0.9)), 
                    url('/instrumentacion.jpg');
  background-size: cover; background-position: center; z-index: 0; 
}

.contenido-hub { position: relative; z-index: 10; padding-top: 120px; }

/* TÍTULOS */
.titulo-seccion { 
  color: white; font-size: 2.2rem; margin-bottom: 15px; font-weight: bold; 
  position: relative; display: inline-block; padding-bottom: 8px;
}
.titulo-seccion::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 4px; background-color: #8cc63f; }
.subtitulo { color: #e0e6ed; font-size: 1.1rem; margin-bottom: 35px; max-width: 800px; }

/* TABS ESTILO PORTAL */
.tabs-categorias { display: flex; gap: 8px; margin-bottom: 25px; }
.tab-btn { 
  padding: 10px 18px; background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2);
  color: white; border-radius: 6px; cursor: pointer; font-weight: bold; transition: 0.3s;
}
.tab-btn.activa { background: #8cc63f; color: #012169; border-color: #8cc63f; }

/* TARJETAS BLANCAS */
.grid-principal { display: grid; grid-template-columns: 1.6fr 1fr; gap: 25px; }
.seccion-bloque { 
  background: white; border-radius: 12px; padding: 30px; 
  box-shadow: 0 8px 25px rgba(0,0,0,0.1); display: flex; flex-direction: column; margin-bottom: 20px;
}
.titulo-fija { color: #012169; font-size: 1.4rem; margin: 0 0 20px 0; border-bottom: 2px solid #f0f0f0; padding-bottom: 12px; }

/* TABLAS Y LISTADOS */
.tabla-sio { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.tabla-sio th { text-align: left; padding: 12px; color: #777; border-bottom: 2px solid #f5f5f5; }
.tabla-sio td { padding: 15px 12px; border-bottom: 1px solid #f9f9f9; }
.info-principal strong { display: block; color: #012169; }
.mini-desc { font-size: 0.8rem; color: #999; }

/* BADGES */
.status-badge { padding: 4px 10px; border-radius: 20px; font-size: 0.7rem; font-weight: bold; text-transform: uppercase; }
.status-badge.disponible { background: #e8f5e9; color: #2e7d32; }
.status-badge.en-uso { background: #fff3e0; color: #ef6c00; }

.btn-check { background: #f0f7ff; color: #0086c0; border: 1px solid #0086c0; padding: 6px 12px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; font-weight: bold; }

/* COLUMNA DERECHA */
.columna-derecha { display: flex; flex-direction: column; }
.instrucciones { font-size: 0.9rem; color: #666; line-height: 1.4; margin-bottom: 15px; }
.descarga-box { 
  display: flex; gap: 12px; align-items: center; background: #f8f9fa; 
  padding: 15px; border-radius: 8px; margin-bottom: 20px; border: 1px dashed #ccc; 
}
.link-download { display: block; font-size: 0.8rem; color: #0086c0; font-weight: bold; }
.btn-upload { 
  display: block; text-align: center; padding: 12px; background: #012169; 
  color: white; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.9rem;
}

/* CALENDARIO */
.card-calendario { border-top: 4px solid #8cc63f; }
.mini-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px; }
.dia { background: #f0f0f0; padding: 6px; text-align: center; font-size: 0.7rem; border-radius: 3px; }
.dia.ocupado { background: #0086c0; color: white; }
.legend { font-size: 0.7rem; color: #999; margin-top: 10px; font-style: italic; }

@media (max-width: 1100px) { .grid-principal { grid-template-columns: 1fr; } }
</style>