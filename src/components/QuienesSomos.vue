<template>
  <div class="portada-sio">
    <div class="hero-section">
      <h1>Servicio de Ingeniería Oceanográfica</h1>
      <p>Apoyo tecnológico e instrumentación de vanguardia para la investigación marina.</p>
    </div>

    <div class="grid-servicios-tres">
      
      <div class="tarjeta-sio bg-proyectos">
        <div class="overlay-tarjeta">
          <h3>Proyectos</h3>
          <p>Apoyo técnico especializado en campañas nacionales e internacionales.</p>
        </div>
      </div>

      <div class="tarjeta-sio bg-instrumentacion-activa" @click="$emit('cambiar-pagina')">
        <div class="overlay-tarjeta">
          <h3>Instrumentación-embarcación</h3>
          <p>Consulta nuestro catálogo de equipos, embarcaciones y gestiona tus reservas.</p>
          <span class="btn-ver-mas">Entrar al Catálogo ➔</span>
        </div>
      </div>

      <div class="tarjeta-sio bg-idi">
        <div class="overlay-tarjeta">
          <h3>Desarrollo I+D+I</h3>
          <p>Diseño de soluciones de ingeniería personalizadas y nuevos sensores.</p>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.hero-section { background-color: #005596; color: white; padding: 50px 20px; text-align: center; border-radius: 8px; margin-bottom: 40px; }
.hero-section h1 { margin: 0; font-size: 2.4rem; }
.hero-section p { opacity: 0.9; font-size: 1.1rem; margin-top: 10px; }

.grid-servicios-tres { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; min-height: 400px; }

.tarjeta-sio { 
  position: relative; 
  border-radius: 12px; 
  overflow: hidden; 
  background-size: cover; 
  background-position: center; 
  min-height: 350px; 
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid #ddd;
}

.tarjeta-sio:hover { transform: translateY(-10px); box-shadow: 0 12px 25px rgba(0,0,0,0.2); }

.bg-proyectos { background-image: url('../assets/proyectos.jpg'); background-color: #e3f2fd; }
.bg-instrumentacion-activa { background-image: url('../assets/instrumentacion.jpg'); background-color: #bbdefb; cursor: pointer; border: 2px solid #005596; }
.bg-idi { background-image: url('../assets/idi.jpg'); background-color: #e1f5fe; }

.overlay-tarjeta { 
  position: absolute; 
  bottom: 0; left: 0; right: 0; 
  background: linear-gradient(transparent, rgba(0,85,150,0.9)); 
  padding: 30px 20px; 
  color: white; 
}

.overlay-tarjeta h3 { margin: 0 0 10px 0; font-size: 1.6rem; }
.overlay-tarjeta p { margin: 0; font-size: 1rem; line-height: 1.4; opacity: 0.95; }
.btn-ver-mas { display: inline-block; margin-top: 15px; font-weight: bold; text-transform: uppercase; font-size: 0.85rem; }

/* Adaptable a móviles */
@media (max-width: 900px) {
  .grid-servicios-tres { grid-template-columns: 1fr; }
  .tarjeta-sio { min-height: 250px; }
}
</style>