<script setup>
import { ref } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Instrumentacion from './components/Instrumentacion.vue'

// Importamos los componentes de la intranet que ya teníamos
import FormularioSensor from './components/FormularioSensor.vue'
import IntranetSensores from './components/IntranetSensores.vue'

const paginaActual = ref('inicio')

// Variables de la Intranet SIO
const estaAutenticado = ref(false)
const usuarioInput = ref('')
const passwordInput = ref('')

// El desplegable mágico de la intranet
const moduloActivo = ref('sensores') 

const intentarLogin = () => {
  if (usuarioInput.value === 'admin' && passwordInput.value === 'sio2026') {
    estaAutenticado.value = true
    usuarioInput.value = ''
    passwordInput.value = ''
  } else {
    alert("❌ Credenciales incorrectas.")
    usuarioInput.value = ''
    passwordInput.value = ''
  }
}

const salir = () => {
  estaAutenticado.value = false
  paginaActual.value = 'inicio'
  moduloActivo.value = 'sensores'
}
</script>

<template>
  <div id="layout-sio">
    <header class="header-icm">
      <div class="logo-area">
        <img src="./assets/logo-sio.jpg" class="logo-img" @click="paginaActual = 'inicio'" alt="Logo SIO" />
      </div>
      <nav class="nav-idiomas">
        <span>CAT | CAS | ENG</span>
        <a href="#" @click.prevent="paginaActual = 'intranet'" class="enlace-privado">
          {{ estaAutenticado ? '🔓 Intranet SIO' : '🔒 Área Privada' }}
        </a>
      </nav>
    </header>

    <main class="contenedor-principal">
      
      <div v-if="paginaActual !== 'intranet'">
        <QuienesSomos v-if="paginaActual === 'inicio'" @ir-a-instrumentacion="paginaActual = 'instrumentacion'" />
        <Instrumentacion v-else-if="paginaActual === 'instrumentacion'" @volver="paginaActual = 'inicio'" />
      </div>

      <div v-else class="seccion-intranet">
        
        <div v-if="!estaAutenticado" class="login-card">
          <h3>Intranet SIO</h3>
          <p>Área exclusiva para personal técnico</p>
          <div class="form-login">
            <div class="campo-input">
              <label>Usuario:</label>
              <input v-model="usuarioInput" type="text" placeholder="ej: admin">
            </div>
            <div class="campo-input">
              <label>Contraseña:</label>
              <input v-model="passwordInput" type="password">
            </div>
            <button @click="intentarLogin" class="btn-entrar">Iniciar Sesión</button>
          </div>
        </div>

        <div v-else class="panel-control">
          <div class="cabecera-panel">
            <h2>⚙️ Panel de Gestión SIO</h2>
            <button @click="salir" class="btn-salir">Cerrar Sesión</button>
          </div>
          
          <div class="caja-desplegable">
            <label for="selector-modulo"><strong>Selecciona el módulo a gestionar:</strong></label>
            <select id="selector-modulo" v-model="moduloActivo" class="select-intranet">
              <option value="sensores">📡 Equipos, Sensores e Instrumentación</option>
              <option value="fondeos">⚓ Fondeos y Despliegues (Fase 2)</option>
            </select>
          </div>

          <div v-if="moduloActivo === 'sensores'" class="vista-modulo">
            <FormularioSensor />
            <hr class="separador-modulo" />
            <IntranetSensores />
          </div>

        </div>
      </div>
    </main>

    <footer class="footer-sio">
      <p>&copy; 2026 SIO - Instituto de Ciencias del Mar (CSIC)</p>
    </footer>
  </div>
</template>

<style>
/* Reset y Estructura */
body { margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f9; color: #333; }
#layout-sio { display: flex; flex-direction: column; min-height: 100vh; }
.contenedor-principal { flex: 1; padding: 40px 20px; width: 100%; max-width: 1200px; margin: 0 auto; box-sizing: border-box; }

/* Cabecera y Logo blindados */
.header-icm { background-color: #005596; color: white; display: flex; justify-content: space-between; align-items: center; padding: 10px 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
.logo-img { height: auto; max-height: 60px; cursor: pointer; display: block; }
.nav-idiomas { display: flex; align-items: center; gap: 20px; font-size: 0.9rem; }
.enlace-privado { background-color: white; color: #005596; padding: 8px 15px; border-radius: 4px; text-decoration: none; font-weight: bold; }

/* Intranet y Login */
.seccion-intranet { display: flex; flex-direction: column; align-items: center; width: 100%; }
.login-card { background: white; padding: 35px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border-top: 4px solid #005596; text-align: center; max-width: 320px; width: 100%; margin: 50px auto; }
.login-card h3 { color: #005596; margin: 0 0 5px 0; }
.login-card p { color: #666; font-size: 0.85rem; margin-bottom: 25px; }
.form-login { display: flex; flex-direction: column; gap: 15px; }
.campo-input { text-align: left; }
.campo-input label { display: block; font-size: 0.9rem; font-weight: bold; margin-bottom: 5px; }
.campo-input input { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }
.btn-entrar { background: #005596; color: white; border: none; padding: 12px; border-radius: 4px; font-weight: bold; cursor: pointer; }

/* Panel de Control */
.panel-control { width: 100%; display: flex; flex-direction: column; align-items: center; }
.cabecera-panel { display: flex; justify-content: space-between; width: 100%; align-items: center; margin-bottom: 30px; border-bottom: 2px solid #eee; padding-bottom: 15px; }
.cabecera-panel h2 { color: #005596; margin: 0; }
.btn-salir { background: #dc3545; color: white; border: none; padding: 8px 15px; border-radius: 4px; cursor: pointer; font-weight: bold; }

/* Desplegable */
.caja-desplegable { background-color: #e2eef7; padding: 20px; border-radius: 8px; width: 100%; display: flex; flex-direction: column; gap: 10px; margin-bottom: 30px; }
.select-intranet { padding: 12px; font-size: 1.1rem; border: 2px solid #005596; border-radius: 6px; cursor: pointer; }

.vista-modulo { width: 100%; }
.separador-modulo { border: 0; border-top: 2px dashed #ccc; margin: 40px 0; }

.footer-sio { background-color: #333; color: #ccc; text-align: center; padding: 20px; margin-top: auto; font-size: 0.9rem; }
</style>