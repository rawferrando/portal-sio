<script setup>
import { ref, computed } from 'vue'

// CATEGORÍAS PRINCIPALES
const categoriaActiva = ref('Física')
const categorias = ['Física', 'Biogeoquímica', 'Geología', 'Laboratorio']

// BASE DE DATOS WIKISIO (Ahora con detalles avanzados estilo Wiki)
const instrumentos = ref([
  { 
    id: 1, tipo: 'Física', subcategoria: 'Sistemas Estacionarios', 
    nombre: 'Sonda Multiparamétrica CTD-48M', marca: 'Sea & Sun Technology', 
    profundidad: '6,000 metros', parametros: 'Conductividad, Temperatura, Profundidad', 
    aplicacion: 'Perfiles de alta precisión en aguas profundas', caracteristicas: 'Carcasa de titanio',
    estado: 'Disponible', ultimaCalibracion: '2023-05-10', 
    descripcionCompleta: 'Equipo robusto diseñado para despliegues en rosetas oceanográficas. Permite obtener perfiles profundos con altísima resolución espacial.',
    detallesAvanzados: null
  },
  { 
    // EL CASTAWAY CON TODA LA INFO DE TU WIKISIO
    id: 2, tipo: 'Física', subcategoria: 'Sistemas Portátiles', 
    nombre: 'CastAway CTD Portátil', marca: 'SonTek/Xylem', 
    profundidad: '0 a 100 metros', parametros: 'Conductividad, Temperatura, Profundidad', 
    aplicacion: 'Perfiles rápidos sin infraestructura de winch', caracteristicas: 'Primer CTD lanzable del mundo, flotabilidad neutra',
    estado: 'En Uso', ultimaCalibracion: '2024-01-15', 
    descripcionCompleta: 'El CastAway CTD es el primer instrumento CTD portátil lanzable del mundo, diseñado para proporcionar perfiles instantáneos de temperatura, salinidad y velocidad del sonido. Revoluciona las mediciones al permitir perfiles CTD de alta precisión sin necesidad de embarcaciones especializadas.',
    detallesAvanzados: {
      mediciones: [
        'Conductividad: 0 a 100,000 µS/cm (Precisión: ±0.25% ±5 µS/cm)',
        'Temperatura: -5°C a +45°C (Precisión: ±0.05°C)',
        'Presión/Profundidad: 0 a 100 metros (Precisión: ±0.25% escala completa)',
        'Parámetros Calculados: Salinidad (PSS-78), Densidad (UNESCO), Velocidad del sonido (Chen-Millero)'
      ],
      fisicas: [
        'Dimensiones: 4.6 cm x 18.6 cm x 33.5 cm',
        'Peso: 0.6 kg en aire (Flotabilidad neutra en agua)',
        'Alimentación: 4 pilas AA (Autonomía >500 perfiles)',
        'Conectividad: Bluetooth para transferencia de datos inalámbrica'
      ],
      operacion: [
        'Software CastAway: Descarga automática vía Bluetooth, gráficos en tiempo real y exportación (CSV, Excel)',
        'Mantenimiento: Enjuague con agua dulce post-uso, inspección de sensores y almacenamiento en seco',
        'Estudios ideales: Caracterización de estuarios, monitoreo portuario, acuicultura y plumas costeras'
      ]
    }
  },
  { 
    id: 3, tipo: 'Física', subcategoria: 'Sensores Físicos', 
    nombre: 'Sensor de Presión SBE 5', marca: 'Sea-Bird Scientific', 
    numSerie: '11599', ultimaCalibracion: 'Mayo 2023', rango: '0-6800 dbar', precision: '±0.1% escala completa',
    estado: 'Disponible', 
    descripcionCompleta: 'Bomba sumergible de titanio para integración modular en sistemas CTD.',
    detallesAvanzados: null
  }
])

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
const diasSeleccionados = ref([])

const verDetalles = (equipo) => {
  equipoSeleccionado.value = equipo
  diasSeleccionados.value = [] 
}

const cambiarCategoria = (cat) => {
  categoriaActiva.value = cat
  equipoSeleccionado.value = null
}

const esOcupado = (n) => {
  return n > 10 && n < 15 && equipoSeleccionado.value.estado === 'En Uso'
}

const toggleDia = (n) => {
  if (esOcupado(n)) return
  const index = diasSeleccionados.value.indexOf(n)
  if (index > -1) {
    diasSeleccionados.value.splice(index, 1) 
  } else {
    diasSeleccionados.value.push(n) 
  }
}

const enviarSolicitud = () => {
  if (diasSeleccionados.value.length === 0) {
    alert("⚠️ Por favor, selecciona al menos un día disponible en el calendario para tu reserva.")
    return
  }

  const diasOrdenados = [...diasSeleccionados.value].sort((a, b) => a - b).join(', ')
  const equipo = equipoSeleccionado.value.nombre

  const subject = encodeURIComponent(`Solicitud de Préstamo SIO: ${equipo}`)
  const body = encodeURIComponent(
`Hola SIO,

Deseo solicitar el equipo de instrumentación:
➡️ ${equipo}

He comprobado la disponibilidad en la web y solicito la reserva para los días: ${diasOrdenados} de este mes.

[POR FAVOR, ADJUNTA EL DOCUMENTO DE RESPONSABILIDAD FIRMADO A ESTE CORREO ANTES DE ENVIARLO].

Gracias y un saludo.`
  )

  window.location.href = `mailto:sio@icm.csic.es?subject=${subject}&body=${body}`
}
</script>

<template>
  <div class="servicios-hub">
    <div class="fondo-servicios"></div>

    <div class="contenido-hub">
      <h1 class="titulo-seccion">Instrumentación Oceanográfica</h1>
      <p class="subtitulo">Catálogo WikiSIO: Características técnicas, calibraciones y gestión de préstamos.</p>

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
        
        <!-- ZONA IZQUIERDA: WIKISIO -->
        <div class="seccion-bloque ficha-wiki">
          <div v-if="Object.keys(instrumentosAgrupados).length === 0" style="color: #666; font-style: italic;">
            No hay instrumentos catalogados en esta sección actualmente.
          </div>

          <div v-for="(lista, subcat) in instrumentosAgrupados" :key="subcat" class="bloque-subcat">
            <h3 class="titulo-subcat">{{ subcat }}</h3>
            <ul class="lista-wiki">
              <li v-for="inst in lista" :key="inst.id">
                <div class="item-header">
                  <span class="punto-azul">•</span>
                  <span class="enlace-wiki" @click="verDetalles(inst)">{{ inst.nombre }}</span>
                  <span class="marca-wiki">({{ inst.marca }})</span>
                </div>
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

        <!-- ZONA DERECHA: RESERVAS Y DESCRIPCIÓN -->
        <div class="seccion-bloque ficha-gestion">
          
          <div v-if="equipoSeleccionado" class="detalles-equipo">
            <div class="cabecera-estado">
              <h2 class="titulo-fija">{{ equipoSeleccionado.nombre }}</h2>
              <span :class="['badge-grande', equipoSeleccionado.estado.toLowerCase().replace(' ', '-')]">
                {{ equipoSeleccionado.estado }}
              </span>
            </div>
            
            <p style="font-size: 0.9rem; color: #666; margin-bottom: 5px;">Paso 1: Descarga el formulario y fírmalo.</p>
            <div class="descarga-box-pequena">
              <span>📄 Responsabilidad_SIO.pdf</span>
              <a href="/Responsabilidad_SIO.pdf" download="Formulario_Responsabilidad_SIO.pdf" class="link-dl-mini">⬇ Descargar</a>
            </div>

            <div class="calendario-mini">
              <h3 class="titulo-mini">Paso 2: Selecciona los días de reserva</h3>
              <div class="grid-dias">
                <!-- CALENDARIO INTERACTIVO -->
                <div 
                  v-for="n in 28" 
                  :key="n" 
                  @click="toggleDia(n)"
                  :class="['dia', { 
                    ocupado: esOcupado(n), 
                    seleccionado: diasSeleccionados.includes(n),
                    disponible: !esOcupado(n)
                  }]"
                >
                  {{ n }}
                </div>
              </div>
              <p class="leyenda">* Gris: Disponible | Azul: Ocupado | Verde: Tu selección</p>
            </div>

            <!-- BOTÓN GENERADOR DE EMAIL -->
            <button class="btn-correo" @click="enviarSolicitud">
              ✉️ Paso 3: Enviar Solicitud por Email
            </button>
            <p style="font-size: 0.75rem; color: #888; text-align: center; margin-top: 5px; margin-bottom: 20px;">
              Se abrirá tu correo. ¡Recuerda adjuntar el PDF firmado!
            </p>

            <!-- DESCRIPCIÓN DETALLADA WIKISIO ABAJO -->
            <div class="info-tecnica-abajo">
              <h3 class="titulo-mini">Ficha Técnica Completa</h3>
              
              <div class="caja-desc">
                <p>{{ equipoSeleccionado.descripcionCompleta }}</p>
              </div>

              <!-- SECCIONES AVANZADAS SI EXISTEN -->
              <div v-if="equipoSeleccionado.detallesAvanzados" class="detalles-avanzados">
                
                <h4 class="titulo-seccion-mini">Mediciones y Precisión</h4>
                <ul class="lista-detalles">
                  <li v-for="(item, idx) in equipoSeleccionado.detallesAvanzados.mediciones" :key="'med-'+idx">{{ item }}</li>
                </ul>

                <h4 class="titulo-seccion-mini">Características Físicas</h4>
                <ul class="lista-detalles">
                  <li v-for="(item, idx) in equipoSeleccionado.detallesAvanzados.fisicas" :key="'fis-'+idx">{{ item }}</li>
                </ul>

                <h4 class="titulo-seccion-mini">Operación y Software</h4>
                <ul class="lista-detalles">
                  <li v-for="(item, idx) in equipoSeleccionado.detallesAvanzados.operacion" :key="'op-'+idx">{{ item }}</li>
                </ul>

              </div>
            </div>
            
            <button class="btn-cerrar" @click="equipoSeleccionado = null">Cerrar Detalles</button>
          </div>

          <!-- VISTA GENERAL (Sin equipo seleccionado) -->
          <div v-else>
            <h2 class="titulo-fija">Préstamos SIO</h2>
            <p class="txt-p">Haga clic en el enlace azul de cualquier instrumento a la izquierda para ver su ficha técnica completa y disponibilidad.</p>
            
            <hr style="border: 0; border-top: 1px solid #eee; margin: 25px 0;">
            <h3 class="titulo-mini">¿Cómo funciona?</h3>
            <ol style="color: #666; font-size: 0.9rem; line-height: 1.6; padding-left: 20px;">
              <li>Selecciona un instrumento de la lista.</li>
              <li>Descarga el PDF de responsabilidad.</li>
              <li>Haz clic en los días del calendario que necesites.</li>
              <li>Pulsa en enviar para notificarnos por email con tu PDF adjunto.</li>
            </ol>
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
.contenido-hub { position: relative; z-index: 10; padding-top: 120px; max-width: 1300px; margin: 0 auto; padding-left: 20px; padding-right: 20px; }
.titulo-seccion { color: white; font-size: 2.2rem; font-weight: bold; position: relative; display: inline-block; padding-bottom: 8px; margin-bottom: 15px; }
.titulo-seccion::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 4px; background-color: #8cc63f; }
.subtitulo { color: #e0e6ed; font-size: 1.1rem; margin-bottom: 35px; max-width: 800px; }

/* TABS */
.tabs-sio { display: flex; gap: 10px; margin-bottom: 25px; overflow-x: auto; }
.tab-btn { padding: 10px 20px; background: rgba(255, 255, 255, 0.1); border: 1px solid white; color: white; border-radius: 8px; cursor: pointer; font-weight: bold; transition: 0.3s; white-space: nowrap; }
.tab-btn.activa { background: #8cc63f; border-color: #8cc63f; color: #012169; }

/* GRID */
.grid-layout { display: grid; grid-template-columns: 1.8fr 1.3fr; gap: 30px; }
.seccion-bloque { background: white; border-radius: 12px; padding: 35px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); min-height: auto; }
.titulo-fija { color: #012169; margin-top: 0; font-size: 1.4rem; margin-bottom: 20px; border-bottom: 2px solid #eee; padding-bottom: 10px; }

/* ESTILO WIKISIO (ZONA IZQUIERDA) */
.bloque-subcat { margin-bottom: 30px; }
.titulo-subcat { font-size: 1.1rem; color: #333; margin-bottom: 15px; border-bottom: 1px solid #ddd; padding-bottom: 5px; }
.lista-wiki { list-style: none; padding-left: 0; margin: 0; }
.item-header { margin-bottom: 8px; font-size: 0.95rem; }
.punto-azul { color: #0056b3; margin-right: 8px; font-size: 1.2rem; line-height: 0; }
.enlace-wiki { color: #0056b3; font-weight: 500; cursor: pointer; text-decoration: none; font-size: 1.05rem; }
.enlace-wiki:hover { text-decoration: underline; }
.marca-wiki { color: #666; font-size: 0.9rem; margin-left: 5px; }
.caja-gris-wiki { background-color: #f1f3f4; border-radius: 6px; padding: 15px; margin-left: 15px; margin-bottom: 20px; font-family: 'Consolas', 'Courier New', Courier, monospace; font-size: 0.85rem; color: #202124; line-height: 1.6; }

/* PANEL DERECHO (GESTIÓN) */
.cabecera-estado { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-bottom: 15px;}
.cabecera-estado .titulo-fija { border-bottom: none; margin-bottom: 0; padding-bottom: 0; font-size: 1.3rem;}

.badge-grande { padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; }
.badge-grande.disponible { background: #e6f4ea; color: #1e7e34; }
.badge-grande.en-uso { background: #fff4e5; color: #b45d00; }
.badge-grande.mantenimiento { background: #fdeaea; color: #c53030; }

/* DESCARGAS */
.txt-p { font-size: 0.95rem; color: #666; line-height: 1.5; margin-bottom: 20px; }
.descarga-box-pequena { background: #eef5fa; padding: 10px 15px; border: 1px dashed #0086c0; border-radius: 6px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; font-size: 0.85rem; }
.link-dl-mini { color: #0086c0; font-weight: bold; text-decoration: none; font-size: 0.8rem; background: white; padding: 4px 8px; border-radius: 4px; border: 1px solid #0086c0;}

/* CALENDARIO INTERACTIVO */
.calendario-mini { margin-bottom: 20px; }
.titulo-mini { font-size: 1.1rem; color: #012169; margin-bottom: 10px; font-weight: bold; }
.grid-dias { display: grid; grid-template-columns: repeat(7, 1fr); gap: 5px; }
.dia { padding: 8px; text-align: center; font-size: 0.85rem; border-radius: 4px; font-weight: bold; transition: 0.2s; user-select: none; }
.dia.disponible { background: #f0f0f0; color: #666; cursor: pointer; border: 1px solid transparent;}
.dia.disponible:hover { border-color: #8cc63f; }
.dia.ocupado { background: #0086c0; color: white; cursor: not-allowed; opacity: 0.6; }
.dia.seleccionado { background: #8cc63f; color: #012169; border: 1px solid #012169; transform: scale(1.05); }
.leyenda { font-size: 0.75rem; color: #999; margin-top: 10px; text-align: center; }

/* BOTÓN EMAIL */
.btn-correo { width: 100%; background-color: #012169; color: white; border: none; padding: 15px; border-radius: 8px; font-size: 1rem; font-weight: bold; cursor: pointer; transition: 0.3s; margin-top: 10px; }
.btn-correo:hover { background-color: #0056b3; transform: translateY(-2px); }

/* SECCIÓN WIKI DETALLADA ABAJO */
.info-tecnica-abajo { margin-top: 30px; border-top: 2px solid #eee; padding-top: 25px; }
.caja-desc { background: #f8f9fa; padding: 15px; border-left: 4px solid #8cc63f; border-radius: 0 8px 8px 0; margin-bottom: 20px;}
.caja-desc p { margin: 0; color: #444; line-height: 1.5; font-size: 0.95rem; text-align: justify;}

.detalles-avanzados { margin-top: 15px; }
.titulo-seccion-mini { font-size: 0.95rem; color: #0056b3; margin-bottom: 8px; margin-top: 15px; border-bottom: 1px solid #e0e0e0; padding-bottom: 4px;}
.lista-detalles { list-style-type: square; padding-left: 20px; color: #555; font-size: 0.85rem; line-height: 1.6; margin-top: 5px; margin-bottom: 0;}

.btn-cerrar { margin-top: 30px; width: 100%; background: #eee; color: #555; border: none; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: bold; transition: 0.2s; }
.btn-cerrar:hover { background: #e0e0e0; color: #333; }

@media (max-width: 992px) { .grid-layout { grid-template-columns: 1fr; } }
</style>