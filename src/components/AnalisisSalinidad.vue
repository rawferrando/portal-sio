<script setup>
import { ref } from 'vue'

const emit = defineEmits(['cambiar-pagina'])

const numMuestras = ref('')
const proyecto = ref('')

const enviarSolicitud = () => {
  if (numMuestras.value === '' || proyecto.value.trim() === '') {
    alert('Por favor, rellena todos los campos.')
    return
  }
  const destinatario = "sio.icm@icm.csic.es"
  const asunto = encodeURIComponent(`Solicitud de Análisis de Salinidad - ${proyecto.value}`)
  const cuerpo = encodeURIComponent(
    `Hola equipo del SIO,\n\nMe gustaría solicitar la lectura de muestras de salinidad.\n\n` +
    `📁 PROYECTO/CAMPAÑA: ${proyecto.value}\n🧪 NÚMERO DE MUESTRAS: ${numMuestras.value}\n\n` +
    `Quedo a la espera para coordinar la entrega.\n\nUn saludo.`
  )
  window.location.href = `mailto:${destinatario}?subject=${asunto}&body=${cuerpo}`
}
</script>

<template>
  <div class="pagina-detalle">
    <div class="hero-detalle hero-salinidad">
      <div class="contenedor-ancho contenido-hero">
        <h1 class="titulo-hero">Análisis de Salinidad</h1>
        <p class="subtitulo-hero">Determinación precisa de salinidad en muestras de agua de mar mediante salinómetro.</p>
      </div>
    </div>

    <div class="contenedor-ancho seccion-principal">
      <div class="grid-dos-columnas">
        <div class="columna-ficha">
          <h2 class="titulo-seccion-pequeno">Ficha Técnica</h2>
          <div class="bloque-info">
            <h3>Descripción General</h3>
            <p>El SIO ofrece el servicio de análisis de salinidad para muestras obtenidas en campañas oceanográficas. Utilizamos equipos de alta precisión calibrados con Standard Seawater.</p>
          </div>
          <div class="bloque-info">
            <h3>Protocolo de Muestreo</h3>
            <ul class="lista-especificaciones">
              <li><strong>Envases:</strong> Botellas de cristal específicas con tapón e inserto.</li>
              <li><strong>Llenado:</strong> Enjuagar 3 veces y llenar hasta el hombro.</li>
              <li><strong>Aclimatación:</strong> Depositar en el laboratorio 24h antes.</li>
            </ul>
          </div>
        </div>

        <div class="columna-reserva">
          <div class="tarjeta-reserva">
            <div class="cabecera-reserva">
              <h2>Solicitud de Análisis</h2>
              <span class="badge-operativa">OPERATIVA</span>
            </div>
            <div class="paso-reserva">
              <p><strong>Notificación de entrega</strong></p>
              <form @submit.prevent="enviarSolicitud" class="formulario-tanques mt-4">
                <div class="grupo-input">
                  <label>Nombre del Proyecto / Campaña:</label>
                  <input type="text" v-model="proyecto" class="input-form" required>
                </div>
                <div class="grupo-input mt-3">
                  <label>Número de muestras a leer:</label>
                  <input type="number" v-model="numMuestras" class="input-form" required>
                </div>
                <button type="submit" class="btn-enviar mt-4">AVISAR AL SIO</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pagina-detalle { background-color: #f4f7f9; min-height: 100vh; padding-bottom: 80px; }
.hero-detalle { background-color: #012169; padding: 120px 0 60px 0; color: white; }
.contenido-hero { position: relative; display: flex; flex-direction: column; align-items: flex-start; }
.titulo-hero { font-size: 3rem; font-weight: bold; margin: 0 0 15px 0; position: relative; display: inline-block; padding-bottom: 10px; }
.titulo-hero::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 5px; background-color: #8cc63f; }
.subtitulo-hero { font-size: 1.15rem; color: #e0e6ed; max-width: 800px; margin: 0; }
.seccion-principal { margin-top: 40px; }
.grid-dos-columnas { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
.columna-ficha { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.05); height: fit-content; }
.titulo-seccion-pequeno { color: #012169; font-size: 1.8rem; border-bottom: 2px solid #0086c0; padding-bottom: 10px; margin-bottom: 30px; margin-top: 0; }
.bloque-info { margin-bottom: 30px; }
.bloque-info h3 { color: #0086c0; font-size: 1.2rem; margin-bottom: 15px; }
.bloque-info p { color: #444; line-height: 1.6; }
.lista-especificaciones { list-style-type: none; padding: 0; }
.lista-especificaciones li { margin-bottom: 12px; color: #444; padding-left: 15px; position: relative; }
.lista-especificaciones li::before { content: '•'; color: #0086c0; font-weight: bold; position: absolute; left: 0; }
.tarjeta-reserva { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.05); }
.cabecera-reserva { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; padding-bottom: 15px; margin-bottom: 25px; }
.cabecera-reserva h2 { color: #012169; font-size: 1.5rem; margin: 0; }
.badge-operativa { background-color: #e6f4ea; color: #1e8e3e; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: bold; border: 1px solid #1e8e3e; }
.formulario-tanques { border-top: 2px dashed #eee; padding-top: 25px; }
.grupo-input { display: flex; flex-direction: column; gap: 8px; }
.grupo-input label { font-size: 0.95rem; font-weight: bold; color: #012169; }
.input-form { padding: 12px; border: 1px solid #ccc; border-radius: 6px; }
.btn-enviar { background-color: #0086c0; color: white; padding: 14px; border: none; border-radius: 6px; font-weight: bold; width: 100%; cursor: pointer; }
@media (max-width: 900px) { .grid-dos-columnas { grid-template-columns: 1fr; } }
</style>