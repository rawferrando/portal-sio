<script setup>
import { ref } from 'vue'

const emit = defineEmits(['volver'])

// Datos de ejemplo extraídos de la WikiSIO
const enCurso = ref([
  { nombre: 'Campaña Antártica', detalle: 'Mantenimiento de sensores de salinidad.' },
  { nombre: 'Observatorio OBSEA', detalle: 'Revisión de infraestructura cableada.' }
])

const solicitados = ref([
  { nombre: 'Expedición Abisal', detalle: 'Propuesta de cámaras de baja luz.' },
  { nombre: 'Muestreo Litoral', detalle: 'Pendiente de aprobación de presupuesto.' }
])
</script>

<template>
  <div class="proyectos-hub">
    <div class="fondo-proyectos"></div>

    <div class="contenedor-ancho contenido-hub">
      
      <h1 class="titulo-seccion">Proyectos y Campañas</h1>
      <p class="subtitulo">Gestión y seguimiento del soporte técnico a la investigación oceanográfica.</p>

      <div class="grid-horizontal">
        
        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Proyectos en Curso</h2>
            <p>Listado de actividades y campañas que se están ejecutando actualmente bajo la supervisión técnica del SIO.</p>
          </div>

          <div class="lista-items">
            <div v-for="(p, i) in enCurso" :key="i" class="item-proyecto">
              <span class="punto-verde">●</span>
              <div>
                <strong>{{ p.nombre }}:</strong> {{ p.detalle }}
              </div>
            </div>
            <button class="btn-ver-mas">Ver todos en WikiSIO</button>
          </div>
        </div>

        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Proyectos Solicitados</h2>
            <p>Propuestas técnicas y solicitudes de equipamiento en fase de evaluación o planificación logística.</p>
          </div>

          <div class="lista-items">
            <div v-for="(p, i) in solicitados" :key="i" class="item-proyecto">
              <span class="punto-azul">●</span>
              <div>
                <strong>{{ p.nombre }}:</strong> {{ p.detalle }}
              </div>
            </div>
            <button class="btn-ver-mas">Consultar solicitudes</button>
          </div>
        </div>

      </div> 
    </div>
  </div>
</template>

<style scoped>
.proyectos-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

/* 🌊 FONDO CON TU IMAGEN Y ESPACIOS CORREGIDOS 🌊 */
.fondo-proyectos { 
  position: absolute; 
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 550px; 
  background-image: linear-gradient(rgba(1, 33, 105, 0.65), rgba(1, 33, 105, 0.85)), 
                    url('/peces%20pecesagua%20alada.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: 0; 
}

/* Título bajo para no chocar con el header */
.contenido-hub { 
  position: relative; 
  z-index: 10; 
  padding-top: 180px; 
}

.titulo-seccion { 
  color: white; 
  font-size: 2rem; 
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

.subtitulo { color: #e0e6ed; font-size: 1rem; margin-bottom: 40px; max-width: 800px; }

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
  min-height: 350px;
}

.titulo-fija { color: #012169; margin-top: 0; font-size: 1.5rem; margin-bottom: 15px; }

.cabecera-bloque p { color: #555; line-height: 1.6; font-size: 1rem; margin-bottom: 25px; }

.lista-items { margin-top: auto; }

.item-proyecto { 
  display: flex; 
  gap: 10px; 
  margin-bottom: 12px; 
  font-size: 0.95rem; 
  color: #333;
  line-height: 1.4;
}

.punto-verde { color: #28a745; }
.punto-azul { color: #007bff; }

.btn-ver-mas { 
  margin-top: 20px;
  background: #0086c0; 
  color: white; 
  border: none; 
  padding: 10px 20px; 
  border-radius: 6px; 
  font-weight: bold; 
  cursor: pointer; 
  width: 100%;
  transition: background 0.3s;
}

.btn-ver-mas:hover { background: #012169; }

@media (max-width: 992px) {
  .grid-horizontal { grid-template-columns: 1fr; }
  .contenido-hub { padding-top: 150px; }
}
</style>