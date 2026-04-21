<script setup>
import { ref, onMounted } from 'vue'

const indiceActual = ref(0)

// AQUÍ ESTÁN TUS IMÁGENES Y TUS TEXTOS
const slides = [
  {
    imagen: 'https://raw.githubusercontent.com/rawferrando/portal-sio/main/src/assets/instrumentacion.jpg', 
    texto: 'Apoyo técnico especializado a grupos de investigación y proyectos en el ámbito de las ciencias del mar. Proporcionamos soluciones técnicas adaptadas a las necesidades específicas de cada cliente, así como asesoramiento experto basado en años de experiencia en el sector.'
  },
  {
    imagen: 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&w=1200', 
    texto: 'Equipo altamente cualificado y con una amplia gama de instrumentación y recursos, lo que nos permite innovar, desarrollar y personalizar equipos, así como diseñar, desplegar e implementar sistemas avanzados de adquisición de datos, tanto fijos como móviles.'
  },
  {
    imagen: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200', 
    texto: 'Herramientas y técnicas específicas de verificación para garantizar la calidad de los datos obtenidos en los estudios oceanográficos.'
  }
]

// Esto hace que el carrusel se mueva solo cada 6 segundos
onMounted(() => {
  setInterval(() => {
    indiceActual.value = (indiceActual.value + 1) % slides.length
  }, 6000)
})
</script>

<template>
  <div class="carrusel-wrapper">
    
    <div class="carrusel-inner" :style="{ transform: `translateX(-${indiceActual * 100}%)` }">
      <div class="carrusel-slide" v-for="(slide, index) in slides" :key="index">
        
        <img :src="slide.imagen" alt="Slide del SIO" class="carrusel-img">
        <div class="carrusel-overlay"></div>
        
        <div class="carrusel-contenido">
          <div class="contenedor-ancho">
            <p class="texto-slide">{{ slide.texto }}</p>
          </div>
        </div>

      </div>
    </div>

    <div class="contenedor-puntos">
      <span 
        v-for="(slide, index) in slides" 
        :key="'punto-' + index"
        class="punto" 
        :class="{ activo: indiceActual === index }"
        @click="indiceActual = index"
      ></span>
    </div>

  </div>
</template>

<style scoped>
/* --- ESTRUCTURA PRINCIPAL DEL CARRUSEL --- */
/* 1. MÁS ALTURA AL CARRUSEL */
.carrusel-wrapper {
  position: relative !important;
  width: 100%;
  overflow: hidden;
  margin-top: -140px !important; 
  top: 0;
  left: 0;
  /* ¡PASAMOS DE 650px A 850px! (Si lo quieres más grande pon 900px) */
  height: 750px; 
  z-index: 1 !important; 
}

.carrusel-inner {
  display: flex;
  height: 100%;
  transition: transform 1s ease-in-out; 
}

.carrusel-slide {
  min-width: 100%;
  height: 100%;
  position: relative;
}

.carrusel-img {
  width: 100%;
  height: 100%;
  object-fit: cover; 
}

/* El degradado oscuro para que se vea el menú y los textos */
.carrusel-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(rgba(1, 33, 105, 0.4), rgba(1, 33, 105, 0.8)); 
}

/* --- ESTILOS DEL TEXTO --- */
.carrusel-contenido {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center; 
  z-index: 5; 
}

/* 2. CENTRAR EL TEXTO */
.texto-slide {
  color: white;
  font-size: 1.4rem; 
  line-height: 1.6;
  max-width: 800px; 
  margin: 0;
  /* Quitamos el padding-bottom de antes para que se centre perfectamente */
  padding-bottom: 0px; 
  /* Le damos un poco de margen arriba para compensar la barra del menú */
  padding-top: 140px; 
  text-shadow: 0 2px 6px rgba(0,0,0,0.8); 
  font-weight: 400;
  letter-spacing: 0.5px;
}

/* --- ESTILOS DE LOS PUNTITOS --- */
.contenedor-puntos {
  position: absolute;
  bottom: 180px; 
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 15px;
  z-index: 999; 
}

.punto {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  border: 1px solid white;
  background-color: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 1px 2px rgba(0,0,0,0.5); 
}

.punto.activo {
  background-color: white;
  transform: scale(1.2);
}

.punto:hover {
  background-color: rgba(255, 255, 255, 0.8);
}

/* --- ADAPTACIÓN PARA MÓVILES --- */
@media (max-width: 768px) {
.carrusel-wrapper {
    /* También lo hacemos bastante más alto en el móvil */
    height: 650px !important; 
  }
  .contenedor-puntos {
    bottom: 130px; 
  }
.texto-slide {
    font-size: 1rem; 
    padding: 0 20px;
    /* Centrado real en móvil */
    padding-bottom: 0px; 
    padding-top: 65px; 
    text-align: center; 
  }
}
</style>