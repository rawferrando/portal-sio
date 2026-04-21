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
      <h1 class="titulo-seccion">Servicios e Instalaciones SIO</h1>
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

/* Fondo oscuro superior */
.fondo-servicios { position: absolute; top: 0; left: 0; width: 100%; height: 350px; background: #012169; z-index: 0; }

.contenido-hub { position: relative; z-index: 10; padding-top: 80px; }

.titulo-seccion { color: white; font-size: 2.5rem; margin-bottom: 10px; font-weight: bold; }
.subtitulo { color: #a8bacc; font-size: 1.2rem; margin-bottom: 40px; max-width: 800px; }

/* ✨ ESTILOS DEL HORIZONTAL ✨ */
.grid-horizontal {
  display: grid;
  grid-template-columns: 1fr 1fr; /* Dos columnas idénticas */
  gap: 30px; 
}

.seccion-bloque { 
  background: white; 
  border-radius: 12px; 
  padding: 40px; 
  box-shadow: 0 10px 30px rgba(0,0,0,0.08); 
  display: flex;
  flex-direction: column; 
}

.titulo-clicable { color: #012169; cursor: pointer; display: inline-flex; align-items: center; gap: 10px; transition: color 0.3s; margin-top: 0