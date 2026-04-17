<script setup>
import { ref, onMounted } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Proyectos from './components/Proyectos.vue'
import Servicios from './components/Servicios.vue'
import DesarrolloIdi from './components/DesarrolloIdi.vue'
import IntranetPanel from './components/IntranetPanel.vue'

// Importación robusta: Esto asegura que Vite procese las imágenes al hacer el build
import logoSio from '@/assets/logovector.png'
import logoCsic from '@/assets/logo-csic.png'
import logoIcm from '@/assets/logo-icm.png'
import logoSevero from '@/assets/logo-severo.png'

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
  <div class="icm-layout">
    
    <div class="top-bar">
      <div class="contenedor-ancho top-bar-inner">
        <div class="spacer"></div>
        <div class="top-nav-group">
          <a href="#" class="top-item border-left">CONTACTO</a>
          <button class="top-item border-left btn-reset" @click="manejarClicIntranet">INTRANET</button>
          <div class="top-item border-left idiomas">
            <span>CA</span> | <span class="active">ES</span> | <span>EN</span>
          </div>
          <div class="top-item border-left search-block">
            <img src="https://icm.csic.es/sites/all/themes/bootstrap_icm/icons/lupa.png" alt="Buscar" class="icon-lupa-img">
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
/* COLORES OFICIALES ICM ACTUALIZADOS */
:root { 
  --icm-navy: #002d4b;   /* Color exacto barra superior ICM */
  --icm-blue: #0086c0;   /* Color exacto logos/lupa/hover */
}

body { margin: 0; font-family: 'Helvetica Neue', Arial, sans-serif; }
.contenedor-ancho { max-width: 1200px; margin: 0 auto; padding: 0 15px; }
.btn-reset { background: none; border: none; color: inherit; font: inherit; cursor: pointer; padding: 0; }

/* TOP BAR */
.top-bar { background: var(--icm-navy); color: white; height: 40px; }
.top-bar-inner { display: flex; justify-content: space-between; align-items: center; height: 100%; }
.top-nav-group { display: flex; height: 100%; align-items: center; border-right: 1px solid rgba(255,255,255,0.2); }
.top-item { 
  display: flex; align-items: center; height: 100%; padding: 0 15px;
  font-size: 11px; font-weight: bold; text-decoration: none; color: white;
}
.border-left { border-left: 1px solid rgba(255,255,255,0.2); }
.idiomas span { opacity: 0.6; margin: 0 2px; }
.idiomas .active { opacity: 1; }
.search-block { background: var(--icm-blue); padding: 0 12px; cursor: pointer; }
.icon-lupa-img { height: 16px; }

/* HEADER Y MENÚ CON SUBRAYADO */
.main-header { background: white; padding: 25px 0; border-bottom: 1px solid #eee; }
.header-inner { display: flex; justify-content: space-between; align-items: center; }
.header-left { display: flex; align-items: center; gap: 20px; }
.logo-sio { height: 65px; cursor: pointer; }
.divider { width: 1px; height: 40px; background: #ddd; }
.logo-severo { height: 45px; }

.nav-menu { display: flex; align-items: center; gap: 25px; }
.nav-item { 
  text-decoration: none; 
  color: var(--icm-navy); 
  font-weight: bold; 
  font-size: 13px;
  position: relative;
  padding: 5px 0;
}

/* Efecto subrayado al pasar el puntero (hover) */
.nav-item::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: var(--icm-blue);
  transition: width 0.3s ease;
}

.nav-item:hover::after, .nav-item.activo::after {
  width: 100%;
}

.nav-item:hover, .nav-item.activo {
  color: var(--icm-blue);
}

.logo-csic-nav { height: 35px; margin-left: 10px; }

.footer-icm { background: #f9f9f9; padding: 60px 0; text-align: center; color: #666; font-size: 12px; }
.footer-logo-main { height: 50px; margin-bottom: 15px; }
</style>