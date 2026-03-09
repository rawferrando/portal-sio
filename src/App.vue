<script setup>
import { ref } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import IntranetFondeos from './components/IntranetFondeos.vue'
import Instrumentacion from './components/Instrumentacion.vue'
import Embarcacion from './components/Embarcacion.vue'

// Esta variable es el "GPS". Ahora controla todas las páginas.
const paginaActual = ref('inicio')
</script>

<script setup>
import { ref } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import IntranetFondeos from './components/IntranetFondeos.vue'
import Instrumentacion from './components/Instrumentacion.vue'
import Embarcacion from './components/Embarcacion.vue'

// Esta variable es el "GPS". Ahora controla todas las páginas.
const paginaActual = ref('inicio')
</script>

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
  color: #005596;
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
  color: rgba(255, 255, 255, 0.9) !important;
  font-size: 1rem;
  transition: all 0.3s;
  cursor: pointer;
  filter: drop-shadow(0 0 2px rgba(0,0,0,0.3));
}

.enlace-privado:hover {
  color: #ffcc00 !important;
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
</style>