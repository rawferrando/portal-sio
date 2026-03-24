<script setup>
import { ref, onMounted } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Instrumentacion from './components/Instrumentacion.vue'

const vistaActual = ref('inicio')
const menuPrivadoVisible = ref(false)
const usuarioLogueadoSio = ref(false)
const inputUsuario = ref('')
const inputPassword = ref('')
const errorLogin = ref(false)

onMounted(() => {
  if (sessionStorage.getItem('sio_auth') === 'true') {
    usuarioLogueadoSio.value = true
  }
})

const intentarLogin = () => {
  if (inputUsuario.value === 'admin' && inputPassword.value === 'sio2026') {
    sessionStorage.setItem('sio_auth', 'true')
    usuarioLogueadoSio.value = true
    errorLogin.value = false
    menuPrivadoVisible.value = false
    vistaActual.value = 'intranet'
  } else {
    errorLogin.value = true
  }
}

const cerrarSesion = () => {
  sessionStorage.removeItem('sio_auth')
  usuarioLogueadoSio.value = false
  vistaActual.value = 'inicio'
}

const irAIntranet = () => {
  vistaActual.value = 'intranet'
  menuPrivadoVisible.value = false
  window.scrollTo(0, 0)
}

const irAInstrumentacion = () => { 
  vistaActual.value = 'instrumentacion'
  window.scrollTo(0, 0)
}

const volverAInicio = () => { 
  vistaActual.value = 'inicio' 
  window.scrollTo(0, 0)
}
</script>

<template>
  <div class="app-container">
    <header class="main-header">
      <div class="contenedor-cabecera">
        <div class="logo-area">
          <img src="./assets/logo-sio.jpg" alt="Logo SIO" class="imagen-logo" @click="volverAInicio" style="cursor:pointer;" />
        </div>
        <nav class="menu-principal">
          <button class="btn-intranet" @click="menuPrivadoVisible = !menuPrivadoVisible">
            <span>{{ usuarioLogueadoSio ? '🔒 Admin SIO' : '👤 Área Privada' }}</span>
          </button>
          <div v-if="menuPrivadoVisible" class="menu-desplegable-privado">
            <div v-if="!usuarioLogueadoSio" class="formulario-login-menu">
              <input v-model="inputUsuario" type="text" placeholder="Usuario" />
              <input v-model="inputPassword" type="password" placeholder="Pass" />
              <button @click="intentarLogin" class="btn-entrar-login">Acceder</button>
            </div>
            <div v-else class="menu-acciones-intranet">
              <button @click="irAIntranet">➕ Añadir Instrumentación</button>
              <button @click="cerrarSesion" class="btn-cerrar-sesion-interna">🚪 Cerrar Sesión</button>
            </div>
          </div>
        </nav>
      </div>
    </header>

    <main class="main-content">
      <QuienesSomos v-if="vistaActual === 'inicio'" @cambiar-pagina="irAInstrumentacion" />
      <Instrumentacion v-else-if="vistaActual === 'instrumentacion'" @volver="volverAInicio" />
      
      <div v-else-if="vistaActual === 'intranet'" class="vista-intranet">
        <button @click="volverAInicio" class="btn-volver">⬅ Volver al Inicio</button>
        <h2>🛡️ Intranet SIO - Gestión de Equipos</h2>
        <p>Panel de administración para el alta de nuevos activos.</p>
      </div>
    </main>

    <footer class="footer-sio">
      <p><strong>Institut de Ciències del Mar (ICM-CSIC)</strong></p>
      <p>📧 sio@icm.csic.es | 📍 Pg. Marítim de la Barceloneta, 37, 08003 Barcelona</p>
    </footer>
  </div>
</template>

<style>
body { margin: 0; font-family: 'Segoe UI', sans-serif; background-color: #f4f7f9; }
.app-container { display: flex; flex-direction: column; min-height: 100vh; }
.main-header { background-color: #005596; color: white; padding: 10px 0; border-bottom: 3px solid #003366; }
.contenedor-cabecera { display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.imagen-logo { height: 55px; }
.main-content { flex: 1; width: 100%; max-width: 1200px; margin: 0 auto; padding: 30px 20px; box-sizing: border-box; }

.footer-sio { background-color: #005596; color: white; text-align: center; padding: 25px 20px; margin-top: auto; border-top: 3px solid #003366; }
.footer-sio p { margin: 5px 0; }

.btn-intranet { background: white; color: #005596; border: none; padding: 8px 18px; border-radius: 4px; cursor: pointer; font-weight: bold; }
.menu-desplegable-privado { position: absolute; right: 20px; background: white; border: 1px solid #ccc; padding: 20px; z-index: 100; box-shadow: 0 4px 12px rgba(0,0,0,0.15); border-radius: 8px; }
.formulario-login-menu { display: flex; flex-direction: column; gap: 10px; }
.btn-entrar-login { background: #005596; color: white; border: none; padding: 10px; cursor: pointer; border-radius: 4px; font-weight: bold; }
.menu-acciones-intranet button { display: block; width: 100%; padding: 10px; border: none; background: none; text-align: left; cursor: pointer; border-bottom: 1px solid #eee; }
.btn-cerrar-sesion-interna { color: #dc3545 !important; }
</style>