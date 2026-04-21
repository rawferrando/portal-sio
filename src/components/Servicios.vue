<script setup>
import { ref } from 'vue'

const emit = defineEmits(['cambiar-pagina'])
const tipoBuscado = ref('Todos')

const buscarYNavegar = () => {
  emit('cambiar-pagina', 'instrumentacion')
}
</script>

<template>
  <div class="servicios-hub">
    <div class="fondo-servicios"></div>

    <div class="contenedor-ancho contenido-hub">
      <h1 class="titulo-seccion">Servicios e instalaciones</h1>
      <p class="subtitulo">Apoyo técnico, plataformas marinas y equipamiento oceanográfico de vanguardia.</p>

      <div class="grid-horizontal">
        
        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 @click="$emit('cambiar-pagina', 'instrumentacion')" class="titulo-clicable">
              Instrumentación Oceanográfica <span class="flecha">➔</span>
            </h2>
            <p>Catálogo completo de sensores, plataformas y perfiladores del Servicio de Ingeniería Oceanográfica. Accede a manuales, características técnicas de la WikiSIO y gestiona tus reservas.</p>
          </div>

          <div class="buscador-rapido">
            <label>Búsqueda rápida por tipo:</label>
            <div class="input-grupo">
              <select v-model="tipoBuscado">
                <option value="Todos">Todos los equipos</option>
                <option value="Sensores">Sensores y Perfiladores</option>
                <option value="Plataformas">Plataformas Autónomas</option>
                <option value="Boyas">Boyas y Estaciones Fijas</option>
                <option value="Acustica">Acústica Submarina</option>
              </select>
              <button @click="buscarYNavegar" class="btn-buscar">Ver Catálogo</button>
            </div>
          </div>
        </div>

        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 @click="$emit('cambiar-pagina', 'pelagia')" class="titulo-clicable">
              Embarcación Pelagia <span class="flecha">➔</span>
            </h2>
            <p>Embarcación de apoyo para trabajos oceanográficos costeros, despliegue de instrumentación y muestreo continuo. Consulta sus características y disponibilidad.</p>
          </div>

          <div class="tarjetas-preview">
            <div class="tarjeta-info" @click="$emit('cambiar-pagina', 'pelagia')">
              <h3>Detalles Técnicos</h3>
              <p>Conoce las especificaciones, motores y capacidad de carga para tus campañas.</p>
            </div>
            <div class="tarjeta-info" @click="$emit('cambiar-pagina', 'pelagia')">
              <h3>Disponibilidad y Reservas</h3>
              <p>Consulta el calendario mensual y el protocolo de uso de la embarcación.</p>
            </div>
          </div>
        </div>

      </div> </div>
  </div>
</template>

<style scoped>
.servicios-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

/* 🌊 ACTUALIZACIÓN DEL FONDO MARINO 🌊 */
.fondo-servicios { 
  position: absolute; 
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 550px; /* Un poco más alto para un efecto más inmersivo */
  /* Capa de color azul semitransparente + NUEVA imagen de fondo de aguas profundas */
  background: linear-gradient(rgba(1, 33, 105, 0.65), rgba(1, 33, 105, 0.85)), 
              url('https://images.unsplash.com/photo-1544321720-6d048d88ba8a?q=80&w=1920&auto=format&fit=crop') center/cover no-repeat;
  z-index: 0; 
}

/* El contenido se mantiene bajado */
.contenido-hub { 
  position: relative; 
  z-index: 10; 
  padding-top: 150px; 
}

/* Título con línea verde inferior y letra reducida a 2rem */
.titulo-seccion { 
  color: white; 
  font-size: 2rem; 
  margin-bottom: 25px; 
  font-weight: bold; 
  position: relative;
  display: inline-block;
  padding-bottom: 10px;
}

/* La línea verde del ICM se mantiene */
.titulo-seccion::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background-color: #8cc63f; 
}

.subtitulo { color: #e0e6ed; font-size: 1.1rem; margin-bottom: 60px; max-width: 800px; }

.grid-horizontal {
  display: grid;
  grid-template-columns: 1fr 1fr; 
  gap: 30px; 
}

.seccion-bloque { 
  background: white; 
  border-radius: 12px; 
  padding: 40px; 
  box-shadow: 0 10px 30px rgba(0,0,0,0.15); 
  display: flex;
  flex-direction: column; 
}

.titulo-clicable { color: #012169; cursor: pointer; display: inline-flex; align-items: center; gap: 10px; transition: color 0.3s; margin-top: 0; }
.titulo-clicable:hover { color: #0086c0; }
.flecha { font-size: 0.8em; transition: transform 0.3s; }
.titulo-clicable:hover .flecha { transform: translateX(5px); }

.cabecera-bloque p { color: #555; line-height: 1.6; font-size: 1.05rem; }

.buscador-rapido { margin-top: auto; padding-top: 20px; } 
.buscador-rapido label { display: block; font-weight: bold; color: #333; margin-bottom: 10px; }
.input-grupo { display: flex; gap: 10px; }
.input-grupo select { flex-grow: 1; padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 0.95rem; }
.btn-buscar { background: #0086c0; color: white; border: none; padding: 0 20px; border-radius: 6px; font-weight: bold; cursor: pointer; transition: background 0.3s; }
.btn-buscar:hover { background: #012169; }

.tarjetas-preview { display: flex; flex-direction: column; gap: 15px; margin-top: auto; padding-top: 20px; }
.tarjeta-info { padding: 15px 20px; border: 1px solid #e0e6ed; border-radius: 8px; cursor: pointer; transition: all 0.3s; }
.tarjeta-info:hover { border-color: #0086c0; background: #f0f7ff; transform: translateX(5px); } 
.tarjeta-info h3 { margin-top: 0; color: #012169; font-size: 1.1rem; margin-bottom: 5px; }
.tarjeta-info p { color: #666; margin: 0; font-size: 0.9rem; }

@media (max-width: 992px) {
  .grid-horizontal { grid-template-columns: 1fr; }
.fondo-servicios { 
  position: absolute; 
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 550px; 
  z-index: 0; 
  /* Imagen de Wikimedia Commons (estable y sin bloqueos) */
  background-image: linear-gradient(rgba(1, 33, 105, 0.65), rgba(1, 33, 105, 0.85)), url('https://media.istockphoto.com/id/469858644/es/foto/medusa-3.webp?s=2048x2048&w=is&k=20&c=n-TiX4QiiZ4C9R7AVMEFcY73vbFoNQFFudQK8R3MMdU=');
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}
}
</style>