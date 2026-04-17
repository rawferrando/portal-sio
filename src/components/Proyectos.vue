<template>
  <div class="pagina-seccion fade-in">
    <div class="cabecera-seccion">
      <button @click="$emit('volver')" class="btn-volver">⬅ Volver al Inicio</button>
      <h2>📂 Proyectos y Campañas</h2>
      <p>Soporte técnico, logístico y operativo para campañas de investigación oceanográfica.</p>
    </div>

    <div class="grid-proyectos">
      
      <div class="card-proyecto">
        <div class="status-badge activa">Activa</div>
        <div class="card-body">
          <h3>Campaña Antártica 2025</h3>
          <p class="ip"><strong>IP:</strong> Dr. Jordi Font</p>
          <p class="desc">Instalación y mantenimiento de sensores de salinidad y temperatura en condiciones extremas.</p>
          <div class="tags">
            <span>#CTD</span> <span>#Antártida</span> <span>#Sensores</span>
          </div>
        </div>
      </div>

      <div class="card-proyecto">
        <div class="status-badge finalizada">Finalizada</div>
        <div class="card-body">
          <h3>Observatorio OBSEA</h3>
          <p class="ip"><strong>IP:</strong> Joaquín del Río</p>
          <p class="desc">Revisión anual de la infraestructura submarina cableada y sistemas de comunicación.</p>
          <div class="tags">
            <span>#OBSEA</span> <span>#ROV</span> <span>#Mantenimiento</span>
          </div>
        </div>
      </div>

      <div class="card-placeholder">
        <p>Añade nuevos proyectos desde la Intranet SIO</p>
      </div>

    </div>
  </div>
</template>

<style scoped>
.pagina-seccion { max-width: 1200px; margin: 0 auto; padding: 40px 20px; }

.cabecera-seccion { margin-bottom: 40px; text-align: center; position: relative; }
.cabecera-seccion h2 { color: #005596; font-size: 2.5rem; margin-top: 20px; }
.cabecera-seccion p { color: #666; font-size: 1.2rem; }

.btn-volver { 
  background-color: #6c757d; color: white; border: none; padding: 10px 20px; 
  border-radius: 5px; cursor: pointer; position: absolute; left: 0; top: 0;
  font-weight: bold; transition: 0.3s; 
}
.btn-volver:hover { background-color: #5a6268; }

/* GRID DE TARJETAS */
.grid-proyectos { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); 
  gap: 25px; 
  margin-top: 50px; 
}

.card-proyecto { 
  background: white; border-radius: 12px; overflow: hidden; 
  box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #005596;
  position: relative; transition: transform 0.3s;
}
.card-proyecto:hover { transform: translateY(-5px); }

.status-badge { 
  position: absolute; top: 15px; right: 15px; padding: 5px 10px; 
  border-radius: 20px; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; 
}
.activa { background: #d4edda; color: #155724; }
.finalizada { background: #e2e3e5; color: #383d41; }

.card-body { padding: 25px; }
.card-body h3 { margin: 0 0 15px 0; color: #333; font-size: 1.4rem; }
.ip { color: #005596; font-size: 0.95rem; margin-bottom: 10px; }
.desc { color: #555; font-size: 0.9rem; line-height: 1.5; margin-bottom: 20px; }

.tags { display: flex; gap: 8px; flex-wrap: wrap; }
.tags span { background: #f0f4f8; color: #005596; padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; }

.card-placeholder { 
  border: 2px dashed #ccc; border-radius: 12px; display: flex; 
  align-items: center; justify-content: center; padding: 40px;
  color: #999; text-align: center; font-style: italic;
}

.fade-in { animation: fadeIn 0.5s ease-in-out; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

@media (max-width: 768px) {
  .btn-volver { position: static; margin-bottom: 20px; }
  .cabecera-seccion h2 { font-size: 2rem; }
}
</style>