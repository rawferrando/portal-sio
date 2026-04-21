<script setup>
import { ref, onMounted } from 'vue'

const emit = defineEmits(['volver'])
const estaLogueado = ref(false)
const seccionActiva = ref('dashboard')

// --- BASE DE DATOS MAESTRA (Sustituye a la Wiki) ---
const instrumentos = ref([
  { 
    id: 1, 
    nombre: 'CTD Sea-Bird 911plus', 
    categoria: 'Sensores', 
    estado: 'Operativo', 
    calibrado: true,
    ultimaCalibracion: '2026-01-10',
    descripcion: 'Perfilador de precisión para conductividad y temperatura.',
    reservas: [{ inicio: '2026-05-01', fin: '2026-05-10', usuario: 'Lab. Biología' }]
  },
  { 
    id: 2, 
    nombre: 'Glider SeaExplorer', 
    categoria: 'Plataformas', 
    estado: 'Mantenimiento', 
    calibrado: false,
    ultimaCalibracion: '2025-06-15',
    descripcion: 'Vehículo autónomo para misiones de larga duración.',
    reservas: []
  }
])

// --- GESTIÓN DE NUEVOS EQUIPOS ---
const editando = ref(null)
const mostrarForm = ref(false)
const formulario = ref({ nombre: '', categoria: 'Sensores', descripcion: '', calibrado: true, estado: 'Operativo' })

const guardarEquipo = () => {
  if (editando.value) {
    const idx = instrumentos.value.findIndex(i => i.id === editando.value)
    instrumentos.value[idx] = { ...formulario.value, id: editando.value }
  } else {
    instrumentos.value.push({ ...formulario.value, id: Date.now(), reservas: [] })
  }
  cerrarForm()
}

const editar = (item) => {
  editando.value = item.id
  formulario.value = { ...item }
  mostrarForm.value = true
}

const cerrarForm = () => {
  mostrarForm.value = false
  editando.value = null
  formulario.value = { nombre: '', categoria: 'Sensores', descripcion: '', calibrado: true, estado: 'Operativo' }
}

// --- LOGIN ---
const user = ref(''); const pass = ref('');
const login = () => { if(user.value==='sio' && pass.value==='admin') { estaLogueado.value=true; sessionStorage.setItem('sio_auth','true'); } }
onMounted(() => { if(sessionStorage.getItem('sio_auth')==='true') estaLogueado.value=true })
</script>

<template>
  <div class="cms-wrapper">
    <div v-if="!estaLogueado" class="login-screen">
      <div class="login-card">
        <h1>SIO Admin</h1>
        <p>Control central de la Plataforma Web</p>
        <input v-model="user" placeholder="Usuario">
        <input v-model="pass" type="password" placeholder="Contraseña">
        <button @click="login">ENTRAR AL SISTEMA</button>
      </div>
    </div>

    <div v-else class="admin-layout">
      <aside class="admin-sidebar">
        <div class="brand">SIO WEB CMS</div>
        <nav>
          <button @click="seccionActiva='dashboard'" :class="{active: seccionActiva==='dashboard'}">Resumen</button>
          <button @click="seccionActiva='instrumentos'" :class="{active: seccionActiva==='instrumentos'}">Instrumentación</button>
          <button @click="seccionActiva='reservas'" :class="{active: seccionActiva==='reservas'}">Validar Reservas</button>
        </nav>
        <button class="logout" @click="() => { sessionStorage.clear(); estaLogueado=false; }">Cerrar Sesión</button>
      </aside>

      <main class="admin-content">
        <header class="content-header">
          <h2>{{ seccionActiva === 'instrumentos' ? 'Gestor de Equipos (Sustituye a Wiki)' : 'Panel de Control' }}</h2>
          <button v-if="seccionActiva==='instrumentos'" class="btn-add" @click="mostrarForm = true">+ Nuevo Equipo</button>
        </header>

        <section v-if="seccionActiva==='instrumentos'">
          <div v-if="mostrarForm" class="modal-form">
            <div class="form-card">
              <h3>{{ editando ? 'Editar Equipo' : 'Traer contenido de Wiki' }}</h3>
              <div class="form-grid">
                <input v-model="formulario.nombre" placeholder="Nombre del equipo">
                <select v-model="formulario.categoria">
                  <option>Sensores</option><option>Plataformas</option><option>Boyas</option>
                </select>
                <textarea v-model="formulario.descripcion" placeholder="Descripción técnica completa..."></textarea>
                <div class="check-box">
                  <label><input type="checkbox" v-model="formulario.calibrado"> ¿Está Calibrado?</label>
                </div>
              </div>
              <div class="form-btns">
                <button @click="guardarEquipo" class="save">GUARDAR EN WEB</button>
                <button @click="cerrarForm" class="cancel">Cancelar</button>
              </div>
            </div>
          </div>

          <table class="cms-table">
            <thead>
              <tr><th>Equipo</th><th>Categoría</th><th>Estado Calibración</th><th>Reservas Activas</th><th>Acciones</th></tr>
            </thead>
            <tbody>
              <tr v-for="item in instrumentos" :key="item.id">
                <td><strong>{{ item.nombre }}</strong></td>
                <td>{{ item.categoria }}</td>
                <td>
                  <span :class="['dot', item.calibrado ? 'green' : 'red']"></span>
                  {{ item.calibrado ? 'OK' : 'Pendiente' }}
                </td>
                <td>{{ item.reservas.length }}</td>
                <td>
                  <button @click="editar(item)" class="edit">Editar</button>
                </td>
              </tr>
            </tbody>
          </table>
        </section>

        <section v-else class="empty-state">
          <h3>Selecciona una sección para gestionar el contenido.</h3>
          <p>Toda la información introducida aquí se sincroniza automáticamente con el catálogo público.</p>
        </section>
      </main>
    </div>
  </div>
</template>

<style scoped>
.cms-wrapper { min-height: 100vh; background: #f0f4f8; font-family: 'Segoe UI', sans-serif; display: flex; width: 100%; }
.admin-layout { display: flex; width: 100%; }
.admin-sidebar { width: 260px; background: #012169; color: white; padding: 20px; display: flex; flex-direction: column; }
.admin-sidebar nav { flex-grow: 1; margin-top: 30px; display: flex; flex-direction: column; gap: 10px; }
.admin-sidebar button { background: none; border: none; color: #a8bacc; text-align: left; padding: 12px; cursor: pointer; border-radius: 6px; }
.admin-sidebar button.active { background: #0086c0; color: white; }

.admin-content { flex-grow: 1; padding: 40px; }
.content-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
.btn-add { background: #0086c0; color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; }

.cms-table { width: 100%; background: white; border-radius: 12px; border-collapse: collapse; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
.cms-table th { padding: 15px; text-align: left; background: #f8f9fa; border-bottom: 2px solid #edf2f7; }
.cms-table td { padding: 15px; border-bottom: 1px solid #edf2f7; }

.dot { height: 10px; width: 10px; border-radius: 50%; display: inline-block; margin-right: 5px; }
.green { background: #48bb78; }
.red { background: #f56565; }

.modal-form { position: fixed; inset: 0; background: rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center; z-index: 1000; }
.form-card { background: white; padding: 30px; border-radius: 12px; width: 500px; }
.form-grid { display: flex; flex-direction: column; gap: 15px; margin: 20px 0; }
.form-grid input, .form-grid textarea, .form-grid select { padding: 12px; border: 1px solid #ddd; border-radius: 6px; }
.form-btns { display: flex; gap: 10px; }
.save { flex: 1; background: #2f855a; color: white; border: none; padding: 12px; border-radius: 6px; cursor: pointer; }

/* Login */
.login-screen { width: 100%; display: flex; justify-content: center; align-items: center; }
.login-card { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); width: 350px; display: flex; flex-direction: column; gap: 15px; border-top: 6px solid #012169; }
</style>