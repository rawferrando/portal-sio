<script setup>
// 1️⃣ IMPORTACIÓN DE TUS NUEVOS FONDOS PNG
// Asegúrate de que los archivos estén en src/assets/ y se llamen exactamente así.
import bgRoig from '../assets/roig.png'
import bgVerd from '../assets/verd.png'
import bgBlue from '../assets/blue.png'
import bgGroc from '../assets/groc.png'

// Imágenes de fondo para el efecto hover (se mantienen)
const imgMemoria = 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=600'
const imgNoticias = 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=600'
const imgEquipo  = 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=600'
const imgBlueLab = 'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=600' 
</script>

<template>
  <section class="seccion-fichas-sio">
    <div class="contenedor-ancho">
      <div class="fichas-grid">

        <div class="ficha-sio text-white" :style="{ backgroundImage: `url(${bgRoig})` }" @click="$emit('cambiar-pagina', 'memoria')">
          <div class="capa-foto" :style="{ backgroundImage: `url(${imgMemoria})` }"></div>
          <div class="contenido"><h3>Memoria anual</h3></div>
        </div>

        <div class="ficha-sio text-white" :style="{ backgroundImage: `url(${bgVerd})` }" @click="$emit('cambiar-pagina', 'noticias')">
          <div class="capa-foto" :style="{ backgroundImage: `url(${imgNoticias})` }"></div>
          <div class="contenido"><h3>Noticias</h3></div>
        </div>

        <div class="ficha-sio text-white" :style="{ backgroundImage: `url(${bgGroc})` }" @click="$emit('cambiar-pagina', 'equipo')">
          <div class="capa-foto" :style="{ backgroundImage: `url(${imgEquipo})` }"></div>
          <div class="contenido"><h3>Equipo SIO</h3></div>
        </div>

        <div class="ficha-sio text-white" :style="{ backgroundImage: `url(${bgBlue})` }" @click="$emit('cambiar-pagina', 'bluelab')">
          <div class="capa-foto" :style="{ backgroundImage: `url(${imgBlueLab})` }"></div>
          <div class="contenido"><h3>BLUE Lab</h3></div>
        </div>

      </div>
    </div>
  </section>
</template>

<style scoped>
.seccion-fichas-sio {
  margin-top: -50px; 
  position: relative;
  z-index: 50;
  width: 100%;
  padding-bottom: 40px;
}

.fichas-grid {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
}

.ficha-sio {
  width: 250px; 
  height: 120px;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
  transition: all 0.4s ease;
  
  /* 🖼️ AJUSTES PARA TUS NUEVOS FONDOS PNG */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

/* 📸 CAPA DE FOTO HOVER (se mantiene) */
.capa-foto {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  opacity: 0;
  transform: scale(1.1);
  transition: all 0.5s ease;
  z-index: 1; /* Por encima del fondo PNG */
}

/* ✍️ AJUSTES DE TEXTO Y LEGIBILIDAD */
.contenido {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10; /* Por encima de la foto hover */
}

.contenido h3 {
  margin: 0;
  font-size: 1.1rem;
  letter-spacing: 1px;
  font-weight: bold;
}

/* ✅ CLASE PARA TEXTO BLANCO (Rojo, Verde, Azul) */
.text-white h3 {
  color: white;
  /* Sombra oscura sutil para resaltar sobre fondos de color */
  text-shadow: 1px 1px 3px rgba(0,0,0,0.6); 
}

/* ✅ CLASE PARA TEXTO OSCURO (Amarillo) */
.text-dark-navy h3 {
  color: #012169; /* Azul marino oscuro corporativo del SIO */
  text-shadow: none; /* No necesita sombra */
}

.ficha-sio {
  width: 250px; 
  height: 120px;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
  transition: all 0.4s ease;
  
  /* 🖼️ AJUSTES PARA TUS FONDOS PNG */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  
  /* 👇 LA CLAVE PARA ATENUAR 👇 */
  /* Añadimos una capa de color azul marino muy sutil (opacity 0.4) 
     que se superpone a la imagen de fondo */
  background-blend-mode: overlay; /* O 'multiply' para un efecto más oscuro */
  background-color: rgba(1, 33, 105, 0.4); 
}
/* Al hacer hover, mostramos la foto y ocultamos el color PNG */
.ficha-sio:hover .capa-foto { opacity: 1; transform: scale(1); }

@media (max-width: 768px) {
  .ficha-sio { width: 45%; height: 100px; }
  .seccion-fichas-sio { margin-top: -30px; } 
}
</style>