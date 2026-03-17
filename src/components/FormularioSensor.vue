<template>
  <div class="card-formulario">
    <h3>📝 Registro de Nuevo Equipamiento</h3>
    <div class="form-grid">
      <input type="text" placeholder="Nombre del Sensor (ej. CTD)" class="input-sio">
      <input type="text" placeholder="S/N (Número de Serie)" class="input-sio">
      <select class="input-sio">
        <option>✅ Operativo</option>
        <option>🛠️ En Revisión</option>
        <option>🌊 Desplegado</option>
      </select>
      <button class="btn-sio">Guardar en Base de Datos</button>
    </div>
  </div>
</template>

<style scoped>
.card-formulario {
  background: white;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  border-top: 5px solid #005596;
  width: 100%;
  max-width: 800px;
  margin-bottom: 30px;
}
h3 { color: #005596; margin-top: 0; }
.form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
.input-sio { padding: 10px; border: 1px solid #ccc; border-radius: 4px; }
.btn-sio { 
  grid-column: span 2; background: #005596; color: white; 
  border: none; padding: 12px; border-radius: 4px; cursor: pointer; font-weight: bold;
}
</style>