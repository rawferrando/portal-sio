<template>
  <div class="pagina-seccion fade-in">
    <div class="cabecera-seccion">
      <button @click="$emit('volver')" class="btn-volver">⬅ Volver al Inicio</button>
      <h2>📂 Proyectos y Campañas</h2>
      <p>Soporte técnico, logístico y operativo para campañas de investigación oceanográfica.</p>
    </div>

    <div class="contenido-proyectos">
      <div class="mensaje-temporal">
        <p>Estamos conectando la base de datos de proyectos...</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pagina-seccion { max-width: 1200px; margin: 0 auto; padding: 20px; }
.cabecera-seccion { margin-bottom: 40px; text-align: center; }
.cabecera-seccion h2 { color: #005596; font-size: 2.2rem; margin-bottom: 10px; }
.cabecera-seccion p { color: #555; font-size: 1.1rem; }

.btn-volver { background-color: #6c757d; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; float: left; font-weight: bold; transition: background-color 0.3s; }
.btn-volver:hover { background-color: #5a6268; }

.mensaje-temporal { text-align: center; padding: 50px; background-color: #f8f9fa; border-radius: 8px; border: 1px dashed #ccc; color: #666; clear: both; margin-top: 60px; }

.fade-in { animation: fadeIn 0.4s ease-in-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
</style>