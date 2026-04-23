<script setup>
const emit = defineEmits(['cambiar-pagina'])
</script>

<template>
  <div class="idi-hub">
    <div class="fondo-idi"></div>

    <div class="contenedor-ancho contenido-hub">
      
      <h1 class="titulo-seccion">I+D+I</h1>
      <p class="subtitulo">Impulsando la innovación tecnológica marina y la transferencia de conocimiento del SIO.</p>

      <div class="grid-horizontal">
        
        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Oficina I+D+I</h2>
            <p>Soporte integral a la investigación: desde la gestión de convocatorias hasta la protección de resultados y transferencia tecnológica.</p>
          </div>

          <div class="lista-items">
            <div class="item-idi">
              <span class="punto-azul">●</span>
              <div>Gestión de proyectos y asesoramiento técnico especializado.</div>
            </div>
            <div class="item-idi">
              <span class="punto-azul">●</span>
              <div>Propiedad intelectual y valorización de la tecnología desarrollada.</div>
            </div>
            <div class="item-idi">
              <span class="punto-azul">●</span>
              <div>Fomento de la colaboración con empresas y centros del sector marino.</div>
            </div>
          </div>
        </div>

          <div class="seccion-bloque" @click="$emit('cambiar-pagina', 'bluelab')" style="cursor: pointer; transition: transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija" style="display: flex; justify-content: space-between; align-items: center;">
              BLUE Lab <span style="font-size: 1rem; color: #0086c0;">Ver más ➔</span>
            </h2>
            <p>Instalación estratégica del ICM-CSIC orientada a acelerar la adopción de la robótica marina autónoma y la IA en la observación del océano.</p>
          </div>

          <div class="lista-items">
            <div class="item-idi">
              <span class="punto-verde">●</span>
              <div>Plataformas robóticas autónomas (AUVs, ASVs y drones).</div>
            </div>
            <div class="item-idi">
              <span class="punto-verde">●</span>
              <div>Diseño bioinspirado y robótica submarina de bajo impacto.</div>
            </div>
            <div class="item-idi">
              <span class="punto-verde">●</span>
              <div>Sensores en animales (Biologging) y Machine Learning.</div>
            </div>
          </div>
        </div>

      </div> 
    </div>
  </div>
</template>

<style scoped>
.idi-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

/* 🌊 CONFIGURACIÓN DEL FONDO 🌊 */
.fondo-idi { 
  position: absolute; 
  top: 0; 
  left: 0; 
  width: 100%; 
  /* Recuperamos la altura original del fondo (550px) */
  height: 550px; 
  background-image: linear-gradient(rgba(1, 33, 105, 0.65), rgba(1, 33, 105, 0.85)), 
                    url('/tortuga.jpg');
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

/* Línea verde ICM */
.titulo-seccion::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background-color: #8cc63f; 
}

/* Recuperamos el margen original del subtítulo (40px) */
.subtitulo { color: #e0e6ed; font-size: 1.1rem; margin-bottom: 40px; max-width: 800px; }

.grid-horizontal {
  display: grid;
  grid-template-columns: 1fr 1fr; 
  gap: 30px; 
}

.seccion-bloque { 
  background: white; 
  border-radius: 12px; 
  /* Recuperamos el padding original (35px) y la altura mínima (350px) */
  padding: 35px; 
  box-shadow: 0 10px 30px rgba(0,0,0,0.15); 
  display: flex;
  flex-direction: column; 
  min-height: 350px; 
}

.titulo-fija { color: #012169; margin-top: 0; font-size: 1.6rem; margin-bottom: 10px; }

/* Recuperamos el margen original de los párrafos (25px) */
.cabecera-bloque p { color: #666; font-size: 0.95rem; line-height: 1.4; margin-bottom: 15px; }

/* 2. LA LISTA DE PUNTOS: Reducimos la separación entre líneas */
.lista-items { 
  margin-top: auto; 
  display: flex; 
  flex-direction: column; 
  gap: 4px; /* BÁJALO: Antes estaba en 10px u 8px. Bájalo a 4px o 2px */
}

.item-idi { 
  display: flex; 
  gap: 10px; 
  margin-bottom: 12px; 
  font-size: 0.95rem; 
  color: #333;
  line-height: 1.4;
}

.punto-azul { color: #007bff; }
.punto-verde { color: #28a745; }

@media (max-width: 992px) {
  .grid-horizontal { grid-template-columns: 1fr; }
  .contenido-hub { padding-top: 150px; }
}
</style>