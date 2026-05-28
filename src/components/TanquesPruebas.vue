<script setup>
import { ref } from 'vue'

const emit = defineEmits(['cambiar-pagina'])

// --- LÓGICA DEL CALENDARIO INTERACTIVO (6 MESES VISTA) ---
const meses = [
  'Mayo 2026', 'Junio 2026', 'Julio 2026', 'Agosto 2026',
  'Septiembre 2026', 'Octubre 2026', 'Noviembre 2026'
]

// Variable que recuerda en qué mes estamos mirando (Empieza en Mayo)
const mesActualIndex = ref(0)

const mesAnterior = () => {
  if (mesActualIndex.value > 0) mesActualIndex.value--
}

const mesSiguiente = () => {
  if (mesActualIndex.value < meses.length - 1) mesActualIndex.value++
}

// Simulador: Reparte días ocupados de forma diferente según el mes
const esOcupado = (dia, mesIndex) => {
  if (mesIndex === 0 && [12, 13, 14].includes(dia)) return true // Mayo
  if (mesIndex === 1 && [2, 5, 14, 15, 22].includes(dia)) return true // Junio
  if (mesIndex === 2 && [10, 11, 12, 28, 29].includes(dia)) return true // Julio
  if (mesIndex === 3 && [1, 2, 3, 20, 21].includes(dia)) return true // Agosto
  if (mesIndex === 4 && [15, 16, 17].includes(dia)) return true // Septiembre
  return false
}
</script>

<template>
  <div class="pagina-detalle">
    
    <!-- CABECERA HERO LIMPIA (SIN BOTÓN DE VOLVER) -->
    <div class="hero-detalle hero-tanques">
      <div class="contenedor-ancho contenido-hero">
        <h1 class="titulo-hero">Tanques de Pruebas</h1>
        <p class="subtitulo-hero">Instalaciones experimentales para ensayos controlados, calibración y biología.</p>
      </div>
    </div>

    <!-- CONTENIDO PRINCIPAL A DOS COLUMNAS -->
    <div class="contenedor-ancho seccion-principal">
      <div class="grid-dos-columnas">
        
        <!-- COLUMNA IZQUIERDA: FICHA TÉCNICA -->
        <div class="columna-ficha">
          <h2 class="titulo-seccion-pequeno">Ficha Técnica</h2>
          
          <div class="bloque-info">
            <h3>Descripción General</h3>
            <p>El SIO dispone de tanques de pruebas de alta capacidad diseñados para la calibración de sensores, ensayos de fatiga de materiales y simulaciones de condiciones marinas controladas.</p>
          </div>

          <div class="bloque-info">
            <h3>Especificaciones Principales</h3>
            <ul class="lista-especificaciones">
              <li><strong>Volumen total:</strong> [Añadir litros/m3]</li>
              <li><strong>Control de Temperatura:</strong> Rango de [X] °C a [Y] °C</li>
              <li><strong>Control de Salinidad:</strong> Sistema automatizado</li>
              <li><strong>Iluminación:</strong> Espectro regulable para fotosíntesis</li>
              <li><strong>Filtración:</strong> Filtros UV y biológicos integrados</li>
            </ul>
          </div>
        </div>

        <!-- COLUMNA DERECHA: RESERVAS Y DESCARGAS ACTUALIZADAS -->
        <div class="columna-reserva">
          <div class="tarjeta-reserva">
            <div class="cabecera-reserva">
              <h2>Solicitud de Uso</h2>
              <span class="badge-operativa">OPERATIVA</span>
            </div>
            
            <div class="paso-reserva">
              <p><strong>Paso 1: Prepara tu solicitud</strong></p>
              <p class="texto-explicativo">Descarga y rellena el documento de solicitud. En él deberás indicarnos:</p>
              <ul class="lista-requisitos">
                <li>Para qué vas a utilizar los tanques (propósito de las pruebas).</li>
                <li>Si vas a necesitar hacer uso de la grúa de carga.</li>
              </ul>
              
              <div class="caja-descarga mt-2">
                <span class="icono-doc">📄 Documento_Solicitud_SIO.docx</span>
                <a href="#" class="btn-descarga">⬇ Descargar Documento</a>
              </div>

              <!-- AVISO SIO PARA USUARIOS NUEVOS -->
              <div class="alerta-info mt-3">
                <strong>ℹ️ ¿No los has utilizado nunca?</strong><br>
                No te preocupes. Si es tu primera vez, el primer día uno de los integrantes del equipo del SIO te explicará al detalle cómo funciona todo.
              </div>
            </div>

            <div class="paso-reserva mt-4">
              <p><strong>Paso 2: Consulta la disponibilidad</strong></p>
              
              <div class="calendario-placeholder">
                <!-- CABECERA DEL CALENDARIO INTERACTIVO -->
                <div class="cabecera-mes">
                  <button class="btn-mes" @click="mesAnterior" :class="{ 'oculto': mesActualIndex === 0 }">❮</button>
                  <span class="mes-actual">{{ meses[mesActualIndex] }}</span>
                  <button class="btn-mes" @click="mesSiguiente" :class="{ 'oculto': mesActualIndex === meses.length - 1 }">❯</button>
                </div>

                <!-- BUCLE DE DÍAS -->
                <div class="grid-calendario">
                   <div v-for="dia in 30" :key="dia" class="dia" :class="{ 'ocupado': esOcupado(dia, mesActualIndex) }">
                     {{ dia }}
                   </div>
                </div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped>
.pagina-detalle { background-color: #f4f7f9; min-height: 100vh; padding-bottom: 80px; }

/* HERO LIMPIO */
.hero-detalle { background-color: #012169; padding: 120px 0 60px 0; color: white; }
.contenido-hero { position: relative; display: flex; flex-direction: column; align-items: flex-start; }
.titulo-hero { font-size: 3rem; font-weight: bold; margin: 0 0 15px 0; position: relative; display: inline-block; padding-bottom: 10px; }
.titulo-hero::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 5px; background-color: #8cc63f; }
.subtitulo-hero { font-size: 1.15rem; color: #e0e6ed; max-width: 800px; margin: 0; }

.seccion-principal { margin-top: 40px; }
.grid-dos-columnas { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }

.columna-ficha { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.05); }
.titulo-seccion-pequeno { color: #012169; font-size: 1.8rem; border-bottom: 2px solid #0086c0; padding-bottom: 10px; margin-bottom: 30px; margin-top: 0; }
.bloque-info { margin-bottom: 30px; }
.bloque-info h3 { color: #0086c0; font-size: 1.2rem; margin-bottom: 15px; }
.bloque-info p { color: #444; line-height: 1.6; }
.lista-especificaciones { list-style-type: none; padding: 0; }
.lista-especificaciones li { margin-bottom: 12px; color: #444; line-height: 1.5; padding-left: 15px; position: relative; }
.lista-especificaciones li::before { content: '•'; color: #0086c0; font-weight: bold; position: absolute; left: 0; }

.tarjeta-reserva { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.05); }
.cabecera-reserva { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; padding-bottom: 15px; margin-bottom: 25px; }
.cabecera-reserva h2 { color: #012169; font-size: 1.5rem; margin: 0; }
.badge-operativa { background-color: #e6f4ea; color: #1e8e3e; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: bold; border: 1px solid #1e8e3e; }

.paso-reserva p { color: #444; margin-bottom: 15px; }
.texto-explicativo { color: #555; font-size: 0.95rem; margin-bottom: 10px; }
.lista-requisitos { margin-top: 0; margin-bottom: 15px; padding-left: 20px; color: #444; font-size: 0.95rem; }
.lista-requisitos li { margin-bottom: 5px; }

.alerta-info { background-color: #e8f4fd; border-left: 4px solid #0086c0; padding: 15px; border-radius: 4px; font-size: 0.9rem; color: #012169; line-height: 1.5; }

.mt-2 { margin-top: 15px; }
.mt-3 { margin-top: 20px; }
.mt-4 { margin-top: 30px; }

.caja-descarga { background-color: #f8f9fa; border: 1px dashed #ccc; padding: 20px; border-radius: 8px; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 10px; }
.btn-descarga { background-color: #0086c0; color: white; text-decoration: none; padding: 10px 20px; border-radius: 4px; font-weight: bold; transition: background 0.3s; }
.btn-descarga:hover { background-color: #012169; }

/* ESTILOS DEL CALENDARIO INTERACTIVO */
.cabecera-mes { display: flex; justify-content: space-between; align-items: center; background-color: #012169; color: white; padding: 10px 15px; border-radius: 8px 8px 0 0; }
.mes-actual { font-weight: bold; font-size: 1.1rem; }
.btn-mes { background: transparent; border: none; color: white; font-size: 1.2rem; cursor: pointer; transition: transform 0.2s; }
.btn-mes:hover { transform: scale(1.2); }
.oculto { visibility: hidden; }

.grid-calendario { display: grid; grid-template-columns: repeat(7, 1fr); gap: 5px; text-align: center; padding: 10px; background: #fbfbfb; border: 1px solid #eee; border-top: none; border-radius: 0 0 8px 8px; }
.dia { background: #f4f7f9; padding: 10px 0; border-radius: 4px; color: #555; font-size: 0.9rem; transition: all 0.3s; }
.dia.ocupado { background: #ffebee; color: #d32f2f; font-weight: bold; }

@media (max-width: 900px) { .grid-dos-columnas { grid-template-columns: 1fr; } }
</style>