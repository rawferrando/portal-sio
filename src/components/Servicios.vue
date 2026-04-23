<script setup>
const emit = defineEmits(['cambiar-pagina'])
</script>

<template>
  <div class="servicios-hub">
    <div class="fondo-servicios"></div>

    <div class="contenedor-ancho contenido-hub">
      
      <h1 class="titulo-seccion">Nuestros Servicios</h1>
      <p class="subtitulo">Soluciones técnicas y tecnológicas de vanguardia para la comunidad científica marina.</p>

      <div class="grid-tres-columnas">
        
        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Soporte Técnico</h2>
            <p>Asesoramiento especializado y apoyo operativo en campañas oceanográficas y proyectos de investigación.</p>
          </div>

          <div class="lista-items">
            <div class="item-servicio">
              <span class="punto-azul">●</span>
              <div>Diseño y despliegue de sistemas de adquisición de datos.</div>
            </div>
            <div class="item-servicio">
              <span class="punto-azul">●</span>
              <div>Configuración y mantenimiento de sensores oceanográficos.</div>
            </div>
            <div class="item-servicio">
              <span class="punto-azul">●</span>
              <div>Asistencia técnica personalizada in-situ.</div>
            </div>
          </div>
        </div>

        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Instrumentación</h2>
            <p>Acceso a una amplia gama de instrumentación y recursos técnicos para el desarrollo de proyectos.</p>
          </div>

          <div class="lista-items">
            <div class="item-servicio">
              <span class="punto-verde">●</span>
              <div>Desarrollo y personalización de equipos a medida.</div>
            </div>
            <div class="item-servicio">
              <span class="punto-verde">●</span>
              <div>Sistemas de comunicaciones y telemetría submarina.</div>
            </div>
            <div class="item-servicio">
              <span class="punto-verde">●</span>
              <div>Laboratorios de electrónica y prototipado rápido.</div>
            </div>
          </div>
        </div>

        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Tanques de Pruebas</h2>
            <p>Alquiler de áreas experimentales y tanques para la validación y calibración de instrumentación en entornos controlados.</p>
          </div>

          <div class="lista-items">
            <div class="item-servicio">
              <span class="punto-azul">●</span>
              <div>Ensayos de estanqueidad, presión y flotabilidad para robótica.</div>
            </div>
            <div class="item-servicio">
              <span class="punto-azul">●</span>
              <div>Calibración de sensores acústicos y ópticos en agua controlada.</div>
            </div>
            <div class="item-servicio">
              <span class="punto-azul">●</span>
              <div>Soporte de ingeniería durante las fases de ensayo previas a campaña.</div>
            </div>
          </div>
        </div>

      </div> 
    </div>
  </div>
</template>

<style scoped>
.servicios-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

/* 🌊 FONDO CON LA IMAGEN DE INSTRUMENTACIÓN 🌊 */
.fondo-servicios { 
  position: absolute; 
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 550px; 
  background-image: linear-gradient(rgba(1, 33, 105, 0.65), rgba(1, 33, 105, 0.85)), 
                    url('/instrumentacion.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: 0; 
}

/* Manteniendo el espacio que te gustó (120px) */
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

/* GRID ACTUALIZADO A 3 COLUMNAS */
.grid-tres-columnas {
  display: grid;
  grid-template-columns: repeat(3, 1fr); 
  gap: 30px; 
}

.seccion-bloque { 
  background: white; 
  border-radius: 12px; 
  padding: 35px; 
  box-shadow: 0 10px 30px rgba(0,0,0,0.15); 
  display: flex;
  flex-direction: column; 
  min-height: 350px; /* Recuperando el espacio blanco que te gustó */
}

.titulo-fija { color: #012169; margin-top: 0; font-size: 1.6rem; margin-bottom: 10px; }
.cabecera-bloque p { color: #666; font-size: 0.95rem; line-height: 1.4; margin-bottom: 25px; }

.lista-items { margin-top: auto; }

.item-servicio { 
  display: flex; 
  gap: 10px; 
  margin-bottom: 12px; 
  font-size: 0.95rem; 
  color: #333;
  line-height: 1.4;
}

.punto-azul { color: #007bff; }
.punto-verde { color: #28a745; }

/* Adaptación para pantallas pequeñas */
@media (max-width: 1100px) {
  .grid-tres-columnas { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 768px) {
  .grid-tres-columnas { grid-template-columns: 1fr; }
  .contenido-hub { padding-top: 150px; }
}
</style>