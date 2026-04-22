<script setup>
import { ref } from 'vue'

const emit = defineEmits(['volver'])

// Listado de proyectos reales (puedes ampliarlo aquí mismo)
const enCurso = ref([
  { 
    titulo: 'Campaña Antártica 2025', 
    tipo: 'Plan Nacional', 
    ip: 'Jordi Font',
    descripcion: 'Soporte técnico para el despliegue de boyas de deriva y sensores CTD en el Mar de Weddell.' 
  },
  { 
    titulo: 'Mantenimiento OBSEA', 
    tipo: 'Infraestructura', 
    ip: 'Joaquín del Río',
    descripcion: 'Operaciones periódicas de limpieza de sensores y revisión del cableado del observatorio submarino.' 
  },
  { 
    titulo: 'Taller Escolar Marino', 
    tipo: 'Divulgación', 
    ip: 'Equipo SIO',
    descripcion: 'Programa de formación en tecnología oceanográfica para institutos locales.' 
  }
])

const solicitados = ref([
  { 
    titulo: 'Propuesta ROV Abisal', 
    tipo: 'Infraestructura', 
    ip: 'Pendiente IP',
    descripcion: 'Solicitud de adquisición de un nuevo vehículo operado remotamente para trabajos a 2000m.' 
  },
  { 
    titulo: 'Proyecto BlueTech', 
    tipo: 'Plan Nacional', 
    ip: 'Raúl Ferrando',
    descripcion: 'Desarrollo de nuevos sistemas de comunicación acústica submarina de bajo consumo.' 
  }
])
</script>

<template>
  <div class="proyectos-hub">
    <div class="fondo-proyectos"></div>

    <div class="contenedor-ancho contenido-hub">
      
      <h1 class="titulo-seccion">Proyectos y Campañas</h1>
      <p class="subtitulo">Visualiza el estado actual de los proyectos técnicos y las solicitudes en curso del servicio.</p>

      <div class="grid-horizontal">
        
        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Proyectos en Curso</h2>
            <p>Actividades y campañas en fase de ejecución técnica actualmente.</p>
          </div>

          <div class="contenedor-proyectos">
            <div v-for="(p, i) in enCurso" :key="'ec'+i" class="mini-tarjeta">
              <div class="header-mini">
                <span class="badge-tipo">{{ p.tipo }}</span>
                <span class="punto-estado verde"></span>
              </div>
              <h3>{{ p.titulo }}</h3>
              <p class="ip-info"><strong>IP:</strong> {{ p.ip }}</p>
              <p class="desc-info">{{ p.descripcion }}</p>
            </div>
          </div>
        </div>

        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Proyectos Solicitados</h2>
            <p>Propuestas técnicas y licitaciones en fase de evaluación o planificación.</p>
          </div>

          <div class="contenedor-proyectos">
            <div v-for="(p, i) in solicitados" :key="'sol'+i" class="mini-tarjeta">
              <div class="header-mini">
                <span class="badge-tipo azul">{{ p.tipo }}</span>
                <span class="punto-estado naranja"></span>
              </div>
              <h3>{{ p.titulo }}</h3>
              <p class="ip-info"><strong>IP:</strong> {{ p.ip }}</p>
              <p class="desc-info">{{ p.descripcion }}</p>
            </div>
          </div>
        </div>

      </div> 
    </div>
  </div>
</template>

<style scoped>
.proyectos-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

/* 🌊 FONDO CON TU IMAGEN (RUTA CON %20 POR LOS ESPACIOS) 🌊 */
.fondo-proyectos { 
  position: absolute; 
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 550px; 
  background-image: linear-gradient(rgba(1, 33, 105, 0.65), rgba(1, 33, 105, 0.85)), 
                    url('/pecesaguasalada.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: 0; 
}

/* Título bajado para máxima legibilidad */
.contenido-hub { 
  position: relative; 
  z-index: 10; 
  padding-top: 120px; 
}

.titulo-seccion { 
  color: white; 
  font-size: 2.2rem; 
  margin-bottom: 15px; 
  font-weight: bold; 
  position: relative;
  display: inline-block;
  padding-bottom: 8px;
}

.titulo-seccion::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background-color: #8cc63f; /* Verde corporativo ICM */
}

.subtitulo { color: #e0e6ed; font-size: 1.1rem; margin-bottom: 40px; max-width: 800px; }

.grid-horizontal {
  display: grid;
  grid-template-columns: 1fr 1fr; 
  gap: 30px; 
}

.seccion-bloque { 
  background: white; 
  border-radius: 12px; 
  padding: 35px; 
  box-shadow: 0 10px 30px rgba(0,0,0,0.15); 
  display: flex;
  flex-direction: column; 
}

.titulo-fija { color: #012169; margin-top: 0; font-size: 1.6rem; margin-bottom: 10px; }
.cabecera-bloque p { color: #666; font-size: 0.95rem; line-height: 1.4; margin-bottom: 25px; }

/* --- CONTENEDOR DE LAS MINI TARJETAS --- */
.contenedor-proyectos {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.mini-tarjeta {
  background: #fdfdfd;
  border-left: 4px solid #0086c0;
  padding: 15px 20px;
  border-radius: 4px 8px 8px 4px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  transition: transform 0.2s;
}

.mini-tarjeta:hover {
  transform: translateX(5px);
  background: white;
}

.header-mini {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.badge-tipo {
  background: #eef2f7;
  color: #012169;
  font-size: 0.75rem;
  font-weight: bold;
  padding: 3px 10px;
  border-radius: 20px;
  text-transform: uppercase;
}

.badge-tipo.azul { background: #e0f0ff; color: #0061af; }

.punto-estado { width: 10px; height: 10px; border-radius: 50%; }
.punto-estado.verde { background: #28a745; box-shadow: 0 0 5px #28a745; }
.punto-estado.naranja { background: #ffc107; box-shadow: 0 0 5px #ffc107; }

.mini-tarjeta h3 { 
  margin: 0 0 5px 0; 
  font-size: 1.15rem; 
  color: #333; 
}

.ip-info { font-size: 0.85rem; color: #0086c0; margin-bottom: 8px; }
.desc-info { font-size: 0.9rem; color: #666; line-height: 1.5; margin: 0; }

@media (max-width: 992px) {
  .grid-horizontal { grid-template-columns: 1fr; }
  .contenido-hub { padding-top: 150px; }
}
</style>