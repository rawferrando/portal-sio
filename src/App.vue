<script setup>
import { ref } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import RecursosTecnicos from './components/RecursosTecnicos.vue'
import IntranetFondeos from './components/IntranetFondeos.vue'

const mostrarIntranet = ref(false)
</script>

<template>
  <div class="quienes-somos">
    <header class="cabecera-seccion">
      <h1>Quiénes Somos</h1>
      <p class="intro">
        El <strong>Servicio de Ingeniería Oceanográfica (SIO)</strong> gestiona las infraestructuras técnicas del ICM-CSIC para el apoyo a la investigación marina.
      </p>
    </header>

    <section class="servicios-unificados">
      <h2 class="titulo-sio">Servicios y Recursos Técnicos</h2>
      
      <div class="grid-servicios">
        <div class="tarjeta">
          <h3>🚢 Operaciones en el Mar</h3>
          <p>Servicio de embarcación propia en el Port Olímpic para despliegue de fondeos, mantenimiento de instrumentación y adquisición de datos costeros.</p>
        </div>

        <div class="tarjeta">
          <h3>🛠️ Ingeniería y Prototipado</h3>
          <p>Diseño y fabricación de equipos a medida en nuestro laboratorio especializado. Mantenimiento preventivo y calibración de sensores oceanográficos.</p>
        </div>

        <div class="tarjeta">
          <h3>🧪 Instrumentación Científica</h3>
          <p>Disponemos de sondas CTD (SBE 911plus y CastAway) para perfiles de alta precisión y salinómetro Autosal 8400B para análisis de laboratorio.</p>
        </div>

        <div class="tarjeta">
          <h3>🏗️ Infraestructuras</h3>
          <p>Gestión de tanques experimentales y áreas de pruebas controladas para la validación de nueva tecnología marina.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<style>
:root {
  --azul-sio-real: #005596; 
}

body, html {
  margin: 0;
  padding: 0;
  width: 100%;
}

#layout-sio {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
  width: 100%;
}

.header-icm {
  background-color: var(--azul-sio-real);
  color: white;
  padding: 1rem 4%; 
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  box-sizing: border-box;
}

.logo-img {
  height: 90px; 
  width: auto;
}

.nav-idiomas {
  display: flex;
  align-items: center;
}

.nav-idiomas a {
  color: white;
  text-decoration: none;
  margin: 0 5px;
}

.separador {
  color: rgba(255, 255, 255, 0.3);
  margin: 0 10px;
}

.enlace-privado {
  color: rgba(255, 255, 255, 0.9) !important; /* Ahora es blanco casi sólido */
  font-size: 1rem; /* Un pelín más grande para que se vea mejor */
  transition: all 0.3s;
  cursor: pointer;
  filter: drop-shadow(0 0 2px rgba(0,0,0,0.3)); /* Le da un poco de relieve */
}

.enlace-privado:hover {
  color: #ffcc00 !important; /* Al pasar el ratón, se vuelve amarillo */
  opacity: 1;
}

.contenedor-principal {
  width: 100% !important;   
  max-width: none !important; 
  margin: 0;
  padding: 3rem 4%; 
  box-sizing: border-box;   
  min-height: 60vh;
}

.footer-sio {
  text-align: center;
  padding: 2.5rem;
  background: #005596;
  color: white;
  width: 100%;
  box-sizing: border-box;
}

hr {
  margin: 1.5rem 0; /* Antes era 4rem, lo bajamos para que no haya tanto hueco */
  border: 0;
  border-top: 1px solid #eee;
}
</style>