<script setup>
import QuienesSomos from './components/QuienesSomos.vue'
import RecursosTecnicos from './components/RecursosTecnicos.vue'
import IntranetFondeos from './components/IntranetFondeos.vue'
</script>

<template>
  <div id="layout-sio">
    <header class="header-icm">
      <div class="logo-area">
        <img src="./assets/logo-sio.jpg" alt="Logo SIO" class="logo-img" /> 
      </div>
      <nav class="nav-idiomas">
        <a href="#" class="active">CA</a> | <a href="#">ES</a> | <a href="#">EN</a>
      </nav>
    </header>

    <main class="contenedor-principal">
      <QuienesSomos />
      <hr />
      <RecursosTecnicos />
      <hr />
      <IntranetFondeos />
    </main>

    <footer class="footer-sio">
      <p>Institut de Ciències del Mar (ICM-CSIC)</p>
      <p>📧 sio@icm.csic.es | 📍 Port Olímpic de Barcelona</p>
    </footer>
  </div>
</template>

<style>
:root {
  /* Este es el azul exacto extraído de la imagen del logo que me pasaste */
  --azul-sio-real: #005596; 
}

/* IMPORTANTE: Quitamos márgenes por defecto del navegador */
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
  padding: 1rem 4%; /* 4% para que no toque los bordes pero se vea ancho */
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  box-sizing: border-box;
}

.logo-img {
  height: 90px; /* Tamaño un poco mayor para que destaque el logo */
  width: auto;
}

/* AQUÍ ESTÁ LA MAGIA PARA EL ANCHO TOTAL */
.contenedor-principal {
  width: 100% !important;   /* Ocupa el 100% de la pantalla */
  max-width: none !important; /* Forzamos que no haya límite de ancho lateral */
  margin: 0;
  padding: 3rem 4%; 
  box-sizing: border-box;   /* Evita que el padding sume ancho extra */
}

.footer-sio {
  text-align: center;
  padding: 2.5rem;
  background: #1a1a1a;
  color: white;
  width: 100%;
  box-sizing: border-box;
}

.nav-idiomas a {
  color: white;
  text-decoration: none;
}

hr {
  margin: 4rem 0;
  border: 0;
  border-top: 1px solid #eee;
}
</style>