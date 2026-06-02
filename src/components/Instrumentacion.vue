<script setup>
import { ref } from 'vue'

// Esta variable recuerda qué instrumento está abierto actualmente (si es null, están todos cerrados)
const instrumentoExpandido = ref(null)

const toggleAcordeon = (index) => {
  // Si haces clic en el que ya está abierto, se cierra. Si haces clic en otro, se abre ese.
  instrumentoExpandido.value = instrumentoExpandido.value === index ? null : index
}

// 🗄️ CATÁLOGO DE INSTRUMENTACIÓN (Aquí meterás toda la info de la Wiki)
// He puesto 3 ejemplos reales del SIO para que veas cómo se rellena
const instrumentos = ref([
  {
    nombre: 'CTD SBE 911plus',
    descripcionCorta: 'Perfilador de conductividad, temperatura y profundidad para alta resolución.',
    detallesWiki: `
      <strong>Fabricante:</strong> Sea-Bird Electronics<br><br>
      <strong>Sensores integrados:</strong> Temperatura, Conductividad, Presión, y Oxígeno disuelto (SBE 43).<br><br>
      <strong>Profundidad máxima:</strong> 6800 m.<br><br>
      <strong>Mantenimiento:</strong> Lavado con agua dulce tras cada inmersión. Rellenar jeringas de Tygon con agua destilada para proteger las celdas de conductividad.
    `,
    fechaInicio: '',
    fechaFin: '',
    proyecto: ''
  },
  {
    nombre: 'ADCP Workhorse Sentinel 300 kHz',
    descripcionCorta: 'Perfilador de corrientes acústico Doppler para medición de la columna de agua.',
    detallesWiki: `
      <strong>Fabricante:</strong> Teledyne RD Instruments<br><br>
      <strong>Frecuencia:</strong> 300 kHz.<br><br>
      <strong>Rango de perfilado típico:</strong> Hasta 150 metros.<br><br>
      <strong>Modos de uso:</strong> Puede ser instalado en fondeos fijos o montado en el casco de embarcaciones para muestreo en movimiento.
    `,
    fechaInicio: '',
    fechaFin: '',
    proyecto: ''
  },
  {
    nombre: 'Roseta Oceanográfica (24 botellas)',
    descripcionCorta: 'Sistema de muestreo de agua acoplado al CTD para recogida a diferentes profundidades.',
    detallesWiki: `
      <strong>Capacidad:</strong> 24 botellas Niskin de 12 litros.<br><br>
      <strong>Sistema de disparo:</strong> Automático mediante Deck Unit SBE 11plus.<br><br>
      <strong>Protocolo Wiki:</strong> Revisar el estado de las gomas y las juntas tóricas inferiores antes de cada inicio de campaña.
    `,
    fechaInicio: '',
    fechaFin: '',
    proyecto: ''
  }
])

const enviarReserva = (instrumento) => {
  if (!instrumento.fechaInicio || !instrumento.fechaFin || !instrumento.proyecto.trim()) {
    alert('Por favor, rellena las fechas y el nombre del proyecto para solicitar la reserva.')
    return
  }
  
  const destinatario = "sio.icm@icm.csic.es"
  const asunto = encodeURIComponent(`Reserva de Instrumentación: ${instrumento.nombre}`)
  const cuerpo = encodeURIComponent(
    `Hola equipo del SIO,\n\nMe gustaría solicitar la disponibilidad del siguiente equipo:\n\n` +
    `⚙️ EQUIPO: ${instrumento.nombre}\n` +
    `📁 PROYECTO/CAMPAÑA: ${instrumento.proyecto}\n` +
    `📅 FECHA INICIO: ${instrumento.fechaInicio}\n` +
    `📅 FECHA FIN: ${instrumento.fechaFin}\n\n` +
    `Quedo a la espera de confirmación.\n\nUn saludo.`
  )
  window.location.href = `mailto:${destinatario}?subject=${asunto}&body=${cuerpo}`
}
</script>

<template>
  <div class="pagina-detalle">
    <div class="hero-detalle hero-instrumentacion">
      <div class="contenedor-ancho contenido-hero">
        <h1 class="titulo-hero">Catálogo de Instrumentación</h1>
        <p class="subtitulo-hero">Explora el equipamiento del SIO extraído de nuestra Wiki. Haz clic en un equipo para ver sus especificaciones técnicas y reservar fechas.</p>
      </div>
    </div>

    <div class="contenedor-ancho seccion-principal">
      <div class="lista-acordeon">

        <div 
          v-for="(instrumento, index) in instrumentos" 
          :key="index" 
          class="item-acordeon"
          :class="{ 'activo': instrumentoExpandido === index }"
        >
          <div class="cabecera-acordeon" @click="toggleAcordeon(index)">
            <div class="info-cabecera">
              <h3>{{ instrumento.nombre }}</h3>
              <p>{{ instrumento.descripcionCorta }}</p>
            </div>
            <div class="icono-desplegable">
              <span v-if="instrumentoExpandido === index" class="texto-ocultar">▲ Plegar info</span>
              <span v-else class="texto-ver">▼ Ver toda la info y calendario</span>
            </div>
          </div>

          <div class="contenido-acordeon" v-show="instrumentoExpandido === index">
            <div class="grid-contenido-instrumento">
              
              <div class="columna-wiki">
                <h4 class="titulo-bloque">Especificaciones Técnicas (Wiki SIO)</h4>
                <div class="texto-wiki" v-html="instrumento.detallesWiki"></div>
                <a href="https://wikisio.icm.csic.es/index.php/P%C3%A1gina_principal" target="_blank" class="enlace-wiki">
                  Consultar fuente original en WikiSIO ↗
                </a>
              </div>

              <div class="columna-reserva">
                <h4 class="titulo-bloque">Comprobar Disponibilidad</h4>
                <form @submit.prevent="enviarReserva(instrumento)" class="formulario-reserva">
                  <div class="grupo-input">
                    <label>Proyecto / Campaña:</label>
                    <input type="text" v-model="instrumento.proyecto" class="input-form" placeholder="Ej: Campaña MedSea 2026" required>
                  </div>
                  
                  <div class="fila-fechas">
                    <div class="grupo-input">
                      <label>Fecha de Inicio:</label>
                      <input type="date" v-model="instrumento.fechaInicio" class="input-form calendario" required>
                    </div>
                    <div class="grupo-input">
                      <label>Fecha de Fin:</label>
                      <input type="date" v-model="instrumento.fechaFin" class="input-form calendario" required>
                    </div>
                  </div>

                  <button type="submit" class="btn-reservar">SOLICITAR EQUIPO</button>
                </form>
              </div>

            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped>
/* ESTILOS GLOBALES DE LA PÁGINA */
.pagina-detalle { background-color: #f4f7f9; min-height: 100vh; padding-bottom: 80px; }
.hero-instrumentacion { background-color: #012169; padding: 120px 0 60px 0; color: white; }
.contenido-hero { position: relative; display: flex; flex-direction: column; align-items: flex-start; }
.titulo-hero { font-size: 3rem; font-weight: bold; margin: 0 0 15px 0; position: relative; display: inline-block; padding-bottom: 10px; }
.titulo-hero::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 5px; background-color: #8cc63f; }
.subtitulo-hero { font-size: 1.15rem; color: #e0e6ed; max-width: 800px; margin: 0; }
.seccion-principal { margin-top: 40px; max-width: 1000px; margin-left: auto; margin-right: auto; }

/* EL ACORDEÓN (LISTA DESPLEGABLE) */
.lista-acordeon { display: flex; flex-direction: column; gap: 15px; }

.item-acordeon { 
  background: white; 
  border-radius: 10px; 
  box-shadow: 0 4px 15px rgba(0,0,0,0.05); 
  overflow: hidden; /* Esto asegura que las esquinas redondeadas se mantengan */
  transition: all 0.3s ease;
  border-left: 5px solid transparent;
}

/* Efecto visual cuando un instrumento está abierto */
.item-acordeon.activo { 
  border-left: 5px solid #8cc63f; 
  box-shadow: 0 8px 25px rgba(0,0,0,0.1); 
  margin: 10px 0; /* Lo separa un poco de los demás para darle protagonismo */
}

/* CABECERA CLICABLE */
.cabecera-acordeon { 
  padding: 25px; 
  display: flex; 
  justify-content: space-between; 
  align-items: center; 
  cursor: pointer; 
  background-color: white;
}
.cabecera-acordeon:hover { background-color: #fcfdfd; }
.info-cabecera h3 { margin: 0 0 5px 0; color: #012169; font-size: 1.4rem; }
.info-cabecera p { margin: 0; color: #666; font-size: 0.95rem; }

.icono-desplegable { font-weight: bold; font-size: 0.9rem; }
.texto-ver { color: #0086c0; }
.texto-ocultar { color: #d32f2f; }

/* CONTENIDO INTERIOR DEL DESPLEGABLE */
.contenido-acordeon { 
  border-top: 1px solid #eee; 
  background-color: #fafbfc;
}

.grid-contenido-instrumento { 
  display: grid; 
  grid-template-columns: 1fr 1fr; /* Mitad Wiki, mitad Reserva */
  gap: 30px; 
  padding: 30px;
}

.titulo-bloque { color: #012169; font-size: 1.1rem; border-bottom: 2px solid #8cc63f; padding-bottom: 8px; margin-top: 0; margin-bottom: 20px; }

/* TEXTOS WIKI */
.texto-wiki { color: #444; line-height: 1.6; font-size: 0.95rem; margin-bottom: 20px; }
.enlace-wiki { display: inline-block; color: #0086c0; text-decoration: none; font-weight: bold; font-size: 0.9rem; }
.enlace-wiki:hover { text-decoration: underline; }

/* FORMULARIO Y CALENDARIOS */
.formulario-reserva { display: flex; flex-direction: column; gap: 15px; }
.fila-fechas { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
.grupo-input { display: flex; flex-direction: column; gap: 6px; }
.grupo-input label { font-size: 0.85rem; font-weight: bold; color: #555; }

/* El truco para el calendario: usar font-family inherit para que se vea moderno */
.input-form { padding: 10px; border: 1px solid #ccc; border-radius: 6px; font-family: inherit; font-size: 0.95rem; color: #333; }
.input-form:focus { outline: none; border-color: #0086c0; box-shadow: 0 0 0 2px rgba(0, 134, 192, 0.2); }

.btn-reservar { background-color: #0086c0; color: white; padding: 12px; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; transition: background 0.2s; margin-top: 10px; }
.btn-reservar:hover { background-color: #006b99; }

/* ADAPTACIÓN A PANTALLAS PEQUEÑAS */
@media (max-width: 768px) { 
  .grid-contenido-instrumento { grid-template-columns: 1fr; } /* Pone el calendario debajo de la info de la wiki en móviles */
  .cabecera-acordeon { flex-direction: column; align-items: flex-start; gap: 15px; }
}
</style>