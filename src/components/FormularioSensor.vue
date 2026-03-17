<script setup>
import { ref } from 'vue'

const nuevoSensor = ref({
  nombre: '',
  marca: '',
  sn: '',
  ultima_calibracion: '',
  estado: 'Operativo'
})

const mensajeEnvio = ref('')

const guardarEnDB = () => {
  // Aquí simulamos que los datos viajan a la base de datos
  console.log("Enviando datos a la base de datos del SIO...", nuevoSensor.value)
  
  mensajeEnvio.value = "✅ ¡Sensor registrado con éxito en la base de datos!"
  
  // Limpiamos el formulario después de guardar
  setTimeout(() => {
    nuevoSensor.value = { nombre: '', marca: '', sn: '', ultima_calibracion: '', estado: 'Operativo' }
    mensajeEnvio.value = ''
  }, 3000)
}
</script>

<template>
  <div class="panel-intranet">
    <h2>🔒 Panel de Control SIO: Alta de Equipos</h2>
    <p class="instrucciones">Rellena los campos para actualizar el inventario global automáticamente.</p>

    <form @submit.prevent="guardarEnDB" class="formulario-tecnico">
      <div class="campo">
        <label>Nombre del Equipo:</label>
        <input v-model="nuevoSensor.nombre" type="text" placeholder="Ej: CTD Sea-Bird 37" required>
      </div>

      <div class="campo">
        <label>Marca / Modelo:</label>
        <input v-model="nuevoSensor.marca" type="text" placeholder="Ej: Sea-Bird Electronics" required>
      </div>

      <div class="campo">
        <label>Número de Serie (S/N):</label>
        <input v-model="nuevoSensor.sn" type="text" placeholder="Ej: 12345-AB" required>
      </div>

      <div class="campo">
        <label>Última Calibración:</label>
        <input v-model="nuevoSensor.ultima_calibracion" type="date" required>
      </div>

      <div class="campo">
        <label>Estado Actual:</label>
        <select v-model="nuevoSensor.estado">
          <option value="Operativo">✅ Operativo</option>
          <option value="Taller">🛠️ En Taller / Calibración</option>
          <option value="Desplegado">🌊 Desplegado en Mar</option>
          <option value="Baja">❌ Fuera de Servicio</option>
        </select>
      </div>

      <button type="submit" class="btn-guardar">💾 Guardar en WikiSIO</button>
    </form>

    <p v-if="mensajeEnvio" class="alerta-exito">{{ mensajeEnvio }}</p>
  </div>
</template>

<style scoped>
.panel-intranet { max-width: 600px; background: #f4f7f9; padding: 30px; border-radius: 12px; border: 1px solid #ddd; }
h2 { color: #005596; margin-top: 0; }
.instrucciones { font-size: 0.9rem; color: #666; margin-bottom: 20px; }

.formulario-tecnico { display: flex; flex-direction: column; gap: 15px; }
.campo { display: flex; flex-direction: column; gap: 5px; }
label { font-weight: bold; font-size: 0.85rem; color: #444; }
input, select { padding: 10px; border: 1px solid #ccc; border-radius: 6px; font-size: 1rem; }

.btn-guardar { 
  background: #005596; color: white; border: none; padding: 15px; 
  border-radius: 6px; font-weight: bold; cursor: pointer; margin-top: 10px;
  transition: background 0.3s;
}
.btn-guardar:hover { background: #003d6b; }
.alerta-exito { margin-top: 20px; color: #155724; background: #d4edda; padding: 10px; border-radius: 6px; text-align: center; }
</style>