<script setup>
import { ref, onMounted } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Proyectos from './components/Proyectos.vue'
import Servicios from './components/Servicios.vue'
import DesarrolloIdi from './components/DesarrolloIdi.vue'
import IntranetPanel from './components/IntranetPanel.vue'

const vistaActual = ref('inicio')
const usuarioLogueadoSio = ref(false)
const mostrarModalLogin = ref(false) 
const inputUsuario = ref('')
const inputPassword = ref('')

onMounted(() => {
  if (sessionStorage.getItem('sio_auth') === 'true') {
    usuarioLogueadoSio.value = true
  }
})

const manejarClicIntranet = () => {
  if (usuarioLogueadoSio.value) {
    cambiarVista('intranet')
  } else {
    mostrarModalLogin.value = true 
  }
}

const intentarLogin = () => {
  if (inputUsuario.value === 'admin' && inputPassword.value === 'sio2026') {
    sessionStorage.setItem('sio_auth', 'true')
    usuarioLogueadoSio.value = true
    mostrarModalLogin.value = false 
    cambiarVista('intranet')
  } else {
    alert("Usuario o contraseña incorrectos")
  }
}

const cerrarModalLogin = () => {
  mostrarModalLogin.value = false
  inputUsuario.value = ''
  inputPassword.value = ''
}

const cambiarVista = (nuevaVista) => { 
  vistaActual.value = nuevaVista
  window.scrollTo(0, 0)
}

const volverAInicio = () => { 
  cambiarVista('inicio')
}
</script>

<template>
  <div class="icm-layout">
    
    <div class="top-bar">
      <div class="contenedor-ancho top-bar-inner">
        <div class="top-links-left">
          <a href="#" class="top-link">Contacto</a>
        </div>
        <div class="top-links-right">
          <button class="btn-intranet-sio" @click="manejarClicIntranet">
            {{ usuarioLogueadoSio ? '🔓 Intranet' : '🔒 Intranet' }}
          </button>
          <div class="idiomas">
            <span class="active">ca</span> | <span>es</span> | <span>en</span>
          </div>
        </div>
      </div>
    </div>

    <header class="main-header">
      <div class="contenedor-ancho header-inner">
        
        <div class="sio-brand" @click="volverAInicio" style="cursor: pointer;">
          <img src="@/assets/logovector.png" alt="SIO" class="logo-sio-main">
        </div>

        <div class="nav-container">
          <nav class="nav-menu">
            <a href="#" @click.prevent="cambiarVista('inicio')" class="nav-item" :class="{ activo: vistaActual === 'inicio' }">Inicio</a>
            <a href="#" @click.prevent="cambiarVista('servicios')" class="nav-item" :class="{ activo: vistaActual === 'servicios' }">Servicios</a>
            <a href="#" @click.prevent="cambiarVista('proyectos')" class="nav-item" :class="{ activo: vistaActual === 'proyectos' }">Proyectos</a>
            <a href="#" @click.prevent="cambiarVista('idi')" class="nav-item" :class="{ activo: vistaActual === 'idi' }">I+D+i</a>
          </nav>
          <button class="btn-search">🔍</button>
        </div>

        <div class="institutional-seals">
          <img src="@/assets/logo-severo.png" alt="" class="seal-img">
          <img src="@/assets/logo-icm.png" alt="" class="seal-img">
        </div>
      </div>
    </header>

    <main class="contenido-principal">
      <QuienesSomos v-if="vistaActual === 'inicio'" @cambiar-pagina="cambiarVista" />
      <Proyectos v-else-if="vistaActual === 'proyectos'" @volver="volverAInicio" />
      <Servicios v-else-if="vistaActual === 'servicios'" @volver="volverAInicio" />
      <DesarrolloIdi v-else-if="vistaActual === 'idi'" @volver="volverAInicio" />
      <IntranetPanel v-else-if="vistaActual === 'intranet'" @volver="volverAInicio" />
    </main>

    <footer class="footer-icm">
      <div class="contenedor-ancho footer-content">
        <img src="@/assets/logo-csic.png" alt="" class="logo-csic-white">
        <div class="footer-info">
          <p><strong>Passeig Marítim de la Barceloneta, 37-49. 08003 Barcelona</strong></p>
          <p>© 2026 Servicio de Ingeniería Oceanográfica (SIO) - ICM-CSIC</p>
        </div>
      </div>
    </footer>

    <div v-if="mostrarModalLogin" class="modal-overlay" @click.self="cerrarModalLogin">
      <div class="modal-login">
        <h3>Acceso Restringido</h3>
        <p>Introduce tus credenciales del SIO</p>
        <input v-model="inputUsuario" type="text" placeholder="Usuario" />
        <input v-model="inputPassword" type="password" placeholder="Contraseña" @keyup.enter="intentarLogin" />
        <div class="modal-actions">
          <button @click="intentarLogin" class="btn-entrar">Acceder</button>
          <button @click="cerrarModalLogin" class="btn-cancelar">Cancelar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Top Bar */
.top-bar { background-color: white; border-bottom: 1px solid #e5e5e5; padding: 10px 0; font-size: 0.85rem; color: #666; }
.top-bar-inner { display: flex; justify-content: space-between; align-items: center; }
.top-link { color: #666; text-decoration: none; font-weight: bold; }
.btn-intranet-sio { background: none; border: none; color: #0088cc; font-weight: bold; cursor: pointer; margin-right: 15px; }
.idiomas .active { font-weight: bold; color: #333; }

/* Header */
.main-header { background: white; padding: 20px 0; position: sticky; top: 0; z-index: 1000; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
.header-inner { display: flex; justify-content: space-between; align-items: center; }
.logo-sio-main { height: 70px; width: auto; }

/* Navegación */
.nav-container { display: flex; align-items: center; gap: 20px; }
.nav-menu { display: flex; gap: 30px; }
.nav-item { text-decoration: none; color: #0a2540; font-weight: bold; font-size: 1.1rem; padding-bottom: 5px; border-bottom: 3px solid transparent; transition: 0.3s; }
.nav-item.activo, .nav-item:hover { color: #0088cc; border-bottom-color: #0088cc; }
.btn-search { background: none; border: none; font-size: 1.2rem; cursor: pointer; }

/* Sellos */
.institutional-seals { display: flex; gap: 15px; }
.seal-img { height: 45px; width: auto; }

/* Footer */
.footer-icm { background: #0a2540; color: white; padding: 50px 0; text-align: center; margin-top: 40px; }
.logo-csic-white { height: 60px; filter: brightness(0) invert(1); margin-bottom: 20px; }
</style>