<script setup>
import { ref, onMounted } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Proyectos from './components/Proyectos.vue'
import Servicios from './components/Servicios.vue'
import DesarrolloIdi from './components/DesarrolloIdi.vue'
import IntranetPanel from './components/IntranetPanel.vue'

import logoSio from './assets/sio.png'
import logoCsic from './assets/csic.png'
import logoIcm from './assets/icm.png'
import logoSevero from './assets/severo.png'

// --- ESTADO ---
const vistaActual = ref('inicio')
const usuarioLogueadoSio = ref(false)
const mostrarModalLogin = ref(false)
const irAContacto = () => {
  cambiarVista('contacto')
}
onMounted(() => {
  if (sessionStorage.getItem('sio_auth') === 'true') {
    usuarioLogueadoSio.value = true
  }
})

// --- FUNCIÓN MÁGICA PARA LOS LOGOS ---
// Esta función le da la ruta a la web sin que Vite intente "importarla"
const getImageUrl = (name) => {
  return `./${name}`
}

const manejarClicIntranet = () => {
  if (usuarioLogueadoSio.value) {
    cambiarVista('intranet')
  } else {
    mostrarModalLogin.value = true 
  }
}

const cambiarVista = (nuevaVista) => { 
  vistaActual.value = nuevaVista
  window.scrollTo(0, 0)
}

const volverAInicio = () => { cambiarVista('inicio') }
</script>

<template>
  <div class="icm-layout">
    <div class="top-bar">
      <div class="contenedor-ancho top-bar-inner">
        <div class="spacer"></div>
        <div class="top-nav-group">
          <a href="#" class="top-item border-left underline-item" @click.prevent="irAContacto">CONTACTO</a>
          <button class="top-item border-left btn-reset underline-item" @click="manejarClicIntranet">INTRANET</button>
          <div class="top-item border-left idiomas-container">
            <span class="lang-link">CA</span> | <span class="lang-link active">CAS</span> | <span class="lang-link">EN</span>
          </div>
          <div class="top-item border-left search-block">
            <span class="search-label">BUSCAR</span>
            <svg class="lupa-svg" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
          </div>
        </div>
      </div>
    </div>

    <header class="main-header">
      <div class="contenedor-ancho header-inner">
        <div class="header-left">
          <img :src="logoSio" alt="SIO" class="logo-sio" @click="volverAInicio">
          <div class="divider"></div>
          <img :src="logoSevero" alt="Severo Ochoa" class="logo-severo">
        </div>
        <nav class="nav-menu">
          <a href="#" @click.prevent="cambiarVista('inicio')" class="nav-item" :class="{ activo: vistaActual === 'inicio' }">EL SIO</a>
          <a href="#" @click.prevent="cambiarVista('servicios')" class="nav-item" :class="{ activo: vistaActual === 'servicios' }">SERVICIOS</a>
          <a href="#" @click.prevent="cambiarVista('proyectos')" class="nav-item" :class="{ activo: vistaActual === 'proyectos' }">PROYECTOS</a>
          <a href="#" @click.prevent="cambiarVista('idi')" class="nav-item" :class="{ activo: vistaActual === 'idi' }">I+D+i</a>
          <img :src="logoCsic" alt="CSIC" class="logo-csic-nav">
        </nav>
      </div>
    </header>

<main class="main-content">
  <QuienesSomos v-if="vistaActual === 'inicio'" @cambiar-pagina="cambiarVista" />
  <Proyectos v-else-if="vistaActual === 'proyectos'" @volver="volverAInicio" />
  <Servicios v-else-if="vistaActual === 'servicios'" @volver="volverAInicio" />
  <DesarrolloIdi v-else-if="vistaActual === 'idi'" @volver="volverAInicio" />
  <IntranetPanel v-else-if="vistaActual === 'intranet'" @volver="volverAInicio" />
  
  <div v-else-if="vistaActual === 'contacto'" class="pagina-contacto">
    <div class="contenedor-ancho">
      <h2 class="titulo-seccion">CONTACTO Y UBICACIÓN</h2>
      
      <div class="contacto-grid">
        <div class="contacto-info">
          <div class="tarjeta-dato">
            <h3>📍 Dirección</h3>
            <p>Passeig Marítim de la Barceloneta, 37-49<br>08003 Barcelona, España</p>
          </div>
          
          <div class="tarjeta-dato">
            <h3>📞 Teléfono</h3>
            <p>+34 93 230 95 00</p>
          </div>

          <div class="tarjeta-dato">
            <h3>✉️ Email</h3>
            <p><a href="mailto:sio.icm@icm.csic.es">sio.icm@icm.csic.es</a></p>
          </div>

          <div class="mapa-contenedor">
            <iframe 
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2994.137817342686!2d2.1910600765874495!3d41.3820249712999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12a4a3f1bc40698d%3A0xc3f6a297921a2245!2sInstitut%20de%20Ci%C3%A8ncies%20del%20Mar%20(ICM-CSIC)!5e0!3m2!1ses!2ses!4v1715851234567!5m2!1ses!2ses" 
              width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy">
            </iframe>
          </div>
        </div>

        <div class="contacto-formulario">
          <h3>Formulario de Consulta</h3>
          <p>Utilice este formulario para solicitar servicios técnicos o información general.</p>
          <form @submit.prevent="enviarFormulario">
            <div class="grupo-input">
              <label>Nombre y Apellidos</label>
              <input type="text" required>
            </div>
            <div class="grupo-input">
              <label>Email de contacto</label>
              <input type="email" required>
            </div>
            <div class="grupo-input">
              <label>Asunto</label>
              <select>
                <option>Servicios de Ingeniería</option>
                <option>Mantenimiento de Equipos</option>
                <option>Proyectos I+D+i</option>
                <option>Otros</option>
              </select>
            </div>
            <div class="grupo-input">
              <label>Mensaje</label>
              <textarea rows="6" required></textarea>
            </div>
            <button type="submit" class="btn-enviar">ENVIAR SOLICITUD</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</main>

    <footer class="footer-icm">
      <div class="contenedor-ancho">
        <img :src="logoIcm" alt="ICM" class="footer-logo-main">
        <p>© 2026 Servicio de Ingeniería Oceanográfica - CSIC</p>
      </div>
    </footer>
  </div>
</template>

<style>
:root { 
  --icm-navy: #012169ff;   
  --icm-blue: #0086c0;
  --icm-gris-claro: #a8bacc; 
}

body { margin: 0; font-family: 'Helvetica Neue', Arial, sans-serif; -webkit-font-smoothing: antialiased; }
.contenedor-ancho { max-width: 1200px; margin: 0 auto; padding: 0 15px; }
.btn-reset { background: none; border: none; color: inherit; font: inherit; cursor: pointer; padding: 0; }

.top-bar { background: var(--icm-navy); height: 40px; }
.top-bar-inner { display: flex; justify-content: space-between; align-items: center; height: 100%; }
.top-nav-group { display: flex; height: 100%; align-items: center; border-right: 1px solid rgba(255,255,255,0.2); }

.top-item { 
  display: flex; align-items: center; height: 100%; padding: 0 15px;
  font-size: 11px; font-weight: bold; color: white; text-decoration: none;
  position: relative;
}
.border-left { border-left: 1px solid rgba(255,255,255,0.2); }

.underline-item::after {
  content: ''; position: absolute; width: 0; height: 2px;
  bottom: 12px; left: 15px; background-color: white; transition: width 0.3s ease;
}
.underline-item:hover::after { width: calc(100% - 30px); }

.idiomas-container { display: flex; gap: 8px; align-items: center; }
.lang-separator { color: var(--icm-gris-claro); font-weight: normal; font-size: 10px; }
.lang-link { color: var(--icm-gris-claro); position: relative; cursor: pointer; padding-bottom: 2px; transition: color 0.3s; }
.lang-link::after { content: ''; position: absolute; width: 0; height: 2px; bottom: -4px; left: 0; background-color: var(--icm-gris-claro); transition: width 0.3s ease; }
.lang-link:hover::after { width: 100%; }
.lang-link.active { color: white; }
.lang-link.active::after { width: 100%; background-color: white; }

.search-block { background: var(--icm-blue); padding: 0 15px; cursor: pointer; transition: background 0.3s; gap: 8px; }
.search-block:hover { background: #00a4eb; }
.lupa-svg { height: 16px; width: 16px; fill: white; }

.main-header { background: white; padding: 25px 0; border-bottom: 1px solid #eee; }
.header-inner { display: flex; justify-content: space-between; align-items: center; }
.logo-sio { height: 65px; cursor: pointer; }
.divider { width: 1px; height: 40px; background: #ddd; margin: 0 15px; }
.logo-severo { height: 45px; }

.nav-menu { display: flex; align-items: center; gap: 25px; }
.nav-item { text-decoration: none; color: var(--icm-navy); font-weight: bold; font-size: 13px; position: relative; padding-bottom: 5px; }
.nav-item::after { content: ''; position: absolute; width: 0; height: 3px; bottom: -2px; left: 0; background-color: var(--icm-blue); transition: width 0.3s; }
.nav-item:hover::after, .nav-item.activo::after { width: 100%; }
.nav-item:hover, .nav-item.activo { color: var(--icm-blue); }

.logo-csic-nav { height: 35px; margin-left: 10px; }

.footer-icm { background: #f9f9f9; padding: 60px 0; text-align: center; color: #666; font-size: 12px; }
.footer-logo-main { height: 50px; margin-bottom: 15px; }
.pagina-contacto { padding: 80px 0; background: #fdfdfd; animation: fadeIn 0.5s ease; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

.tarjeta-dato { background: white; padding: 20px; border-left: 4px solid var(--icm-blue); margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
.tarjeta-dato h3 { margin: 0 0 10px 0; font-size: 16px; color: var(--icm-navy); }

.grupo-input { display: flex; flex-direction: column; gap: 5px; margin-bottom: 15px; }
.grupo-input label { font-size: 13px; font-weight: bold; color: #555; }
.grupo-input input, .grupo-input select, .grupo-input textarea { padding: 12px; border: 1px solid #ddd; border-radius: 4px; }

.btn-enviar { width: 100%; letter-spacing: 1px; }
</style>