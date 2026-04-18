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
  </div>
</template>

<style scoped>
/* Scoped asegura que este CSS no rompa tu App.vue */
.carrusel-wrapper {
  position: absolute; 
  /* 🛑 CLAVE PARA LA TOP BAR: Empieza justo debajo de ella */
  top: 40px; 
  left: 0;
  width: 100%;
  /* 📏 ALTURA DEL CARRUSEL: He subido un poco la altura para que se vea más profesional */
  height: 650px; 
  overflow: hidden;
  /* Layering: Se asegura de estar debajo del menú flotante */
  z-index: 10; 
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
/* --- ADAPTACIÓN DEL CARRUSEL PARA MÓVILES --- */
@media (max-width: 768px) {
  .carrusel-wrapper {
    height: 350px; /* En lugar de 650px, lo hacemos más manejable en móvil */
  }
}
</style>