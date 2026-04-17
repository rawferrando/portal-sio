<script setup>
import { ref, onMounted } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Proyectos from './components/Proyectos.vue'
import Servicios from './components/Servicios.vue'
import DesarrolloIdi from './components/DesarrolloIdi.vue'
import IntranetPanel from './components/IntranetPanel.vue'

// ⚠️ CARRUSEL DESACTIVADO para que GitHub no dé error rojo (ponlo cuando lo crees)
// import CarruselComponente from './components/CarruselComponente.vue'

// IMPORTACIONES DE LOGOS
import logoSio from './assets/sioblanco.png'
import logoCsic from './assets/csic.png'
import logoIcm from './assets/icm.png'
import logoSevero from './assets/severo.png'

const vistaActual = ref('inicio')
const usuarioLogueadoSio = ref(false)

onMounted(() => {
  if (sessionStorage.getItem('sio_auth') === 'true') {
    usuarioLogueadoSio.value = true
  }
})

const cambiarVista = (nuevaVista) => { 
  vistaActual.value = nuevaVista
  window.scrollTo(0, 0)
}

const irAContacto = () => { cambiarVista('contacto') }
const volverAInicio = () => { cambiarVista('inicio') }

const manejarClicIntranet = () => {
  if (usuarioLogueadoSio.value) {
    cambiarVista('intranet')
  } else {
    alert('Acceso restringido a personal autorizado')
  }
}
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
            <span class="lang-link">CA</span> | <span class="lang-link active">ES</span> | <span class="lang-link">EN</span>
          </div>
          <div class="top-item border-left search-block">
            <span class="search-label">BUSCAR</span>
            <svg class="lupa-svg" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
          </div>
        </div>
      </div>
    </div>

    <header class="main-header header-transparente">
      <div class="contenedor-ancho header-inner">
        
        <div class="header-left">
          <img :src="logoSio" alt="SIO" class="logo-sio" @click="volverAInicio">
          
          <div class="divider"></div>
          
          <div class="logos-institucionales">
            <a href="https://www.icm.csic.es" target="_blank">
              <img :src="logoIcm" alt="ICM" class="logo-secundario">
            </a>
            <a href="https://www.icm.csic.es/es/excelencia-severo-ochoa" target="_blank">
              <img :src="logoSevero" alt="Severo Ochoa" class="logo-secundario">
            </a>
            <a href="https://www.csic.es" target="_blank">
              <img :src="logoCsic" alt="CSIC" class="logo-secundario filter-white">
            </a>
          </div>
        </div>

        <nav class="nav-menu">
          <a href="#" @click.prevent="cambiarVista('inicio')" class="nav-item">EL SIO</a>
          <a href="#" @click.prevent="cambiarVista('servicios')" class="nav-item">SERVICIOS</a>
          <a href="#" @click.prevent="cambiarVista('proyectos')" class="nav-item">PROYECTOS</a>
          <a href="#" @click.prevent="cambiarVista('idi')" class="nav-item">I+D+i</a>
        </nav>
        
      </div>
    </header>

    <main class="main-content">
      <div v-if="vistaActual === 'inicio'" class="inicio-container">
        
        <div class="hero-temporal-bg"></div>
        
        <QuienesSomos @cambiar-pagina="cambiarVista" />
      </div>
      
      <div v-else class="vistas-secundarias">
        <Proyectos v-if="vistaActual === 'proyectos'" @volver="volverAInicio" />
        <Servicios v-else-if="vistaActual === 'servicios'" @volver="volverAInicio" />
        <DesarrolloIdi v-else-if="vistaActual === 'idi'" @volver="volverAInicio" />
        <IntranetPanel v-else-if="vistaActual === 'intranet'" @volver="volverAInicio" />
        
        <div v-else-if="vistaActual === 'contacto'" class="pagina-contacto">
          <div class="contenedor-ancho">
            <h2>CONTACTO</h2>
            <p>Email: sio.icm@icm.csic.es</p>
          </div>
        </div>
      </div>
    </main>

    <footer class="footer-icm">
      <div class="contenedor-ancho">
        <p>© 2026 Servicio de Ingeniería Oceanográfica - CSIC</p>
      </div>
    </footer>
    
  </div>
</template>

<style>
/* --- CONFIGURACIÓN BASE --- */
:root { 
  --icm-navy: #012169;   
  --icm-blue: #0086c0;
  --icm-gris-claro: #a8bacc; 
}

body { margin: 0; font-family: 'Helvetica Neue', Arial, sans-serif; -webkit-font-smoothing: antialiased; }
.contenedor-ancho { max-width: 1200px; margin: 0 auto; padding: 0 15px; }
.btn-reset { background: none; border: none; color: inherit; font: inherit; cursor: pointer; padding: 0; }

/* --- 1. BARRA SUPERIOR (INTOCABLE) --- */
.top-bar { background: var(--icm-navy); height: 40px; position: relative; z-index: 1000; }
.top-bar-inner { display: flex; justify-content: flex-end; align-items: center; height: 100%; }
.top-nav-group { display: flex; height: 100%; align-items: center; border-right: 1px solid rgba(255,255,255,0.2); }
.top-item { display: flex; align-items: center; height: 100%; padding: 0 15px; font-size: 11px; font-weight: bold; color: white; text-decoration: none; }
.border-left { border-left: 1px solid rgba(255,255,255,0.2); }
.idiomas-container { display: flex; gap: 8px; align-items: center; }
.lang-link { color: var(--icm-gris-claro); cursor: pointer; }
.lang-link.active { color: white; }
.search-block { background: var(--icm-blue); padding: 0 15px; cursor: pointer; gap: 8px; color: white; }
.lupa-svg { height: 16px; width: 16px; fill: white; }

/* --- 2. HEADER TRANSPARENTE --- */
.header-transparente {
  position: absolute;
  top: 40px; /* Queda justo debajo de la barra superior */
  left: 0;
  right: 0;
  background: transparent !important;
  z-index: 900;
  padding: 20px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}
.header-inner { display: flex; justify-content: space-between; align-items: center; }
.header-left { display: flex; align-items: center; }

/* LOGOS */
.logo-sio { height: 75px; cursor: pointer; transition: transform 0.3s; }
.divider { width: 1px; height: 40px; background: rgba(255,255,255,0.4); margin: 0 25px; }
.logos-institucionales { display: flex; align-items: center; gap: 20px; }
.logo-secundario { height: 40px; transition: transform 0.3s; }
.logo-secundario:hover { transform: scale(1.05); }

/* Filtro para que el CSIC se ponga blanco automáticamente si no lo has limpiado aún */
.filter-white { filter: brightness(0) invert(1); } 

/* MENÚ */
.nav-menu { display: flex; align-items: center; gap: 30px; }
.nav-item { 
  color: white !important; 
  text-decoration: none; 
  font-weight: bold; 
  font-size: 14px;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.8); /* Sombra para que se lea sobre fondos claros */
}

/* --- 3. CONTENIDO PRINCIPAL --- */
.main-content { margin-top: 0; }
.hero-temporal-bg {
  background: linear-gradient(rgba(1, 33, 105, 0.5), rgba(1, 33, 105, 0.7)), url('https://raw.githubusercontent.com/rawferrando/portal-sio/main/src/assets/instrumentacion.jpg');
  background-size: cover;
  background-position: center;
  height: 500px;
  width: 100%;
}
.vistas-secundarias { padding-top: 140px; min-height: 600px; }

/* --- 4. FOOTER --- */
.footer-icm { background: #f4f4f4; padding: 40px 0; text-align: center; margin-top: 40px; }
</style>