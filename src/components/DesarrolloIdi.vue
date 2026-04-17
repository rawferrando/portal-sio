<template>
  <div class="pagina-seccion fade-in">
    <div class="cabecera-seccion">
      <button @click="$emit('volver')" class="btn-volver">⬅ Volver al Inicio</button>
      <h2>💡 Desarrollo I+D+i</h2>
      <p>Diseño e integración de soluciones tecnológicas a medida para la observación marina.</p>
    </div>

    <div class="contenido-idi">
      <div class="grid-idi">
        <div class="tarjeta-idi">
          <h3>Ingeniería de Prototipos</h3>
          <p>Diseño y fabricación de piezas técnicas y carcasas resistentes a la presión y corrosión marina.</p>
        </div>
        <div class="tarjeta-idi">
          <h3>Integración de Sensores</h3>
          <p>Adaptación de instrumentación oceanográfica en plataformas autónomas y dataloggers propios.</p>
        </div>
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

.grid-idi { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; clear: both; margin-top: 60px; }
.tarjeta-idi { background-color: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid #00aae4; }
.tarjeta-idi h3 { color: #005596; margin-top: 0; }

.fade-in { animation: fadeIn 0.4s ease-in-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
</style>