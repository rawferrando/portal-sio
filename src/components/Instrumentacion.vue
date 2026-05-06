<script setup>
import { ref, computed } from 'vue'

// 1. CATEGORÍAS
const categoriaActiva = ref('Física')
const categorias = ['Física', 'Biogeoquímica', 'Geología', 'Laboratorio']

// 2. BASE DE DATOS WIKISIO (Ampliada con características)
const instrumentos = ref([
  // FÍSICA
  { id: 1, nombre: 'CTD SeaBird 911plus', tipo: 'Física', ultimaCalibracion: '2025-11-15', estado: 'Disponible', marca: 'Sea-Bird Scientific', descripcion: 'Sistema CTD estándar para perfiles en aguas profundas. Integrable con roseta oceanográfica.', parametros: 'Conductividad, Temperatura, Presión, Oxígeno, Fluorescencia' },
  { id: 2, nombre: 'ADCP Teledyne Workhorse 300kHz', tipo: 'Física', ultimaCalibracion: '2026-01-20', estado: 'En Uso', marca: 'Teledyne Marine', descripcion: 'Perfilador de corrientes acústico Doppler para despliegues en fondeos o montado en casco.', parametros: 'Velocidad y dirección de corrientes 3D' },
  { id: 3, nombre: 'Correntímetro Aquadopp', tipo: 'Física', ultimaCalibracion: '2025-08-10', estado: 'Disponible', marca: 'Nortek', descripcion: 'Correntímetro puntual acústico, ideal para despliegues prolongados en aguas someras.', parametros: 'Corrientes puntuales' },
  // BIOGEOQUÍMICA
  { id: 4, nombre: 'Sensor de Oxígeno SBE 43', tipo: 'Biogeoquímica', ultimaCalibracion: '2025-09-10', estado: 'Disponible', marca: 'Sea-Bird Scientific', descripcion: 'Sensor de oxígeno disuelto tipo Clark, diseñado para integración rápida en CTD.', parametros: 'Oxígeno disuelto' },
  { id: 5, nombre: 'Fluorímetro ECO-AFL', tipo: 'Biogeoquímica', ultimaCalibracion: '2025-12-05', estado: 'Mantenimiento', marca: 'WET Labs', descripcion: 'Sensor óptico de alta resolución para la medición de clorofila-a in situ.', parametros: 'Fluorescencia (Clorofila-a)' },
  { id: 6, nombre: 'Transmisómetro C-Star', tipo: 'Biogeoquímica', ultimaCalibracion: '2026-02-15', estado: 'Disponible', marca: 'WET Labs', descripcion: 'Mide la atenuación de la luz en el agua para estimar la concentración de material particulado.', parametros: 'Transmitancia lumínica' },
  // GEOLOGÍA
  { id: 7, nombre: 'Draga Van Veen', tipo: 'Geología', ultimaCalibracion: 'N/A', estado: 'Disponible', marca: 'KC Denmark', descripcion: 'Draga de mandíbulas de acero inoxidable para la toma de muestras de sedimentos superficiales.', parametros: 'Muestreo de sedimento superficial' },
  { id: 8, nombre: 'Testigo de Gravedad', tipo: 'Geología', ultimaCalibracion: 'N/A', estado: 'En Uso', marca: 'SIO Custom', descripcion: 'Sistema de tubo lastrado (Gravity Corer) para obtener perfiles estratificados de sedimento.', parametros: 'Perfiles de sedimento' },
  // LABORATORIO
  { id: 9, nombre: 'Salinómetro Portasal', tipo: 'Laboratorio', ultimaCalibracion: '2025-10-20', estado: 'Disponible', marca: 'Guildline', descripcion: 'Medidor de salinidad de altísima precisión para procesar muestras de agua discretas.', parametros: 'Salinidad (muestras)' },
  { id: 10, nombre: 'Autoanalizador Nutrientes', tipo: 'Laboratorio', ultimaCalibracion: '2026-03-01', estado: 'Mantenimiento', marca: 'Seal Analytical', descripcion: 'Sistema de análisis colorimétrico continuo para nutrientes en agua de mar.', parametros: 'Nitratos, Fosfatos, Silicatos' }
])

// 3. LÓGICA DE INTERFAZ
const instrumentosFiltrados = computed(() => {
  return instrumentos.value.filter(inst => inst.tipo === categoriaActiva.value)
})

const equipoSeleccionado = ref(null)

const verDetalles = (equipo) => {
  equipoSeleccionado.value = equipo
}

const cambiarCategoria = (cat) => {
  categoriaActiva.value = cat
  equipoSeleccionado.value = null // Oculta el detalle si cambias de pestaña
}
</script>

<template>
  <div class="servicios-hub">
    <div class="fondo-servicios"></div>

    <div class="contenido-hub">
      <h1 class="titulo-seccion">Instrumentación Oceanográfica</h1>
      <p class="subtitulo">Catálogo técnico WikiSIO, características, calibraciones y disponibilidad de equipos.</p>

      <!-- PESTAÑAS -->
      <div class="tabs-sio">
        <button 
          v-for="cat in categorias" 
          :key="cat" 
          :class="['tab-btn', { activa: categoriaActiva === cat }]" 
          @click="cambiarCategoria(cat)"
        >
          {{ cat }}
        </button>
      </div>

      <div class="grid-layout">
        <!-- IZQUIERDA: LISTADO (WikiSIO) -->
        <div class="seccion-bloque ficha-tabla">
          <h2 class="titulo-fija">Equipamiento: {{ categoriaActiva }}</h2>
          <div class="tabla-scroll">
            <table class="tabla-sio">
              <thead>
                <tr>
                  <th>Instrumento</th>
                  <th>Calibración</th>
                  <th>Estado</th>
                  <th>Acción</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="inst in instrumentosFiltrados" :key="inst.id" :class="{ 'fila-activa': equipoSeleccionado?.id === inst.id }">
                  <td><strong>{{ inst.nombre }}</strong></td>
                  <td>{{ inst.ultimaCalibracion }}</td>
                  <td>
                    <span :class="['badge', inst.estado.toLowerCase().replace(' ', '-')]">
                      {{ inst.estado }}
                    </span>
                  </td>
                  <td>
                    <button class="btn-mini" @click="verDetalles(inst)">Ver Ficha</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- DERECHA: DETALLES Y CALENDARIO -->
        <div class="seccion-bloque ficha-gestion">
          
          <!-- ESTADO 1: CUANDO HAY UN EQUIPO SELECCIONADO -->
          <div v-if="equipoSeleccionado" class="detalles-equipo">
            <h2 class="titulo-fija">{{ equipoSeleccionado.nombre }}</h2>
            
            <div class="info-tecnica">
              <p><strong>Marca/Fabricante:</strong> {{ equipoSeleccionado.marca }}</p>
              <p><strong>Parámetros:</strong> {{ equipoSeleccionado.parametros }}</p>
              <div class="caja-desc">
                <p>{{ equipoSeleccionado.descripcion }}</p>
              </div>
            </div>

            <div class="calendario-mini">
              <h3 class="titulo-mini">Disponibilidad de Reservas</h3>
              <div class="grid-dias">
                <!-- Simulamos días ocupados aleatorios para que se vea la diferencia -->
                <div v-for="n in 28" :key="n" :class="['dia', { ocupado: n > 12 && n < 16 && equipoSeleccionado.estado === 'En Uso' }]">
                  {{ n }}
                </div>
              </div>
              <p class="leyenda">* Días en azul: Equipo reservado o no disponible.</p>
            </div>
            
            <button class="btn-cerrar" @click="equipoSeleccionado = null">Cerrar Ficha</button>
          </div>

          <!-- ESTADO 2: VISTA GENERAL (Cuando no hay equipo seleccionado) -->
          <div v-else>
            <h2 class="titulo-fija">Gestión de Préstamos</h2>
            <p class="txt-p">Seleccione <strong>"Ver Ficha"</strong> en cualquier instrumento para consultar sus características técnicas y calendario de disponibilidad.</p>
            
            <hr style="border: 0; border-top: 1px solid #eee; margin: 25px 0;">
            
            <h3 class="titulo-mini">Documentación Necesaria</h3>
            <p class="txt-p" style="font-size: 0.85rem;">Es obligatorio adjuntar el documento de responsabilidad firmado para tramitar la salida de cualquier equipo del SIO.</p>
            
            <div class="descarga-box">
              <span>📄 Compromiso_SIO.pdf</span>
              <a href="#" class="link-dl">Descargar</a>
            </div>

            <label class="btn-upload">
              📤 Subir Documento Firmado
              <input type="file" style="display: none;">
            </label>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* ESTILOS GLOBALES UNIFICADOS */
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
.tabs-sio { display: flex; gap: 10px; margin-bottom: 25px; overflow-x: auto; }
.tab-btn { padding: 10px 20px; background: rgba(255, 255, 255, 0.1); border: 1px solid white; color: white; border-radius: 8px; cursor: pointer; font-weight: bold; transition: 0.3s; white-space: nowrap; }
.tab-btn.activa { background: #8cc63f; border-color: #8cc63f; color: #012169; }

/* GRID */
.grid-layout { display: grid; grid-template-columns: 1.6fr 1fr; gap: 30px; }
.seccion-bloque { background: white; border-radius: 12px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); min-height: auto; }
.titulo-fija { color: #012169; margin-top: 0; font-size: 1.4rem; margin-bottom: 20px; border-bottom: 2px solid #eee; padding-bottom: 10px; }

/* TABLA */
.tabla-scroll { overflow-x: auto; }
.tabla-sio { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.tabla-sio th { text-align: left; padding: 12px; color: #666; border-bottom: 2px solid #f0f0f0; }
.tabla-sio td { padding: 15px 12px; border-bottom: 1px solid #f9f9f9; vertical-align: middle; }
.fila-activa td { background-color: #f0f7ff; } /* Resalta la fila seleccionada */

.badge { padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; white-space: nowrap; }
.badge.disponible { background: #e6f4ea; color: #1e7e34; }
.badge.en-uso { background: #fff4e5; color: #b45d00; }
.badge.mantenimiento { background: #fdeaea; color: #c53030; }

.btn-mini { background: #f0f7ff; color: #0086c0; border: 1px solid #0086c0; padding: 6px 12px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; font-weight: bold; transition: 0.2s; }
.btn-mini:hover { background: #0086c0; color: white; }

/* PANEL DERECHO (DETALLES) */
.info-tecnica p { font-size: 0.9rem; color: #444; margin-bottom: 8px; line-height: 1.4; }
.caja-desc { background: #f8f9fa; padding: 15px; border-left: 4px solid #8cc63f; margin-top: 15px; border-radius: 0 8px 8px 0; }
.caja-desc p { margin: 0; color: #555; font-style: italic; }

.btn-cerrar { margin-top: 20px; width: 100%; background: #f0f0f0; color: #666; border: none; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: bold; }
.btn-cerrar:hover { background: #e0e0e0; }

/* GESTIÓN DOCUMENTAL (ESTADO 2) */
.txt-p { font-size: 0.95rem; color: #666; line-height: 1.5; margin-bottom: 20px; }
.descarga-box { background: #f8f9fa; padding: 15px; border: 1px dashed #ccc; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; font-size: 0.9rem; }
.link-dl { color: #0086c0; font-weight: bold; text-decoration: none; font-size: 0.85rem; }
.btn-upload { display: block; text-align: center; padding: 12px; background: #012169; color: white; border-radius: 8px; cursor: pointer; font-weight: bold; }

/* CALENDARIO */
.calendario-mini { margin-top: 25px; border-top: 2px solid #f9f9f9; padding-top: 20px; }
.titulo-mini { font-size: 1rem; color: #012169; margin-bottom: 15px; font-weight: bold; }
.grid-dias { display: grid; grid-template-columns: repeat(7, 1fr); gap: 5px; }
.dia { background: #f0f0f0; padding: 8px; text-align: center; font-size: 0.8rem; border-radius: 4px; color: #777; }
.dia.ocupado { background: #0086c0; color: white; font-weight: bold; }
.leyenda { font-size: 0.75rem; color: #999; margin-top: 10px; font-style: italic; }

@media (max-width: 992px) { .grid-layout { grid-template-columns: 1fr; } }
</style>