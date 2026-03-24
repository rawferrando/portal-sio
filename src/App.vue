<script setup>
import { ref, onMounted } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Instrumentacion from './components/Instrumentacion.vue'
import IntranetPanel from './components/IntranetPanel.vue'

const vistaActual = ref('inicio')
const menuPrivadoVisible = ref(false)
const usuarioLogueadoSio = ref(false)
const inputUsuario = ref('')
const inputPassword = ref('')
const errorLogin = ref(false)

onMounted(() => {
  if (sessionStorage.getItem('sio_auth') === 'true') {
    usuarioLogueadoSio.value = true
  }
})

const intentarLogin = () => {
  if (inputUsuario.value === 'admin' && inputPassword.value === 'sio2026') {
    sessionStorage.setItem('sio_auth', 'true')
    usuarioLogueadoSio.value = true
    errorLogin.value = false
    menuPrivadoVisible.value = false
    vistaActual.value = 'intranet'
  } else {
    errorLogin.value = true
  }
}

const cerrarSesion = () => {
  sessionStorage.removeItem('sio_auth')
  usuarioLogueadoSio.value = false
  vistaActual.value = 'inicio'
}

const irAIntranet = () => {
  vistaActual.value = 'intranet'
  menuPrivadoVisible.value = false
  window.scrollTo(0, 0)
}

const irAInstrumentacion = () => { 
  vistaActual.value = 'instrumentacion'
  window.scrollTo(0, 0)
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
            <button class="btn-intranet" @click="menuPrivadoVisible = !menuPrivadoVisible">
              <span>{{ usuarioLogueadoSio ? '🔒 Admin SIO' : '👤 Área Privada' }}</span>
            </button>
            
            <div v-if="menuPrivadoVisible" class="menu-desplegable-privado">
              <div v-if="!usuarioLogueadoSio" class="formulario-login-menu">
                <input v-model="inputUsuario" type="text" placeholder="Usuario" />
                <input v-model="inputPassword" type="password" placeholder="Pass" />
                <button @click="intentarLogin" class="btn-entrar-login">Acceder</button>
              </div>
              <div v-else class="menu-acciones-intranet">
                <button @click="irAIntranet">➕ Añadir Instrumentación</button>
                <button @click="cerrarSesion" class="btn-cerrar-sesion-interna">🚪 Cerrar Sesión</button>
              </div>
            </div>
          </div>
        </nav>
      </div>
    </header>

    <main class="main-content">
      <QuienesSomos v-if="vistaActual === 'inicio'" @cambiar-pagina="irAInstrumentacion" />
      <Instrumentacion v-else-if="vistaActual === 'instrumentacion'" @volver="volverAInicio" />
      
      <div v-else-if="vistaActual === 'intranet'" class="vista-intranet">
        <button @click="volverAInicio" class="btn-volver">⬅ Volver al Inicio</button>
        <h2>🛡️ Intranet SIO</h2>
      </div>
    </main>

    <footer class="footer-sio">
      <p><strong>Institut de Ciències del Mar (ICM-CSIC)</strong></p>
      <p>📧 sio@icm.csic.es | 📍 Pg. Marítim de la Barceloneta, 37, 08003 Barcelona</p>
    </footer>
  </div>
</template>

<style>
body { margin: 0; font-family: 'Segoe UI', sans-serif; background-color: #f4f7f9; }
.app-container { display: flex; flex-direction: column; min-height: 100vh; }

/* HEADER AJUSTADO AL CONTENIDO (MENOS ALTO) */
.main-header { 
  background-color: #005596; 
  color: white; 
  padding: 5px 0; 
  border-bottom: 2px solid #003366; 
}
.contenedor-cabecera { 
  display: flex; 
  justify-content: space-between; 
  align-items: center; 
  max-width: 1200px; 
  margin: 0 auto; 
  padding: 0 20px; 
}

.menu-principal { display: flex; align-items: center; gap: 20px; }

/* ESTILOS IDIOMAS */
.selector-idiomas { display: flex; gap: 5px; }
.btn-idioma { 
  background: none; 
  border: none; 
  color: white; 
  font-size: 0.75rem; 
  cursor: pointer; 
  padding: 2px 5px; 
  border-radius: 3px; 
  opacity: 0.7;
}
.btn-idioma.active { opacity: 1; font-weight: bold; border: 1px solid white; }

.btn-intranet { 
  background: white; 
  color: #005596; 
  border: none; 
  padding: 5px 12px; 
  border-radius: 4px; 
  cursor: pointer; 
  font-weight: bold; 
  font-size: 0.85rem;
}

.main-content { 
  flex: 1;
  width: 100%; 
  max-width: 1200px; 
  margin: 0 auto; 
  padding: 20px; /* Le damos 60px de margen por abajo para que respire un poco antes del footer */
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: center; 
}
.footer-sio { background-color: #005596; color: white; text-align: center; padding: 20px; margin-top: auto; border-top: 3px solid #003366; font-size: 0.9rem; }
.footer-sio p { margin: 3px 0; }
</style>