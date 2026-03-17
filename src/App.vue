<script setup>
import { ref } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Instrumentacion from './components/Instrumentacion.vue'
import Embarcacion from './components/Embarcacion.vue'
import Proyectos from './components/Proyectos.vue'
import Diseno from './components/Diseno.vue'
import IntranetFondeos from './components/IntranetFondeos.vue'
import FormularioSensor from './components/FormularioSensor.vue'

const paginaActual = ref('inicio')

const gestionarAcceso = () => {
  if (paginaActual.value === 'intranet') {
    paginaActual.value = 'inicio';
  } else {
    const usuario = prompt("👤 USUARIO SIO:");
    if (usuario === "admin") {
      const password = prompt("🔑 CONTRASEÑA TÉCNICA:");
      if (password === "sio2026") {
        paginaActual.value = 'intranet';
      } else {
        alert("❌ Contraseña incorrecta.");
      }
    } else if (usuario !== null) {
      alert("❌ Usuario no reconocido.");
    }
  }
}
</script>

<template>
  <div id="layout-sio">
    <header class="header-icm">
      <div class="logo-area">
        <img src="./assets/logo-sio.jpg" class="logo-img" @click="paginaActual = 'inicio'" alt="Logo SIO" />
      </div>
      <nav class="nav-idiomas">
        <span>CAT | ES | EN</span>
        <a href="#" @click.prevent="gestionarAcceso" class="enlace-privado">
          {{ paginaActual === 'intranet' ? '🔓 Salir' : '🔒' }}
        </a>
      </nav>
    </header>

    <main class="contenedor-principal">
      <div v-if="paginaActual !== 'intranet'">
        <QuienesSomos v-if="paginaActual === 'inicio'" @cambiar-pagina="paginaActual = $event" />
        <Instrumentacion v-else-if="paginaActual === 'instrumentacion'" @volver="paginaActual = 'inicio'" />
        <Embarcacion v-else-if="paginaActual === 'embarcacion'" @volver="paginaActual = 'inicio'" />
        <Proyectos v-else-if="paginaActual === 'proyectos'" @volver="paginaActual = 'inicio'" />
        <Diseno v-else-if="paginaActual === 'diseno'" @volver="paginaActual = 'inicio'" />
      </div>

      <div v-else class="seccion-intranet">
        <h2 style="color: #005596;">⚙️ Panel de Gestión SIO</h2>
        <FormularioSensor />
        <hr />
        <IntranetFondeos />
      </div>
    </main>

    <footer class="footer-sio">
      <p><strong>Institut de Ciències del Mar (ICM-CSIC)</strong></p>
      <p>📧 sio@icm.csic.es | 📍 Pg. Marítim de la Barceloneta, 37, 08003 Barcelona</p>
    </footer>
  </div>
</template>

<style>
#layout-sio { font-family: Arial, sans-serif; display: flex; flex-direction: column; min-height: 100vh; }
.header-icm { background-color: #005596; color: white; display: flex; justify-content: space-between; align-items: center; padding: 1rem 5%; }
.logo-img { height: 80px; cursor: pointer; }
.nav-idiomas { display: flex; align-items: center; gap: 15px; font-weight: bold; color: white; }
.enlace-privado { font-size: 1.2rem; text-decoration: none; cursor: pointer; color: white; }
.contenedor-principal { flex: 1; padding: 2rem 5%; max-width: 1200px; margin: 0 auto; width: 100%; }
.seccion-intranet { display: flex; flex-direction: column; gap: 40px; align-items: center; width: 100%; }
hr { width: 100%; border: 0; border-top: 2px solid #ddd; }
.footer-sio { background-color: #005596; color: white; text-align: center; padding: 2rem 1rem; margin-top: auto; }
</style>