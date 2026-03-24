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

const nuevoEquipo = ref({ id: '', nombre: '', tipo: 'Sensores de Presión', fabricante: '' })

onMounted(() => {
  if (sessionStorage.getItem('sio_auth') === 'true') {
    usuarioLogueadoSio.value = true
  }
})

const intentarLogin = () => {
  if (inputUsuario.value === 'admin' && inputPassword.value === 'sio2026') {
    sessionStorage.setItem('sio_auth', 'true')
    usuarioLogueadoSio.value = true
    inputUsuario.value = ''
    inputPassword.value = ''
    errorLogin.value = false
    menuPrivadoVisible.value = false
    vistaActual.value = 'intranet'
  } else {
    errorLogin.value = true
    inputPassword.value = ''
  }
}

const cerrarSesion = () => {
  sessionStorage.removeItem('sio_auth')
  usuarioLogueadoSio.value = false
  menuPrivadoVisible.value = false
  if (vistaActual.value === 'intranet') vistaActual.value = 'inicio'
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

const guardarNuevoEquipo = () => {
  alert(`✅ Equipo ${nuevoEquipo.value.nombre} guardado.`)
  nuevoEquipo.value = { id: '', nombre: '', tipo: 'Sensores de Presión', fabricante: '' }
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
          <button class="btn-intranet" :class="{ 'logueado': usuarioLogueadoSio }" @click="menuPrivadoVisible = !menuPrivadoVisible">
            <span>Intranet SIO</span>
          </button>
          <div v-if="menuPrivadoVisible" class="menu-desplegable-privado">
            <div v-if="!usuarioLogueadoSio" class="formulario-login-menu">
              <input v-model="inputUsuario" type="text" placeholder="Usuario" />
              <input v-model="inputPassword" type="password" placeholder="Pass" />
              <button @click="intentarLogin" class="btn-entrar-login">Acceder</button>
            </div>
            <div v-else class="menu-acciones-intranet">
              <button @click="irAIntranet">➕ Añadir Equipo</button>
              <button @click="cerrarSesion" class="btn-cerrar-sesion-interna">🚪 Salir</button>
            </div>
          </div>
        </nav>
      </div>
    </header>

    <main class="main-content">
      <QuienesSomos v-if="vistaActual === 'inicio'" @cambiar-pagina="irAInstrumentacion" />
      <Instrumentacion v-else-if="vistaActual === 'instrumentacion'" @volver="volverAInicio" />
      <div v-else-if="vistaActual === 'intranet'" class="vista-intranet">
        <button @click="volverAInicio" class="btn-volver">⬅ Volver</button>
        <h2>🛡️ Alta de Equipos</h2>
      </div>
    </main>

    <footer class="footer-sio">
      <p><strong>Institut de Ciències del Mar (ICM-CSIC)</strong></p>
      <p>📧 sio@icm.csic.es | 📍 Pg. Marítim de la Barceloneta, 37, 08003 Barcelona</p>
    </footer>
  </div>
</template>

<style>
body { margin: 0; font-family: sans-serif; background-color: #f4f7f9; }
.app-container { display: flex; flex-direction: column; min-height: 100vh; }
.main-header { background-color: #005596; color: white; padding: 10px 0; }
.contenedor-cabecera { display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.imagen-logo { height: 50px; }
.main-content { flex: 1; padding: 20px; max-width: 1200px; margin: 0 auto; width: 100%; }

/* EL FOOTER AZUL Y CENTRADO QUE QUERÍAS */
.footer-sio {
  background-color: #005596;
  color: white;
  text-align: center;
  padding: 20px;
  margin-top: auto;
}
.footer-sio p { margin: 5px 0; }

.btn-intranet { background: white; color: #005596; border: none; padding: 8px 15px; border-radius: 4px; cursor: pointer; font-weight: bold; }
.menu-desplegable-privado { position: absolute; right: 20px; top: 60px; background: white; border: 1px solid #ccc; padding: 15px; z-index: 100; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
.formulario-login-menu { display: flex; flex-direction: column; gap: 10px; }
.btn-entrar-login { background: #005596; color: white; border: none; padding: 8px; cursor: pointer; }
</style>