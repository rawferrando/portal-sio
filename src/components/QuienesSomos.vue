<script setup>
const emit = defineEmits(['ir-a-instrumentacion'])
</script>

<template>
  <div class="portada-sio">
    <div class="hero-section">
      <div class="hero-texto">
        <h1>Servicio de Ingeniería Oceanográfica</h1>
        <p>Instituto de Ciencias del Mar (ICM-CSIC)</p>
      </div>
    </div>

    <h2 class="titulo-seccion">Nuestras Áreas de Servicio</h2>
    <div class="grid-servicios">
      
      <div class="tarjeta-servicio destacada" @click="$emit('ir-a-instrumentacion')">
        <div class="imagen-tarjeta bg-instrumentacion"></div>
        <div class="contenido-tarjeta">
          <h3>📊 Instrumentación Oceanográfica</h3>
          <p>Catálogo de sensores, CTDs, rosetas y perfiladores. Accede a las fichas técnicas, WIKISIO y gestiona tus reservas.</p>
        </div>
      </div>

      <div class="tarjeta-servicio">
        <div class="imagen-tarjeta bg-vehiculos"></div>
        <div class="contenido-tarjeta">
          <h3>🚁 Vehículos Autónomos</h3>
          <p>Operación de plataformas no tripuladas (UAS, USV, ROVs).</p>
        </div>
      </div>

      <div class="tarjeta-servicio">
        <div class="imagen-tarjeta bg-laboratorio"></div>
        <div class="contenido-tarjeta">
          <h3>🔬 Laboratorios y Calibración</h3>
          <p>Instalaciones para el análisis de muestras y salinometría.</p>
        </div>
      </div>

      <div class="tarjeta-servicio">
        <div class="imagen-tarjeta bg-tanques"></div>
        <div class="contenido-tarjeta">
          <h3>🌊 Zona de Acuarios y Tanques</h3>
          <p>Mantenimiento de sistemas de experimentación in vivo.</p>
        </div>
      </div>

      <div class="tarjeta-servicio">
        <div class="imagen-tarjeta bg-mecatronica"></div>
        <div class="contenido-tarjeta">
          <h3>⚙️ Taller de Mecatrónica</h3>
          <p>Diseño CAD, impresión 3D y reparación electromecánica.</p>
        </div>
      </div>

      <div class="tarjeta-servicio">
        <div class="imagen-tarjeta bg-logistica"></div>
        <div class="contenido-tarjeta">
          <h3>📦 Logística de Campañas</h3>
          <p>Preparación, embalaje y envío de material científico.</p>
        </div>
      </div>

      <div class="tarjeta-servicio">
        <div class="imagen-tarjeta bg-fondeos"></div>
        <div class="contenido-tarjeta">
          <h3>⚓ Fondeos y Boyas</h3>
          <p>Diseño y despliegue de líneas de fondeo oceanográfico.</p>
        </div>
      </div>

      <div class="tarjeta-servicio">
        <div class="imagen-tarjeta bg-datos"></div>
        <div class="contenido-tarjeta">
          <h3>💻 Telemetría y Datos</h3>
          <p>Sistemas de adquisición de datos en tiempo real.</p>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.portada-sio { animation: fadeIn 0.4s ease; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
.hero-section { background-color: #005596; color: white; padding: 40px 20px; border-radius: 8px; text-align: center; margin-bottom: 40px; }
.hero-texto h1 { margin: 0 0 10px 0; font-size: 2.2rem; }
.hero-texto p { margin: 0; font-size: 1.1rem; opacity: 0.9; }
.titulo-seccion { color: #005596; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-bottom: 30px; font-size: 1.6rem; }
.grid-servicios { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
.tarjeta-servicio { background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: transform 0.2s; display: flex; flex-direction: column; }
.tarjeta-servicio:hover { transform: translateY(-5px); box-shadow: 0 8px 15px rgba(0,0,0,0.1); }
.tarjeta-servicio.destacada { cursor: pointer; border: 2px solid #005596; }
.imagen-tarjeta { height: 140px; background-color: #e2eef7; }
.contenido-tarjeta { padding: 20px; flex: 1; }
.contenido-tarjeta h3 { margin: 0 0 10px 0; color: #005596; font-size: 1.1rem; }
.contenido-tarjeta p { margin: 0; color: #555; font-size: 0.9rem; line-height: 1.5; }
.bg-instrumentacion { background-color: #a0c4ff; }
.bg-vehiculos { background-color: #bdb2ff; }
.bg-laboratorio { background-color: #ffc6ff; }
.bg-tanques { background-color: #9bf6ff; }
.bg-mecatronica { background-color: #ffadad; }
.bg-logistica { background-color: #ffd6a5; }
.bg-fondeos { background-color: #fdffb6; }
.bg-datos { background-color: #caffbf; }
</style>