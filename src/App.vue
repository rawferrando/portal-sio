<script setup>
import { ref } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Instrumentacion from './components/Instrumentacion.vue'
import Embarcacion from './components/Embarcacion.vue'
import IntranetFondeos from './components/IntranetFondeos.vue'

// VITAL: Que ponga 'inicio' entre comillas y en minúsculas
const paginaActual = ref('inicio')
</script>

<template>
  <div id="layout-sio">
    <header class="header-icm">
      <div class="logo-area">
        <img src="./assets/logo-sio.jpg" class="logo-img" @click="paginaActual = 'inicio'" style="cursor: pointer;" />
      </div>
      <nav class="nav-idiomas">
        <a href="#" class="active">CA</a> | <a href="#">ES</a> | <a href="#">EN</a>
        <span class="separador"></span>
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

      <Instrumentacion 
        v-else-if="paginaActual === 'embarcacion'" 
        @volver="paginaActual = 'inicio'" 
      />

      <IntranetFondeos 
        v-else-if="paginaActual === 'intranet'" 
      />
    </main>

    <footer class="footer-sio">
       <p>Institut de Ciències del Mar (ICM-CSIC)</p>
       <p>📧 sio@icm.csic.es | 📍 Pg. Marítim de la Barceloneta, 37, 08003 Barcelona</p>
    </footer>
  </div>
</template>