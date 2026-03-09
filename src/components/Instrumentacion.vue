<template>
  <div class="seccion-tecnica">
    <button class="btn-volver" @click="$emit('volver')">⬅ Volver al Inicio</button>
    
    <header class="cabecera-instrumentos">
      <h1>Catálogo de Instrumentación Científica</h1>
      <p>Equipamiento de alta precisión gestionado por el SIO para campañas oceanográficas.</p>
    </header>

    <div class="lista-equipos">
      <div class="equipo-item">
        <h3>Sondas CTD (SBE 911plus)</h3>
        <p>Perfilador vertical de conductividad, temperatura y presión. El estándar de oro para la oceanografía física.</p>
        <span class="estado">Disponible</span>
      </div>

      <div class="equipo-item">
        <h3>Salinómetro Autosal 8400B</h3>
        <p>Medición de salinidad en muestras de agua con precisión de laboratorio de referencia.</p>
        <span class="estado">En mantenimiento</span>
      </div>
      
      <div class="equipo-item">
        <h3>Sonda CastAway CTD</h3>
        <p>Equipo portátil para perfiles rápidos de hasta 100 metros con GPS integrado.</p>
        <span class="estado">Disponible</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.seccion-tecnica {
  max-width: 1000px;
  margin: 0 auto;
}

.btn-volver {
  background: none;
  border: 1px solid #005596;
  color: #005596;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 2rem;
  transition: all 0.3s;
}

.btn-volver:hover {
  background: #005596;
  color: white;
}

.cabecera-instrumentos h1 {
  color: #005596;
  border-bottom: 2px solid #eee;
  padding-bottom: 1rem;
}

.lista-equipos {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-top: 2rem;
}

.equipo-item {
  padding: 1.5rem;
  background: #fdfdfd;
  border-left: 5px solid #005596;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.equipo-item h3 {
  margin: 0 0 0.5rem 0;
  color: #333;
}

.estado {
  display: inline-block;
  margin-top: 1rem;
  font-size: 0.8rem;
  font-weight: bold;
  text-transform: uppercase;
  color: #005596;
}
</style>