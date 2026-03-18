<script setup>
import { ref } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Instrumentacion from './components/Instrumentacion.vue'
import Embarcacion from './components/Embarcacion.vue'
import Proyectos from './components/Proyectos.vue'
import Diseno from './components/Diseno.vue'

// Importamos los formularios y las tablas
import FormularioSensor from './components/FormularioSensor.vue'
import IntranetSensores from './components/IntranetSensores.vue'
import FormularioFondeo from './components/FormularioFondeo.vue'
import IntranetFondeos from './components/IntranetFondeos.vue'

const paginaActual = ref('inicio')
const estaAutenticado = ref(false)
const usuarioInput = ref('')
const passwordInput = ref('')

// 👇 NUEVA VARIABLE PARA EL DESPLEGABLE 👇
const moduloActivo = ref('sensores') 

const intentarLogin = () => {
  if (usuarioInput.value === 'admin' && passwordInput.value === 'sio2026') {
    estaAutenticado.value = true
  } else {
    alert("❌ Credenciales incorrectas.")
    usuarioInput.value = ''
    passwordInput.value = ''
  }
}

const salir = () => {
  estaAutenticado.value = false
  paginaActual.value = 'inicio'
  usuarioInput.value = ''
  passwordInput.value = ''
  moduloActivo.value = 'sensores' // Resetea el desplegable al salir
}
</script>

<template>
  <div id="layout-sio">
    <header class="header-icm">
      <div class="logo-area">
        <img src="./assets/logo-sio.jpg" class="logo-img" @click="paginaActual = 'inicio'" alt="Logo SIO" />
      </div>
      <nav class="nav-idiomas">
        <span>CA | ES | EN</span>
        <a href="#" @click.prevent="paginaActual = 'intranet'" class="enlace-privado">
          {{ estaAutenticado ? '🔓 Salir' : '🔒' }}
        </a>
      </nav>
    </header>

    <main class="contenedor-principal">
      <div v-if="paginaActual !== 'intranet'">
        <QuienesSomos v-if="paginaActual === 'inicio'" @cambiar-pagina="paginaActual = $event" />
        <Instrumentacion v-else-if="paginaActual === 'instrumentacion'" @volver="paginaActual = 'inicio'" />
        <Embarcacion v-else-if="paginaActual === 'embarcacion'" @volver="paginaActual = 'inicio'" />
        <Proyectos v-else-if="paginaActual === 'proyectos'" @volver="paginaActual = 'inicio'" />
        <Diseno v-else-if="paginaActual === 'diseno'" @volver="paginaActual = 'inicio'" />
      </div>

      <div v-else class="seccion-intranet">
        
        <div v-if="!estaAutenticado" class="login-card">
          <h3 style="color: #005596; margin-bottom: 5px;">Intranet SIO</h3>
          <p style="color: #666; font-size: 0.85rem; margin-top: 0; margin-bottom: 25px;">Área exclusiva para personal investigador</p>
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
            <h2 style="color: #005596; margin: 0;">⚙️ Panel de Gestión SIO</h2>
            <button @click="salir" class="btn-salir">Cerrar Sesión</button>
          </div>
          
          <div class="caja-desplegable">
            <label for="selector-modulo"><strong>Selecciona el módulo a gestionar:</strong></label>
            <select id="selector-modulo" v-model="moduloActivo" class="select-intranet">
              <option value="sensores">📡 Equipos, Sensores e Instrumentación</option>
              <option value="fondeos">⚓ Fondeos y Despliegues en el Mar</option>
            </select>
          </div>

          <div v-if="moduloActivo === 'sensores'" class="vista-modulo">
            <FormularioSensor />
            <hr class="separador-modulo" />
            <IntranetSensores />
          </div>

          <div v-if="moduloActivo === 'fondeos'" class="vista-modulo">
            <FormularioFondeo />
            <hr class="separador-modulo" />
            <IntranetFondeos />
          </div>

        </div>
      </div>
    </main>

    <footer class="footer-sio">
      <p><strong>Institut de Ciències del Mar (ICM-CSIC)</strong></p>
      <p>📧 sio@icm.csic.es | 📍 Pg. Marítim de la Barceloneta, 37, 08003 Barcelona</p>
    </footer>
  </div>
</template>

<style>
#layout-sio { font-family: Arial, sans-serif; display: flex; flex-direction: column; min-height: 100vh; }
.header-icm { background-color: #005596; color: white; display: flex; justify-content: space-between; align-items: center; padding: 1rem 5%; }
.logo-img { height: 80px; cursor: pointer; }
.nav-idiomas { display: flex; align-items: center; gap: 15px; font-weight: bold; color: white; }
.enlace-privado { font-size: 1.2rem; text-decoration: none; cursor: pointer; color: white; }
.contenedor-principal { flex: 1; padding: 2rem 5%; max-width: 1200px; margin: 0 auto; width: 100%; }
.seccion-intranet { display: flex; flex-direction: column; align-items: center; width: 100%; }
.panel-control { width: 100%; display: flex; flex-direction: column; align-items: center; }

/* Cabecera del panel */
.cabecera-panel { display: flex; justify-content: space-between; width: 100%; align-items: center; margin-bottom: 30px; border-bottom: 2px solid #eee; padding-bottom: 15px; }
.btn-salir { background: #dc3545; color: white; border: none; padding: 8px 15px; border-radius: 4px; cursor: pointer; font-weight: bold; }

/* Estilos del Desplegable */
.caja-desplegable { background-color: #f8f9fa; padding: 20px; border-radius: 8px; width: 100%; max-width: 900px; display: flex; flex-direction: column; gap: 10px; margin-bottom: 30px; border: 1px solid #ddd; }
.select-intranet { padding: 12px; font-size: 1.1rem; border: 2px solid #005596; border-radius: 6px; cursor: pointer; background-color: white; color: #333; font-weight: bold; }
.select-intranet:focus { outline: none; border-color: #003d6b; box-shadow: 0 0 5px rgba(0,85,150,0.3); }

/* Contenedor de Formulario + Tabla */
.vista-modulo { width: 100%; display: flex; flex-direction: column; align-items: center; animation: fadeIn 0.3s ease-in-out; }
.separador-modulo { width: 100%; max-width: 900px; border: 0; border-top: 3px dashed #ccc; margin: 40px 0; }

@keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }

/* Estilos Login */
.login-card { background: white; padding: 35px 40px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border-top: 4px solid #005596; text-align: center; max-width: 320px; width: 100%; margin: 50px auto; }
.form-login { display: flex; flex-direction: column; gap: 20px; }
.campo-input { text-align: left; }
.campo-input label { display: block; font-size: 0.9rem; font-weight: bold; color: #333; margin-bottom: 5px; }
.campo-input input { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; font-size: 0.95rem; box-sizing: border-box; }
.btn-entrar { background: #005596; color: white; border: none; padding: 12px; border-radius: 4px; font-weight: bold; cursor: pointer; font-size: 1rem; width: 100%; margin-top: 10px; }
.btn-entrar:hover { background: #00447a; }

.footer-sio { background-color: #005596; color: white; text-align: center; padding: 2rem 1rem; margin-top: auto; }
</style>