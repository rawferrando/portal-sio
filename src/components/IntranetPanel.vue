<script setup>
import { ref, onMounted } from 'vue'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'

const apiUrl = 'http://localhost:5000/api/instrumentos'

const estaLogueado = ref(false)
const seccionActiva = ref('dashboard')
const usuario = ref('')
const password = ref('')
const recordarSesion = ref(false)
const instrumentos = ref([])

// Variable per saber si estem editant o creant
const editandoId = ref(null)

const nuevoEquipo = ref({ 
  nombre: '', marca: '', numero_serie: '', categoria: '', subcategoria: '', ultima_calibracion: '', descripcion: '', parametros_tecnicos: '' 
})

const cargarInstrumentos = async () => {
  try {
    const respuesta = await fetch(apiUrl)
    instrumentos.value = await respuesta.json()
  } catch (error) { console.error("Error carregant:", error) }
}

onMounted(() => {
  if (sessionStorage.getItem('sio_auth') === 'true' || localStorage.getItem('sio_auth') === 'true') {
    estaLogueado.value = true
    cargarInstrumentos()
  }
})

const iniciarSesion = () => {
  if (usuario.value === 'sio' && password.value === 'admin') {
    if (recordarSesion.value) {
      localStorage.setItem('sio_auth', 'true')
    } else {
      sessionStorage.setItem('sio_auth', 'true')
    }
    estaLogueado.value = true
    cargarInstrumentos()
  } else {
    alert("Usuari o contrasenya incorrectes")
  }
}

const cerrarSesion = () => {
  sessionStorage.removeItem('sio_auth')
  localStorage.removeItem('sio_auth')
  estaLogueado.value = false
}

// AQUÍ ESTÀ LA FUNCIÓ PER CARREGAR L'EDICIÓ
const cargarParaEditar = (inst) => {
  editandoId.value = inst.id
  nuevoEquipo.value = { 
    nombre: inst.nombre, 
    marca: inst.marca || '', 
    numero_serie: inst.numero_serie || '',
    categoria: inst.categoria || '', 
    subcategoria: inst.subcategoria || '', 
    ultima_calibracion: inst.ultima_calibracion || '', 
    descripcion: inst.descripcion || '', 
    parametros_tecnicos: inst.parametros_tecnicos || '' 
  }
  seccionActiva.value = 'instrumentacion' // Canvia directament a la pestanya del formulari
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const cancelarEdicion = () => {
  editandoId.value = null
  nuevoEquipo.value = { nombre: '', marca: '', numero_serie: '', categoria: '', subcategoria: '', ultima_calibracion: '', descripcion: '', parametros_tecnicos: '' }
  seccionActiva.value = 'dashboard'
}

const guardarInstrumento = async () => {
  try {
    const metodo = editandoId.value ? 'PUT' : 'POST'
    const url = editandoId.value ? `${apiUrl}/${editandoId.value}` : apiUrl

    const respuesta = await fetch(url, {
      method: metodo,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(nuevoEquipo.value)
    })
    if (respuesta.ok) {
      alert(editandoId.value ? "✅ Instrument actualitzat!" : "✅ Equip registrat!")
      cancelarEdicion()
      cargarInstrumentos()
    }
  } catch (error) { console.error(error) }
}

const eliminarInstrumento = async (id) => {
  if (!confirm("Segur que vols esborrar aquest instrument?")) return
  try {
    const respuesta = await fetch(`${apiUrl}/${id}`, { method: 'DELETE' })
    if (respuesta.ok) {
      alert("🗑️ Instrument eliminat")
      cargarInstrumentos()
    }
  } catch (error) { console.error(error) }
}
</script>

<template>
  <div class="intranet-wrapper">
    
    <div v-if="!estaLogueado" class="login-overlay">
      <div class="login-box">
        <h2>Accés SIO</h2>
        <form @submit.prevent="iniciarSesion">
          <input v-model="usuario" placeholder="Usuari" required>
          <input type="password" v-model="password" placeholder="Contrasenya" required>
          
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 15px; font-size: 0.9rem; color: #555;">
            <input type="checkbox" v-model="recordarSesion" id="recordar" style="width: auto; margin: 0;">
            <label for="recordar" style="cursor: pointer;">Recordar sessió</label>
          </div>

          <button type="submit">ENTRAR</button>
        </form>
      </div>
    </div>

    <div v-else class="dashboard-grid">
      <aside class="sidebar">
        <h3 class="sidebar-title">Panel SIO</h3>
        <nav class="sidebar-nav">
          <a href="#" @click="cancelarEdicion" :class="{active: seccionActiva === 'dashboard'}">📊 Visión General</a>
          <a href="#" @click="seccionActiva = 'instrumentacion'" :class="{active: seccionActiva === 'instrumentacion'}">
            {{ editandoId ? '✏️ Editant Instrument' : '🛠️ Alta Instrumento' }}
          </a>
          <a href="/" target="_blank" class="btn-web">🌐 Ver Web Pública</a>
        </nav>
        <button @click="cerrarSesion" class="btn-logout">Cerrar Sessió</button>
      </aside>

      <main class="main-content">
        <div v-if="seccionActiva === 'instrumentacion'" class="admin-panel">
          <h2>{{ editandoId ? '✏️ Editar Instrument' : '➕ Registrar Nou Instrument' }}</h2>
          
          <form @submit.prevent="guardarInstrumento" class="grid-form">
            
            <div style="grid-column: span 2; display: flex; gap: 10px; margin-bottom: 5px;">
              <div style="flex: 1;">
                <label style="font-size: 0.85rem; font-weight: bold; color: #555;">Nom de l'equip:</label>
                <input v-model="nuevoEquipo.nombre" placeholder="Ex: CTD-48M" required style="width: 100%; box-sizing: border-box;">
              </div>
              <div style="flex: 1;">
                <label style="font-size: 0.85rem; font-weight: bold; color: #555;">Marca / Fabricant:</label>
                <input v-model="nuevoEquipo.marca" placeholder="Ex: Sea-Bird" style="width: 100%; box-sizing: border-box;">
              </div>
              <div style="flex: 1; background-color: #fff3cd; padding: 5px 10px; border-radius: 4px; border: 1px dashed #ffeeba;">
                <label style="color: #856404; font-size: 0.85rem; font-weight: bold;">🔒 Número de Sèrie (Privat):</label>
                <input v-model="nuevoEquipo.numero_serie" placeholder="Ex: SN-180" style="background: white; width: 100%; box-sizing: border-box;" />
              </div>
            </div>

            <div style="grid-column: span 2; display: flex; gap: 10px; margin-bottom: 10px;">
              <select v-model="nuevoEquipo.categoria" required style="flex: 1;">
                <option value="" disabled selected>Categoria</option>
                <option value="Física">Física</option>
                <option value="Química">Química</option>
                <option value="Biologia">Biologia</option>
                <option value="Geologia">Geologia</option>
              </select>
              <select v-model="nuevoEquipo.subcategoria" required style="flex: 1;">
                <option value="" disabled selected>Subcategoria</option>
                <option value="General">General</option>
                <option value="Sondes">Sondes</option>
                <option value="Mostreig">Mostreig</option>
                <option value="Sistemes Estacionaris">Sistemes Estacionaris</option>
              </select>
              <input v-model="nuevoEquipo.ultima_calibracion" type="date" required style="flex: 1;">
            </div>

            <div style="grid-column: span 2; margin-top: 10px;">
              <label style="font-weight: bold; color: #333;">Descripció tècnica:</label>
              <div style="background: white; border-radius: 4px;">
                <QuillEditor theme="snow" v-model:content="nuevoEquipo.descripcion" contentType="html" toolbar="essential" />
              </div>
            </div>

            <div style="grid-column: span 2; margin-top: 10px; margin-bottom: 20px;">
              <label style="font-weight: bold; color: #333;">Paràmetres / Manuals:</label>
              <div style="background: white; border-radius: 4px;">
                <QuillEditor theme="snow" v-model:content="nuevoEquipo.parametros_tecnicos" contentType="html" toolbar="essential" />
              </div>
            </div>

            <div style="grid-column: span 2; display: flex; gap: 10px;">
              <button type="submit" style="flex: 1; padding: 12px; font-weight: bold; background: #012169; color: white; border: none; border-radius: 4px; cursor: pointer;">
                {{ editandoId ? '💾 Desar Canvis' : '➕ Registrar al Catàleg' }}
              </button>
              
              <button v-if="editandoId" type="button" @click="cancelarEdicion" style="flex: 0.3; background: #ccc; color: #333; font-weight: bold; padding: 12px; border: none; border-radius: 4px; cursor: pointer;">
                ❌ Cancel·lar
              </button>
            </div>
          </form>
        </div>

        <div v-else class="dashboard-view">
          <h3>Inventari actual</h3>
          <table class="tabla-instrumentos">
            <tr v-for="inst in instrumentos" :key="inst.id">
              <td>
                <strong>{{ inst.nombre }}</strong> <br> 
                <small>{{ inst.marca }}</small>
                <span v-if="inst.numero_serie" style="color: #d32f2f; font-size: 0.85em; margin-left: 10px; background: #ffebee; padding: 2px 6px; border-radius: 4px;">
                  🔒 SN: {{ inst.numero_serie }}
                </span>
              </td>
              <td style="text-align: right; width: 220px;">
                <button @click="cargarParaEditar(inst)" class="btn-edit" style="margin-right: 5px;">✏️ Editar</button>
                <button @click="eliminarInstrumento(inst.id)" class="btn-delete">🗑️ Esborrar</button>
              </td>
            </tr>
          </table>
        </div>
      </main>
    </div>
  </div>
</template>

<style scoped>
.btn-web { background: #8cc63f; color: white !important; margin-top: 15px; border-radius: 4px; padding: 10px; text-align: center; }
.btn-web:hover { background: #7ab335; }
.tabla-instrumentos { width: 100%; border-collapse: collapse; margin-top: 20px; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
.tabla-instrumentos td { padding: 15px; border-bottom: 1px solid #eee; vertical-align: middle; }
.btn-delete { background: #d9534f; color: white; border: none; padding: 8px 12px; border-radius: 4px; cursor: pointer; transition: 0.2s; }
.btn-delete:hover { background: #c9302c; }
.btn-edit { background: #0086c0; color: white; border: none; padding: 8px 12px; border-radius: 4px; cursor: pointer; transition: 0.2s; }
.btn-edit:hover { background: #005f8a; }
.intranet-wrapper { min-height: 100vh; }
.login-overlay { position: fixed; inset: 0; background: #012169; display: flex; align-items: center; justify-content: center; z-index: 100; }
.login-box { background: white; padding: 40px; border-radius: 8px; width: 300px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); }
.login-box input { width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;}
.login-box button { width: 100%; padding: 10px; background: #8cc63f; color: #012169; font-weight: bold; border: none; border-radius: 4px; cursor: pointer; }
.dashboard-grid { display: flex; min-height: 100vh; }
.sidebar { width: 250px; background: #012169; color: white; padding: 20px; display: flex; flex-direction: column; }
.sidebar-nav a { display: block; color: #ccc; padding: 10px; text-decoration: none; border-radius: 4px; margin-bottom: 5px; }
.sidebar-nav a:hover { background: rgba(255,255,255,0.1); }
.sidebar-nav a.active { color: white; font-weight: bold; border-left: 3px solid #8cc63f; background: rgba(255,255,255,0.05); }
.btn-logout { margin-top: auto; background: none; border: 1px solid white; color: white; padding: 10px; cursor: pointer; border-radius: 4px; transition: 0.2s; }
.btn-logout:hover { background: white; color: #012169; }
.main-content { flex-grow: 1; padding: 40px; background: #f4f7f9; }
.grid-form { display: grid; gap: 10px; max-width: 800px; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
.grid-form input, .grid-form select { padding: 10px; border: 1px solid #ccc; border-radius: 4px; }
</style>