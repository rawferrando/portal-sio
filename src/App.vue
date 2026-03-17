<script setup>
import { ref } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Instrumentacion from './components/Instrumentacion.vue'
import Embarcacion from './components/Embarcacion.vue'
import Proyectos from './components/Proyectos.vue'
import Diseno from './components/Diseno.vue'
import IntranetFondeos from './components/IntranetFondeos.vue'
import FormularioSensor from './components/FormularioSensor.vue'

// Control de navegación y seguridad
const paginaActual = ref('inicio')
const estaAutenticado = ref(false)
const usuarioInput = ref('')
const passwordInput = ref('')

// Función de acceso (Login visual)
const intentarLogin = () => {
  if (usuarioInput.value === 'admin' && passwordInput.value === 'sio2026') {
    estaAutenticado.value = true // ¡Abre la puerta!
  } else {
    alert("❌ Credenciales incorrectas.")
    usuarioInput.value = ''
    passwordInput.value = ''
  }
}

// Función para salir
const salir = () => {
  estaAutenticado.value = false
  paginaActual.value = 'inicio'
  usuarioInput.value = ''
  passwordInput.value = ''
}
</script>

<template>
  <div id="layout-sio">
    <header class="header-icm">
      <div class="logo-area">
        <img src="./assets/logo-sio.jpg" class="logo-img" @click="paginaActual = 'inicio'" alt="Logo SIO" />
      </div>
      <nav class="nav-idiomas">
        <span>CA | ES | EN</span>
        <a href="#" @click.prevent="paginaActual = 'intranet'" class="enlace-privado">
          {{ estaAutenticado ? '🔓 Salir' : '🔒' }}
        </a>
      </nav>
    </header>

    <main class="contenedor-principal">
      
      <div v-if="paginaActual !== 'intranet'">
        <QuienesSomos v-if="paginaActual === 'inicio'" @camb