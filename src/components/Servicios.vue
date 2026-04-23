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
            <p>Catálogo completo de sensores, plataformas y perfiladores. Accede a manuales, características técnicas y reservas.</p>
          </div>

          <div class="buscador-rapido">
            <label>Búsqueda rápida:</label>
            <div class="input-grupo">
              <select v-model="tipoBuscado">
                <option value="Todos">Todos los equipos</option>
                <option value="Sensores">Sensores y Perfiladores</option>
                <option value="Plataformas">Plataformas Autónomas</option>
              </select>
              <button @click="buscarYNavegar" class="btn-buscar">Ver</button>
            </div>
          </div>
        </div>

        <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 @click="$emit('cambiar-pagina', 'pelagia')" class="titulo-clicable">
              Embarcación Pelagia <span class="flecha">➔</span>
            </h2>
            <p>Embarcación de apoyo para trabajos costeros y despliegue de instrumentación. Consulta características y disponibilidad.</p>
          </div>

          <div class="tarjetas-preview">
            <div class="tarjeta-info" @click="$emit('cambiar-pagina', 'pelagia')">
              <h3>Detalles Técnicos y Reservas</h3>
              <p>Capacidad, motores y calendario de disponibilidad.</p>
            </div>
          </div>
        </div>

      </div> 
    </div>
  </div>
  <div class="seccion-bloque">
          <div class="cabecera-bloque">
            <h2 class="titulo-fija">Tanques de Pruebas</h2>
            <p>Alquiler de áreas experimentales y tanques para la validación, calibración y ensayo de instrumentación oceanográfica en entornos controlados.</p>
          </div>

          <div class="lista-items">
            <div class="item-idi">
              <span class="punto-azul">●</span>
              <div>Ensayos de estanqueidad, presión y flotabilidad para equipos submarinos y robótica.</div>
            </div>
            <div class="item-idi">
              <span class="punto-azul">●</span>
              <div>Calibración y validación de sensores acústicos, ópticos y de calidad del agua.</div>
            </div>
            <div class="item-idi">
              <span class="punto-azul">●</span>
              <div>Soporte técnico y supervisión de ingeniería durante las campañas de pruebas.</div>
            </div>
          </div>
        </div>
</template>

<style scoped>
.servicios-hub { position: relative; min-height: 100vh; padding-bottom: 40px; background-color: #f4f7f9; }

/* 🌊 CONFIGURACIÓN DEL FONDO 🌊 */
.fondo-servicios { 
  position: absolute; 
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 480px; /* Reducido para que no ocupe tanto espacio vertical */
  z-index: 0; 
  /* IMPORTANTE: Cambia 'medusa.png' por el nombre de tu foto en la carpeta public */
  background-image: linear-gradient(rgba(1, 33, 105, 0.6), rgba(1, 33, 105, 0.8)), url('/medusa.png');
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}

/* Reducimos el padding-top para que el título suba (antes 150px) */
.contenido-hub { 
  position: relative; 
  z-index: 10; 
  padding-top: 120px; 
}

.titulo-seccion { 
  color: white; 
  font-size: 2rem; 
  margin-bottom: 15px; 
  font-weight: bold; 
  position: relative;
  display: inline-block;
  padding-bottom: 8px;
}

.titulo-seccion::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background-color: #8cc63f; 
}

/* Reducimos el margen inferior del subtítulo para que las fichas suban (antes 60px) */
.subtitulo { color: #e0e6ed; font-size: 1rem; margin-bottom: 30px; max-width: 800px; }

.grid-horizontal {
  display: grid;
  /* Cambiamos de '1fr 1fr' a 3 columnas automáticas que se adaptan al tamaño */
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
  gap: 30px; 
}

.seccion-bloque { 
  background: white; 
  border-radius: 12px; 
  padding: 30px; 
  box-shadow: 0 10px 30px rgba(0,0,0,0.15); 
  display: flex;
  flex-direction: column;
  min-height: 280px; /* Altura controlada */
}

.titulo-clicable { color: #012169; cursor: pointer; display: inline-flex; align-items: center; gap: 10px; transition: color 0.3s; margin-top: 0; font-size: 1.4rem; }
.titulo-clicable:hover { color: #0086c0; }
.flecha { font-size: 0.8em; }

.cabecera-bloque p { color: #555; line-height: 1.5; font-size: 0.95rem; }

.buscador-rapido { margin-top: auto; padding-top: 15px; } 
.buscador-rapido label { display: block; font-weight: bold; color: #333; margin-bottom: 8px; font-size: 0.9rem; }
.input-grupo { display: flex; gap: 8px; }
.input-grupo select { flex-grow: 1; padding: 10px; border: 1px solid #ccc; border-radius: 6px; font-size: 0.9rem; }
.btn-buscar { background: #0086c0; color: white; border: none; padding: 0 15px; border-radius: 6px; font-weight: bold; cursor: pointer; }

.tarjetas-preview { display: flex; flex-direction: column; gap: 10px; margin-top: auto; padding-top: 15px; }
.tarjeta-info { padding: 12px 15px; border: 1px solid #e0e6ed; border-radius: 8px; cursor: pointer; transition: all 0.3s; }
.tarjeta-info:hover { border-color: #0086c0; background: #f0f7ff; } 
.tarjeta-info h3 { margin-top: 0; color: #012169; font-size: 1rem; margin-bottom: 3px; }
.tarjeta-info p { color: #666; margin: 0; font-size: 0.85rem; }

@media (max-width: 992px) {
  .grid-horizontal { grid-template-columns: 1fr; }
  .fondo-servicios { height: 400px; }
}
</style>