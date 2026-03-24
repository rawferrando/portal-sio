<template>
  <div class="panel-wrapper">
    <button class="btn-volver" @click="$emit('volver')">
      ⬅ Volver al Inicio
    </button>

    <div class="intranet-container">
      <div class="header-intranet">
        <h2>Panel Central de Administración SIO</h2>
        <p>Selecciona el módulo de gestión al que deseas acceder.</p>
      </div>

      <div class="selector-formularios">
        <label for="tipo-formulario" class="label-destacado">¿Qué deseas gestionar?</label>
        <select id="tipo-formulario" v-model="formularioActivo" class="dropdown-intranet">
          <option value="">-- Selecciona un módulo --</option>
          <option value="proyectos">📂 Alta y Edición de Proyectos</option>
          <option value="instrumentacion">⚙️ Alta de Instrumentación General</option>
          <option value="fondeos">⚓ Gestión de Fondeos</option>
          <option value="sensores">📡 Gestión de Sensores</option>
        </select>
      </div>

      <div v-if="formularioActivo === 'fondeos' || formularioActivo === 'sensores'" class="formulario-box fade-in text-center">
        <h3>Redirigiendo al módulo específico...</h3>
        <p>Aquí cargaremos tu componente <strong>Intranet{{ formularioActivo === 'fondeos' ? 'Fondeos' : 'Sensores' }}.vue</strong>.</p>
      </div>

      <div v-if="formularioActivo === 'instrumentacion'" class="formulario-box fade-in">
        <h3>Ficha Técnica de Instrumentación General</h3>
        <form @submit.prevent="guardarInstrumento">
          <div class="grid-form">
            <div class="form-group"><label>Nombre del Equipo</label><input type="text" placeholder="Ej: Roseta CTD" required></div>
            <div class="form-group"><label>Marca / Fabricante</label><input type="text" placeholder="Ej: Sea-Bird"></div>
            <div class="form-group"><label>Modelo</label><input type="text" placeholder="Ej: SBE 911plus"></div>
            <div class="form-group"><label>S/N</label><input type="text"></div>
            <div class="form-group"><label>Categoría</label><select><option>Perfiladores</option><option>Acústica</option><option>Óptica</option><option>Otros</option></select></div>
            <div class="form-group"><label>Estado</label><select><option>🟢 Operativo</option><option>🟡 Mantenimiento</option><option>🔴 Baja</option></select></div>
            <div class="form-group full-width"><label>Observaciones</label><textarea rows="3"></textarea></div>
          </div>
          <div class="form-actions"><button type="submit" class="btn-guardar">Guardar Instrumento</button></div>
        </form>
      </div>

      <div v-if="formularioActivo === 'proyectos'" class="formulario-box fade-in">
        <h3>Alta de Proyecto (Plantilla Wiki SIO)</h3>
        <form @submit.prevent="guardarProyecto">
          <div class="grid-form">
            <div class="form-group full-width"><label>Título del Proyecto</label><input type="text" required></div>
            <div class="form-group full-width"><label>Descripción General</label><textarea rows="3"></textarea></div>
            <div class="form-group full-width"><label>Objetivos</label><textarea rows="3"></textarea></div>
            <div class="form-group full-width"><label>Nuestro Rol</label><textarea rows="3"></textarea></div>
            <div class="form-group"><label>Estado</label><select><option>En Curso</option><option>Finalizado</option></select></div>
            <div class="form-group"><label>Responsable</label><input type="text"></div>
          </div>
          <div class="form-actions"><button type="submit" class="btn-guardar">Guardar Proyecto</button></div>
        </form>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const formularioActivo = ref('')

const guardarInstrumento = () => alert("Instrumento guardado.")
const guardarProyecto = () => alert("Proyecto guardado.")
</script>

<style scoped>
.panel-wrapper { padding: 20px; }
.btn-volver { background-color: #6c757d; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; margin-bottom: 20px; font-weight: bold; }
.btn-volver:hover { background-color: #5a6268; }

/* Estilos de la intranet */
.intranet-container { max-width: 1000px; margin: 0 auto; padding: 30px; background-color: #f8f9fa; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
.header-intranet { text-align: center; margin-bottom: 30px; }
.header-intranet h2 { color: #005596; margin-bottom: 5px; }

.selector-formularios { background-color: #ffffff; padding: 20px; border-radius: 8px; border-left: 5px solid #005596; margin-bottom: 30px; display: flex; flex-direction: column; gap: 10px; border: 1px solid #eee; }
.label-destacado { font-weight: bold; color: #333; font-size: 1.1rem; }
.dropdown-intranet { padding: 12px; font-size: 1rem; border: 1px solid #ccc; border-radius: 6px; cursor: pointer; background-color: #f1f8ff; color: #005596; font-weight: bold; }

.formulario-box { background-color: white; padding: 30px; border-radius: 8px; border: 1px solid #e0e0e0; }
.formulario-box h3 { color: #005596; border-bottom: 2px solid #f0f0f0; padding-bottom: 10px; margin-bottom: 25px; margin-top: 0;}
.text-center { text-align: center; }

.grid-form { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.form-group { display: flex; flex-direction: column; gap: 5px; }
.full-width { grid-column: span 2; }
.form-group label { font-size: 0.9rem; font-weight: bold; color: #555; }
.form-group input, .form-group select, .form-group textarea { padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-family: inherit; }

.form-actions { margin-top: 30px; display: flex; justify-content: flex-end; }
.btn-guardar { background-color: #005596; color: white; padding: 12px 25px; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; }
.btn-guardar:hover { background-color: #003d73; }
.fade-in { animation: fadeIn 0.4s ease-in-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
@media (max-width: 768px) { .grid-form { grid-template-columns: 1fr; } .full-width { grid-column: span 1; } }
</style>