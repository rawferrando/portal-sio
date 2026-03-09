<template>
  <div class="intranet-container">
    
    <div v-if="!isLoggedIn" class="login-box">
      <h2>Intranet SIO</h2>
      <p class="subtitulo">Área exclusiva para personal investigador</p>

      <form @submit.prevent="login" class="formulario">
        <div class="grupo-input">
          <label>Usuario:</label>
          <input type="text" v-model="username" placeholder="ej: admin" required />
        </div>
        <div class="grupo-input">
          <label>Contraseña:</label>
          <input type="password" v-model="password" required />
        </div>
        
        <p v-if="error" class="mensaje-error">{{ error }}</p>
        
        <button type="submit" class="btn-entrar">Iniciar Sesión</button>
      </form>
    </div>

    <div v-else class="dashboard">
      <header class="cabecera-dash">
        <h2>Intranet SIO - Estado de Fondeos</h2>
        <button @click="logout" class="btn-salir">Cerrar Sesión</button>
      </header>

      <div class="tabla-contenedor">
        <table class="tabla-fondeos">
          <thead>
            <tr>
              <th>ID Fondeo</th>
              <th>Ubicación</th>
              <th>Profundidad</th>
              <th>Estado</th>
              <th>Última Revisión</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="fondeo in fondeos" :key="fondeo.id">
              <td><strong>{{ fondeo.id }}</strong></td>
              <td>{{ fondeo.ubicacion }}</td>
              <td>{{ fondeo.profundidad }}</td>
              <td>
                <span :class="['etiqueta', fondeo.estado.toLowerCase()]">
                  {{ fondeo.estado }}
                </span>
              </td>
              <td>{{ fondeo.fecha }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'

// Variables para controlar el estado de la pantalla
const isLoggedIn = ref(false)
const username = ref('')
const password = ref('')
const error = ref('')

// Datos simulados para la maqueta
const fondeos = ref([
  { id: 'FND-001', ubicacion: 'Cañón de Blanes', profundidad: '150m', estado: 'Operativo', fecha: '2026-03-01' },
  { id: 'FND-002', ubicacion: 'Delta del Ebro', profundidad: '50m', estado: 'Mantenimiento', fecha: '2026-02-28' },
  { id: 'FND-003', ubicacion: 'Golfo de Rosas', profundidad: '90m', estado: 'Operativo', fecha: '2026-03-05' }
])

// Función que comprueba la contraseña
const login = () => {
  if (username.value === 'admin' && password.value === 'sio2026') {
    isLoggedIn.value = true // Abre el candado
    error.value = ''
  } else {
    error.value = 'Usuario o contraseña incorrectos.'
  }
}

// Función para salir
const logout = () => {
  isLoggedIn.value = false // Cierra el candado
  username.value = ''
  password.value = ''
}
</script>

<style scoped>
.intranet-container {
  max-width: 1000px;
  margin: 4rem auto;
  padding: 0 1rem;
  font-family: Arial, sans-serif;
}

/* Estilos del Login */
.login-box {
  max-width: 400px;
  margin: 0 auto;
  padding: 2.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  background-color: #f8f9fa;
  border-top: 5px solid #0056b3;
}

.login-box h2 {
  color: #0056b3;
  text-align: center;
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.subtitulo {
  text-align: center;
  color: #666;
  margin-bottom: 2rem;
  font-size: 0.9rem;
}

.grupo-input {
  margin-bottom: 1.5rem;
}

.grupo-input label {
  display: block;
  margin-bottom: 0.5rem;
  color: #333;
  font-weight: bold;
}

.grupo-input input {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.mensaje-error {
  color: #dc3545;
  font-size: 0.9rem;
  text-align: center;
}

.btn-entrar {
  width: 100%;
  padding: 0.8rem;
  background-color: #0056b3;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s;
}

.btn-entrar:hover {
  background-color: #004494;
}

/* Estilos del Dashboard / Tabla */
.cabecera-dash {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  border-bottom: 2px solid #e0e0e0;
  padding-bottom: 1rem;
}

.cabecera-dash h2 {
  color: #0056b3;
  margin: 0;
}

.btn-salir {
  padding: 0.5rem 1rem;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.tabla-contenedor {
  overflow-x: auto;
}

.tabla-fondeos {
  width: 100%;
  border-collapse: collapse;
  background-color: white;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.tabla-fondeos th, .tabla-fondeos td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
}

.tabla-fondeos th {
  background-color: #f8f9fa;
  color: #333;
}

/* Etiquetas de estado */
.etiqueta {
  padding: 0.3rem 0.6rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: bold;
}

.etiqueta.operativo {
  background-color: #d4edda;
  color: #155724;
}

.etiqueta.mantenimiento {
  background-color: #fff3cd;
  color: #856404;
}
</style>