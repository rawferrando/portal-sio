<template>
  <div class="contenedor-fondeos">
    <div class="cabecera-tabla">
      <h2>🌊 Estado Global de Fondeos</h2>
    </div>
    <table class="tabla-sio">
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
        <tr>
          <td><strong>FND-001</strong></td>
          <td>Cañón de Blanes</td>
          <td>150m</td>
          <td><span class="status op">Operativo</span></td>
          <td>2026-03-01</td>
        </tr>
        <tr>
          <td><strong>FND-002</strong></td>
          <td>Delta del Ebro</td>
          <td>50m</td>
          <td><span class="status mt">Mantenimiento</span></td>
          <td>2026-02-28</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.contenedor-fondeos { background: white; padding: 20px; border-radius: 8px; width: 100%; max-width: 900px; }
.cabecera-tabla { margin-bottom: 20px; border-bottom: 2px solid #eee; padding-bottom: 10px; }
h2 { color: #005596; margin: 0; font-size: 1.4rem; }
.tabla-sio { width: 100%; border-collapse: collapse; text-align: left; }
.tabla-sio th, .tabla-sio td { padding: 12px; border-bottom: 1px solid #eee; }
.status { padding: 4px 8px; border-radius: 12px; font-size: 0.8rem; font-weight: bold; }
.op { background: #d4edda; color: #155724; }
.mt { background: #fff3cd; color: #856404; }
</style>