<template>
  <div class="seccion-tecnica">
    <button class="btn-volver" @click="$emit('volver')">⬅ Volver</button>
    <h1>Diseño e Instalación de Fondeos</h1>
    <div class="contenido-diseno">
      <div class="info-bloque">
        <h3>📐 Ingeniería de Fondeos</h3>
        <p>Diseñamos líneas de fondeo adaptadas a profundidades de hasta 2000 metros, calculando tensiones y flotabilidades.</p>
      </div>
      <div class="info-bloque">
        <h3>🛠 Sistemas a medida</h3>
        <p>Desarrollo de estructuras para sensores específicos, protección contra biofouling y sistemas de recuperación mediante disparadores acústicos.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.seccion-tecnica { max-width: 900px; margin: 0 auto; padding: 20px; }
.btn-volver { border: 1px solid #005596; color: #005596; background: white; padding: 5px 15px; cursor: pointer; margin-bottom: 20px; }
.info-bloque { margin-top: 20px; padding: 15px; background: white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
h1 { color: #005596; }
h3 { color: #004080; margin-top: 0; }
</style>