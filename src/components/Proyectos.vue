<script setup>
import { ref } from 'vue'

const emit = defineEmits(['volver'])

// TUS PROYECTOS REALES DE LA WIKISIO
const enCurso = ref([
  { titulo: 'ALBARANES', tipo: 'Infraestructura' },
  { titulo: 'SALADET', tipo: 'Contrato' },
  { titulo: 'TECTUGA', tipo: 'Plan Nacional' },
  { titulo: 'EPSP', tipo: 'Otro' },
  { titulo: 'CAMARAS PLAYA', tipo: 'Infraestructura' },
  { titulo: 'OPT4DIV', tipo: 'Plan Nacional' }
])

const solicitados = ref([
  { titulo: 'ÒHPERA DEL MAR', tipo: 'Divulgación Científica' },
  { titulo: 'PROTEO', tipo: 'Divulgación Científica' }
])

// Función para darle el color exacto a la etiqueta según el tipo
const clasePorTipo = (tipo) => {
  switch (tipo) {
    case 'Infraestructura': return 'badge-verde';
    case 'Contrato': return 'badge-turquesa';
    case 'Plan Nacional': return 'badge-amarillo';
    case 'Otro': return 'badge-naranja';
    case 'Divulgación Científica': return 'badge-morado';
    default: return 'badge-gris';
  }
}
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
                <span :class="['badge-tipo', clasePorTipo(p.tipo)]">{{ p.tipo }}</span>
                <span class="punto-estado verde" title="En curso"></span>
              </div>
              <h3>{{ p.titulo }}</h3>
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
                <span :class="['badge-tipo', clasePorTipo(p.tipo)]">{{ p.tipo }}</span>
                <span class="punto-estado naranja" title="Solicitado"></span>
              </div>
              <h3>{{ p.titulo }}</h3>
            </div>
          </div>
        </div>

      </div> 
    </div>
  </div>
</template>

<style scoped>
.proyectos-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

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
  background-color: #8cc63f; 
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

/* --- CONTENEDOR Y MINI TARJETAS --- */
.contenedor-proyectos {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.mini-tarjeta {
  background: #fdfdfd;
  border-left: 4px solid #0086c0;
  padding: 12px 18px;
  border-radius: 4px 8px 8px 4px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  transition: transform 0.2s, box-shadow 0.2s;
}

.mini-tarjeta:hover {
  transform: translateX(5px);
  background: white;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.header-mini {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 5px;
}

/* --- COLORES DE LAS ETIQUETAS (COPIADOS DE LA WIKISIO) --- */
.badge-tipo {
  font-size: 0.75rem;
  font-weight: bold;
  padding: 4px 10px;
  border-radius: 20px;
  color: white;
}

.badge-verde { background-color: #28a745; } /* Infraestructura */
.badge-turquesa { background-color: #17a2b8; } /* Contrato */
.badge-amarillo { background-color: #ffc107; color: #333; } /* Plan Nacional */
.badge-naranja { background-color: #fd7e14; } /* Otro */
.badge-morado { background-color: #6f42c1; } /* Divulgación Científica */
.badge-gris { background-color: #6c757d; }

/* Puntos de estado */
.punto-estado { width: 10px; height: 10px; border-radius: 50%; }
.punto-estado.verde { background: #28a745; box-shadow: 0 0 5px rgba(40, 167, 69, 0.5); }
.punto-estado.naranja { background: #ffc107; box-shadow: 0 0 5px rgba(255, 193, 7, 0.5); }

.mini-tarjeta h3 { 
  margin: 5px 0 0 0; 
  font-size: 1.1rem; 
  color: #333; 
}

@media (max-width: 992px) {
  .grid-horizontal { grid-template-columns: 1fr; }
  .contenido-hub { padding-top: 150px; }
}
</style>