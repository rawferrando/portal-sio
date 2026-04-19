<script setup>
// IMPORTANTE: Asegúrate de que faviconsio.png esté en src/assets/
import logoTrozo from '../assets/faviconsio.png'

// Imágenes para el efecto al pasar el ratón
const imgMemoria = 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=600'
const imgEquipo  = 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=600'
const imgNoticia = 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=600'
const imgDotacion = 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=600'
</script>

<template>
  <section class="seccion-fichas-sio">
    <div class="contenedor-ancho">
      <div class="fichas-grid">

        <div class="ficha-sio c-navy" @click="$emit('cambiar-pagina', 'memoria')">
          <div class="capa-logo pos-1" :style="{ backgroundImage: `url(${logoTrozo})` }"></div>
          <div class="capa-foto" :style="{ backgroundImage: `url(${imgMemoria})` }"></div>
          <div class="contenido"><h3>MEMORIA ANUAL</h3></div>
        </div>

        <div class="ficha-sio c-azul" @click="$emit('cambiar-pagina', 'equipo')">
          <div class="capa-logo pos-2" :style="{ backgroundImage: `url(${logoTrozo})` }"></div>
          <div class="capa-foto" :style="{ backgroundImage: `url(${imgEquipo})` }"></div>
          <div class="contenido"><h3>EQUIPO SIO</h3></div>
        </div>

        <div class="ficha-sio c-medio" @click="$emit('cambiar-pagina', 'noticias')">
          <div class="capa-logo pos-3" :style="{ backgroundImage: `url(${logoTrozo})` }"></div>
          <div class="capa-foto" :style="{ backgroundImage: `url(${imgNoticia})` }"></div>
          <div class="contenido"><h3>NOTICIAS</h3></div>
        </div>

        <div class="ficha-sio c-icm" @click="$emit('cambiar-pagina', 'dotacion')">
          <div class="capa-logo pos-4" :style="{ backgroundImage: `url(${logoTrozo})` }"></div>
          <div class="capa-foto" :style="{ backgroundImage: `url(${imgDotacion})` }"></div>
          <div class="contenido"><h3>DOTACIÓN</h3></div>
        </div>

      </div>
    </div>
  </section>
</template>

<style scoped>
.seccion-fichas-sio {
  padding: 60px 0;
  background: white;
  width: 100%;
  position: relative;
  z-index: 20;
}

.fichas-grid {
  display: flex;
  gap: 15px;
  justify-content: center; /* Centrado total */
  flex-wrap: wrap;
}

.ficha-sio {
  width: 220px; /* Tamaño compacto */
  height: 100px;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
}

/* Colores en escala de azules */
.c-navy  { background-color: #012169; }
.c-azul  { background-color: #004a87; }
.c-medio { background-color: #0071b2; }
.c-icm   { background-color: #0086c0; }

.capa-logo {
  position: absolute;
  inset: 0;
  background-size: 250%; /* Zoom al logo */
  opacity: 0.15;
  transition: 0.3s;
}
/* Posiciones diferentes para que cada ficha use un "trozo" del logo */
.pos-1 { background-position: left top; }
.pos-2 { background-position: right top; }
.pos-3 { background-position: left bottom; }
.pos-4 { background-position: right bottom; }

.capa-foto {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  opacity: 0;
  transition: 0.4s ease;
}

.contenido {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}

.contenido h3 {
  color: white;
  margin: 0;
  font-size: 0.9rem;
  letter-spacing: 1.5px;
  font-weight: bold;
}

/* Efecto hover */
.ficha-sio:hover { transform: translateY(-5px); }
.ficha-sio:hover .capa-foto { opacity: 1; }
.ficha-sio:hover .capa-logo { opacity: 0; }

@media (max-width: 768px) {
  .ficha-sio { width: 45%; height: 90px; }
}
</style>