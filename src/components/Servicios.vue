<script setup>
const emit = defineEmits(['cambiar-pagina'])
</script>

<template>
  <div class="servicios-hub">
    <div class="fondo-servicios"></div>

    <div class="contenedor-ancho contenido-hub">
      
      <h1 class="titulo-seccion">Nuestros Servicios</h1>
      <p class="subtitulo">Infraestructuras y soluciones tecnológicas para la comunidad científica marina.</p>

      <div class="grid-tres-columnas">
        
        <div class="seccion-bloque" @click="$emit('cambiar-pagina', 'pelagia')" style="cursor: pointer;">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Embarcación Pelagia</h2>
            <p>Plataforma polivalente para trabajos de oceanografía costera, equipada para el despliegue de instrumentación y muestreo.</p>
          </div>

          <div class="lista-items">
            <div class="item-servicio">
              <span class="punto-azul">●</span>
              <div>Operaciones de despliegue y recuperación de equipos (ROVs, fondeos).</div>
            </div>
            <div class="item-servicio">
              <span class="punto-azul">●</span>
              <div>Campañas de muestreo biológico, geológico y físico-químico.</div>
            </div>
            <div class="item-servicio">
              <span class="punto-azul">●</span>
              <div>Gestión logística y tripulación especializada en ciencias del mar.</div>
            </div>
          </div>
        </div>

        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Instrumentación</h2>
            <p>Acceso a una amplia gama de instrumentación oceanográfica y soporte técnico para su configuración.</p>
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
              <div>Mantenimiento preventivo y correctivo de sensores.</div>
            </div>
          </div>
        </div>

        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Tanques de Pruebas</h2>
            <p>Alquiler de áreas experimentales para la validación y calibración de instrumentación en entornos controlados.</p>
          </div>

          <div class="lista-items">
            <div class="item-servicio">
              <span class="punto-azul">●</span>
              <div>Ensayos de estanqueidad y flotabilidad para robótica.</div>
            </div>
            <div class="item-servicio">
              <span class="punto-azul">●</span>
              <div>Calibración de sensores acústicos y ópticos.</div>
            </div>
            <div class="item-servicio">
              <span class="punto-azul">●</span>
              <div>Soporte de ingeniería especializado durante los ensayos.</div>
            </div>
          </div>
        </div>

      </div> 
    </div>
  </div>
</template>

<style scoped>
.servicios-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

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

.contenido-hub { position: relative; z-index: 10; padding-top: 120px; }

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

/* GRID DE 3 COLUMNAS */
.grid-tres-columnas {
  display: grid;
  grid-template-columns: repeat(3, 1fr); 
  gap: 30px; 
}

.seccion-bloque { 
  background: white; 
  border-radius: 12px; 
  padding: 35px; /* Recuperamos el espacio blanco */
  box-shadow: 0 10px 30px rgba(0,0,0,0.15); 
  display: flex;
  flex-direction: column; 
  min-height: 350px; /* Recuperamos la altura elegante */
  transition: transform 0.3s;
}

.seccion-bloque:hover { transform: translateY(-5px); }

.titulo-fija { color: #012169; margin-top: 0; font-size: 1.6rem; margin-bottom: 10px; }

/* COMPRIMIMOS EL TEXTO DENTRO DE LA FICHA */
.cabecera-bloque p { 
  color: #666; 
  font-size: 0.95rem; 
  line-height: 1.3; 
  margin-bottom: 10px; /* Párrafo más pegado a la lista */
}

.lista-items { 
  margin-top: 15px; 
  display: flex; 
  flex-direction: column; 
  gap: 5px; /* Puntos de la lista muy juntos */
}

.item-servicio { 
  display: flex; 
  gap: 10px; 
  margin-bottom: 0px !important; /* Quitamos el margen inferior rebelde */
  font-size: 0.9rem; 
  color: #333;
  line-height: 1.2;
}

.punto-azul { color: #007bff; }
.punto-verde { color: #28a745; }

@media (max-width: 1100px) { .grid-tres-columnas { grid-template-columns: 1fr 1fr; } }
@media (max-width: 768px) { .grid-tres-columnas { grid-template-columns: 1fr; } .contenido-hub { padding-top: 150px; } }
</style>