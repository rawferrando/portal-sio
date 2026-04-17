<script setup>
import { ref, onMounted } from 'vue'
// Tus 4 componentes principales (Inicio y las 3 fichas)
import QuienesSomos from './components/QuienesSomos.vue'
import Proyectos from './components/Proyectos.vue'
import Servicios from './components/Servicios.vue' // <--- NUEVO: Ficha de Servicios
import DesarrolloIdi from './components/DesarrolloIdi.vue'
import IntranetPanel from './components/IntranetPanel.vue'

// --- ESTADO Y SEGURIDAD ---
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
        <div class="social-icons">
          <span>X (Twitter)</span> | <span>YouTube</span>
        </div>
        <div class="top-enlaces">
          <a href="#">Contacto</a>
          <button class="btn-intranet-sio" @click="manejarClicIntranet">
            {{ usuarioLogueadoSio ? '🔒 Admin SIO' : '👤 Intranet SIO' }}
          </button>
          <div class="idiomas">
            <span class="active">ca</span>
            <span>es</span>
            <span>en</span>
          </div>
        </div>
      </div>
    </div>

    <header class="main-header">
      <div class="contenedor-ancho header-inner">
        <div class="logos-area" style="cursor: pointer;" @click="volverAInicio">
          <h1 class="logo-icm">
            <strong>Institut de Ciències del Mar</strong><br>
            <span class="sub-logo">Servicio de Ingeniería Oceanográfica (SIO)</span>
          </h1>
        </div>
        <nav class="nav-menu">
          <a href="#" @click.prevent="cambiarVista('inicio')" class="nav-item" :class="{ activo: vistaActual === 'inicio' }">Inicio</a>
          <a href="#" @click.prevent="cambiarVista('proyectos')" class="nav-item" :class="{ activo: vistaActual === 'proyectos' }">Proyectos</a>
          <a href="#" @click.prevent="cambiarVista('servicios')" class="nav-item" :class="{ activo: vistaActual === 'servicios' }">Servicios</a>
          <a href="#" @click.prevent="cambiarVista('idi')" class="nav-item" :class="{ activo: vistaActual === 'idi' }">I+D+i</a>
        </nav>
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
        <p><strong>Passeig Marítim de la Barceloneta, 37-49. 08003 Barcelona (Spain)</strong></p>
        <p>T. +34 93 230 95 00 | CSIC Gobierno de España. Ministerio de Ciencia e Innovación</p>
      </div>
    </footer>

    <div v-if="mostrarModalLogin" class="modal-overlay" @click.self="cerrarModalLogin">
      <div class="modal-login">
        <h3>Acceso Restringido</h3>
        <p>Introduce tus credenciales del SIO</p>
        <div class="form-group">
          <input v-model="inputUsuario" type="text" placeholder="Usuario" @keyup.enter="intentarLogin" autofocus />
        </div>
        <div class="form-group">
          <input v-model="inputPassword" type="password" placeholder="Contraseña" @keyup.enter="intentarLogin" />
        </div>
        <div class="modal-actions">
          <button @click="intentarLogin" class="btn-entrar">Acceder</button>
          <button @click="cerrarModalLogin" class="btn-cancelar">Cancelar</button>
        </div>
      </div>
    </div>

  </div>
</template>

<style>
/* --- VARIABLES CORPORATIVAS ICM --- */
:root {
  --icm-azul-oscuro: #0a2540;
  --icm-azul-claro: #0088cc;
  --icm-gris-fondo: #f5f7fa;
  --icm-blanco: #ffffff;
  --icm-texto: #333333;
}

body { margin: 0; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background-color: var(--icm-blanco); color: var(--icm-texto); }
.icm-layout { display: flex; flex-direction: column; min-height: 100vh; }
.contenedor-ancho { max-width: 1300px; margin: 0 auto; padding: 0 20px; width: 100%; box-sizing: border-box; }

/* --- 1. TOP BAR --- */
.top-bar { background-color: var(--icm-blanco); border-bottom: 1px solid #eee; font-size: 0.8rem; padding: 8px 0; }
.top-bar-inner { display: flex; justify-content: space-between; align-items: center; }
.top-enlaces { display: flex; gap: 20px; align-items: center; }
.top-enlaces a { text-decoration: none; color: #666; font-weight: bold; }
.btn-intranet-sio { background: none; border: none; color: var(--icm-azul-claro); font-weight: bold; font-size: 0.8rem; cursor: pointer; padding: 0; }
.btn-intranet-sio:hover { text-decoration: underline; }
.idiomas { display: flex; gap: 10px; border-left: 1px solid #ccc; padding-left: 15px; }
.idiomas span { cursor: pointer; color: #999; }
.idiomas span.active { color: var(--icm-texto); font-weight: bold; }

/* --- 2. HEADER PRINCIPAL --- */
.main-header { background-color: var(--icm-blanco); padding: 20px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 100; }
.header-inner { display: flex; justify-content: space-between; align-items: center; }
.logo-icm { margin: 0; font-size: 1.5rem; color: var(--icm-azul-oscuro); line-height: 1.2; }
.sub-logo { font-size: 0.9rem; color: var(--icm-azul-claro); font-weight: normal; }
.nav-menu { display: flex; gap: 25px; }
.nav-item { text-decoration: none; color: var(--icm-azul-oscuro); font-weight: 600; font-size: 1.05rem; transition: color 0.3s; padding-bottom: 5px; border-bottom: 2px solid transparent; }
.nav-item:hover, .nav-item.activo { color: var(--icm-azul-claro); border-bottom: 2px solid var(--icm-azul-claro); }

/* --- 3. CONTENIDO PRINCIPAL --- */
.contenido-principal { flex: 1; background-color: var(--icm-gris-fondo); }

/* --- 4. FOOTER --- */
.footer-icm { background-color: var(--icm-azul-oscuro); color: var(--icm-blanco); padding: 40px 0; font-size: 0.9rem; margin-top: auto; }
.footer-icm p { margin: 5px 0; color: #a0aec0; }
.footer-icm strong { color: var(--icm-blanco); }

/* --- 5. MODAL LOGIN --- */
.modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.6); display: flex; justify-content: center; align-items: center; z-index: 9999; backdrop-filter: blur(3px); }
.modal-login { background-color: white; padding: 30px; border-radius: 8px; width: 90%; max-width: 350px; text-align: center; }
.modal-login h3 { color: var(--icm-azul-oscuro); margin-top: 0; margin-bottom: 5px; }
.modal-login input { width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
.modal-actions { display: flex; gap: 10px; }
.btn-entrar { flex: 1; background-color: var(--icm-azul-claro); color: white; border: none; padding: 10px; border-radius: 4px; font-weight: bold; cursor: pointer; }
.btn-cancelar { flex: 1; background-color: #e0e0e0; color: #333; border: none; padding: 10px; border-radius: 4px; font-weight: bold; cursor: pointer; }
</style>