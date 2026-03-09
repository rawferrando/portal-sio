<template>
  <section class="intranet">
    <div class="lock-icon">🔒 Área Reservada</div>
    <h2>3. Gestión Interna de Fondeos</h2>
    <p class="intro">Acceso exclusivo para personal técnico del SIO.</p>
    
    <div class="tabla-simulada">
      <table>
        <thead>
          <tr>
            <th>ID Fondeo</th>
            <th>Ubicación</th>
            <th>Estado</th>
            <th>Última Revisión</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>FND-2025-01</td>
            <td>Barcelona - Besòs</td>
            <td><span class="status ok">Activo</span></td>
            <td>15/02/2026</td>
          </tr>
          <tr>
            <td>FND-2025-04</td>
            <td>Vilanova i la Geltrú</td>
            <td><span class="status warning">Mantenimiento</span></td>
            <td>01/03/2026</td>
          </tr>
        </tbody>
      </table> </div>
    <button class="btn-login">Acceder al histórico completo</button>
  </section>
</template>

<style scoped>
.intranet { background-color: #f4f4f4; padding: 2rem; border-radius: 12px; border: 1px dashed #aaa; }
.lock-icon { font-weight: bold; color: #d9534f; margin-bottom: 0.5rem; }
.status.ok { color: green; font-weight: bold; }
.status.warning { color: orange; font-weight: bold; }
table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; background: white; }
th, td { padding: 12px; border: 1px solid #ddd; text-align: left; }
.btn-login { background-color: #0056b3; color: white; border: none; padding: 0.8rem 1.5rem; border-radius: 5px; cursor: pointer; }
</style>