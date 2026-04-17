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
          </p>
        </div> 
      </div> 
    </div> 
    
    <div class="grid-servicios-tres">
      <div class="tarjeta-sio bg-proyectos" style="cursor: pointer;" @click="$emit('cambiar-pagina', 'proyectos')">
        <div class="overlay-tarjeta">
          <h3>Proyectos</h3>
          <p>Soporte técnico y logístico para campañas de investigación.</p>
          <span class="btn-ver-mas">Ver Campañas ➔</span>
        </div>
      </div>

      <div class="tarjeta-sio bg-instrumentacion-activa" style="cursor: pointer;" @click="$emit('cambiar-pagina', 'instrumentacion')">
        <div class="overlay-tarjeta">
          <h3>Instrumentación-embarcación</h3>
          <p>Accede al catálogo completo de equipos y reserva.</p>
          <span class="btn-ver-mas">Entrar al Catálogo ➔</span>
        </div>
      </div>

      <div class="tarjeta-sio bg-idi" style="cursor: pointer;" @click="$emit('cambiar-pagina', 'idi')">
        <div class="overlay-tarjeta">
          <h3>Desarrollo I+D+I</h3>
          <p>Innovación tecnológica y prototipos a medida.</p>
          <span class="btn-ver-mas">Conoce más ➔</span>
        </div>
      </div>
    </div> 
  </div> 
</template>

<style scoped>
.portada-sio { display: flex; flex-direction: column; gap: 40px; }
.hero-section { background-color: #005596; padding: 40px 20px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
.hero-container { display: flex; align-items: center; gap: 30px; max-width: 1000px; margin: 0 auto; }
.hero-logo-box { flex: 0 0 auto; }
.logo-hero { width: 150px; border-radius: 50%; box-shadow: 0 4px 8px rgba(0,0,0,0.2); border: 4px solid white; }
.hero-text-box { flex: 1; }
.resumen-sio { font-size: 1.1rem; line-height: 1.6; color: #e6f0fa; margin: 0; }
.highlight-white { color: white; font-size: 1.3rem; font-weight: bold; display: block; margin-bottom: 10px; }
.destacado-bold { font-weight: bold; color: #ffcc00; }

.grid-servicios-tres { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
  gap: 20px; 
  margin-top: 30px;
}

.tarjeta-sio { position: relative; height: 250px; border-radius: 10px; overflow: hidden; background-size: cover; background-position: center; box-shadow: 0 4px 8px rgba(0,0,0,0.15); transition: transform 0.3s; }
.tarjeta-sio:hover { transform: translateY(-5px); }
.bg-proyectos { background-color: #007bb5; } /* Color de fondo provisional si no hay imagen */
.bg-instrumentacion-activa { background-color: #00aae4; }
.bg-idi { background-color: #005596; }

.overlay-tarjeta { position: absolute; bottom: 0; left: 0; width: 100%; padding: 20px; background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0)); color: white; box-sizing: border-box; }
.overlay-tarjeta h3 { margin: 0 0 10px 0; font-size: 1.4rem; text-shadow: 1px 1px 3px rgba(0,0,0,0.8); }
.overlay-tarjeta p { margin: 0 0 10px 0; font-size: 0.95rem; opacity: 0.9; }
.btn-ver-mas { display: inline-block; font-size: 0.85rem; font-weight: bold; color: #ffcc00; text-transform: uppercase; }

@media (max-width: 768px) {
  .hero-container { flex-direction: column; text-align: center; }
}
</style>