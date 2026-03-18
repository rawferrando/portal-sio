<template>
  <div class="contenedor-tabla">
    <div class="cabecera-tabla">
      <h3>📊 Inventario Global de Equipos</h3>
    </div>
    <table class="tabla-sio">
      <thead>
        <tr>
          <th>ID Equipo</th>
          <th>Tipo / Modelo</th>
          <th>Número de Serie</th>
          <th>Estado Actual</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>SNS-001</strong></td>
          <td>CTD Sea-Bird 911</td>
          <td>SN-12345</td>
          <td><span class="status op">Operativo</span></td>
        </tr>
        <tr>
          <td><strong>SNS-002</strong></td>
          <td>Salinómetro Guildline</td>
          <td>SN-67890</td>
          <td><span class="status cal">En Calibración</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.contenedor-tabla { background: white; padding: 20px; border-radius: 8px; border: 1px solid #e0e0e0; width: 100%; max-width: 900px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
.cabecera-tabla { margin-bottom: 20px; border-bottom: 2px solid #eee; padding-bottom: 10px; }
h3 { color: #005596; margin: 0; font-size: 1.2rem; }
.tabla-sio { width: 100%; border-collapse: collapse; text-align: left; }
.tabla-sio th, .tabla-sio td { padding: 12px; border-bottom: 1px solid #eee; }
.status { padding: 4px 8px; border-radius: 12px; font-size: 0.8rem; font-weight: bold; }
.op { background: #d4edda; color: #155724; }
.cal { background: #cce5ff; color: #004085; }
</style>