<template>
  <div class="seccion-tecnica">
    <button class="btn-volver" @click="$emit('volver')">⬅ Volver</button>
    <h1>Proyectos de Investigación</h1>
    <div class="lista-proyectos">
      <div class="proyecto-card">
        <h3>Proyecto MINERVA (2025-2027)</h3>
        <p>Monitorización de ecosistemas bentónicos mediante sistemas de visión submarina autónomos.</p>
        <span class="tag">Activo</span>
      </div>
      <div class="proyecto-card">
        <h3>Red OBSEA</h3>
        <p>Soporte técnico y mantenimiento del observatorio marino cableado en Vilanova i la Geltrú.</p>
        <span class="tag">Colaboración</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.seccion-tecnica { max-width: 900px; margin: 0 auto; padding: 20px; }
.btn-volver { border: 1px solid #005596; color: #005596; background: white; padding: 5px 15px; cursor: pointer; margin-bottom: 20px; }
.proyecto-card { background: #f4f7f9; padding: 20px; margin-bottom: 15px; border-radius: 8px; border-left: 5px solid #005596; }
.tag { background: #005596; color: white; padding: 3px 8px; font-size: 0.8rem; border-radius: 4px; }
h1 { color: #005596; border-bottom: 2px solid #eee; padding-bottom: 10px; }
</style>