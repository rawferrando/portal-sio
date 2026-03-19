<script setup>
import { ref } from 'vue'

// Variables de estado organizadas por bloques
const identificacion = ref({
  modelo: '',
  numeroSerie: '',
  fabricante: '',
  estado: 'Operativo',
  categoria: 'Sensores de Presión'
})

const especificaciones = ref({
  rango: '',
  precision: '',
  voltaje: '',
  salida: ''
})

const calibracion = ref({
  ultimaFecha: '',
  periodicidad: '12 meses'
})

const documentacion = ref({
  enlaceManual: '',
  descripcion: ''
})

const guardarSensor = () => {
  if (!identificacion.value.modelo || !identificacion.value.numeroSerie) {
    alert("⚠️ Por favor, rellena al menos el Modelo y el Número de Serie.")
    return
  }
  alert(`✅ Ficha técnica del equipo ${identificacion.value.modelo} guardada con éxito en la base de datos.`)
  
  // Limpiar formulario tras guardar
  identificacion.value = { modelo: '', numeroSerie: '', fabricante: '', estado: 'Operativo', categoria: 'Sensores de Presión' }
  especificaciones.value = { rango: '', precision: '', voltaje: '', salida: '' }
  calibracion.value = { ultimaFecha: '', periodicidad: '12 meses' }
  documentacion.value = { enlaceManual: '', descripcion: '' }
}
</script>

<template>
  <div class="tarjeta-formulario">
    <div class="cabecera-form">
      <h3>📝 Ficha Técnica de Nuevo Equipamiento</h3>
      <p>Rellena los metadatos del instrumento para digitalizar su hoja de vida operativa.</p>
    </div>
    
    <div class="cuerpo-form">
      
      <fieldset class="bloque-datos">
        <legend>1. Identificación y Estado</legend>
        <div class="grid-2-col">
          <div class="campo">
            <label>Modelo del Equipo:</label>
            <input v-model="identificacion.modelo" type="text" placeholder="Ej: SBE 5 Pressure Sensor">
          </div>
          <div class="campo">
            <label>Número de Serie (S/N):</label>
            <input v-model="identificacion.numeroSerie" type="text" placeholder="Ej: 11599">
          </div>
          <div class="campo">
            <label>Fabricante:</label>
            <input v-model="identificacion.fabricante" type="text" placeholder="Ej: Sea-Bird Scientific">
          </div>
          <div class="campo">
            <label>Categoría:</label>
            <select v-model="identificacion.categoria">
              <option value="CTD Perfilador">CTD Perfilador</option>
              <option value="Sensores de Presión">Sensores de Presión</option>
              <option value="Correntímetros">Correntímetros</option>
              <option value="Muestreo">Muestreo</option>
            </select>
          </div>
          <div class="campo">
            <label>Estado Actual:</label>
            <select v-model="identificacion.estado">
              <option value="Operativo">🟢 Operativo</option>
              <option value="Calibración">🟡 En Calibración</option>
              <option value="Reparación">🔴 En Reparación</option>
            </select>
          </div>
        </div>
      </fieldset>

      <fieldset class="bloque-datos">
        <legend>2. Especificaciones Técnicas y Eléctricas</legend>
        <div class="grid-2-col">
          <div class="campo">
            <label>Rango de Medición:</label>
            <input v-model="especificaciones.rango" type="text" placeholder="Ej: 0 a 10.000 psia">
          </div>
          <div class="campo">
            <label>Precisión:</label>
            <input v-model="especificaciones.precision" type="text" placeholder="Ej: ±0.015% del rango">
          </div>
          <div class="campo">
            <label>Voltaje de Alimentación:</label>
            <input v-model="especificaciones.voltaje" type="text" placeholder="Ej: 8-18 V DC">
          </div>
          <div class="campo">
            <label>Señal de Salida:</label>
            <input v-model="especificaciones.salida" type="text" placeholder="Ej: 0-5 V DC">
          </div>
        </div>
      </fieldset>

      <fieldset class="bloque-datos">
        <legend>3. Calibración y Mantenimiento</legend>
        <div class="grid-2-col">
          <div class="campo">
            <label>Fecha Última Calibración:</label>
            <input v-model="calibracion.ultimaFecha" type="date">
          </div>
          <div class="campo">
            <label>Periodicidad Recomendada:</label>
            <select v-model="calibracion.periodicidad">
              <option value="6 meses">Cada 6 meses</option>
              <option value="12 meses">Cada 12 meses</option>
              <option value="24 meses">Cada 24 meses</option>
            </select>
          </div>
        </div>
      </fieldset>

      <fieldset class="bloque-datos">
        <legend>4. Documentación y Descripción</legend>
        <div class="campo" style="margin-bottom: 15px;">
          <label>URL del Manual del Fabricante:</label>
          <input v-model="documentacion.enlaceManual" type="url" placeholder="https://www.seabird.com/...">
        </div>
        <div class="campo">
          <label>Descripción y Notas de Funcionamiento:</label>
          <textarea v-model="documentacion.descripcion" rows="4" placeholder="Escribe aquí el principio de funcionamiento, advertencias sobre temperatura, etc..."></textarea>
        </div>
      </fieldset>

      <button @click="guardarSensor" class="btn-guardar">💾 Guardar Ficha Completa en Base de Datos</button>
    </div>
  </div>
</template>

<style scoped>
.tarjeta-formulario { background: white; border-radius: 8px; border: 1px solid #e0e0e0; width: 100%; box-shadow: 0 4px 12px rgba(0,0,0,0.08); overflow: hidden; }
.cabecera-form { background-color: #005596; padding: 20px; color: white; }
.cabecera-form h3 { margin: 0 0 5px 0; font-size: 1.3rem; }
.cabecera-form p { margin: 0; font-size: 0.9rem; color: #e0f2fe; }

.cuerpo-form { padding: 25px; display: flex; flex-direction: column; gap: 20px; }

/* Estilo de los bloques agrupados (fieldset) */
.bloque-datos { border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin: 0; background-color: #fcfcfc; }
.bloque-datos legend { background-color: #e2eef7; color: #005596; padding: 5px 15px; border-radius: 4px; font-weight: bold; font-size: 0.95rem; border: 1px solid #cce0f0; }

/* Cuadrícula a 2 columnas para que quede compacto */
.grid-2-col { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }

.campo { display: flex; flex-direction: column; gap: 6px; }
.campo label { font-weight: bold; color: #444; font-size: 0.85rem; }
.campo input, .campo select, .campo textarea { padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 0.95rem; font-family: inherit; }
.campo input:focus, .campo select:focus, .campo textarea:focus { outline: none; border-color: #005596; box-shadow: 0 0 0 2px rgba(0,85,150,0.2); }
.campo textarea { resize: vertical; }

/* Si la pantalla es pequeña (móvil), pasamos a 1 columna */
@media (max-width: 600px) {
  .grid-2-col { grid-template-columns: 1fr; }
}

.btn-guardar { background-color: #28a745; color: white; border: none; padding: 15px; border-radius: 6px; font-weight: bold; font-size: 1.1rem; cursor: pointer; transition: background 0.3s; margin-top: 10px; }
.btn-guardar:hover { background-color: #218838; }
</style>