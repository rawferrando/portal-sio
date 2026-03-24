<template>
  <div class="portada-sio">
    <div class="hero-section">
      <img src="../assets/logo-sio.jpg" alt="Logo SIO" class="logo-hero" />
    </div>

    <div class="grid-servicios-tres">
      <div class="tarjeta-sio bg-proyectos">
        <div class="overlay-tarjeta">
          <h3>Proyectos</h3>
          <p>Soporte técnico y logístico para campañas de investigación.</p>
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
          <p>Innovación tecnológica y diseño de soluciones a medida.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* HERO AJUSTADO PARA EL LOGO */
.hero-section { 
  background-color: #005596; 
  padding: 30px 20px; 
  text-align: center; 
  border-radius: 8px; 
  margin-bottom: 40px; 
  display: flex;
  justify-content: center;
  align-items: center;
}
.logo-hero { 
  max-width: 400px; 
  height: auto; 
  filter: drop-shadow(0 0 10px rgba(0,0,0,0.2));
}

.grid-servicios-tres { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; }

.tarjeta-sio { 
  position: relative; 
  border-radius: 12px; 
  overflow: hidden; 
  background-size: cover; 
  background-position: center; 
  min-height: 350px; 
  transition: transform 0.3s ease;
  border: 1px solid #ddd;
}
.tarjeta-sio:hover { transform: translateY(-10px); }

.bg-proyectos { background-image: url('../assets/proyectos.jpg'); background-color: #e3f2fd; }
.bg-instrumentacion-activa { background-image: url('../assets/instrumentacion.jpg'); background-color: #bbdefb; cursor: pointer; border: 2px solid #005596; }
.bg-idi { background-image: url('../assets/idi.jpg'); background-color: #e1f5fe; }

.overlay-tarjeta { 
  position: absolute; 
  bottom: 0; left: 0; right: 0; 
  background: linear-gradient(transparent, rgba(0,85,150,0.95)); 
  padding: 25px 15px; 
  color: white; 
}
.overlay-tarjeta h3 { margin: 0 0 8px 0; font-size: 1.4rem; }
.overlay-tarjeta p { margin: 0; font-size: 0.95rem; line-height: 1.4; }
.btn-ver-mas { display: inline-block; margin-top: 10px; font-weight: bold; font-size: 0.8rem; }

@media (max-width: 900px) {
  .grid-servicios-tres { grid-template-columns: 1fr; }
  .logo-hero { max-width: 80%; }
}
</style>