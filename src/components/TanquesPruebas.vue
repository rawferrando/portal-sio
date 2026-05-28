<script setup>
const emit = defineEmits(['cambiar-pagina'])
</script>

<template>
  <div class="pagina-detalle">
    
    <div class="hero-detalle hero-tanques">
      <div class="contenedor-ancho contenido-hero">
        <button class="btn-volver" @click="$emit('cambiar-pagina', 'servicios')">
          ⬅ Volver a Servicios
        </button>
        
        <h1 class="titulo-hero">Tanques de Pruebas</h1>
        <p class="subtitulo-hero">Instalaciones experimentales para ensayos controlados, calibración y biología.</p>
      </div>
    </div>

    <div class="contenedor-ancho seccion-principal">
      <div class="grid-dos-columnas">
        
        <div class="columna-ficha">
          <h2 class="titulo-seccion-pequeno">Ficha Técnica</h2>
          
          <div class="bloque-info">
            <h3>Descripción General</h3>
            <p>El SIO dispone de tanques de pruebas de alta capacidad diseñados para la calibración de sensores, ensayos de fatiga de materiales y simulaciones de condiciones marinas controladas.</p>
          </div>

          <div class="bloque-info">
            <h3>Especificaciones Principales</h3>
            <ul class="lista-especificaciones">
              <li><strong>Volumen total:</strong> [Añadir litros/m3]</li>
              <li><strong>Control de Temperatura:</strong> Rango de [X] °C a [Y] °C</li>
              <li><strong>Control de Salinidad:</strong> Sistema automatizado</li>
              <li><strong>Iluminación:</strong> Espectro regulable para fotosíntesis</li>
              <li><strong>Filtración:</strong> Filtros UV y biológicos integrados</li>
            </ul>
          </div>
        </div>

        <div class="columna-reserva">
          <div class="tarjeta-reserva">
            <div class="cabecera-reserva">
              <h2>Solicitud de Uso</h2>
              <span class="badge-operativa">OPERATIVA</span>
            </div>
            
            <div class="paso-reserva">
              <p>Paso 1: Descarga la normativa de los tanques.</p>
              <div class="caja-descarga">
                <span class="icono-doc">📄 Normativa_Tanques.pdf</span>
                <a href="#" class="btn-descarga">⬇ Descargar Normativa</a>
              </div>
            </div>

            <div class="paso-reserva mt-4">
              <p><strong>Paso 2: Selecciona los días de uso</strong></p>
              
              <div class="calendario-placeholder">
                <div class="grid-calendario">
                   <div class="dia">1</div><div class="dia ocupado">2</div><div class="dia">3</div><div class="dia">4</div><div class="dia ocupado">5</div><div class="dia">6</div><div class="dia">7</div>
                   <div class="dia">8</div><div class="dia">9</div><div class="dia">10</div><div class="dia">11</div><div class="dia">12</div><div class="dia">13</div><div class="dia ocupado">14</div>
                   <div class="dia ocupado">15</div><div class="dia">16</div><div class="dia">17</div><div class="dia">18</div><div class="dia">19</div><div class="dia">20</div><div class="dia">21</div>
                   <div class="dia ocupado">22</div><div class="dia">23</div><div class="dia">24</div><div class="dia">25</div><div class="dia">26</div><div class="dia">27</div><div class="dia">28</div>
                </div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped>
.pagina-detalle {
  background-color: #f4f7f9;
  min-height: 100vh;
  padding-bottom: 80px;
}

/* --- HERO CLAVADO AL DE PELAGIA --- */
.hero-detalle {
  background-color: #012169; /* Azul ICM */
  padding: 120px 0 60px 0;
  color: white;
}

.contenido-hero {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.btn-volver {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.4);
  color: white;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.85rem;
  margin-bottom: 25px;
  transition: all 0.3s ease;
}

.btn-volver:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: white;
}

.titulo-hero {
  font-size: 3rem;
  font-weight: bold;
  margin: 0 0 15px 0;
  position: relative;
  display: inline-block;
  padding-bottom: 10px;
}

/* LA RAYA VERDE DEL CSIC */
.titulo-hero::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 5px;
  background-color: #8cc63f; 
}

.subtitulo-hero {
  font-size: 1.15rem;
  color: #e0e6ed;
  max-width: 800px;
  margin: 0;
}

/* --- CONTENIDO PRINCIPAL --- */
.seccion-principal {
  margin-top: 40px;
}

.grid-dos-columnas {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}

/* --- COLUMNA IZQUIERDA --- */
.columna-ficha {
  background: white;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.05);
}

.titulo-seccion-pequeno {
  color: #012169;
  font-size: 1.8rem;
  border-bottom: 2px solid #0086c0;
  padding-bottom: 10px;
  margin-bottom: 30px;
  margin-top: 0;
}

.bloque-info {
  margin-bottom: 30px;
}

.bloque-info h3 {
  color: #0086c0;
  font-size: 1.2rem;
  margin-bottom: 15px;
}

.bloque-info p {
  color: #444;
  line-height: 1.6;
}

.lista-especificaciones {
  list-style-type: none;
  padding: 0;
}

.lista-especificaciones li {
  margin-bottom: 12px;
  color: #444;
  line-height: 1.5;
  padding-left: 15px;
  position: relative;
}

.lista-especificaciones li::before {
  content: '•';
  color: #0086c0;
  font-weight: bold;
  position: absolute;
  left: 0;
}

/* --- COLUMNA DERECHA --- */
.tarjeta-reserva {
  background: white;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.05);
}

.cabecera-reserva {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #eee;
  padding-bottom: 15px;
  margin-bottom: 25px;
}

.cabecera-reserva h2 {
  color: #012169;
  font-size: 1.5rem;
  margin: 0;
}

.badge-operativa {
  background-color: #e6f4ea;
  color: #1e8e3e;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: bold;
  border: 1px solid #1e8e3e;
}

.paso-reserva p {
  color: #444;
  margin-bottom: 15px;
}

.mt-4 {
  margin-top: 30px;
}

.caja-descarga {
  background-color: #f8f9fa;
  border: 1px dashed #ccc;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.btn-descarga {
  background-color: #0086c0;
  color: white;
  text-decoration: none;
  padding: 10px 20px;
  border-radius: 4px;
  font-weight: bold;
  transition: background 0.3s;
}

.btn-descarga:hover {
  background-color: #012169;
}

/* CALENDARIO SIMULADO */
.grid-calendario {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 5px;
  text-align: center;
}
.dia {
  background: #f4f7f9;
  padding: 10px 0;
  border-radius: 4px;
  color: #555;
  font-size: 0.9rem;
}
.dia.ocupado {
  background: #ffebee;
  color: #d32f2f;
}

@media (max-width: 900px) {
  .grid-dos-columnas {
    grid-template-columns: 1fr;
  }
}
</style> 