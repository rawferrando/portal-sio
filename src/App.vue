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

// Función para el login bonito
const intentarLogin = () => {
  if (usuarioInput.value === 'admin' && passwordInput.value === 'sio2026') {
    estaAutenticado.value = true // ¡Abre la puerta al panel!
  } else {
    alert("❌ Credenciales incorrectas. Inténtalo de nuevo.")
    usuarioInput.value = ''
    passwordInput.value = ''
  }
}

// Función para el botón de salir
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
        <span>CAT | ES | EN</span>
        <a href="#" @click.prevent="paginaActual = 'intranet'" class="enlace-privado">
          {{ estaAutenticado ? '🔓 Salir' : '🔒' }}
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
        
        <div v-if="!estaAutenticado" class="login-card">
          <h3 style="color: #005596;">🔐 Acceso Intranet SIO</h3>
          <p>Introduce tus credenciales para gestionar la base de datos.</p>
          <div class="form-login">
            <input v-model="usuarioInput" type="text" placeholder="Usuario (ej: admin)">
            <input v-model="passwordInput" type="password" placeholder="Contraseña">
            <button @click="intentarLogin" class="btn-entrar">Iniciar Sesión</button>
          </div>
        </div>

        <div v-else class="panel-control">
          <h2 style="color: #005596; margin-bottom: 20px;">⚙️ Panel de Gestión SIO</h2>
          
          <FormularioSensor />
          <hr style="width: 100%; border: 0; border-top: 1px solid #ccc; margin: 40px 0;" />
          <IntranetFondeos />
          
        </div>

      </div>
    </main>

    <footer class="footer-sio">
      <p><strong>Institut de Ciències del Mar (ICM-CSIC)</strong></p>
      <p>📧 sio@icm.csic.es | 📍 Pg. Marítim de la Barceloneta, 37, 08003 Barcelona</p>
    </footer>
  </div>
</template>

<style>
/* Estilos Globales */
#layout-sio { font-family: Arial, sans-serif; display: flex; flex-direction: column; min-height: 100vh; }
.header-icm { background-color: #005596; color: white; display: flex; justify-content: space-between; align-items: center; padding: 1rem 5%; }
.logo-img { height: 80px; cursor: pointer; }
.nav-idiomas { display: flex; align-items: center; gap: 15px; font-weight: bold; color: white; }
.enlace-privado { font-size: 1.2rem; text-decoration: none; cursor: pointer; color: white; }
.contenedor-principal { flex: 1; padding: 2rem 5%; max-width: 1200px; margin: 0 auto; width: 100%; }

/* Estructura Intranet */
.seccion-intranet { display: flex; flex-direction: column; align-items: center; width: 100%; }
.panel-control { width: 100%; display: flex; flex-direction: column; align-items: center; }

/* Estilos del Login Bonito */
.login-card { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); border-top: 6px solid #005596; text-align: center; max-width: 400px; margin: 50px auto; width: 100%;}
.login-card h3 { margin-top: 0; font-size: 1.6rem; }
.login-card p { color: #666; font-size: 0.9rem; margin-bottom: 25px; }
.form-login { display: flex; flex-direction: column; gap: 15px; }
.form-login input { padding: 12px; border: 1px solid #ddd; border-radius: 6px; font-size: 1rem; }
.btn-entrar { background: #005596; color: white; border: none; padding: 12px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 1.1rem; }
.btn-entrar:hover { background: #003d6b; }

.footer-sio { background-color: #005596; color: white; text-align: center; padding: 2rem 1rem; margin-top: auto; }
</style>