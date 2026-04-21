<script setup>
import { ref, onMounted } from 'vue'

const emit = defineEmits(['volver'])

const estaLogueado = ref(false)
const usuario = ref('')
const password = ref('')
const errorLogin = ref(false)

// Comprobamos si ya habíamos iniciado sesión antes
onMounted(() => {
  if (sessionStorage.getItem('sio_auth') === 'true') {
    estaLogueado.value = true
  }
})

// Función para entrar
const iniciarSesion = () => {
  // 💡 CREDENCIALES DE PRUEBA: usuario "sio" y contraseña "admin"
  if (usuario.value === 'sio' && password.value === 'admin') {
    sessionStorage.setItem('sio_auth', 'true')
    estaLogueado.value = true
    errorLogin.value = false
  } else {
    errorLogin.value = true
  }
}
<button @click="$emit('volver')" class="btn-ver-web">🌍 Ver Web Pública</button>
// Función para salir
const cerrarSesion = () => {
  sessionStorage.removeItem('sio_auth')
  estaLogueado.value = false
  emit('volver') // Nos devuelve a la portada automáticamente
}
</script>

<template>
  <div class="intranet-wrapper">
    
    <div v-if="!estaLogueado" class="login-container">
      <div class="login-box">
        <div class="login-header">
          <h2>SIO Intranet</h2>
          <p>Acceso restringido a personal</p>
        </div>
        
        <form @submit.prevent="iniciarSesion" class="login-form">
          <div class="input-group">
            <label>Usuario</label>
            <input type="text" v-model="usuario" placeholder="Introduce tu usuario" required>
          </div>
          <div class="input-group">
            <label>Contraseña</label>
            <input type="password" v-model="password" placeholder="••••••••" required>
          </div>
          
          <div v-if="errorLogin" class="error-msg">
            Credenciales incorrectas. Inténtalo de nuevo.
          </div>
          
          <button type="submit" class="btn-login">ACCEDER</button>
        </form>
        <button class="btn-volver-login" @click="$emit('volver')">← Volver a la web pública</button>
      </div>
    </div>

    <div v-else class="dashboard-container">
      
      <aside class="sidebar">
        <div class="sidebar-header">
          <h3>Panel SIO</h3>
          <span class="badge">Admin</span>
        </div>
        <nav class="sidebar-nav">
          <a href="#" class="nav-active">📊 Visión General</a>
          <a href="#">🌊 Estado de Boyas</a>
          <a href="#">🛠️ Equipamiento</a>
          <a href="#">📁 Informes Técnicos</a>
          <a href="#">⚙️ Configuración</a>
        </nav>
        <div class="sidebar-footer">
          <button @click="cerrarSesion" class="btn-logout">Cerrar Sesión</button>
        </div>
      </aside>

      <main class="dashboard-main">
        <header class="dashboard-topbar">
          <h2>Visión General de Sistemas</h2>
          <div class="user-profile">Hola, Equipo SIO</div>
        </header>

        <div class="dashboard-content">
          
          <div class="stats-grid">
            <div class="stat-card">
              <div class="stat-title">Instrumentos Activos</div>
              <div class="stat-value">24</div>
              <div class="stat-status text-green">● Operativos</div>
            </div>
            <div class="stat-card">
              <div class="stat-title">Mantenimientos Pendientes</div>
              <div class="stat-value">3</div>
              <div class="stat-status text-orange">● Esta semana</div>
            </div>
            <div class="stat-card">
              <div class="stat-title">Datos Recopilados (Hoy)</div>
              <div class="stat-value">12.4 GB</div>
              <div class="stat-status text-blue">● Sincronizado</div>
            </div>
          </div>

          <div class="data-section">
            <h3>Monitorización en Tiempo Real</h3>
            <table class="data-table">
              <thead>
                <tr>
                  <th>Estación / Equipo</th>
                  <th>Tipo</th>
                  <th>Última Conexión</th>
                  <th>Estado</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Boya Oceanográfica Costera</td>
                  <td>CTD / Fluorímetro</td>
                  <td>Hace 2 min</td>
                  <td><span class="tag tag-green">En línea</span></td>
                </tr>
                <tr>
                  <td>Glider Submarino (Misión 4)</td>
                  <td>Perfilador</td>
                  <td>Hace 15 min</td>
                  <td><span class="tag tag-green">En línea</span></td>
                </tr>
                <tr>
                  <td>Estación Meteorológica Port</td>
                  <td>Viento / Temp</td>
                  <td>Hace 4 horas</td>
                  <td><span class="tag tag-orange">Revisión req.</span></td>
                </tr>
                <tr>
                  <td>ROV Explorador (BLUE Lab)</td>
                  <td>Cámara / Brazos</td>
                  <td>Apagado</td>
                  <td><span class="tag tag-gray">En taller</span></td>
                </tr>
              </tbody>
            </table>
          </div>

        </div>
      </main>
    </div>
    
  </div>
</template>

<style scoped>
/* Estilos Generales de la Intranet */
.intranet-wrapper {
  min-height: 80vh;
  background-color: #f0f2f5;
  display: flex;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

/* --- ESTILOS DEL LOGIN --- */
.login-container {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 50px 20px;
}
.login-box {
  background: white;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 400px;
  border-top: 5px solid #012169;
}
.login-header h2 { margin: 0; color: #012169; font-size: 24px; }
.login-header p { color: #666; margin-top: 5px; font-size: 14px; margin-bottom: 30px; }

.input-group { display: flex; flex-direction: column; margin-bottom: 20px; }
.input-group label { font-size: 12px; font-weight: bold; color: #333; margin-bottom: 5px; text-transform: uppercase; }
.input-group input { padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; transition: border 0.3s; }
.input-group input:focus { border-color: #0086c0; outline: none; }

.error-msg { color: #d32f2f; background: #ffebee; padding: 10px; border-radius: 6px; font-size: 13px; margin-bottom: 20px; text-align: center; }

.btn-login { width: 100%; padding: 14px; background: #0086c0; color: white; border: none; border-radius: 6px; font-weight: bold; font-size: 16px; cursor: pointer; transition: background 0.3s; }
.btn-login:hover { background: #012169; }

.btn-volver-login { width: 100%; background: none; border: none; color: #666; margin-top: 20px; font-size: 14px; cursor: pointer; }
.btn-volver-login:hover { color: #012169; text-decoration: underline; }
.btn-ver-web {
  width: 100%;
  padding: 10px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid #0086c0;
  color: white;
  border-radius: 6px;
  cursor: pointer;
  margin-bottom: 10px;
  transition: all 0.3s;
} 
.btn-ver-web:hover { background: #0086c0; }

/* --- ESTILOS DEL DASHBOARD --- */
.dashboard-container {
  display: flex;
  width: 100%;
  min-height: 80vh;
}

/* Sidebar */
.sidebar {
  width: 250px;
  background: #012169;
  color: white;
  display: flex;
  flex-direction: column;
}
.sidebar-header { padding: 30px 20px; border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: space-between; }
.sidebar-header h3 { margin: 0; font-size: 18px; }
.badge { background: #0086c0; font-size: 11px; padding: 3px 8px; border-radius: 20px; font-weight: bold; }

.sidebar-nav { display: flex; flex-direction: column; padding: 20px 0; flex-grow: 1; }
.sidebar-nav a { color: #a8bacc; text-decoration: none; padding: 15px 20px; font-size: 15px; transition: all 0.3s; }
.sidebar-nav a:hover, .sidebar-nav a.nav-active { background: rgba(255,255,255,0.1); color: white; border-left: 4px solid #0086c0; }

.sidebar-footer { padding: 20px; border-top: 1px solid rgba(255,255,255,0.1); }
.btn-logout { width: 100%; padding: 10px; background: transparent; border: 1px solid rgba(255,255,255,0.3); color: white; border-radius: 6px; cursor: pointer; transition: all 0.3s; }
.btn-logout:hover { background: rgba(255,255,255,0.1); border-color: white; }

/* Main Content */
.dashboard-main { flex-grow: 1; padding: 30px; overflow-y: auto; }
.dashboard-topbar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
.dashboard-topbar h2 { margin: 0; color: #333; }
.user-profile { font-weight: bold; color: #012169; }

/* Tarjetas de estadísticas */
.stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 40px; }
.stat-card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-left: 4px solid #012169; }
.stat-title { font-size: 14px; color: #666; margin-bottom: 10px; }
.stat-value { font-size: 32px; font-weight: bold; color: #333; margin-bottom: 10px; }
.stat-status { font-size: 13px; font-weight: bold; }

.text-green { color: #2e7d32; }
.text-orange { color: #f57c00; }
.text-blue { color: #0086c0; }

/* Tabla de datos */
.data-section { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
.data-section h3 { margin-top: 0; margin-bottom: 20px; color: #012169; }
.data-table { width: 100%; border-collapse: collapse; text-align: left; }
.data-table th { background: #f8f9fa; padding: 12px 15px; color: #555; font-size: 13px; text-transform: uppercase; border-bottom: 2px solid #eee; }
.data-table td { padding: 15px; border-bottom: 1px solid #eee; font-size: 14px; color: #333; }

.tag { padding: 5px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; }
.tag-green { background: #e8f5e9; color: #2e7d32; }
.tag-orange { background: #fff3e0; color: #f57c00; }
.tag-gray { background: #f5f5f5; color: #757575; }

/* Responsive Dashboard */
@media (max-width: 768px) {
  .dashboard-container { flex-direction: column; }
  .sidebar { width: 100%; }
  .sidebar-nav { flex-direction: row; flex-wrap: wrap; justify-content: center; padding: 10px 0; }
  .sidebar-nav a { padding: 10px; font-size: 13px; border-left: none; border-bottom: 2px solid transparent; }
  .sidebar-nav a:hover, .sidebar-nav a.nav-active { border-left: none; border-bottom: 2px solid #0086c0; }
  .data-section { overflow-x: auto; }
}
</style>