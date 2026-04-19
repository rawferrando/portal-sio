<script setup>
// Asegúrate de que siga siendo faviconsio.png (en minúsculas)
import logoTrozo from '../assets/faviconsio.png'

const imgMemoria = 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=600'
const imgNoticias = 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=600'
const imgEquipo  = 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=600'
</script>

<template>
  <section class="seccion-fichas-sio">
    <div class="contenedor-ancho">
      <div class="fichas-grid">

        <div class="ficha-sio c-navy" @click="$emit('cambiar-pagina', 'memoria')">
          <div class="capa-logo pos-1" :style="{ backgroundImage: `url(${logoTrozo})` }"></div>
          <div class="capa-foto" :style="{ backgroundImage: `url(${imgMemoria})` }"></div>
          <div class="contenido"><h3>Memoria anual</h3></div>
        </div>

        <div class="ficha-sio c-azul" @click="$emit('cambiar-pagina', 'noticias')">
          <div class="capa-logo pos-2" :style="{ backgroundImage: `url(${logoTrozo})` }"></div>
          <div class="capa-foto" :style="{ backgroundImage: `url(${imgNoticias})` }"></div>
          <div class="contenido"><h3>Noticias</h3></div>
        </div>

        <div class="ficha-sio c-icm" @click="$emit('cambiar-pagina', 'equipo')">
          <div class="capa-logo pos-3" :style="{ backgroundImage: `url(${logoTrozo})` }"></div>
          <div class="capa-foto" :style="{ backgroundImage: `url(${imgEquipo})` }"></div>
          <div class="contenido"><h3>Equipo SIO</h3></div>
        </div>

      </div>
    </div>
  </section>
</template>

<style scoped>
.seccion-fichas-sio {
  /* ¡ESTO ES LO QUE LAS BAJA! */
  margin-top: -50px; /* Si se quedan cortas, súbelo a 600px. Si se pasan, bájalo a 450px */
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
  width: 260px;
  height: 120px;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
  transition: all 0.4s ease;
}

/* Colores */
.c-navy  { background-color: #012169; }
.c-azul  { background-color: #005a87; }
.c-icm   { background-color: #0086c0; }

/* Logo de fondo */
.capa-logo {
  position: absolute;
  inset: 0;
  background-size: 250%; 
  opacity: 0.15;
  transition: 0.3s;
}
.pos-1 { background-position: left top; }
.pos-2 { background-position: center; }
.pos-3 { background-position: right bottom; }

/* Foto hover */
.capa-foto {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  opacity: 0;
  transform: scale(1.1);
  transition: all 0.5s ease;
}

/* Texto */
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
  font-size: 1.1rem;
  letter-spacing: 1px;
  font-weight: bold;
  text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
}

/* Hover */
.ficha-sio:hover { transform: translateY(-5px); box-shadow: 0 12px 25px rgba(0,0,0,0.25); }
.ficha-sio:hover .capa-foto { opacity: 1; transform: scale(1); }
.ficha-sio:hover .capa-logo { opacity: 0; }

@media (max-width: 768px) {
  .ficha-sio { width: 90%; height: 100px; }
  .seccion-fichas-sio { margin-top: 300px; } /* En móvil el carrusel es más corto */
}
</style>