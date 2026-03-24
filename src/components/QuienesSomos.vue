<template>
  <div class="portada-sio">
    <div class="hero-section">
      <div class="hero-container">
        <div class="hero-logo-box">
          <img src="../assets/logo-sio.jpg" alt="Logo SIO" class="logo-hero" />
        </div>
        <div class="hero-text-box">
          <p class="resumen-sio">
            <span class="highlight-white">Soporte tecnológico integral para la investigación marina:</span><br>
            Como equipo integrante del ICM-CSIC, el Servicio de Ingeniería Oceanográfica aporta experiencia técnica, soporte logístico e I+D+I en todas las fases de la investigación científica. 
            Nos encargamos del diseño, preparación e instalación de fondeos instrumentados, la gestión de un catálogo avanzado de instrumentación oceanográfica y el soporte operativo con embarcación propia. 
            Trabajamos de forma colaborativa para maximizar la calidad de los resultados y asegurar el éxito de cada proyecto en el medio marino.
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
          <p>Catálogo de equipos, embarcaciones y gestión de reservas.</p>
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
.hero-section { 
  background-color: #005596; 
  padding: 15px 25px; /* Ajustado el padding lateral */
  border-radius: 8px; 
  margin-bottom: 40px; 
}

.hero-container {
  max-width: 1200px;
  margin: 0; /* Logo y texto alineados a la izquierda del recuadro */
  display: flex;
  align-items: center;
  gap: 30px;
}

.hero-logo-box {
  flex: 0 0 280px; /* Logo ligeramente más compacto para ganar espacio */
}

.logo-hero { 
  width: 100%;
  height: auto; 
  border-radius: 2px;
  display: block;
}

.hero-text-box {
  flex: 0;
}

.resumen-sio {
  color: white;
  font-size: 1.05rem;
  line-height: 1.4;
  text-align: justify; /* Texto sigue justificado */
  margin: 0;
}

.highlight-white {
  display: inline-block;
  color: #ffffff;
  font-weight: bold;
  font-size: 1.2rem;
  margin-bottom: 5px;
  text-align: left;
  width: 100%;
}

.destacado-bold {
  font-weight: bold;
  color: #ffffff;
}

.grid-servicios-tres { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; }

.tarjeta-sio { 
  position: relative; 
  border-radius: 12px; 
  overflow: hidden; 
  background-size: cover; 
  background-position: center; 
  min-height: 360px; 
  transition: transform 0.3s ease;
  border: 1px solid #ddd;
}
.tarjeta-sio:hover { transform: translateY(-8px); }

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

@media (max-width: 950px) {
  .hero-container { flex-direction: column; text-align: center; margin: 0 auto; }
  .resumen-sio { text-align: center; }
  .grid-servicios-tres { grid-template-columns: 1fr; }
}
</style>