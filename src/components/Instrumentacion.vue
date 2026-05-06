<script setup>
import { ref, computed } from 'vue'

// 1. CATEGORÍAS PRINCIPALES (Pestañas)
const categoriaActiva = ref('Física')
const categorias = ['Física', 'Biogeoquímica', 'Geología', 'Laboratorio']

// 2. BASE DE DATOS WIKISIO (Clavada a tu captura)
const instrumentos = ref([
  // --- FÍSICA: Sistemas Estacionarios ---
  { 
    id: 1, tipo: 'Física', subcategoria: 'Sistemas Estacionarios', 
    nombre: 'Sonda Multiparamétrica CTD-48M', marca: 'Sea & Sun Technology', 
    profundidad: '6,000 metros', parametros: 'Conductividad, Temperatura, Profundidad + sensor opcional', 
    aplicacion: 'Perfiles de alta precisión en aguas profundas', caracteristicas: 'Carcasa de titanio, memoria interna 128 MB',
    estado: 'Disponible', ultimaCalibracion: '2023-05-10', descripcionCompleta: 'Equipo robusto para despliegues en rosetas oceanográficas para perfiles profundos.'
  },
  // --- FÍSICA: Sistemas Portátiles ---
  { 
    id: 2, tipo: 'Física', subcategoria: 'Sistemas Portátiles', 
    nombre: 'CastAway CTD Portátil', marca: 'SonTek/Xylem', 
    profundidad: '100 metros', parametros: 'Conductividad, Temperatura, Profundidad', 
    aplicacion: 'Perfiles rápidos sin infraestructura de winch', caracteristicas: 'Primer CTD lanzable del mundo, operación autónoma',
    estado: 'En Uso', ultimaCalibracion: '2024-01-15', descripcionCompleta: 'CTD de mano ideal para embarcaciones pequeñas y fondeos rápidos en costa.'
  },
  // --- FÍSICA: Sensores Físicos ---
  { 
    id: 3, tipo: 'Física', subcategoria: 'Sensores Físicos', 
    nombre: 'Sensor de Presión SBE 5', marca: 'Sea-Bird Scientific', 
    numSerie: '11599', ultimaCalibracion: 'Mayo 2023', rango: '0-6800 dbar (equiv. 6800m profundidad)', precision: '±0.1% escala completa',
    estado: 'Disponible', descripcionCompleta: 'Bomba sumergible de titanio para integración modular en sistemas CTD.'
  },
  { 
    id: 4, tipo: 'Física', subcategoria: 'Sensores Físicos', 
    nombre: 'Sensor de Temperatura SBE 3', marca: 'Sea-Bird Scientific', 
    numSerie: '6694', ultimaCalibracion: 'Julio 2022', rango: '-5 a +35°C', precision: '±0.002°C',
    estado: 'Mantenimiento', descripcionCompleta: 'Termómetro oceanográfico de altísima precisión y respuesta rápida.'
  },
  // --- BIOGEOQUÍMICA ---
  { 
    id: 5, tipo: 'Biogeoquímica', subcategoria: 'Sensores Ópticos', 
    nombre: 'Fluorímetro ECO-AFL', marca: 'WET Labs', 
    profundidad: '6,000 metros', parametros: 'Fluorescencia (Clorofila-a)', aplicacion: 'Detección de fitoplancton', caracteristicas: 'Óptica de alta resolución',
    estado: 'Disponible', ultimaCalibracion: '2023-11-20', descripcionCompleta: 'Sensor óptico para medir la concentración de clorofila-a in situ.'
  }
])

// 3. AGRUPACIÓN PARA EL DISEÑO WIKI
// Esto agrupa los instrumentos por su "subcategoría" automáticamente
const instrumentosAgrupados = computed(() => {
  const filtrados = instrumentos.value.filter(inst => inst.tipo === categoriaActiva.value)
  const grupos = {}
  filtrados.forEach(inst => {
    if (!grupos[inst.subcategoria]) grupos[inst.subcategoria] = []
    grupos[inst.subcategoria].push(inst)
  })
  return grupos
})

const equipoSeleccionado = ref(null)

const verDetalles = (equipo) => {
  equipoSeleccionado.value = equipo
}

const cambiarCategoria = (cat) => {
  categoriaActiva.value = cat
  equipoSeleccionado.value = null
}
</script>

<template>
  <div class="servicios-hub">
    <div class="fondo-servicios"></div>

    <div class="contenido-hub">
      <h1 class="titulo-seccion">Instrumentación Oceanográfica</h1>
      <p class="subtitulo">Catálogo WikiSIO: Características técnicas, calibraciones y gestión de préstamos.</p>

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
        
        <!-- ========================================== -->
        <!-- FICHA IZQUIERDA: ESTILO WIKISIO CLAVADO -->
        <!-- ========================================== -->
        <div class="seccion-bloque ficha-wiki">
          
          <div v-if="Object.keys(instrumentosAgrupados).length === 0" style="color: #666; font-style: italic;">
            No hay instrumentos catalogados en esta sección actualmente.
          </div>

          <div v-for="(lista, subcat) in instrumentosAgrupados" :key="subcat" class="bloque-subcat">
            <h3 class="titulo-subcat">{{ subcat }}</h3>
            
            <ul class="lista-wiki">
              <li v-for="inst in lista" :key="inst.id">
                
                <!-- Título Clickable Estilo Enlace -->
                <div class="item-header">
                  <span class="punto-azul">•</span>
                  <span class="enlace-wiki" @click="verDetalles(inst)">{{ inst.nombre }}</span>
                  <span class="marca-wiki">({{ inst.marca }})</span>
                </div>

                <!-- Caja Gris Tipo Código -->
                <div class="caja-gris-wiki">
                  <div v-if="inst.numSerie"><strong>- Número de serie:</strong> {{ inst.numSerie }}</div>
                  <div v-if="inst.profundidad"><strong>- Profundidad máxima:</strong> {{ inst.profundidad }}</div>
                  <div v-if="inst.parametros"><strong>- Parámetros:</strong> {{ inst.parametros }}</div>
                  <div v-if="inst.aplicacion"><strong>- Aplicación:</strong> {{ inst.aplicacion }}</div>
                  <div v-if="inst.caracteristicas"><strong>- Características:</strong> {{ inst.caracteristicas }}</div>
                  <div v-if="inst.ultimaCalibracion"><strong>- Última calibración:</strong> {{ inst.ultimaCalibracion }}</div>
                  <div v-if="inst.rango"><strong>- Rango:</strong> {{ inst.rango }}</div>
                  <div v-if="inst.precision"><strong>- Precisión:</strong> {{ inst.precision }}</div>
                </div>

              </li>
            </ul>
          </div>
        </div>

        <!-- ========================================== -->
        <!-- FICHA DERECHA: GESTIÓN Y CALENDARIO -->
        <!-- ========================================== -->
        <div class="seccion-bloque ficha-gestion">
          
          <!-- SI HAY UN EQUIPO SELECCIONADO AL HACER CLIC -->
          <div v-if="equipoSeleccionado" class="detalles-equipo">
            <div class="cabecera-estado">
              <h2 class="titulo-fija">{{ equipoSeleccionado.nombre }}</h2>
              <span :class="['badge-grande', equipoSeleccionado.estado.toLowerCase().replace(' ', '-')]">
                {{ equipoSeleccionado.estado }}
              </span>
            </div>
            
            <div class="info-tecnica">
              <p><strong>Clasificación:</strong> {{ equipoSeleccionado.subcategoria }}</p>
              <div class="caja-desc">
                <p>{{ equipoSeleccionado.descripcionCompleta }}</p>
              </div>
            </div>

            <div class="calendario-mini">
              <h3 class="titulo-mini">Disponibilidad de Reservas</h3>
              <div class="grid-dias">
                <!-- Generamos un calendario de ejemplo -->
                <div v-for="n in 28" :key="n" :class="['dia', { ocupado: n > 10 && n < 15 && equipoSeleccionado.estado === 'En Uso' }]">
                  {{ n }}
                </div>
              </div>
              <p class="leyenda">* Días en azul: Equipo en uso / Mantenimiento.</p>
            </div>
            
            <button class="btn-cerrar" @click="equipoSeleccionado = null">Cerrar Detalles</button>
          </div>

          <!-- VISTA GENERAL POR DEFECTO -->
          <div v-else>
            <h2 class="titulo-fija">Préstamos SIO</h2>
            <p class="txt-p">Haga clic en el enlace azul de cualquier instrumento a la izquierda para ver su disponibilidad en tiempo real.</p>
            
            <hr style="border: 0; border-top: 1px solid #eee; margin: 25px 0;">
            
            <h3 class="titulo-mini">Documentación Obligatoria</h3>
            <p class="txt-p" style="font-size: 0.85rem;">Es imprescindible tramitar el documento de responsabilidad para la retirada de material.</p>
            
            <div class="descarga-box">
              <span>📄 Responsabilidad_SIO.pdf</span>
              <!-- ¡AQUÍ ESTÁ LA MAGIA DE LA DESCARGA! -->
              <a href="/Responsabilidad_SIO.pdf" download="Formulario_Responsabilidad_SIO.pdf" class="link-dl">⬇ Descargar PDF</a>
            </div>

            <label class="btn-upload">
              📤 Subir Formulario Firmado
              <input type="file" style="display: none;">
            </label>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* ================= ESTRUCTURA GLOBAL ================= */
.servicios-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }
.fondo-servicios { 
  position: absolute; top: 0; left: 0; width: 100%; height: 550px; 
  background-image: linear-gradient(rgba(1, 33, 105, 0.75), rgba(1, 33, 105, 0.9)), url('/instrumentacion.jpg');
  background-size: cover; background-position: center; z-index: 0; 
}
.contenido-hub { position: relative; z-index: 10; padding-top: 120px; max-width: 1300px; margin: 0 auto; padding-left: 20px; padding-right: 20px; }
.titulo-seccion { color: white; font-size: 2.2rem; font-weight: bold; position: relative; display: inline-block; padding-bottom: 8px; margin-bottom: 15px; }
.titulo-seccion::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 4px; background-color: #8cc63f; }
.subtitulo { color: #e0e6ed; font-size: 1.1rem; margin-bottom: 35px; max-width: 800px; }

/* ================= TABS ================= */
.tabs-sio { display: flex; gap: 10px; margin-bottom: 25px; overflow-x: auto; }
.tab-btn { padding: 10px 20px; background: rgba(255, 255, 255, 0.1); border: 1px solid white; color: white; border-radius: 8px; cursor: pointer; font-weight: bold; transition: 0.3s; white-space: nowrap; }
.tab-btn.activa { background: #8cc63f; border-color: #8cc63f; color: #012169; }

/* ================= GRID ================= */
.grid-layout { display: grid; grid-template-columns: 1.8fr 1fr; gap: 30px; }
.seccion-bloque { background: white; border-radius: 12px; padding: 35px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); min-height: auto; }
.titulo-fija { color: #012169; margin-top: 0; font-size: 1.4rem; margin-bottom: 20px; border-bottom: 2px solid #eee; padding-bottom: 10px; }

/* ================= ESTILO WIKISIO (ZONA IZQUIERDA) ================= */
.bloque-subcat { margin-bottom: 30px; }
.titulo-subcat { font-size: 1.1rem; color: #333; margin-bottom: 15px; border-bottom: 1px solid #ddd; padding-bottom: 5px; }
.lista-wiki { list-style: none; padding-left: 0; margin: 0; }
.item-header { margin-bottom: 8px; font-size: 0.95rem; }
.punto-azul { color: #0056b3; margin-right: 8px; font-size: 1.2rem; line-height: 0; }
.enlace-wiki { color: #0056b3; font-weight: 500; cursor: pointer; text-decoration: none; }
.enlace-wiki:hover { text-decoration: underline; }
.marca-wiki { color: #666; font-size: 0.9rem; margin-left: 5px; }

.caja-gris-wiki { 
  background-color: #f1f3f4; 
  border-radius: 6px; 
  padding: 15px; 
  margin-left: 15px; 
  margin-bottom: 20px;
  font-family: 'Consolas', 'Courier New', Courier, monospace; /* Letra tipo código */
  font-size: 0.85rem; 
  color: #202124;
  line-height: 1.6;
}

/* ================= PANEL DERECHO (GESTIÓN) ================= */
.cabecera-estado { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-bottom: 20px;}
.cabecera-estado .titulo-fija { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }

.badge-grande { padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; }
.badge-grande.disponible { background: #e6f4ea; color: #1e7e34; }
.badge-grande.en-uso { background: #fff4e5; color: #b45d00; }
.badge-grande.mantenimiento { background: #fdeaea; color: #c53030; }

.info-tecnica p { font-size: 0.95rem; color: #444; margin-bottom: 8px; }
.caja-desc { background: #f8f9fa; padding: 15px; border-left: 4px solid #8cc63f; margin-top: 15px; border-radius: 0 8px 8px 0; }
.caja-desc p { margin: 0; color: #555; line-height: 1.5; }

.btn-cerrar { margin-top: 20px; width: 100%; background: #eee; color: #555; border: none; padding: 12px; border-radius: 6px; cursor: pointer; font-weight: bold; transition: 0.2s; }
.btn-cerrar:hover { background: #e0e0e0; color: #333; }

/* DESCARGAS */
.txt-p { font-size: 0.95rem; color: #666; line-height: 1.5; margin-bottom: 20px; }
.descarga-box { background: #eef5fa; padding: 15px; border: 1px dashed #0086c0; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.link-dl { color: #0086c0; font-weight: bold; text-decoration: none; font-size: 0.9rem; background: white; padding: 5px 10px; border-radius: 4px; border: 1px solid #0086c0;}
.link-dl:hover { background: #0086c0; color: white; }
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