<script setup>
import { ref, onMounted } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Proyectos from './components/Proyectos.vue'
import Servicios from './components/Servicios.vue'
import DesarrolloIdi from './components/DesarrolloIdi.vue'
import IntranetPanel from './components/IntranetPanel.vue'

// --- CARGA DE IMÁGENES BLINDADA ---
import logoSio from './assets/logovector.png'
import logoCsic from './assets/logo-csic.png'
import logoIcm from './assets/logo-icm.png'
import logoSevero from './assets/logo-severo.png'

const vistaActual = ref('inicio')
const usuarioLogueadoSio = ref(false)
const mostrarModalLogin = ref(false)

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

const cambiarVista = (nuevaVista) => { 
  vistaActual.value = nuevaVista
  window.scrollTo(0, 0)
}

const volverAInicio = () => { cambiarVista('inicio') }
</script>

<template>
  <header class="main-header">
    <div class="contenedor-ancho header-inner">
      <div class="header-left">
        <img src="/logovector.png" alt="SIO" class="logo-sio" @click="volverAInicio">
        <div class="divider"></div>
        <img src="/logo-severo.png" alt="Severo Ochoa" class="logo-severo">
      </div>

      <nav class="nav-menu">
        <a href="#" @click.prevent="cambiarVista('inicio')" class="nav-item" :class="{ activo: vistaActual === 'inicio' }">EL SIO</a>
        <a href="#" @click.prevent="cambiarVista('servicios')" class="nav-item" :class="{ activo: vistaActual === 'servicios' }">SERVICIOS</a>
        <a href="#" @click.prevent="cambiarVista('proyectos')" class="nav-item" :class="{ activo: vistaActual === 'proyectos' }">PROYECTOS</a>
        <a href="#" @click.prevent="cambiarVista('idi')" class="nav-item" :class="{ activo: vistaActual === 'idi' }">I+D+i</a>
        <img src="/logo-csic.png" alt="CSIC" class="logo-csic-nav">
      </nav>
    </div>
  </header>

  <footer class="footer-icm">
    <div class="contenedor-ancho">
      <img src="/logo-icm.png" alt="ICM" class="footer-logo-main">
      <p>© 2026 Servicio de Ingeniería Oceanográfica - CSIC</p>
    </div>
  </footer>
</template>
<style>
/* COLORES OFICIALES ICM */
:root { 
  --icm-navy: #002d4b;   
  --icm-blue: #0086c0;
  --icm-gris-claro: #a8bacc; /* Gris azulado para los idiomas inactivos */
}

body { margin: 0; font-family: 'Helvetica Neue', Arial, sans-serif; -webkit-font-smoothing: antialiased; }
.contenedor-ancho { max-width: 1200px; margin: 0 auto; padding: 0 15px; }
.btn-reset { background: none; border: none; color: inherit; font: inherit; cursor: pointer; padding: 0; }

/* TOP BAR */
.top-bar { background: var(--icm-navy); height: 40px; }
.top-bar-inner { display: flex; justify-content: space-between; align-items: center; height: 100%; }
.top-nav-group { display: flex; height: 100%; align-items: center; border-right: 1px solid rgba(255,255,255,0.2); }

.top-item { 
  display: flex; align-items: center; height: 100%; padding: 0 15px;
  font-size: 11px; font-weight: bold; color: white; text-decoration: none;
}
.border-left { border-left: 1px solid rgba(255,255,255,0.2); }

/* SUBRAYADO BLANCO PARA CONTACTO E INTRANET */
.underline-item {
  position: relative;
  cursor: pointer;
}
.underline-item::after {
  content: ''; 
  position: absolute; 
  width: 0; 
  height: 2px;
  bottom: 12px; /* ¡Subimos la línea para que sea visible dentro de la barra! */
  left: 15px;   /* La alineamos con el texto salvando el margen */
  background-color: white; 
  transition: width 0.3s ease;
}
.underline-item:hover::after { 
  width: calc(100% - 30px); /* La línea medirá exactamente lo que mide la palabra */
}

/* --- LÓGICA DE IDIOMAS (GRIS Y BLANCO) --- */
.idiomas-container { display: flex; gap: 8px; align-items: center; }
.lang-separator { color: var(--icm-gris-claro); font-weight: normal; font-size: 10px; }

/* Inactivos por defecto: Texto gris y línea gris invisible */
.lang-link { 
  color: var(--icm-gris-claro); 
  position: relative; 
  cursor: pointer; 
  padding-bottom: 2px;
  transition: color 0.3s; 
}
.lang-link::after {
  content: ''; position: absolute; width: 0; height: 2px;
  bottom: -4px; left: 0; 
  background-color: var(--icm-gris-claro); /* Subrayado en gris */
  transition: width 0.3s ease;
}

/* Al pasar el ratón por los inactivos: se subraya en gris */
.lang-link:hover::after { width: 100%; }

/* El idioma activo: Texto blanco y línea blanca siempre visible */
.lang-link.active { 
  color: white; 
}
.lang-link.active::after { 
  width: 100%; 
  background-color: white; 
}

/* BLOQUE BUSCAR */
.search-block { 
  background: var(--icm-blue); padding: 0 15px; cursor: pointer; transition: background 0.3s; gap: 8px;
}
.search-block:hover { background: #00a4eb; }
.search-label { font-size: 11px; letter-spacing: 0.5px; }
.lupa-svg { height: 16px; width: 16px; fill: white; }

/* HEADER */
.main-header { background: white; padding: 25px 0; border-bottom: 1px solid #eee; }
.header-inner { display: flex; justify-content: space-between; align-items: center; }
.logo-sio { height: 65px; cursor: pointer; }
.divider { width: 1px; height: 40px; background: #ddd; margin: 0 15px; }
.logo-severo { height: 45px; }

.nav-menu { display: flex; align-items: center; gap: 25px; }
.nav-item { 
  text-decoration: none; color: var(--icm-navy); 
  font-weight: bold; font-size: 13px; position: relative; padding-bottom: 5px;
}
.nav-item::after {
  content: ''; position: absolute; width: 0; height: 3px;
  bottom: -2px; left: 0; background-color: var(--icm-blue); transition: width 0.3s;
}
.nav-item:hover::after, .nav-item.activo::after { width: 100%; }
.nav-item:hover, .nav-item.activo { color: var(--icm-blue); }

.logo-csic-nav { height: 35px; margin-left: 10px; }

.footer-icm { background: #f9f9f9; padding: 60px 0; text-align: center; color: #666; font-size: 12px; }
.footer-logo-main { height: 50px; margin-bottom: 15px; }
</style>