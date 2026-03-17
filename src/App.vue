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
        <a href="#">CA</a> | <a href="#">ES</a> | <a href="#">EN</a>
        <a href="#" @click.prevent="gestionarAcceso" class="enlace-privado">
          {{ paginaActual === 'intranet' ? '🔓 Salir' : '🔒' }}
        </a>
      </nav>
    </header>

    <main class="contenedor-principal">
      <div v-if="paginaActual !== 'intranet'" class="vista-publica">
        <QuienesSomos v-if="paginaActual === 'inicio'" @cambiar-pagina="paginaActual = $event" />
        <Instrumentacion v-else-if="paginaActual === 'instrumentacion'" @volver="paginaActual = 'inicio'" />
        <Embarcacion v-else-if="paginaActual === 'embarcacion'" @volver="paginaActual = 'inicio'" />
        <Proyectos v-else-if="paginaActual === 'proyectos'" @volver="paginaActual = 'inicio'" />
        <Diseno v-else-if="paginaActual === 'diseno'" @volver="paginaActual = 'inicio'" />
      </div>

      <div v-else class="vista-privada">
        <FormularioSensor />
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
/* Estilos generales */
#layout-sio { font-family: 'Segoe UI', Arial, sans-serif; display: flex; flex-direction: column; min-height: 100vh; color: #333; }
.header-icm { background-color: #005596; color: white; display: flex; justify-content: space-between; align-items: center; padding: 1rem 5%; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
.logo-img { height: 80px; width: auto; cursor: pointer; }
.nav-idiomas a { color: white; text-decoration: none; font-weight: bold; margin: 0 5px; }
.enlace-privado { margin-left: 15px; font-size: 1.2rem; cursor: pointer; text-decoration: none; }

/* Contenedor principal */
.contenedor-principal { flex: 1; padding: 3rem 5%; max-width: 1200px; margin: 0 auto; width: 100%; }

/* Estilo dedicado para ordenar la Intranet */
.vista-privada { display: flex; flex-direction: column; gap: 40px; align-items: center; width: 100%; }

/* Footer sticky */
.footer-sio { background-color: #005596; color: white; text-align: center; padding: 2rem 1rem; margin-top: auto; font-size: 0.9rem; }
.footer-sio p { margin: 5px 0; }
</style>