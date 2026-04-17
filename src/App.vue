<script setup>
import { ref, onMounted } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Proyectos from './components/Proyectos.vue'
import Servicios from './components/Servicios.vue'
import DesarrolloIdi from './components/DesarrolloIdi.vue'
import IntranetPanel from './components/IntranetPanel.vue'

// --- ESTADO Y SEGURIDAD ---
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
          <img src="./assets/logovector.png" alt="SIO" class="logo-sio-main">
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
          <img src="./assets/logo-csic.png" alt="" class="seal-img">
          <img src="./assets/logo-icm.png" alt="" class="seal-img">
          <img src="./assets/logo-severo.png" alt="" class="seal-img">
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
        <div class="footer-logos">
          <img src="./assets/logo-csic.png" alt="" class="logo-csic-footer">
        </div>
        <div class="footer-info">
          <p><strong>Passeig Marítim de la Barceloneta, 37-49. 08003 Barcelona</strong></p>
          <p>© 2026 Servicio de Ingeniería Oceanográfica (SIO) - ICM-CSIC</p>
        </div>
      </div>
    </footer>

    <div v-if="mostrarModalLogin" class="modal-overlay" @click.self="cerrarModalLogin">
      <div class="modal-login">
        <h3>Acceso Restringido SIO</h3>
        <p>Introduce tus credenciales</p>
        <input v-model="inputUsuario" type="text" placeholder="Usuario" @keyup.enter="intentarLogin" autofocus />
        <input v-model="inputPassword" type="password" placeholder="Contraseña" @keyup.enter="intentarLogin" />
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
  --icm-texto-gris: #666666;
  --icm-texto-principal: #333333;
}

body {
  margin: 0;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  background-color: var(--icm-blanco);
  color: var(--icm-texto-principal);
}

.icm-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.contenedor-ancho {
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 20px;
  width: 100%;
  box-sizing: border-box;
}

/* --- 1. BARRA SUPERIOR (TOP BAR) --- */
.top-bar {
  background-color: var(--icm-blanco);
  border-bottom: 1px solid #e1e4e8;
  font-size: 0.85rem;
  padding: 10px 0;
  color: var(--icm-texto-gris);
}
.top-bar-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.top-enlaces {
  display: flex;
  gap: 20px;
  align-items: center;
}
.top-link {
  text-decoration: none;
  color: var(--icm-texto-gris);
  font-weight: bold;
}
.top-link:hover {
  text-decoration: underline;
}
.btn-intranet-sio {
  background: none;
  border: none;
  color: var(--icm-azul-claro);
  font-weight: bold;
  font-size: 0.85rem;
  cursor: pointer;
  margin-right: 15px;
}
.idiomas {
  display: flex;
  gap: 10px;
  border-left: 1px solid #ccc;
  padding-left: 15px;
}
.idiomas span { cursor: pointer; color: #999; }
.idiomas span.active { color: var(--icm-texto-principal); font-weight: bold; }

/* --- 2. HEADER PRINCIPAL --- */
.main-header {
  background-color: var(--icm-blanco);
  padding: 15px 0;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  position: sticky;
  top: 0;
  z-index: 1000;
}
.header-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.logo-sio-main {
  height: 80px;
  width: auto;
}

/* Navegación y Buscador (Centro) */
.nav-container {
  display: flex;
  align-items: center;
  gap: 20px;
}
.nav-menu {
  display: flex;
  gap: 25px;
}
.nav-item {
  text-decoration: none;
  color: var(--icm-azul-oscuro);
  font-weight: bold;
  font-size: 1.1rem;
  padding-bottom: 5px;
  border-bottom: 3px solid transparent;
  transition: color 0.3s;
}
.nav-item:hover, .nav-item.activo {
  color: var(--icm-azul-claro);
  border-bottom-color: var(--icm-azul-claro);
}
.btn-search {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  padding: 0;
}

/* Sellos (Derecha) */
.institutional-seals {
  display: flex;
  gap: 15px;
  align-items: center;
}
.seal-img {
  height: 50px;
  width: auto;
}

/* --- 3. CONTENIDO PRINCIPAL --- */
.contenido-principal {
  flex: 1;
  background-color: var(--icm-blanco);
}

/* --- 4. FOOTER --- */
.footer-icm {
  background-color: var(--icm-azul-oscuro);
  color: var(--icm-blanco);
  padding: 40px 0;
  font-size: 0.9rem;
  margin-top: 40px;
}
.footer-logos {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}
.logo-csic-footer {
  height: 60px;
  filter: brightness(0) invert(1); /* Pone el logo en blanco */
}
.footer-info {
  text-align: center;
}
.footer-info p { margin: 5px 0; color: #a0aec0; }
.footer-info strong { color: var(--icm-blanco); }

/* --- 5. MODAL LOGIN (El "Blindaje") --- */
.modal-overlay {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex; justify-content: center; align-items: center;
  z-index: 2000; backdrop-filter: blur(3px);
}
.modal-login {
  background-color: white; padding: 30px; border-radius: 8px;
  width: 90%; max-width: 350px;
  text-align: center;
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}
.modal-login h3 { color: var(--icm-azul-oscuro); margin-top: 0; }
.modal-login p { font-size: 0.9rem; color: #666; margin-bottom: 20px; }
.modal-login input {
  width: 100%; padding: 12px;
  border: 1px solid #ccc; border-radius: 4px;
  box-sizing: border-box; margin-bottom: 15px;
}
.modal-actions { display: flex; gap: 10px; }
.btn-entrar {
  flex: 1; background-color: var(--icm-azul-claro);
  color: white; border: none; padding: 10px;
  border-radius: 4px; font-weight: bold; cursor: pointer;
}
.btn-cancelar {
  flex: 1; background-color: #eee;
  color: #333; border: none; padding: 10px;
  border-radius: 4px; cursor: pointer;
}
</style>