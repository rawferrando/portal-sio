<template>
  <div class="portada-sio">
    <div class="hero-section">
      <div class="hero-container">
        <div class="hero-logo-box">
          <img src="../assets/logo-sio.jpg" alt="Logo SIO" class="logo-hero" />
        </div>
        <div class="hero-text-box">
          <p class="resumen-sio">
            <strong>Soporte tecnológico integral para la investigación marina:</strong> 
            gestión de instrumentación científica avanzada, diseño y despliegue de fondeos, 
            apoyo técnico especializado en campañas y servicios de logística con embarcación propia. 
            Aportamos innovación y experiencia para maximizar la calidad de tus resultados científicos.
          </p>
        </div>
      </div>
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
/* HERO SECTION: DISTRIBUCIÓN HORIZONTAL */
.hero-section { 
  background-color: #005596; 
  padding: 40px; 
  border-radius: 8px; 
  margin-bottom: 40px; 
}

.hero-container {
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  gap: 40px; /* Espacio entre logo y texto */
}

.hero-logo-box {
  flex: 0 0 350px; /* Ancho fijo para el logo */
}

.logo-hero { 
  width: 100%;
  height: auto; 
  border-radius: 4px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.hero-text-box {
  flex: 1; /* El texto ocupa el resto del espacio */
}

.resumen-sio {
  color: white;
  font-size: 1.15rem;
  line-height: 1.6;
  text-align: left; /* Justificado a la izquierda como pediste */
  margin: 0;
}

.resumen-sio strong {
  display: block;
  font-size: 1.3rem;
  margin-bottom: 10px;
  color: #b0dfff; /* Un tono celeste para destacar el título */
}

/* GRID DE 3 FICHAS */
.grid-servicios-tres { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; }

.tarjeta-sio { 
  position: relative; 
  border-radius: 12px; 
  overflow: hidden; 
  background-size: cover; 
  background-position: center; 
  min-height: 380px; 
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

/* Responsive para tablets y móviles */
@media (max-width: 900px) {
  .hero-container { flex-direction: column; text-align: center; }
  .resumen-sio { text-align: center; }
  .grid-servicios-tres { grid-template-columns: 1fr; }
  .hero-logo-box { flex: 0 0 auto; max-width: 250px; }
}
</style>