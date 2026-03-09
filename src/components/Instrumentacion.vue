<template>
  <div class="seccion-tecnica">
    <button class="btn-volver" @click="$emit('volver')">⬅ Volver al Inicio</button>
    
    <header class="cabecera-instrumentos">
      <h1>Catálogo de Instrumentación Científica</h1>
      <p>Equipamiento de alta precisión gestionado por el SIO para campañas oceanográficas.</p>
    </header>

    <div class="lista-equipos">
      <div class="equipo-item">
        <div class="info">
          <h3>Sondas CTD (SBE 911plus)</h3>
          <p>Perfilador vertical de conductividad, temperatura y presión. El estándar de oro para la oceanografía física.</p>
        </div>
        <span class="estado disponible">Disponible</span>
      </div>

      <div class="equipo-item">
        <div class="info">
          <h3>Salinómetro Autosal 8400B</h3>
          <p>Medición de salinidad en muestras de agua con precisión de laboratorio de referencia.</p>
        </div>
        <span class="estado mantenimiento">En mantenimiento</span>
      </div>
      
      <div class="equipo-item">
        <div class="info">
          <h3>Sonda CastAway CTD</h3>
          <p>Equipo portátil para perfiles rápidos de hasta 100 metros con GPS integrado.</p>
        </div>
        <span class="estado disponible">Disponible</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.seccion-tecnica { max-width: 1000px; margin: 0 auto; padding: 2rem; }
.btn-volver { 
  background: white; border: 1px solid #005596; color: #005596; 
  padding: 0.6rem 1.2rem; border-radius: 4px; cursor: pointer; margin-bottom: 2rem;
  font-weight: bold; transition: all 0.3s;
}
.btn-volver:hover { background: #005596; color: white; }
.cabecera-instrumentos h1 { color: #005596; border-bottom: 2px solid #eee; padding-bottom: 1rem; }
.lista-equipos { display: flex; flex-direction: column; gap: 1.5rem; margin-top: 2rem; }
.equipo-item { 
  padding: 1.5rem; background: white; border-left: 6px solid #005596; 
  box-shadow: 0 4px 10px rgba(0,0,0,0.05); display: flex; justify-content: space-between; align-items: center;
}
.equipo-item h3 { margin: 0 0 0.5rem 0; color: #333; }
.equipo-item p { margin: 0; color: #666; font-size: 0.95rem; }
.estado { padding: 0.4rem 0.8rem; border-radius: 20px; font-size: 0.75rem; font-weight: bold; }
.disponible { background: #e6f4ea; color: #1e7e34; }
.mantenimiento { background: #fff3e0; color: #e65100; }
</style>