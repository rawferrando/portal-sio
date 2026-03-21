<script setup>
import { ref, onMounted } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Instrumentacion from './components/Instrumentacion.vue'

// Vistas: 'inicio', 'instrumentacion', 'intranet'
const vistaActual = ref('inicio')
const menuPrivadoVisible = ref(false)

// Login Intranet SIO
const usuarioLogueadoSio = ref(false)
const inputUsuario = ref('')
const inputPassword = ref('')
const errorLogin = ref(false)

// Formulario de Alta en Intranet
const nuevoEquipo = ref({ id: '', nombre: '', tipo: 'Sensores de Presión', fabricante: '' })

onMounted(() => {
  if (sessionStorage.getItem('sio_auth') === 'true') {
    usuarioLogueadoSio.value = true
  }
})

const intentarLogin = () => {
  if (inputUsuario.value === 'admin' && inputPassword.value === 'sio2026') {
    sessionStorage.setItem('sio_auth', 'true')
    usuarioLogueadoSio.value = true
    inputUsuario.value = ''
    inputPassword.value = ''
    errorLogin.value = false
  } else {
    errorLogin.value = true
    inputPassword.value = ''
  }
}

const cerrarSesion = () => {
  sessionStorage.removeItem('sio_auth')
  usuarioLogueadoSio.value = false
  menuPrivadoVisible.value = false
  if (vistaActual.value === 'intranet') vistaActual.value = 'inicio'
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

const guardarNuevoEquipo = () => {
  alert(`✅ El equipo ${nuevoEquipo.value.nombre} ha sido guardado en la base de datos del catálogo.`)
  nuevoEquipo.value = { id: '', nombre: '', tipo: 'Sensores de Presión', fabricante: '' }
}
</script>

<template>
  <div class="app-container">
    <header class="main-header">
      <div class="contenedor-cabecera">
        
        <div class="logo-area">
          <img src="./assets/logo-sio.jpg" alt="Logo SIO ICM-CSIC" class="imagen-logo" />
        </div>
        
        <nav class="menu-principal">
          <div class="selector-idiomas">
            <button class="btn-idioma">CAT</button>
            <button class="btn-idioma active">CAS</button>
            <button class="btn-idioma">ENG</button>
          </div>
          
          <div class="area-privada-wrapper">
            <button class="btn-intranet" :class="{ 'logueado': usuarioLogueadoSio }" @click="menuPrivadoVisible = !menuPrivadoVisible">
              <span v-if="!usuarioLogueadoSio">👤 Área Privada</span>
              <span v-else>🔒 Admin SIO</span>
            </button>
            
            <div v-if="menuPrivadoVisible" class="menu-desplegable-privado">
              <div v-if="!usuarioLogueadoSio" class="formulario-login-menu">
                <h6>Acceso Corporativo SIO</h6>
                <input v-model="inputUsuario" type="text" placeholder="Usuario (admin)" />
                <input v-model="inputPassword" type="password" placeholder="Contraseña (sio2026)" />
                <p v-if="errorLogin" class="error-text">❌ Credenciales incorrectas.</p>
                <button @click="intentarLogin" class="btn-entrar-login">Entrar</button>
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
      <QuienesSomos v-if="vistaActual === 'inicio'" @ir-a-instrumentacion="irAInstrumentacion" />
      
      <Instrumentacion v-else-if="vistaActual === 'instrumentacion'" @volver="volverAInicio" />

      <div v-else-if="vistaActual === 'intranet'" class="vista-intranet">
        <button @click="volverAInicio" class="btn-volver">⬅ Volver al Inicio</button>
        <h2>🛡️ Intranet SIO - Alta de Instrumentación</h2>
        <p>Añade nuevos equipos al catálogo de la WIKISIO.</p>
        
        <div class="caja-formulario-alta">
          <div class="campo">
            <label>ID del Equipo:</label>
            <input v-model="nuevoEquipo.id" type="text" placeholder="Ej. SNS-005" />
          </div>
          <div class="campo">
            <label>Nombre del Instrumento:</label>
            <input v-model="nuevoEquipo.nombre" type="text" placeholder="Ej. CTD SBE 911plus" />
          </div>
          <div class="campo">
            <label>Categoría:</label>
            <select v-model="nuevoEquipo.tipo">
              <option value="Sensores de Presión">Sensores de Presión</option>
              <option value="Laboratorio">Equipos de Laboratorio</option>
              <option value="Vehículos Autónomos">Vehículos Autónomos</option>
            </select>
          </div>
          <div class="campo">
            <label>Fabricante:</label>
            <input v-model="nuevoEquipo.fabricante" type="text" placeholder="Ej. Sea-Bird" />
          </div>
          <button @click="guardarNuevoEquipo" class="btn-guardar-alta">💾 Añadir al Catálogo</button>
        </div>
      </div>
    </main>

    <footer class="main-footer">
      <p>&copy; 2026 SIO - Instituto de Ciencias del Mar (CSIC)</p>
    </footer>
  </div>
</template>

<style>
body { margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f9; color: #333; }
.app-container { display: flex; flex-direction: column; min-height: 100vh; }
.main-content { flex: 1; padding: 30px 20px; box-sizing: border-box; width: 100%; max-width: 1200px; margin: 0 auto; }

.main-header { background-color: #005596; color: white; padding: 10px 0; display: flex; justify-content: center; border-bottom: 3px solid #003366; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
.contenedor-cabecera { width: 100%; max-width: 1200px; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; }
.logo-area { display: flex; align-items: center; }
.imagen-logo { height: auto; max-height: 60px; width: auto; display: block; }

.menu-principal { display: flex; align-items: center; gap: 20px; }
.selector-idiomas { display: flex; gap: 5px; }
.btn-idioma { background: none; border: none; color: white; font-size: 0.85rem; cursor: pointer; padding: 3px 6px; border-radius: 3px; transition: background 0.2s; }
.btn-idioma:hover { background-color: rgba(255,255,255,0.1); }
.btn-idioma.active { background-color: white; color: #005596; font-weight: bold; }

.area-privada-wrapper { position: relative; }
.btn-intranet { background-color: white; color: #005596; border: none; padding: 8px 15px; border-radius: 4px; cursor: pointer; font-weight: bold; display: flex; align-items: center; gap: 5px; }
.btn-intranet.logueado { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }

.menu-desplegable-privado { position: absolute; top: 100%; right: 0; background: white; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: flex; flex-direction: column; min-width: 250px; margin-top: 10px; z-index: 100; overflow: hidden; }
.formulario-login-menu { padding: 20px; display: flex; flex-direction: column; gap: 10px; }
.formulario-login-menu h6 { margin: 0 0 10px 0; color: #005596; font-size: 1rem; text-align: center; border-bottom: 1px solid #eee; padding-bottom: 10px; }
.formulario-login-menu input { padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 0.9rem; }
.error-text { color: #dc3545; font-size: 0.8rem; margin: 0; text-align: center; font-weight: bold; }
.btn-entrar-login { background-color: #005596; color: white; border: none; padding: 12px; border-radius: 4px; cursor: pointer; font-weight: bold; margin-top: 5px; }

.menu-acciones-intranet { display: flex; flex-direction: column; }
.menu-acciones-intranet button { background: none; border: none; color: #333; padding: 12px 15px; text-align: left; cursor: pointer; font-size: 0.95rem; border-bottom: 1px solid #eee; transition: background 0.2s; }
.menu-acciones-intranet button:hover { background-color: #f4f7f9; color: #005596; font-weight: bold; }
.btn-cerrar-sesion-interna { background-color: #fff5f5 !important; color: #dc3545 !important; border-bottom: none !important; }

/* ESTILOS INTRANET */
.vista-intranet { animation: fadeIn 0.4s ease; }
.vista-intranet h2 { color: #005596; margin-bottom: 5px; }
.btn-volver { background: #6c757d; color: white; border: none; padding: 10px 18px; border-radius: 4px; cursor: pointer; font-weight: bold; margin-bottom: 20px; }
.caja-formulario-alta { background: white; padding: 30px; border-radius: 8px; border: 1px solid #ddd; max-width: 600px; margin-top: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
.campo { display: flex; flex-direction: column; margin-bottom: 15px; gap: 5px; }
.campo label { font-weight: bold; color: #555; font-size: 0.9rem; }
.campo input, .campo select { padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 1rem; }
.btn-guardar-alta { background-color: #28a745; color: white; border: none; padding: 12px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; font-size: 1rem; margin-top: 10px; width: 100%; }

.main-footer { background-color: #333; color: #ccc; padding: 15px 20px; text-align: center; font-size: 0.9rem; margin-top: auto; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
</style>