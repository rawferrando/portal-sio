<script setup>
import { ref } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Instrumentacion from './components/Instrumentacion.vue'
import Embarcacion from './components/Embarcacion.vue'
import IntranetFondeos from './components/IntranetFondeos.vue'

const paginaActual = ref('inicio')
</script>

<template>
  <div id="layout-sio">
    <header class="header-icm">
      <div class="logo-area">
        <img 
          src="./assets/logo-sio.jpg" 
          class="logo-img" 
          @click="paginaActual = 'inicio'" 
          alt="Logo SIO"
        />
      </div>
      <nav class="nav-idiomas">
        <a href="#">CAT</a> | <a href="#">ES</a> | <a href="#">EN</a>
        <a href="#" @click.prevent="paginaActual = 'intranet'" class="enlace-privado">
          {{ paginaActual === 'intranet' ? '🔓 Volver' : '🔒' }}
        </a>
      </nav>
    </header>

    <main class="contenedor-principal">
      <QuienesSomos 
        v-if="paginaActual === 'inicio'" 
        @cambiar-pagina="paginaActual = $event" 
      />
      <Instrumentacion 
        v-else-if="paginaActual === 'instrumentacion'" 
        @volver="paginaActual = 'inicio'" 
      />
      <Embarcacion 
        v-else-if="paginaActual === 'embarcacion'" 
        @volver="paginaActual = 'inicio'" 
      />
      <IntranetFondeos 
        v-else-if="paginaActual === 'intranet'" 
      />
    </main>

    <footer class="footer-sio">
      <p><strong>Institut de Ciències del Mar (ICM-CSIC)</strong></p>
      <p>📧 sio@icm.csic.es | 📍 Pg. Marítim de la Barceloneta, 37, 08003 Barcelona</p>
    </footer>
  </div>
</template>

<style>
/* Reset básico para que no queden huecos blancos */
body { margin: 0; padding: 0; }

#layout-sio {
  font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Cabecera Azul */
.header-icm {
  background-color: #005596;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 5%;
}

/* Domamos el logo gigante */
.logo-img {
  height: 120px; /* <--- Esto es lo que lo hace pequeño y elegante */
  width: auto;
  cursor: pointer;
}

.nav-idiomas a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

/* Contenido centrado */
.contenedor-principal {
  flex: 1;
  padding: 2rem 5%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Footer Azul Centrado */
.footer-sio {
  background-color: #005596;
  color: white;
  text-align: center; /* Centra el texto */
  padding: 2rem 1rem;
  margin-top: auto;
}

.footer-sio p { margin: 0.5rem 0; }
</style>
