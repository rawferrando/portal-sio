<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// ✨ AQUÍ ESTÁ EL CAMBIO: Ahora tenemos 3 fotos diferentes de ejemplo ✨
const imagenes = ref([
  // Imagen 1 (Vuestra): Instrumentación
  'https://raw.githubusercontent.com/rawferrando/portal-sio/main/src/assets/instrumentacion.jpg',
  // Imagen 2 (Ejemplo): Barco Oceanográfico
  'https://images.unsplash.com/photo-1518107616985-bd48230d3b20?q=80&w=1600&auto=format&fit=crop',
  // Imagen 3 (Ejemplo): Equipo de tecnología marina
  'https://images.unsplash.com/photo-1582967702081-4bf917531776?q=80&w=1600&auto=format&fit=crop'
])

const indiceActual = ref(0)
let intervalo = null

const siguiente = () => {
  indiceActual.value = (indiceActual.value + 1) % imagenes.value.length
}

onMounted(() => {
  // Cambia de foto cada 5 segundos
  intervalo = setInterval(siguiente, 5000) 
})

onUnmounted(() => {
  clearInterval(intervalo)
})
</script>

<template>
  <div class="carrusel-wrapper">
    
    <div class="carrusel-inner" :style="{ transform: `translateX(-${indiceActual * 100}%)` }">
      <div class="carrusel-slide" v-for="(img, index) in imagenes" :key="index">
        <img :src="img" alt="Slide del SIO" class="carrusel-img">
        <div class="carrusel-overlay"></div>
      </div>
    </div>

    <div class="contenedor-puntos">
      <span 
        v-for="(img, index) in imagenes" 
        :key="'punto-' + index"
        class="punto" 
        :class="{ activo: indiceActual === index }"
        @click="indiceActual = index"
      ></span>
    </div>

  </div>
</template>

<style scoped>
/* Scoped asegura que este CSS no rompa tu App.vue */

.carrusel-wrapper {
  position: relative; 
  
  /* 🔥 LA MAGIA PARA QUITAR LA FRANJA BLANCA EN TODAS LAS PANTALLAS */
  margin-top: -140px !important; /* Tira de la foto hacia arriba para tapar el hueco */
  top: 0; /* Sustituimos tu top: 40px por 0 para que no lo empuje hacia abajo */
  left: 0;
  width: 100%;
  
  /* 📏 ALTURA DEL CARRUSEL */
  height: 650px; 
  overflow: hidden;
  
  /* Layering: Capa baja (1) para quedarse por detrás del menú y los logos */
  z-index: 0 !important; 
}

.carrusel-inner {
  display: flex;
  height: 100%;
  /* Transición suave y elegante de 1 segundo al cambiar de foto */
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
  /* Importante: Ajusta la foto sin deformarla */
  object-fit: cover; 
}

.carrusel-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /* Degradado sutil con el azul SIO para unificar el diseño */
  background: linear-gradient(rgba(1, 33, 105, 0.4), rgba(1, 33, 105, 0.7)); 
}

/* --- ESTILOS DE LOS PUNTITOS --- */
.contenedor-puntos {
  position: absolute;
  bottom: 90px; /* Separación desde abajo */
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
  z-index: 999; /* Por encima de la foto y el degradado */
}

.punto {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  border: 1.5px solid white;
  background-color: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 1px 3px rgba(0,0,0,0.4); /* Sombrita para que se vean siempre */
}

.punto.activo {
  background-color: white;
  transform: scale(1.3);
}

.punto:hover {
  background-color: rgba(255, 255, 255, 0.8);
}

/* --- ADAPTACIÓN DEL CARRUSEL PARA MÓVILES --- */
@media (max-width: 768px) {
  .carrusel-wrapper {
    height: 400px; /* En móviles el carrusel queda mejor si es más bajito */
  }
  .contenedor-puntos {
    bottom: 60px; /* Bajamos los puntos porque la foto es más pequeña */
  }
}
</style>