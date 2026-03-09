<script setup>
import { ref } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import RecursosTecnicos from './components/RecursosTecnicos.vue'
import IntranetFondeos from './components/IntranetFondeos.vue'

// Este es el interruptor. Por defecto está en 'false' (muestra la web pública)
const mostrarIntranet = ref(false)
</script>

<template>
  <div id="layout-sio">
    <header class="header-icm">
      <div class="logo-area">
        <img src="./assets/logo-sio.jpg" alt="Logo SIO" class="logo-img" /> 
      </div>
      <nav class="nav-idiomas">
        <a href="#" class="active">CA</a> | <a href="#">ES</a> | <a href="#">EN</a>
        
        <span class="separador">|</span>
        <a href="#" @click.prevent="mostrarIntranet = !mostrarIntranet" class="enlace-privado" title="Área de Personal">
          <span v-if="!mostrarIntranet">🔒</span>
          <span v-else>Volver al portal</span>
        </a>
      </nav>
    </header>

    <main class="contenedor-principal">
      
      <div v-if="!mostrarIntranet">
        <QuienesSomos />
        <hr />
        <RecursosTecnicos />
      </div>

      <div v-else>
        <IntranetFondeos />
      </div>

    </main>

    <footer class="footer-sio">
      <p>Institut de Ciències del Mar (ICM-CSIC)</p>
      <p>📧 sio@icm.csic.es | 📍 Port Olímpic de Barcelona</p>
    </footer>
  </div>
</template>

<style>
:root {
  var(--azul-sio-real): #005596; 
}

body, html {
  margin: 0;
  padding: 0;
  width: 100%;
}

#layout-sio {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
  width: 100%;
}

.header-icm {
  background-color: var(--azul-sio-real);
  color: white;
  padding: 1rem 4%; 
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  box-sizing: border-box;
}

.logo-img {
  height: 90px; 
  width: auto;
}

.nav-idiomas {
  display: flex;
  align-items: center;
}

.nav-idiomas a {
  color: white;
  text-decoration: none;
  margin: 0 5px;
}

/* Estilos para que el acceso sea muy discreto */
.separador {
  color: rgba(255, 255, 255, 0.3);
  margin: 0 10px;
}

.enlace-privado {
  color: rgba(255, 255, 255, 0.5) !important;
  font-size: 0.85rem;
  transition: opacity 0.3s;
}

.enlace-privado:hover {
  opacity: 1;
}

.contenedor-principal {
  width: 100% !important;   
  max-width: none !important; 
  margin: 0;
  padding: 3rem 4%; 
  box-sizing: border-box;   
  min-height: 60vh; /* Asegura que el pie de página no se suba mucho */
}

.footer-sio {
  text-align: center;
  padding: 2.5rem;
  background: #1a1a1a;
  color: white;
  width: 100%;
  box-sizing: border-box;
}

hr {
  margin: 4rem 0;
  border: 0;
  border-top: 1px solid #eee;
}
</style>