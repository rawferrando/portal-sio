<template>
  <div class="recursos-container">
    
    <section class="seccion-recursos">
      <h2 class="titulo-sio">Recursos Técnicos</h2>
      <div class="grid-tarjetas">
        <div class="tarjeta">
          <h3>Embarcación</h3>
          <p>Servicio de embarcación en el Port Olímpic.</p>
        </div>
        <div class="tarjeta">
          <h3>Laboratorio</h3>
          <p>Espacio de prototipado y mantenimiento.</p>
        </div>
      </div>
    </section>

    <section class="seccion-recursos">
      <h2 class="titulo-sio">Instrumentación</h2>
      <div class="grid-tarjetas">
        <div class="tarjeta">
          <h3>Sondas CTD</h3>
          <p>Equipos de perfilado oceanográfico.</p>
        </div>
        <div class="tarjeta">
          <h3>Salinometría</h3>
          <p>Análisis de precisión de muestras de agua.</p>
        </div>
      </div>
    </section>

  </div>
</template>

<style scoped>
.recursos-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0.5rem 1rem; /* Reducimos el padding superior */
}
.seccion-recursos {
  margin-bottom: 1rem; /* Reducimos mucho el margen entre bloques internos */
}

.titulo-sio {
  color: #0056b3;
  font-size: 2rem; /* Cambio aplicado: Ahora todos a 2rem */
  margin-bottom: 1.5rem;
  border-bottom: 2px solid #e0e0e0;
  padding-bottom: 0.5rem;
}

.grid-tarjetas {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.tarjeta {
  background-color: #f8f9fa;
  border-left: 5px solid #0056b3;
  padding: 1.2rem;
  border-radius: 6px;
}

.tarjeta h3 {
  color: #0056b3;
  margin: 0 0 0.5rem 0;
  font-size: 1.1rem;
}
</style>