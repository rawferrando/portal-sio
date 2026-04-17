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
  if (nuevaVista === 'intranet' && !usuarioLogueadoSio.value) {
    mostrarModalLogin.value = true
    return
  }
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
          <a href="https://icm.csic.es" target="_blank">Web ICM-CSIC</a>
        </div>
        <div class="top-links-right">
          <button class="btn-intranet-sio" @click="manejarClicIntranet">
            {{ usuarioLogueadoSio ? '🔒 Admin SIO' : '👤 Intranet SIO' }}
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
          <img src="../assets/logovector.png" alt="Logo SIO" class="logo-sio-main">
          <div class="sio-text">
            <span class="sio-siglas">SIO</span>
            <span class="sio-nombre">Servicio de Ingeniería Oceanográfica</span>
          </div>
        </div>

        <nav class="nav-menu">
          <a href="#" @click.prevent="cambiarVista('inicio')" class="nav-item" :class="{ activo: vistaActual === 'inicio' }">Inicio</a>
          <a href="#" @click.prevent="cambiarVista('servicios')" class="nav-item" :class="{ activo: vistaActual === 'servicios' }">Servicios</a>
          <a href="#" @click.prevent="cambiarVista('proyectos')" class="nav-item" :class="{ activo: vistaActual === 'proyectos' }">Proyectos</a>
          <a href="#" @click.prevent="cambiarVista('idi')" class="nav-item" :class="{ activo: vistaActual === 'idi' }">I+D+i</a>
        </nav>

        <div class="institutional-seals">
          <img src="../assets/logo-severo.png" alt="Severo Ochoa" class="seal-img">
          <img src="../assets/logo-icm.png" alt="ICM" class="seal-img">
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
        <div class="footer-logo-csic">
          <img src="../assets/logo-csic.png" alt="CSIC" class="logo-csic-white">
        </div>
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
        <input v-model="inputUsuario" type="text" placeholder="Usuario" @keyup.enter="intentarLogin" />
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
/* Estructura General */
.icm-layout { display: flex; flex-direction: column; min-height: 100vh; }
.contenedor-ancho { max-width: 1400px; margin: 0 auto; padding: 0 20px; width: 100%; box-sizing: border-box; }

/* Barra Superior */
.top-bar { background-color: #f8f9fa; border-bottom: 1px solid #e9ecef; padding: 8px 0; font-size: 0.85rem; }
.top-bar-inner { display: flex; justify-content: space-between; align-items: center; }
.top-links-left a { color: #666; text-decoration: none; }
.top-links-right { display: flex; gap: 20px; align-items: center; }
.btn-intranet-sio { background: none; border: none; color: #0088cc; font-weight: bold; cursor: pointer; padding: 0; font-size: 0.85rem; }
.idiomas { color: #999; }
.idiomas .active { color: #333; font-weight: bold; }

/* Header */
.main-header { background: white; padding: 15px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 1000; }
.header-inner { display: flex; justify-content: space-between; align-items: center; }

/* Marca SIO (Izquierda) */
.sio-brand { display: flex; align-items: center; gap: 15px; }
.logo-sio-main { height: 60px; width: auto; }
.sio-text { display: flex; flex-direction: column; }
.sio-siglas { font-size: 1.6rem; font-weight: 800; color: #0a2540; line-height: 1; }
.sio-nombre { font-size: 0.85rem; color: #666; }

/* Menú (Centro) */
.nav-menu { display: flex; gap: 30px; }
.nav-item { text-decoration: none; color: #0a2540; font-weight: 600; font-size: 1rem; padding-bottom: 5px; border-bottom: 3px solid transparent; transition: 0.3s; }
.nav-item:hover, .nav-item.activo { color: #0088cc; border-bottom-color: #0088cc; }

/* Sellos (Derecha) */
.institutional-seals { display: flex; gap: 15px; align-items: center; }
.seal-img { height: 45px; width: auto; filter: grayscale(100%); opacity: 0.7; transition: 0.3s; }
.seal-img:hover { filter: grayscale(0%); opacity: 1; }

/* Contenido */
.contenido-principal { flex: 1; background-color: #ffffff; }

/* Footer */
.footer-icm { background-color: #0a2540; color: white; padding: 40px 0; text-align: center; }
.logo-csic-white { height: 50px; margin-bottom: 20px; filter: brightness(0) invert(1); }
.footer-info p { margin: 5px 0; opacity: 0.8; font-size: 0.9rem; }

/* Modal Login */
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.7); display: flex; justify-content: center; align-items: center; z-index: 2000; backdrop-filter: blur(4px); }
.modal-login { background: white; padding: 30px; border-radius: 8px; width: 320px; text-align: center; }
.modal-login h3 { margin-top: 0; color: #0a2540; }
.modal-login input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }
.modal-actions { display: flex; gap: 10px; margin-top: 15px; }
.btn-entrar { flex: 1; background: #0088cc; color: white; border: none; padding: 10px; border-radius: 4px; font-weight: bold; cursor: pointer; }
.btn-cancelar { flex: 1; background: #eee; border: none; padding: 10px; border-radius: 4px; cursor: pointer; }

@media (max-width: 1024px) {
  .header-inner { flex-direction: column; gap: 20px; }
  .nav-menu { order: 3; }
}
</style>