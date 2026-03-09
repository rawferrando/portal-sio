<template>
  <div class="seccion-tecnica">
    <button class="btn-volver" @click="$emit('volver')">⬅ Volver al Panel Principal</button>
    
    <header class="cabecera-proyectos">
      <h1>Proyectos de Ingeniería y Apoyo Científico</h1>
      <p class="subtitulo">Gestión técnica integral: desde el diseño conceptual hasta la operación en alta mar.</p>
    </header>

    <section class="grid-proyectos">
      <div class="card-proyecto">
        <div class="header-card">
          <span class="estado activo">En Curso</span>
          <h3>Proyecto MINERVA</h3>
        </div>
        <p>Desarrollo de sistemas autónomos de visión submarina para la monitorización de especies bentónicas en áreas protegidas.</p>
        <div class="detalles-tecnicos">
          <span><strong>Tecnología:</strong> IA + Cámaras 4K</span>
          <span><strong>Profundidad:</strong> 50m - 200m</span>
        </div>
      </div>

      <div class="card-proyecto">
        <div class="header-card">
          <span class="estado permanente">Mantenimiento</span>
          <h3>Observatorio OBSEA</h3>
        </div>
        <p>Gestión de la infraestructura cableada del observatorio marino. Proporcionamos soporte técnico continuo y despliegue de nuevos sensores.</p>
        <div class="detalles-tecnicos">
          <span><strong>Ubicación:</strong> Vilanova i la Geltrú</span>
          <span><strong>Conexión:</strong> Fibra Óptica</span>
        </div>
      </div>

      <div class="card-proyecto">
        <div class="header-card">
          <span class="estado finalizado">Finalizado</span>
          <h3>Campaña NEREIDA</h3>
        </div>
        <p>Instalación de una red de fondeos oceanográficos para el estudio de corrientes profundas en el Cañón de Palamós.</p>
        <div class="detalles-tecnicos">
          <span><strong>Hito:</strong> Fondeo a 1500m</span>
          <span><strong>Equipos:</strong> RDI ADCP + SBE37</span>
        </div>
      </div>
    </section>

    <footer class="info-adicional">
      <p>💡 ¿Tienes un nuevo proyecto? El SIO ofrece consultoría técnica desde la fase de solicitud de financiación.</p>
    </footer>
  </div>
</template>

<style scoped>
.seccion-tecnica {
  max-width: 1100px;
  margin: 0 auto;
  padding: 1.5rem;
}

.btn-volver {
  background: white;
  border: 1px solid #005596;
  color: #005596;
  padding: 0.6rem 1.2rem;
  border-radius: 4px;
  font-weight: bold;
  cursor: pointer;
  margin-bottom: 2rem;
  transition: all 0.3s ease;
}

.btn-volver:hover {
  background: #005596;
  color: white;
}

.cabecera-proyectos h1 {
  color: #005596;
  font-size: 2.2rem;
  margin-bottom: 0.5rem;
}

.subtitulo {
  color: #666;
  font-style: italic;
  margin-bottom: 3rem;
}

/* Grid de proyectos */
.grid-proyectos {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
}

.card-proyecto {
  background: white;
  border-top: 5px solid #005596;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
}

.header-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.header-card h3 {
  margin: 0;
  color: #333;
}

.estado {
  font-size: 0.7rem;
  text-transform: uppercase;
  font-weight: bold;
  padding: 4px 8px;
  border-radius: 12px;
}

.activo { background: #e3f2fd; color: #1976d2; }
.permanente { background: #fff3e0; color: #f57c00; }
.finalizado { background: #e8f5e9; color: #388e3c; }

.detalles-tecnicos {
  margin-top: auto;
  padding-top: 1rem;
  border-top: 1px dashed #eee;
  display: flex;
  flex-direction: column;
  font-size: 0.85rem;
  color: #555;
  gap: 5px;
}

.info-adicional {
  margin-top: 4rem;
  padding: 1.5rem;
  background: #f0f7ff;
  border-radius: 8px;
  text-align: center;
  color: #005596;
  font-weight: bold;
}
</style>