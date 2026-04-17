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
const errorLogin = ref(false)

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
    errorLogin.value = false
    mostrarModalLogin.value = false 
    cambiarVista('intranet')
    inputUsuario.value = ''         
    inputPassword.value = ''        
  } else {
    errorLogin.value = true
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
        <div class="top-enlaces-izquierda">
          <a href="https://icm.csic.es" target="_blank" style="color: #666; font-size: 0.85rem; text-decoration: none;">← Volver al ICM</a>
        </div>
        <div class="top-enlaces-derecha">
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
        
        <div class="logos-area" style="cursor: pointer;" @click="volverAInicio">
          <h1 class="logo-icm">
            <strong>SIO</strong><br>
            <span class="sub-logo">Servicio de Ingeniería Oceanográfica</span>
          </h1>
        </div>

        <nav class="nav-menu">
          <a href="#" @click.prevent="cambiarVista('inicio')" class="nav-item" :class="{ activo: vistaActual === 'inicio' }">Inicio</a>
          <a href="#" @click.prevent="cambiarVista('servicios')" class="nav-item" :class="{ activo: vistaActual === 'servicios' }">Servicios</a>
          <a href="#" @click.prevent="cambiarVista('proyectos')" class="nav-item" :class="{ activo: vistaActual === 'proyectos' }">Proyectos</a>
          <a href="#" @click.prevent="cambiarVista('idi')" class="nav-item" :class="{ activo: vistaActual === 'idi' }">I+D+i</a>
        </nav>

        <div class="header-logos-derecha">
          <img src="https://icm.csic.es/sites/default/files/logo_severo_ochoa.png" alt="Severo Ochoa" class="logo-header">
          <img src="https://icm.csic.es/sites/default/files/logo_icm_footer.png" alt="ICM" class="logo-header">
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
      <div class="contenedor-ancho">
        <div class="logos-footer">
          <img src="https://icm.csic.es/sites/default/files/logo_csic_footer.png" alt="CSIC" class="logo-f">
        </div>
        <div class="info-footer">
          <p><strong>Passeig Marítim de la Barceloneta, 37-49. 08003 Barcelona</strong></p>
          <p>© 2026 Servicio de Ingeniería Oceanográfica (ICM-CSIC)</p>
        </div>
      </div>
    </footer>

    <div v-if="mostrarModalLogin" class="modal-overlay" @click.self="cerrarModalLogin">
      <div class="modal-login">
        <h3>Acceso Restringido</h3>
        <p>Introduce tus credenciales del SIO</p>
        <div class="form-group"><input v-model="inputUsuario" type="text" placeholder="Usuario" @keyup.enter="intentarLogin" autofocus /></div>
        <div class="form-group"><input v-model="inputPassword" type="password" placeholder="Contraseña" @keyup.enter="intentarLogin" /></div>
        <div class="modal-actions">
          <button @click="intentarLogin" class="btn-entrar">Acceder</button>
          <button @click="cerrarModalLogin" class="btn-cancelar">Cancelar</button>
        </div>
      </div>
    </div>

  </div>
</template>

<style>
/* --- VARIABLES --- */
:root { --icm-azul-oscuro: #0a2540; --icm-azul-claro: #0088cc; --icm-blanco: #ffffff; --icm-texto: #333333; }
body { margin: 0; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background-color: var(--icm-blanco); color: var(--icm-texto); }
.icm-layout { display: flex; flex-direction: column; min-height: 100vh; }
.contenedor-ancho { max-width: 1400px; margin: 0 auto; padding: 0 20px; width: 100%; box-sizing: border-box; }

/* TOP BAR */
.top-bar { background-color: #f5f7fa; border-bottom: 1px solid #e1e4e8; padding: 8px 0; font-size: 0.85rem; }
.top-bar-inner { display: flex; justify-content: space-between; align-items: center; }
.top-enlaces-derecha { display: flex; gap: 20px; align-items: center; }
.btn-intranet-sio { background: none; border: none; color: var(--icm-azul-claro); font-weight: bold; font-size: 0.85rem; cursor: pointer; padding: 0; }
.idiomas span { cursor: pointer; color: #999; margin: 0 5px; } .idiomas span.active { color: var(--icm-texto); font-weight: bold; }

/* HEADER PRINCIPAL */
.main-header { background-color: var(--icm-blanco); padding: 20px 0; box-shadow: 0 2px 15px rgba(0,0,0,0.08); position: sticky; top: 0; z-index: 100; }
.header-inner { display: flex; justify-content: space-between; align-items: center; gap: 30px; }
.logo-icm { margin: 0; font-size: 1.8rem; color: var(--icm-azul-oscuro); line-height: 1.1; }
.sub-logo { font-size: 0.95rem; color: #666; font-weight: normal; }

.nav-menu { display: flex; gap: 25px; flex: 1; justify-content: center; }
.nav-item { text-decoration: none; color: var(--icm-azul-oscuro); font-weight: bold; font-size: 1.05rem; padding-bottom: 5px; border-bottom: 3px solid transparent; transition: 0.2s; }
.nav-item:hover, .nav-item.activo { color: var(--icm-azul-claro); border-bottom-color: var(--icm-azul-claro); }

.header-logos-derecha { display: flex; gap: 15px; align-items: center; }
/* Hacemos un invert temporal para que los logos que eran para fondo oscuro se vean en el blanco */
.logo-header { height: 45px; filter: brightness(0); opacity: 0.8; transition: opacity 0.3s; }
.logo-header:hover { opacity: 1; }

/* MAIN & FOOTER */
.contenido-principal { flex: 1; background-color: #ffffff; }
.footer-icm { background-color: var(--icm-azul-oscuro); color: var(--icm-blanco); padding: 40px 0 20px 0; margin-top: auto; }
.logos-footer { display: flex; justify-content: center; margin-bottom: 20px; }
.logo-f { height: 50px; filter: brightness(0) invert(1); opacity: 0.8; }
.info-footer { text-align: center; opacity: 0.7; font-size: 0.85rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; }

/* MODAL */
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.6); display: flex; justify-content: center; align-items: center; z-index: 9999; backdrop-filter: blur(3px); }
.modal-login { background: white; padding: 30px; border-radius: 8px; width: 90%; max-width: 350px; text-align: center; }
.modal-login h3 { color: var(--icm-azul-oscuro); margin-top: 0; }
.modal-login input { width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
.modal-actions { display: flex; gap: 10px; }
.btn-entrar { flex: 1; background-color: var(--icm-azul-claro); color: white; border: none; padding: 10px; border-radius: 4px; font-weight: bold; cursor: pointer; }
.btn-cancelar { flex: 1; background-color: #e0e0e0; color: #333; border: none; padding: 10px; border-radius: 4px; cursor: pointer; }
</style>