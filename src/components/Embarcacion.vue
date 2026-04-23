<template>
  <div class="seccion-tecnica">
    <button class="btn-volver" @click="$emit('volver')">⬅ Volver al Inicio</button>
    
    <header class="cabecera-seccion">
      <h1>Embarcación SIO: "Nereis"</h1>
      <p class="intro">Nuestra unidad de apoyo costero basada en el Port Olímpic de Barcelona.</p>
    </header>

    <div class="grid-detalles">
      <div class="ficha-tecnica">
        <h3>📊 Especificaciones</h3>
        <ul>
          <li><strong>Eslora:</strong> 7,5 metros</li>
          <li><strong>Motorización:</strong> 200 HP fueraborda</li>
          <li><strong>Capacidad:</strong> 6 personas (incluyendo patrón)</li>
          <li><strong>Equipamiento:</strong> Grúa para despliegue de instrumentos, GPS diferencial y sonda.</li>
        </ul>
      </div>

      <div class="servicios-mar">
        <h3>🌊 Operaciones Habituales</h3>
        <p>Realizamos despliegues de fondeos, mantenimiento de boyas, muestreos de agua y sedimentos, y apoyo a buceo científico.</p>
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
.cabecera-seccion h1 { color: #005596; border-bottom: 2px solid #eee; padding-bottom: 1rem; }
.grid-detalles { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 2rem; }
.ficha-tecnica, .servicios-mar { padding: 1.5rem; background: #f8f9fa; border-left: 5px solid #005596; border-radius: 4px; }
ul { list-style: none; padding: 0; }
li { margin-bottom: 0.8rem; color: #444; border-bottom: 1px solid #eee; padding-bottom: 0.4rem; }
h3 { color: #005596; margin-top: 0; }
</style>