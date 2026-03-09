<template>
  <section class="recursos">
    <h2>2. Recursos Técnicos Destacados</h2>
    <div class="grid-recursos">
      <div class="card">
        <h3>🛥️ Embarcación Propia</h3>
        <p>Ubicada en el Puerto Olímpico para despliegue y adquisición de datos en las cercanías de Barcelona.</p>
      </div>
      <div class="card">
        <h3>🛠️ Laboratorio de Prototipado</h3>
        <p>Espacio dedicado al diseño, mantenimiento y verificación de instrumentación científica.</p>
      </div>
      <div class="card">
        <h3>🧪 Tanques Experimentales</h3>
        <p>Simulaciones y pruebas controladas para garantizar la calidad de los datos.</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.grid-recursos {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-top: 1rem;
}
.card {
  background: #fdfdfd;
  border: 1px solid #ddd;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
h3 { color: #0056b3; margin-top: 0; }
</style>