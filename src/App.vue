<script setup>
import { ref, onMounted } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Proyectos from './components/Proyectos.vue'
import Servicios from './components/Servicios.vue'
import DesarrolloIdi from './components/DesarrolloIdi.vue'
import IntranetPanel from './components/IntranetPanel.vue'

// IMPORTACIÓN SEGURA DE LOGOS (Esto evita errores de ruta)
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
        <div class="top-links-left">
          <a href="#" class="top-link">CONTACTO</a>
        </div>
        <div class="top-links-right">
          <button class="btn-intranet-sio" @click="manejarClicIntranet">
            {{ usuarioLogueadoSio ? 'INTRANET (Acceso)' : 'INTRANET' }}
          </button>
          <div class="idiomas">
            <span>CA</span> | <span class="active">ES</span> | <span>EN</span>
          </div>
          <button class="btn-search-top">🔍</button>
        </div>
      </div>
    </div>

    <header class="main-header">
      <div class="contenedor-ancho header-inner">
        <div class="brand-and-seals">
          <img :src="logoSio" alt="SIO" class="logo-sio-header" @click="volverAInicio">
          <div class="vertical-divider"></div>
          <img :src="logoSevero" alt="Severo Ochoa" class="seal-header">
        </div>

        <nav class="nav-menu">
          <a href="#" @click.prevent="cambiarVista('inicio')" class="nav-item" :class="{ activo: vistaActual === 'inicio' }">EL SIO</a>
          <a href="#" @click.prevent="cambiarVista('servicios')" class="nav-item" :class="{ activo: vistaActual === 'servicios' }">SERVEIS</a>
          <a href="#" @click.prevent="cambiarVista('proyectos')" class="nav-item" :class="{ activo: vistaActual === 'proyectos' }">PROJECTES</a>
          <a href="#" @click.prevent="cambiarVista('idi')" class="nav-item" :class="{ activo: vistaActual === 'idi' }">RECERCA I+D+i</a>
          <img :src="logoCsic" alt="CSIC" class="logo-csic-header">
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
        <img :src="logoIcm" alt="ICM" class="logo-footer">
        <div class="footer-info">
          <p>Passeig Marítim de la Barceloneta, 37-49. 08003 Barcelona (Spain)</p>
          <p>© 2026 Servicio de Ingeniería Oceanográfica (SIO) - CSIC</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
:root {
  --icm-blue: #0a2540;
  --icm-light-blue: #0088cc;
}

body { margin: 0; font-family: 'Helvetica Neue', Arial, sans-serif; }

/* BARRA SUPERIOR */
.top-bar { background-color: var(--icm-blue); color: white; padding: 10px 0; font-size: 0.75rem; }
.top-bar-inner { display: flex; justify-content: space-between; align-items: center; }
.top-link { color: white; text-decoration: none; font-weight: bold; }
.btn-intranet-sio { background: #2b4b6b; border: 1px solid #4a6a8a; color: white; padding: 4px 12px; font-weight: bold; cursor: pointer; border-radius: 2px; }
.idiomas { font-weight: bold; }
.idiomas .active { color: white; }
.idiomas span { opacity: 0.6; cursor: pointer; }
.btn-search-top { background: var(--icm-light-blue); border: none; color: white; padding: 5px 10px; cursor: pointer; }

/* HEADER */
.main-header { background: white; border-bottom: 1px solid #eee; padding: 20px 0; }
.header-inner { display: flex; justify-content: space-between; align-items: center; }
.brand-and-seals { display: flex; align-items: center; gap: 20px; }
.logo-sio-header { height: 65px; cursor: pointer; }
.seal-header { height: 45px; }
.vertical-divider { width: 1px; height: 40px; background: #ddd; }

.nav-menu { display: flex; align-items: center; gap: 25px; }
.nav-item { text-decoration: none; color: var(--icm-blue); font-weight: bold; font-size: 0.9rem; transition: 0.3s; }
.nav-item.activo, .nav-item:hover { color: var(--icm-light-blue); }
.logo-csic-header { height: 35px; margin-left: 10px; }

/* CONTENIDO Y FOOTER */
.contenido-principal { min-height: 600px; }
.footer-icm { background: #f8f9fa; padding: 40px 0; text-align: center; border-top: 1px solid #eee; }
.logo-footer { height: 50px; margin-bottom: 20px; }
.footer-info { font-size: 0.8rem; color: #666; }
</style>