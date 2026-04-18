<script setup>
import { ref, onMounted } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Proyectos from './components/Proyectos.vue'
import Servicios from './components/Servicios.vue'
import DesarrolloIdi from './components/DesarrolloIdi.vue'
import IntranetPanel from './components/IntranetPanel.vue'
import CarruselComponente from './components/CarruselComponente.vue'
// ⚠️ El carrusel está comentado para que GitHub no dé error rojo.
// import CarruselComponente from './components/CarruselComponente.vue'

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
  if (usuarioLogueadoSio.value) { cambiarVista('intranet') } 
  else { alert('Acceso restringido a personal autorizado') }
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
    <header class="main-header header-transparente" :class="{ 'header-solido-contacto': vistaActual === 'contacto' }">
      <div class="contenedor-ancho header-inner">
        
<div class="header-left">
          <img :src="logoSio" alt="SIO" class="logo-principal" @click="volverAInicio">
          
          <div class="divider"></div>
          
          <div class="logos-grupo">
            <a href="https://www.icm.csic.es" target="_blank" rel="noopener noreferrer">
              <img :src="logoIcm" alt="ICM" class="logo-pequeno">
            </a>
            
            <a href="https://www.aei.gob.es/ayudas-concedidas/centros-unidades-excelencia" target="_blank" rel="noopener noreferrer">
              <img :src="logoSevero" alt="Severo Ochoa" class="logo-pequeno">
            </a>
            
            <a href="https://www.csic.es" target="_blank" rel="noopener noreferrer">
              <img :src="logoCsic" alt="CSIC" class="logo-pequeno filter-white">
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
        
        <CarruselComponente />
        
        <QuienesSomos @cambiar-pagina="cambiarVista" />
      </div>
      
      <div v-else-if="vistaActual === 'proyectos'"><Proyectos @volver="volverAInicio" /></div>
      <div v-else-if="vistaActual === 'servicios'"><Servicios @volver="volverAInicio" /></div>
      <div v-else-if="vistaActual === 'idi'"><DesarrolloIdi @volver="volverAInicio" /></div>
      <div v-else-if="vistaActual === 'intranet'"><IntranetPanel @volver="volverAInicio" /></div>
      
<div v-else-if="vistaActual === 'contacto'" class="pagina-contacto">
        <div class="contenedor-ancho">
          <h2 class="titulo-seccion">CONTACTO Y UBICACIÓN</h2>
          
          <div class="contacto-unacolumna">
            
            <div class="tarjeta-dato datos-unificados">
              <h3>Información del SIO</h3>
              <p><strong>Dirección:</strong> Passeig Marítim de la Barceloneta, 37-49, 08003 Barcelona</p>
              <p><strong>Teléfono:</strong> +34 93 230 95 00</p>
              <p><strong>Email:</strong> <a href="mailto:sio.icm@icm.csic.es">sio.icm@icm.csic.es</a></p>
            </div>

            <div class="mapa-container">
              <iframe 
                src="https://maps.google.com/maps?q=Institut+de+Ci%C3%A8ncies+del+Mar,+Passeig+Mar%C3%ADtim+de+la+Barceloneta,+37-49,+Barcelona&t=&z=16&ie=UTF8&iwloc=&output=embed" 
                width="100%" 
                height="400" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
              </iframe>
            </div>

            <div class="tarjeta-dato formulario-amplio">
              <h3>Envíanos tu consulta</h3>
              <form @submit.prevent>
                <div class="grupo-input">
                  <label for="nombre">Nombre</label>
                  <input type="text" id="nombre" placeholder="Tu nombre" required>
                </div>
                <div class="grupo-input">
                  <label for="email">Email</label>
                  <input type="email" id="email" placeholder="tu@email.com" required>
                </div>
                <div class="grupo-input">
                  <label for="mensaje">Mensaje</label>
                  <textarea id="mensaje" rows="6" placeholder="¿En qué podemos ayudarte?" required></textarea>
                </div>
                <button type="submit" class="btn-enviar">ENVIAR CONSULTA</button>
              </form>
            </div>
            
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
:root { 
  --icm-navy: #012169ff;   
  --icm-blue: #0086c0;
  --icm-gris-claro: #a8bacc; 
}

body { margin: 0; font-family: 'Helvetica Neue', Arial, sans-serif; -webkit-font-smoothing: antialiased; }
.contenedor-ancho { max-width: 1200px; margin: 0 auto; padding: 0 15px; }
.btn-reset { background: none; border: none; color: inherit; font: inherit; cursor: pointer; padding: 0; }

/* 🛑 TU BARRA SUPERIOR ORIGINAL (INTOCABLE) 🛑 */
.top-bar { background: var(--icm-navy); height: 40px; }
.top-bar-inner { display: flex; justify-content: space-between; align-items: center; height: 100%; }
.top-nav-group { display: flex; height: 100%; align-items: center; border-right: 1px solid rgba(255,255,255,0.2); }
.top-item { display: flex; align-items: center; height: 100%; padding: 0 15px; font-size: 11px; font-weight: bold; color: white; text-decoration: none; position: relative; }
.border-left { border-left: 1px solid rgba(255,255,255,0.2); }
.underline-item::after { content: ''; position: absolute; width: 0; height: 2px; bottom: 12px; left: 15px; background-color: white; transition: width 0.3s ease; }
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

/* ✨ HEADER TRANSPARENTE ✨ */
.header-transparente { 
  position: absolute; 
  top: 40px; 
  left: 0; 
  right: 0; 
  background: transparent !important; 
  padding: 25px 0; 
  z-index: 900; 
  border-bottom: 1px solid rgba(255,255,255,0.2); 
}
.header-inner { display: flex; justify-content: space-between; align-items: center; }
.header-left { display: flex; align-items: center; }

/* ✨ JERARQUÍA DE LOGOS ✨ */
.logo-principal { height: 60px; cursor: pointer; transition: transform 0.3s; }
/* Añadimos el mismo hover para que vuestro logo también crezca */
.logo-principal:hover { transform: scale(1.05); } 

.divider { width: 1px; height: 45px; background: rgba(255,255,255,0.4); margin: 0 25px; }
.logos-grupo { display: flex; align-items: center; gap: 15px; }
.logo-pequeno { height: 35px; opacity: 0.9; transition: transform 0.3s; }
.logo-pequeno:hover { transform: scale(1.05); opacity: 1; }
.filter-white { filter: brightness(0) invert(1); }

/* ✨ MENÚ BLANCO CON EFECTO HOVER AZUL ✨ */
.nav-menu { display: flex; align-items: center; gap: 25px; }
.nav-item { 
  color: white !important; 
  text-decoration: none; 
  font-weight: bold; 
  font-size: 14px; 
  text-shadow: 1px 1px 3px rgba(0,0,0,0.9); /* Sombra restaurada y oscurecida para máxima legibilidad */
  position: relative; /* Necesario para la línea de subrayado */
  padding-bottom: 5px; /* Espacio entre el texto y la línea */
  transition: color 0.3s ease; /* Transición suave de color */
}

/* 1. Cambia el color del texto al azul del botón "Buscar" */
.nav-item:hover {
  color: var(--icm-blue) !important;
}

/* 2. Prepara la línea de subrayado oculta (width: 0) */
.nav-item::after {
  content: ''; 
  position: absolute; 
  width: 0; 
  height: 3px; 
  bottom: -2px; 
  left: 0; 
  background-color: var(--icm-blue); 
  transition: width 0.3s ease; 
}

/* 3. Al pasar el ratón, la línea crece hasta el 100% de la palabra */
.nav-item:hover::after {
  width: 100%;
}
/* ✨ SIMULADOR DEL CARRUSEL ✨ */
.main-content { margin-top: 0; }
.hero-bg {
  /* Fondo oscuro azulado para que se vean bien tus logos blancos */
  background: linear-gradient(rgba(1, 33, 105, 0.4), rgba(1, 33, 105, 0.8)), url('https://raw.githubusercontent.com/rawferrando/portal-sio/main/src/assets/instrumentacion.jpg');
  background-size: cover;
  background-position: center;
  height: 600px;
  width: 100%;
}

/* OTROS ESTILOS DE TU WEB */
/* --- TÍTULO DE SECCIÓN --- */
.titulo-seccion { 
  color: var(--icm-navy); 
  font-size: 28px; 
  border-bottom: 2px solid var(--icm-blue); 
  padding-bottom: 10px; 
  margin-bottom: 30px; 
}

/* --- ESTRUCTURA GENERAL A UNA COLUMNA --- */
.contacto-unacolumna { 
  display: flex; 
  flex-direction: column; 
  gap: 30px; 
  max-width: 900px; /* Centrado y no demasiado ancho */
  margin: 0 auto; 
}

/* --- TU CSS BASE DE CONTACTO --- */
.pagina-contacto { padding: 80px 0; background: #fdfdfd; animation: fadeIn 0.5s ease; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

.tarjeta-dato { background: white; padding: 20px; border-left: 4px solid var(--icm-blue); margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
.tarjeta-dato h3 { margin: 0 0 10px 0; font-size: 16px; color: var(--icm-navy); }

.grupo-input { display: flex; flex-direction: column; gap: 5px; margin-bottom: 15px; }
.grupo-input label { font-size: 13px; font-weight: bold; color: #555; }
.grupo-input input, .grupo-input select, .grupo-input textarea { padding: 12px; border: 1px solid #ddd; border-radius: 4px; }

/* El botón con los colores corporativos */
.btn-enviar { 
  width: 100%; 
  letter-spacing: 1px; 
  background: var(--icm-blue); 
  color: white; 
  padding: 12px; 
  border: none; 
  border-radius: 4px; 
  cursor: pointer; 
  font-weight: bold; 
  transition: background 0.3s; 
}
.btn-enviar:hover { background: var(--icm-navy); }

/* --- AÑADIDOS PARA EL NUEVO DISEÑO --- */
.datos-unificados p { 
  font-size: 15px; 
  color: #444; 
  margin: 12px 0; 
  line-height: 1.5; 
}
.datos-unificados a { 
  color: var(--icm-blue); 
  text-decoration: none; 
  font-weight: bold; 
}
.datos-unificados a:hover { 
  text-decoration: underline; 
}

.mapa-container { 
  width: 100%; 
  border-radius: 8px; 
  overflow: hidden; 
  box-shadow: 0 4px 15px rgba(0,0,0,0.15); 
  border: 1px solid #ddd; 
}

.formulario-amplio { 
  border-top: 4px solid var(--icm-blue); 
  border-left: none; /* Cambiamos la raya de la izquierda arriba para este cuadro grande */
  padding: 30px; 
}
/* --- HEADER ESPECIAL PARA CONTACTO --- */
.header-solido-contacto {
  background: var(--icm-navy) !important; 
  position: relative !important; 
  top: 0 !important; 
  border-bottom: none !important;
}

.header-solido-contacto + .main-content .pagina-contacto {
  padding-top: 40px;
}
</style>