<template>
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
        <option value="fondeos">⚓ Gestión de Fondeos (Ir a tu módulo)</option>
        <option value="sensores">📡 Gestión de Sensores (Ir a tu módulo)</option>
      </select>
    </div>

    <div v-if="formularioActivo === 'fondeos' || formularioActivo === 'sensores'" class="formulario-box fade-in text-center">
      <h3>Redirigiendo al módulo específico...</h3>
      <p>Aquí conectaríamos con tu componente <strong>Intranet{{ formularioActivo === 'fondeos' ? 'Fondeos' : 'Sensores' }}.vue</strong>.</p>
      </div>

    <div v-if="formularioActivo === 'instrumentacion'" class="formulario-box fade-in">
      <h3>Ficha Técnica de Instrumentación General</h3>
      <form @submit.prevent="guardarInstrumento">
        <div class="grid-form">
          <div class="form-group"><label>Nombre del Equipo</label><input type="text" placeholder="Ej: Roseta CTD" required></div>
          <div class="form-group"><label>Marca / Fabricante</label><input type="text" placeholder="Ej: Sea-Bird Scientific"></div>
          <div class="form-group"><label>Modelo</label><input type="text" placeholder="Ej: SBE 911plus"></div>
          <div class="form-group"><label>Número de Serie (S/N)</label><input type="text" placeholder="Ej: 09P45678-1234"></div>
          
          <div class="form-group">
            <label>Categoría</label>
            <select>
              <option>Perfiladores (CTD, SVP)</option>
              <option>Acústica (ADCP, Ecosondas)</option>
              <option>Óptica y Biogeoquímica</option>
              <option>Otros</option>
            </select>
          </div>
          <div class="form-group">
            <label>Estado Actual</label>
            <select>
              <option>🟢 Operativo</option>
              <option>🟡 En calibración / Mantenimiento</option>
              <option>🔵 En campaña (Desplegado)</option>
            </select>
          </div>
          
          <div class="form-group"><label>Profundidad Máx. Operativa (m)</label><input type="number"></div>
          <div class="form-group"><label>Ubicación / Almacén</label><input type="text"></div>
          <div class="form-group"><label>Responsable Asignado</label><input type="text"></div>
          <div class="form-group"><label>Subir Fotografía</label><input type="file" accept="image/*"></div>

          <div class="form-group full-width">
            <label>Observaciones Técnicas</label>
            <textarea rows="3"></textarea>
          </div>
        </div>
        <div class="form-actions">
          <button type="submit" class="btn-guardar">Guardar Instrumento</button>
        </div>
      </form>
    </div>

    <div v-if="formularioActivo === 'proyectos'" class="formulario-box fade-in">
      <h3>Alta de Proyecto (Plantilla Wiki SIO)</h3>
      <form @submit.prevent="guardarProyecto">
        <div class="grid-form">
          
          <div class="form-group full-width">
            <label>Título del Proyecto</label>
            <input type="text" required>
          </div>
          <div class="form-group full-width">
            <label>Descripción General</label>
            <textarea rows="4" placeholder="Introduce aquí una descripción detallada del proyecto..."></textarea>
          </div>

          <div class="form-group full-width">
            <label>Objetivos</label>
            <textarea rows="3" placeholder="Objetivo 1&#10;Objetivo 2..."></textarea>
          </div>
          <div class="form-group full-width">
            <label>Nuestro Rol</label>
            <textarea rows="3" placeholder="Describe detalladamente qué hace el SIO en este proyecto..."></textarea>
          </div>
          <div class="form-group full-width">
            <label>Metodología</label>
            <textarea rows="3"></textarea>
          </div>
          <div class="form-group full-width">
            <label>Resultados y Logros</label>
            <textarea rows="3"></textarea>
          </div>

          <div class="form-group">
            <label>Estado</label>
            <select><option>En Curso</option><option>Finalizado</option></select>
          </div>
          <div class="form-group"><label>Financiamiento</label><input type="text"></div>
          <div class="form-group"><label>Fecha de Inicio</label><input type="date"></div>
          <div class="form-group"><label>Fecha Prevista de Finalización</label><input type="date"></div>

          <div class="form-group"><label>Responsable (Contacto)</label><input type="text"></div>
          <div class="form-group"><label>Email</label><input type="email"></div>
          <div class="form-group"><label>Teléfono</label><input type="tel"></div>
          <div class="form-group"><label>Web oficial</label><input type="url"></div>
        </div>
        <div class="form-actions">
          <button type="submit" class="btn-guardar">Guardar Proyecto</button>
        </div>
      </form>
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
/* Estilos compactos y modernos para la intranet */
.intranet-container { max-width: 1000px; margin: 40px auto; padding: 30px; background-color: #f8f9fa; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
.header-intranet { text-align: center; margin-bottom: 30px; }
.header-intranet h2 { color: #005596; margin-bottom: 5px; }

.selector-formularios { background-color: #ffffff; padding: 20px; border-radius: 8px; border-left: 5px solid #005596; margin-bottom: 30px; display: flex; flex-direction: column; gap: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
.label-destacado { font-weight: bold; color: #333; font-size: 1.1rem; }
.dropdown-intranet { padding: 12px; font-size: 1rem; border: 1px solid #ccc; border-radius: 6px; cursor: pointer; background-color: #f1f8ff; color: #005596; font-weight: bold; }
.dropdown-intranet:focus { outline: none; border-color: #005596; box-shadow: 0 0 5px rgba(0,85,150,0.3); }

.formulario-box { background-color: white; padding: 30px; border-radius: 8px; border: 1px solid #e0e0e0; }
.formulario-box h3 { color: #005596; border-bottom: 2px solid #f0f0f0; padding-bottom: 10px; margin-top: 0; margin-bottom: 25px; }
.text-center { text-align: center; }

.grid-form { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.form-group { display: flex; flex-direction: column; gap: 5px; }
.full-width { grid-column: span 2; }
.form-group label { font-size: 0.9rem; font-weight: bold; color: #555; }
.form-group input, .form-group select, .form-group textarea { padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-family: inherit; }
.form-group input:focus, .form-group select:focus, .form-group textarea:focus { border-color: #005596; outline: none; }

.form-actions { margin-top: 30px; display: flex; justify-content: flex-end; }
.btn-guardar { background-color: #005596; color: white; padding: 12px 25px; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; }
.btn-guardar:hover { background-color: #003d73; }

.fade-in { animation: fadeIn 0.4s ease-in-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }

@media (max-width: 768px) { .grid-form { grid-template-columns: 1fr; } .full-width { grid-column: span 1; } }
</style>