<script setup>
import { ref, onMounted } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Instrumentacion from './components/Instrumentacion.vue'
import IntranetPanel from './components/IntranetPanel.vue'
// Importamos las páginas nuevas
import Proyectos from './components/Proyectos.vue'
import DesarrolloIdi from './components/DesarrolloIdi.vue'

// --- VARIABLES DE ESTADO ---
const vistaActual = ref('inicio')
const usuarioLogueadoSio = ref(false)
const mostrarModalLogin = ref(false) 
const inputUsuario = ref('')
const inputPassword = ref('')
const errorLogin = ref(false)

// --- LÓGICA DE SESIÓN ---
onMounted(() => {
  if (sessionStorage.getItem('sio_auth') === 'true') {
    usuarioLogueadoSio.value = true
  }
})

const manejarClicIntranet = () => {
  if (usuarioLogueadoSio.value) {
    vistaActual.value = 'intranet' 
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
    vistaActual.value = 'intranet'  
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

const cerrarSesion = () => {
  sessionStorage.removeItem('sio_auth')
  usuarioLogueadoSio.value = false
  vistaActual.value = 'inicio'
}

const cambiarVista = (nuevaVista) => { 
  console.log("Cambiando a:", nuevaVista); // Esto te ayudará a ver si el clic funciona
  
  if (nuevaVista === 'intranet' && !usuarioLogueadoSio.value) {
    mostrarModalLogin.value = true;
    return;
  }
  
  vistaActual.value = nuevaVista;
  window.scrollTo(0, 0);
}

const volverAInicio = () => { 
  vistaActual.value = 'inicio' 
  window.scrollTo(0, 0)
}
</script>

<template>
  <div class="app-container">
    <header class="main-header">
      <div class="contenedor-cabecera">
        <div class="vacio-izquierda"></div> 
        
        <nav class="menu-principal">
          <div class="selector-idiomas">
            <button class="btn-idioma">CAT</button>
            <button class="btn-idioma active">CAS</button>
            <button class="btn-idioma">ENG</button>
          </div>

          <div class="area-privada-wrapper">
            <button class="btn-intranet-sio" @click="manejarClicIntranet">
              {{ usuarioLogueadoSio ? '🔒 Admin SIO' : '👤 Intranet SIO' }}
            </button>
          </div>
        </nav>
      </div>
    </header>

    <main class="main-content">
      <QuienesSomos v-if="vistaActual === 'inicio'" @cambiar-pagina="cambiarVista" />
      <Instrumentacion v-else-if="vistaActual === 'instrumentacion'" @volver="volverAInicio" />
      
      <Proyectos v-else-if="vistaActual === 'proyectos'" @volver="volverAInicio" />
      <DesarrolloIdi v-else-if="vistaActual === 'idi'" @volver="volverAInicio" />
      
      <IntranetPanel v-else-if="vistaActual === 'intranet'" @volver="volverAInicio" />
    </main>

    <footer class="footer-sio">
      <p><strong>Institut de Ciències del Mar (ICM-CSIC)</strong></p>
      <p>📧 sio@icm.csic.es | 📍 Pg. Marítim de la Barceloneta, 37, 08003 Barcelona</p>
    </footer>

    <div v-if="mostrarModalLogin" class="modal-overlay" @click.self="cerrarModalLogin">
      <div class="modal-login">
        <h3>Acceso Restringido</h3>
        <p>Introduce tus credenciales del SIO</p>
        
        <div class="form-group">
          <input 
            v-model="inputUsuario" 
            type="text" 
            placeholder="Usuario" 
            @keyup.enter="intentarLogin"
            autofocus 
          />
        </div>
        
        <div class="form-group">
          <input 
            v-model="inputPassword" 
            type="password" 
            placeholder="Contraseña" 
            @keyup.enter="intentarLogin" 
          />
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
/* ESTILOS GENERALES */
body { margin: 0; font-family: 'Segoe UI', sans-serif; background-color: #f4f7f9; }
.app-container { display: flex; flex-direction: column; min-height: 100vh; }

/* HEADER */
.main-header { background-color: #005596; color: white; padding: 5px 0; border-bottom: 2px solid #003366; }
.contenedor-cabecera { display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.menu-principal { display: flex; align-items: center; gap: 20px; }

/* IDIOMAS */
.selector-idiomas { display: flex; gap: 5px; }
.btn-idioma { background: none; border: none; color: white; font-size: 0.75rem; cursor: pointer; padding: 2px 5px; border-radius: 3px; opacity: 0.7; }
.btn-idioma.active { opacity: 1; font-weight: bold; border: 1px solid white; }

/* BOTÓN INTRANET CABECERA */
.btn-intranet-sio { background-color: white; color: #005596; border: none; padding: 5px 12px; border-radius: 4px; font-weight: bold; font-size: 0.85rem; cursor: pointer; transition: background-color 0.3s; }
.btn-intranet-sio:hover { background-color: #e6f0fa; }

/* CONTENIDO PRINCIPAL Y FOOTER */
.main-content { flex: 1; width: 100%; max-width: 1200px; margin: 0 auto; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; }
.footer-sio { background-color: #005596; color: white; text-align: center; padding: 20px; margin-top: auto; border-top: 3px solid #003366; font-size: 0.9rem; }
.footer-sio p { margin: 3px 0; }

/* ESTILOS DE LA VENTANA EMERGENTE (MODAL) */
.modal-overlay {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  background-color: rgba(0, 0, 0, 0.6); display: flex; justify-content: center; align-items: center;
  z-index: 9999; backdrop-filter: blur(3px);
}
.modal-login { background-color: white; padding: 30px; border-radius: 12px; width: 90%; max-width: 350px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); text-align: center; }
.modal-login h3 { color: #005596; margin-top: 0; margin-bottom: 5px; }
.modal-login p { font-size: 0.9rem; color: #666; margin-bottom: 20px; }
.modal-login .form-group { margin-bottom: 15px; }
.modal-login input { width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }
.modal-login input:focus { border-color: #005596; outline: none; }
.modal-actions { display: flex; gap: 10px; margin-top: 20px; }
.btn-entrar { flex: 1; background-color: #005596; color: white; border: none; padding: 10px; border-radius: 6px; font-weight: bold; cursor: pointer; }
.btn-entrar:hover { background-color: #003d73; }
.btn-cancelar { flex: 1; background-color: #e0e0e0; color: #333; border: none; padding: 10px; border-radius: 6px; font-weight: bold; cursor: pointer; }
.btn-cancelar:hover { background-color: #ccc; }
</style>  