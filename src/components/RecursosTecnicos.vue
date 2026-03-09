<template>
  <div class="recursos-container">
    
    <section class="seccion-recursos">
      <h2 class="titulo-sio">2. Recursos Técnicos Destacados</h2>
      
      <div class="grid-tarjetas">
        <div class="tarjeta">
          <h3>🚢 Embarcación Propia</h3>
          <p>Ubicada en el Puerto Olímpico para despliegue y adquisición de datos en las cercanías de Barcelona.</p>
        </div>
        <div class="tarjeta">
          <h3>🛠️ Laboratorio de Prototipado</h3>
          <p>Espacio dedicado al diseño, mantenimiento y verificación de instrumentación científica.</p>
        </div>
        <div class="tarjeta">
          <h3>🧪 Tanques Experimentales</h3>
          <p>Simulaciones y pruebas controladas para garantizar la calidad de los datos.</p>
        </div>
      </div>
    </section>

    <section class="seccion-recursos">
      <h2 class="titulo-sio">3. Instrumentación Disponible</h2>
      
      <div class="grid-tarjetas">
        <div class="tarjeta">
          <h3>Sonda CTD-48M</h3>
          <p>Sistema estacionario para perfiles de alta precisión en aguas profundas (hasta 6.000 metros).</p>
        </div>
        <div class="tarjeta">
          <h3>CastAway CTD Portátil</h3>
          <p>Primer CTD portátil lanzable del mundo. Operación sin cables ideal para estudios costeros (hasta 100m).</p>
        </div>
        <div class="tarjeta">
          <h3>Salinómetro Autosal 8400B</h3>
          <p>Salinómetro de laboratorio de alta precisión para análisis de referencia y calibración CTD.</p>
        </div>
      </div>
    </section>

  </div>
</template>

<style scoped>
.recursos-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
  font-family: Arial, sans-serif;
  color: #333;
}

.seccion-recursos {
  margin-bottom: 4rem;
}

/* AQUÍ ESTÁ LA MAGIA PARA QUE LOS TÍTULOS SEAN IDÉNTICOS A QUIÉNES SOMOS */
.titulo-sio {
  color: #0056b3;
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  border-bottom: 2px solid #e0e0e0;
  padding-bottom: 0.5rem;
  text-align: left;
}

.grid-tarjetas {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 1rem;
}

.tarjeta {
  background-color: #f8f9fa;
  border-left: 5px solid #0056b3;
  padding: 1.5rem;
  border-radius: 6px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  transition: transform 0.2s ease;
}

.tarjeta:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.tarjeta h3 {
  color: #0056b3;
  margin-top: 0;
  margin-bottom: 0.8rem;
  font-size: 1.2rem;
}

.tarjeta p {
  margin: 0;
  line-height: 1.5;
  color: #666;
}
</style>