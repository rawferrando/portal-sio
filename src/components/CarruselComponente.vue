<script setup>
import { ref, onMounted } from 'vue'

const indiceActual = ref(0)

// AQUÍ ESTÁN TUS IMÁGENES Y TUS TEXTOS
const slides = [
  {
    imagen: 'peces.png', 
    texto: 'Apoyo técnico especializado en el ámbito de las ciencias del mar'
  },
  {
    imagen: 'niskin.png', 
    texto: 'Equipo cualificado, con una amplia gama de instrumentación y recursos'
  },
  {
    imagen: 'oficinatecnica.jpeg', 
    texto: 'Herramientas y técnicas específicas de verificación para garantizar la calidad de los datos obtenidos en los estudios oceanográficos.'
  },
  {
  imagen: 'robotmari.jpg',
    texto: 'Asesoramiento y soluciones técnicas adaptadas a las necesidades específicas'
  },
  {
    imagen: 'marmarejada.jpg', 
    texto: 'Asesoramiento y soluciones técnicas adaptadas a las necesidades específicas'
  },
  {
    imagen: 'reflexesmar.jpg', 
    texto: 'Innovar, Desarrollar, Diseñar, Desplegar, Iplementar i Personalizar equipos '
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

/* 1. EL CONTENEDOR: Lo dejamos libre */
.carrusel-contenido {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 5; 
}
/* 2. EL TEXTO: Anclado fijamente por encima de los puntos */
.texto-slide {
  position: absolute;
  /* MAGIA: Esto clava la base del texto a 160px del fondo (los puntos están a 100px) */
  bottom: 170px; 
  left: 50%;
  transform: translateX(-50%); /* Lo centra de forma perfecta */
  
  width: 95%; /* De extremo a extremo como querías */
  color: rgba(255, 255, 255, 0.80); /* Un blanco casi puro para máxima legibilidad */
  font-size: 1.25rem; /* Letra un pelín más grande */
  line-height: 1.5;
  text-align: center; 
  margin: 0;
  padding: 0; 
  
  /* Doble sombra oscura para garantizar que se lea aunque el fondo sea claro */
  text-shadow: 1px 1px 4px rgba(0,0,0,0.9), 0px 0px 15px rgba(0,0,0,0.6); 
  font-weight: 400;
  letter-spacing: 0.5px;
}
/* --- ESTILOS DE LOS PUNTITOS --- */
.contenedor-puntos {
  position: absolute;
  bottom: 100px; 
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
    bottom: 70px; 
  }
.texto-slide {
    font-size: 0.95rem; 
    bottom: 110px; /* En móvil los puntos bajan, así que bajamos el texto también */
    width: 95%; /* Que aproveche a tope la pantalla pequeña */
  }
}
</style>