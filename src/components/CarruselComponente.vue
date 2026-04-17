<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// Aquí puedes añadir las rutas de tus fotos. He puesto la de instrumentación por defecto.
const imagenes = ref([
  'https://raw.githubusercontent.com/rawferrando/portal-sio/main/src/assets/instrumentacion.jpg',
  // Añade más URLs de imágenes aquí separadas por comas
])

const indiceActual = ref(0)
let intervalo = null

const siguiente = () => {
  indiceActual.value = (indiceActual.value + 1) % imagenes.value.length
}

onMounted(() => {
  // Cambia de foto cada 5 segundos (5000 milisegundos)
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
  </div>
</template>

<style scoped>
.carrusel-wrapper {
  position: absolute; 
  top: 40px;
  left: 0;
  width: 100%;
  height: 600px; /* Ajusta la altura si lo quieres más grande o pequeño */
  overflow: hidden;
  z-index: 10; /* Lo pone por debajo de tu header (que tiene z-index 900) */
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

.carrusel-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /* Mantiene el tono azul corporativo para que todo se lea bien */
  background: linear-gradient(rgba(1, 33, 105, 0.4), rgba(1, 33, 105, 0.8)); 
}
</style>