<script setup>
import { ref } from 'vue'

const emit = defineEmits(['volver'])

// Aquí puedes ir añadiendo todos los proyectos que tienes en la WikiSIO
const proyectos = ref([
  {
    id: 1,
    titulo: 'Campaña Antártica 2025',
    estado: 'ACTIVA',
    claseEstado: 'badge-activa',
    ip: 'Dr. Jordi Font',
    descripcion: 'Instalación y mantenimiento de sensores de salinidad y temperatura en condiciones extremas.',
    etiquetas: ['#CTD', '#Antártida', '#Sensores']
  },
  {
    id: 2,
    titulo: 'Observatorio OBSEA',
    estado: 'FINALIZADA',
    claseEstado: 'badge-finalizada',
    ip: 'Joaquín del Río',
    descripcion: 'Revisión anual de la infraestructura submarina cableada y sistemas de comunicación.',
    etiquetas: ['#OBSEA', '#ROV', '#Mantenimiento']
  },
  // PLANTILLA: Copia este bloque para añadir nuevos proyectos de la WikiSIO
  {
    id: 3,
    titulo: 'Nombre del Proyecto (WikiSIO)',
    estado: 'EN CURSO',
    claseEstado: 'badge-activa', // Puedes usar: badge-activa, badge-finalizada o badge-planificacion
    ip: 'Nombre del IP',
    descripcion: 'Pega aquí la descripción o el resumen del proyecto sacado directamente de la WikiSIO.',
    etiquetas: ['#Tecnología', '#Zona', '#Equipo']
  }
])
</script>

<template>
  <div class="proyectos-hub">
    <div class="fondo-proyectos"></div>

    <div class="contenedor-ancho contenido-hub">
      
      <h1 class="titulo-seccion">Proyectos y Campañas</h1>
      <p class="subtitulo">Soporte técnico, logístico y operativo para campañas de investigación oceanográfica.</p>

      <div class="grid-proyectos">
        
        <div v-for="proyecto in proyectos" :key="proyecto.id" class="seccion-bloque tarjeta-proyecto">
          <div class="cabecera-proyecto">
            <h2 class="titulo-proyecto">{{ proyecto.titulo }}</h2>
            <span :class="['badge', proyecto.claseEstado]">{{ proyecto.estado }}</span>
          </div>
          
          <p class="ip-proyecto"><strong>IP:</strong> {{ proyecto.ip }}</p>
          <p class="descripcion-proyecto">{{ proyecto.descripcion }}</p>
          
          <div class="contenedor-etiquetas">
            <span v-for="(tag, index) in proyecto.etiquetas" :key="index" class="etiqueta-hash">{{ tag }}</span>
          </div>
        </div>

        <div class="seccion-bloque tarjeta-anadir" @click="$emit('volver')">
          <div class="contenido-anadir">
            <span class="icono-mas">+</span>
            <p>Gestionar proyectos en Intranet</p>
          </div>
        </div>

      </div> </div>
  </div>
</template>

<style scoped>
.proyectos-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

/* 🌊 FONDO CON TU IMAGEN DE PECES 🌊 */
.fondo-proyectos { 
  position: absolute; 
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 480px; 
  
  /* Aquí enlazamos tu imagen desde la carpeta public, manteniendo el degradado corporativo encima */
  background-image: linear-gradient(rgba(1, 33, 105, 0.65), rgba(1, 33, 105, 0.85)), url('/pecesaguasalada.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  
  z-index: 0; 
}

/* El contenido bajado a la misma altura que servicios */
.contenido-hub { 
  position: relative; 
  z-index: 10; 
  padding-top: 80px; 
}

/* Título con línea verde inferior */
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
  background-color: #8cc63f; /* Verde corporativo ICM */
}

.subtitulo { color: #e0e6ed; font-size: 1rem; margin-bottom: 40px; max-width: 800px; }

/* Grid idéntico al de servicios pero permitiendo más filas */
.grid-proyectos {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(450px, 1fr)); 
  gap: 30px; 
}

/* Cajas blancas idénticas a las de los servicios */
.seccion-bloque { 
  background: white; 
  border-radius: 12px; 
  padding: 35px; 
  box-shadow: 0 10px 30px rgba(0,0,0,0.15); 
  display: flex;
  flex-direction: column; 
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.seccion-bloque:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0,0,0,0.2);
}

/* Estilos internos de la tarjeta de proyecto */
.cabecera-proyecto {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 15px;
  gap: 15px;
}

.titulo-proyecto { 
  color: #012169; 
  margin: 0; 
  font-size: 1.5rem; 
}

.ip-proyecto {
  color: #005596;
  font-size: 1.05rem;
  margin-bottom: 15px;
}

.descripcion-proyecto {
  color: #555;
  line-height: 1.6;
  margin-bottom: 25px;
  flex-grow: 1; /* Empuja las etiquetas hacia abajo */
}

/* Etiquetas (Tags) */
.contenedor-etiquetas {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: auto;
}

.etiqueta-hash {
  background-color: #f0f7ff;
  color: #0086c0;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: bold;
}

/* Badges de estado */
.badge {
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  white-space: nowrap;
}

.badge-activa { background-color: #d4edda; color: #155724; }
.badge-finalizada { background-color: #e2e3e5; color: #383d41; }
.badge-planificacion { background-color: #fff3cd; color: #856404; }

/* Tarjeta especial para añadir (con borde discontinuo) */
.tarjeta-anadir {
  border: 2px dashed #ccc;
  background-color: rgba(255, 255, 255, 0.5);
  box-shadow: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.tarjeta-anadir:hover {
  background-color: white;
  border-color: #0086c0;
}

.contenido-anadir { color: #888; }
.icono-mas { font-size: 3rem; display: block; margin-bottom: 10px; color: #ccc; }
.tarjeta-anadir:hover .contenido-anadir, .tarjeta-anadir:hover .icono-mas { color: #0086c0; }

@media (max-width: 768px) {
  .grid-proyectos { grid-template-columns: 1fr; }
  .fondo-proyectos { height: 400px; }
}
</style>