<script setup>
import { ref, onMounted } from 'vue'

const currentSlide = ref(0)
const slides = [
  {
    image: 'https://images.unsplash.com/photo-1518152006812-edab29b069ac?auto=format&fit=crop&w=1920&q=80',
    title: 'Ingeniería Oceánica de Vanguardia',
    text: 'Soporte tecnológico avanzado para la comunidad investigadora marina.'
  },
  {
    image: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1920&q=80',
    title: 'Innovación Tecnológica',
    text: 'Diseño y desarrollo de prototipos e instrumentación a medida.'
  }
]

onMounted(() => {
  setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.length
  }, 5000)
})
</script>

<template>
  <div class="home-sio">
    <section class="hero-carrusel">
      <div v-for="(slide, index) in slides" :key="index" 
           class="slide" :class="{ active: currentSlide === index }"
           :style="{ backgroundImage: `url(${slide.image})` }">
        <div class="slide-overlay">
          <div class="contenedor-ancho">
            <h2>{{ slide.title }}</h2>
            <p>{{ slide.text }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="contenedor-ancho grid-servicios">
      <div class="tarjeta-sio" @click="$emit('cambiar-pagina', 'servicios')">
        <div class="icono">⚙️</div>
        <h3>Servicios</h3>
        <p>Catálogo de instrumentación y soporte operativo.</p>
      </div>
      <div class="tarjeta-sio" @click="$emit('cambiar-pagina', 'proyectos')">
        <div class="icono">📂</div>
        <h3>Proyectos</h3>
        <p>Soporte técnico y logístico para campañas.</p>
      </div>
      <div class="tarjeta-sio" @click="$emit('cambiar-pagina', 'idi')">
        <div class="icono">💡</div>
        <h3>Desarrollo I+D+i</h3>
        <p>Innovación tecnológica y prototipos.</p>
      </div>
    </section>
  </div>
</template>

<style scoped>
.hero-carrusel { height: 500px; position: relative; overflow: hidden; background: #0a2540; }
.slide { position: absolute; inset: 0; background-size: cover; background-position: center; opacity: 0; transition: opacity 1s ease-in-out; }
.slide.active { opacity: 1; }
.slide-overlay { height: 100%; background: rgba(10, 37, 64, 0.5); display: flex; align-items: center; color: white; }
.slide-overlay h2 { font-size: 3.5rem; font-weight: 300; margin-bottom: 10px; }
.slide-overlay p { font-size: 1.4rem; opacity: 0.9; }

.grid-servicios { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin-top: -60px; z-index: 10; position: relative; }
.tarjeta-sio { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: center; cursor: pointer; transition: 0.3s; }
.tarjeta-sio:hover { transform: translateY(-10px); }
.tarjeta-sio .icono { font-size: 3rem; margin-bottom: 15px; }
.tarjeta-sio h3 { color: #0a2540; margin-bottom: 10px; }
</style>