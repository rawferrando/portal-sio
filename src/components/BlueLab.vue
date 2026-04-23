<script setup>
import { ref } from 'vue'

const emit = defineEmits(['volver'])

const researchAreas = ref([
  {
    titulo: 'Plataformas Robóticas',
    icono: '🚤', 
    descripcion: 'Desarrollo de autonomía supervisada y muestreo adaptativo integrando AUVs, ASVs y drones. Operan como nodos de comunicación y monitorización en tiempo real.',
    etiquetas: ['AUV', 'ASV', 'Mapeo Costero']
  },
  {
    titulo: 'Diseños Bioinspirados',
    icono: '🦀',
    descripcion: 'Robótica submarina inspirada en organismos marinos para interactuar con el lecho marino con una perturbación ambiental y acústica mínima.',
    etiquetas: ['Locomoción', 'Bajo Impacto']
  },
  {
    titulo: 'Sensores en Animales',
    icono: '🦈',
    descripcion: 'Uso de megafauna marina como plataformas móviles (biologging) para obtener datos in situ en áreas dinámicas e inaccesibles.',
    etiquetas: ['Biotelemetría', 'Megafauna']
  },
  {
    titulo: 'Machine Learning (IA)',
    icono: '🧠',
    descripcion: 'Aplicación de Inteligencia Artificial (RL) para la coordinación de flotas y clasificación de datos, respaldado por clusters HPC.',
    etiquetas: ['IA', 'Machine Learning']
  }
])
</script>

<template>
  <div class="bluelab-hub">
    <div class="fondo-bluelab"></div>

    <div class="contenedor-ancho contenido-hub">
      
      <h1 class="titulo-seccion">BLUE Lab</h1>
   
      <div class="seccion-intro">
        <p>
        Su misión es dotar a los investigadores de capacidades avanzadas en sensórica robótica, plataformas autónomas e innovación tecnológica.
        </p>
      </div>

      <div class="grid-areas">
        <div v-for="(area, i) in researchAreas" :key="i" class="tarjeta-area">
          <div class="icono-area">{{ area.icono }}</div>
          <h3 class="titulo-tarjeta">{{ area.titulo }}</h3>
          <p class="desc-tarjeta">{{ area.descripcion }}</p>
          <div class="contenedor-etiquetas">
            <span v-for="(tag, j) in area.etiquetas" :key="j" class="etiqueta-hash">#{{ tag }}</span>
          </div>
        </div>
      </div> 

    </div>
  </div>
</template>

<style scoped>
.bluelab-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

/* 🌊 FONDO ACTUALIZADO A LA IMPRESORA 3D 🌊 */
.fondo-bluelab { 
  position: absolute; 
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 550px; 
  background-image: linear-gradient(rgba(1, 33, 105, 0.75), rgba(1, 33, 105, 0.9)), 
                    url('/impresora3d.jpg'); /* ¡AQUÍ ESTÁ TU NUEVA IMAGEN! */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: 0; 
}

.contenido-hub { position: relative; z-index: 10; padding-top: 120px; }
.titulo-seccion { color: white; font-size: 2.5rem; margin-bottom: 15px; font-weight: bold; position: relative; display: inline-block; padding-bottom: 8px; }
.titulo-seccion::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 4px; background-color: #8cc63f; }
.subtitulo { color: #e0e6ed; font-size: 1.2rem; margin-bottom: 40px; max-width: 800px; }

.seccion-intro { background: rgba(255, 255, 255, 0.1); border-left: 4px solid #8cc63f; padding: 20px 25px; border-radius: 0 8px 8px 0; margin-bottom: 50px; backdrop-filter: blur(5px); }
.seccion-intro p { color: white; font-size: 1.1rem; line-height: 1.6; margin: 0; }

.titulo-areas { color: #012169; font-size: 1.8rem; margin-bottom: 25px; border-bottom: 2px solid #e0e6ed; padding-bottom: 10px; }

.grid-areas { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px; }
.tarjeta-area { background: white; border-radius: 12px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease; }
.tarjeta-area:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(0,0,0,0.15); }
.icono-area { font-size: 2.5rem; margin-bottom: 15px; }
.titulo-tarjeta { color: #012169; font-size: 1.3rem; margin-top: 0; margin-bottom: 15px; }
.desc-tarjeta { color: #555; line-height: 1.5; font-size: 0.95rem; margin-bottom: 20px; flex-grow: 1; }
.contenedor-etiquetas { display: flex; flex-wrap: wrap; gap: 8px; margin-top: auto; }
.etiqueta-hash { background-color: #f0f7ff; color: #0086c0; padding: 5px 10px; border-radius: 15px; font-size: 0.8rem; font-weight: bold; }

@media (max-width: 992px) { .grid-areas { grid-template-columns: 1fr; } .contenido-hub { padding-top: 120px; } }
</style>