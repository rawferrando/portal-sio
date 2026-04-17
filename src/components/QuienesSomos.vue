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
            Como equipo integrante del <span class="destacado-bold">Institut de Ciències del Mar (ICM-CSIC)</span>, el Servicio de Ingeniería Oceanográfica aporta experiencia técnica, soporte logístico e <span class="destacado-bold">I+D+I</span> en todas las fases de la investigación científica. 
            Nos encargamos del diseño, preparación e instalación de fondeos instrumentados, la gestión de un catálogo avanzado de instrumentación oceanográfica y el soporte operativo con embarcación propia. 
            Trabajamos de forma colaborativa para maximizar la calidad de los resultados y asegurar el éxito de cada proyecto en el medio marino.
          </p>
        </div> 
      </div> 
    </div> 
    
    <div class="grid-servicios-tres">
      
      <div 
        class="tarjeta-sio bg-proyectos" 
        style="background-image: url('../assets/proyectos.jpg'); cursor: pointer;"
        @click="$emit('cambiar-pagina', 'proyectos')"
      >
        <div class="overlay-tarjeta">
          <h3>Proyectos</h3>
          <p>Soporte técnico y logístico para campañas de investigación en el medio marino.</p>
          <span class="btn-ver-mas">Ver Campañas ➔</span>
        </div>
      </div>

      <div 
        class="tarjeta-sio bg-instrumentacion-activa" 
        style="background-image: url('../assets/instrumentacion.jpg'); cursor: pointer;" 
        @click="$emit('cambiar-pagina', 'instrumentacion')"
      >
        <div class="overlay-tarjeta">
          <h3>Instrumentación-embarcación</h3>
          <p>Accede al catálogo completo de equipos, consulta disponibilidad de la lancha y reserva.</p>
          <span class="btn-ver-mas">Entrar al Catálogo ➔</span>
        </div>
      </div>

      <div 
        class="tarjeta-sio bg-idi" 
        style="background-image: url('../assets/idi.jpg'); cursor: pointer;" 
        @click="$emit('cambiar-pagina', 'idi')"
      >
        <div class="overlay-tarjeta">
          <h3>Desarrollo I+D+I</h3>
          <p>Innovación tecnológica, diseño de prototipos y soluciones de ingeniería a medida.</p>
          <span class="btn-ver-mas">Conoce más ➔</span>
        </div>
      </div>

    </div> 
  </div> 
</template>

<style scoped>
/* Respetamos tu grid inteligente para que no se rompa en móviles */
.grid-servicios-tres { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
  gap: 20px; 
  margin-top: 30px;
}

/* El resto de tus estilos de tarjeta (asumiendo que los tienes en un CSS general o aquí) */
.tarjeta-sio { 
  position: relative; 
  height: 250px; 
  border-radius: 10px; 
  overflow: hidden; 
  background-size: cover; 
  background-position: center; 
  box-shadow: 0 4px 8px rgba(0,0,0,0.15); 
  transition: transform 0.3s; 
}
.tarjeta-sio:hover { transform: translateY(-5px); }

.overlay-tarjeta { 
  position: absolute; bottom: 0; left: 0; width: 100%; 
  padding: 20px; background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0)); 
  color: white; box-sizing: border-box; 
}
.overlay-tarjeta h3 { margin: 0 0 10px 0; font-size: 1.4rem; text-shadow: 1px 1px 3px rgba(0,0,0,0.8); }
.overlay-tarjeta p { margin: 0 0 10px 0; font-size: 0.95rem; opacity: 0.9; }
.btn-ver-mas { display: inline-block; font-size: 0.85rem; font-weight: bold; color: #ffcc00; text-transform: uppercase; }
</style>