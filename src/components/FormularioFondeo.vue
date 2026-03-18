<script setup>
import { ref } from 'vue'

const idFondeo = ref('')
const ubicacion = ref('')
const profundidad = ref('')
const estado = ref('Operativo')

const guardarFondeo = () => {
  if (!idFondeo.value || !ubicacion.value || !profundidad.value) {
    alert("⚠️ Por favor, rellena todos los campos clave del fondeo.")
    return
  }
  alert(`✅ Fondeo ${idFondeo.value} en ${ubicacion.value} listo para enviar a la base de datos.`)
  // Aquí limpiaremos el formulario tras guardar
  idFondeo.value = ''
  ubicacion.value = ''
  profundidad.value = ''
  estado.value = 'Operativo'
}
</script>

<template>
  <div class="tarjeta-formulario">
    <div class="cabecera-form">
      <h3>⚓ Alta de Nuevo Fondeo</h3>
    </div>
    <div class="cuerpo-form">
      <div class="fila-inputs">
        <input v-model="idFondeo" type="text" placeholder="ID Fondeo (ej. FND-003)">
        <input v-model="ubicacion" type="text" placeholder="Ubicación (ej. Blanes)">
      </div>
      <div class="fila-inputs">
        <input v-model="profundidad" type="number" placeholder="Profundidad (m)">
        <select v-model="estado">
          <option value="Operativo">Operativo</option>
          <option value="Mantenimiento">Mantenimiento</option>
          <option value="Perdido">Perdido / Sin señal</option>
        </select>
      </div>
      <button @click="guardarFondeo" class="btn-guardar">Registrar Fondeo</button>
    </div>
  </div>
</template>

<style scoped>
.tarjeta-formulario { background: white; border-radius: 8px; border: 1px solid #e0e0e0; max-width: 900px; width: 100%; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
.cabecera-form { background-color: #f8f9fa; padding: 15px 20px; border-bottom: 1px solid #e0e0e0; border-radius: 8px 8px 0 0; }
.cabecera-form h3 { margin: 0; color: #005596; font-size: 1.2rem; display: flex; align-items: center; gap: 8px; }
.cuerpo-form { padding: 20px; display: flex; flex-direction: column; gap: 15px; }
.fila-inputs { display: flex; gap: 15px; }
.fila-inputs input, .fila-inputs select { flex: 1; padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 0.95rem; }
.btn-guardar { background-color: #005596; color: white; border: none; padding: 12px; border-radius: 4px; font-weight: bold; cursor: pointer; transition: background 0.3s; }
.btn-guardar:hover { background-color: #00447a; }
</style>