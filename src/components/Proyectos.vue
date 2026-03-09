<template>
  <div class="seccion-tecnica">
    <button class="btn-volver" @click="$emit('volver')">⬅ Volver al Panel Principal</button>
    
    <header class="cabecera-proyectos">
      <h1>WikiSIO: Registro de Proyectos y Operaciones</h1>
      <p class="subtitulo">Histórico y estado actual de las infraestructuras tecnológicas del SIO.</p>
    </header>

    <section class="grid-proyectos">
      <div class="card-proyecto">
        <div class="header-card">
          <span class="estado activo">Operativo</span>
          <h3>Observatorio OBSEA</h3>
        </div>
        <p>Mantenimiento integral del observatorio submarino cableado. Gestión de la plataforma de sensores y el nodo de comunicaciones submarino.</p>
        <div class="detalles-tecnicos">
          <span><strong>📍 Ubicación:</strong> Vilanova i la Geltrú (4 km costa)</span>
          <span><strong>📡 Comunicación:</strong> Fibra óptica submarina</span>
          <span><strong>🛠 Tareas:</strong> Limpieza de biofouling y calibración de CTDs.</span>
        </div>
      </div>

      <div class="card-proyecto">
        <div class="header-card">
          <span class="estado activo">Operativo</span>
          <h3>Red de Radares HF (COSMO)</h3>
        </div>
        <p>Monitorización de corrientes superficiales mediante tecnología de radar de alta frecuencia. Soporte técnico a las estaciones terrestres.</p>
        <div class="detalles-tecnicos">
          <span><strong>📍 Cobertura:</strong> Costa Catalana y Baleares</span>
          <span><strong>💻 Software:</strong> Procesado de datos SeaSonde</span>
          <span><strong>🔌 Mantenimiento:</strong> Revisión de antenas y fuentes de alimentación.</span>
        </div>
      </div>

      <div class="card-proyecto">
        <div class="header-card">
          <span class="estado mantenimiento">Revisión</span>
          <h3>Boya de Barcelona (ICM)</h3>
        </div>
        <p>Estación oceanográfico-meteorológica fija. Adquisición de datos en tiempo real de oleaje, viento y temperatura del agua.</p>
        <div class="detalles-tecnicos">
          <span><strong>📍 Posición:</strong> 41° 22.8' N | 002° 12.0' E</span>
          <span><strong>🔋 Sistema:</strong> Paneles solares + Baterías AGM</span>
          <span><strong>⚠️ Estado:</strong> Sustitución prevista de sensores meteorológicos.</span>
        </div>
      </div>
    </section>

    <div class="wiki-footer">
      <p>📝 <em>Nota de WikiSIO: Para consultar esquemas de cableado o protocolos de despliegue, acceder al repositorio técnico en la Intranet.</em></p>
    </div>
  </div>
</template>

<style scoped>
/* (Mantén los estilos que ya teníamos, son los que mejor funcionan) */
.seccion-tecnica { max-width: 1100px; margin: 0 auto; padding: 1.5rem; }
.btn-volver { background: white; border: 1px solid #005596; color: #005596; padding: 0.6rem 1.2rem; border-radius: 4px; font-weight: bold; cursor: pointer; margin-bottom: 2rem; }
.cabecera-proyectos h1 { color: #005596; font-size: 2rem; border-bottom: 2px solid #eee; padding-bottom: 10px; }
.grid-proyectos { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; margin-top: 2rem; }
.card-proyecto { background: #fff; border-top: 5px solid #005596; padding: 1.5rem; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
.header-card { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
.estado { font