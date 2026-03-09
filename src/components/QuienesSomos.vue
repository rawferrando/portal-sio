<template>
  <div class="quienes-somos">
    <header class="cabecera-seccion">
      <h1>Quiénes Somos</h1>
      <p class="intro">
        El <strong>Servicio de Ingeniería Oceanográfica</strong> del Instituto de Ciencias del Mar ofrece apoyo técnico especializado a grupos de investigación y proyectos en el ámbito de las ciencias del mar.
      </p>
      <p class="descripcion">
        Nuestro objetivo es proporcionar soluciones técnicas adaptadas a las necesidades específicas de cada cliente, así como ofrecer asesoramiento experto basado en años de experiencia en el sector. Disponemos de un equipo altamente cualificado y de una amplia gama de instrumentación y recursos, lo que nos permite innovar, desarrollar y personalizar equipos, así como diseñar, desplegar e implementar sistemas avanzados de adquisición de datos, tanto fijos como móviles.
      </p>
    </header>

    <section class="servicios">
      <h2>¿Qué ofrecemos?</h2>
      
      <div class="grid-servicios">
        <div class="tarjeta">
          <h3>Proyectos de Investigación</h3>
          <p>Aportamos experiencia técnica especializada, innovación tecnológica y soporte logístico en todas las fases del proyecto.</p>
        </div>

        <div class="tarjeta">
          <h3>Diseño e Instalación</h3>
          <p>Diseño e instalación de fondeos oceanográficos y desarrollo de sistemas de observación marinos instrumentados.</p>
        </div>

        <div class="tarjeta">
          <h3>Despliegue y Mantenimiento</h3>
          <p>Despliegue, mantenimiento de instrumentación y alquiler de espacio en áreas experimentales.</p>
        </div>

        <div class="tarjeta">
          <h3>Análisis y Caracterización</h3>
          <p>Caracterización de agua marina con perfilador vertical y servicio de análisis de salinidad del agua.</p>
        </div>

        <div class="tarjeta">
          <h3>Servicios de Embarcación</h3>
          <p>Disponemos de servicio de embarcación en el Puerto Olímpico de Barcelona para estudios oceanográficos y despliegues.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.quienes-somos {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
  font-family: Arial, sans-serif;
  color: #333;
}

.cabecera-seccion {
  margin-bottom: 3rem;
  text-align: left; /* Fuerza a que todo se alinee a la izquierda desde la raíz */
}

.cabecera-seccion h1 {
  color: #0056b3; /* Esto le devuelve el color azul institucional */
  font-size: 2rem;
  margin-bottom: 1.5rem;
  border-bottom: 2px solid #e0e0e0; /* Esto crea la línea gris */
  padding-bottom: 0.5rem; /* Esto separa un poco el texto de la línea */
}

.intro {
  font-size: 1.25rem;
  color: #0056b3;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.descripcion {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #555;
}

.servicios h2 {
  color: #0056b3;
  font-size: 2rem;
  border-bottom: 2px solid #e0e0e0;
  padding-bottom: 0.5rem;
  margin-bottom: 2rem;
}

.grid-servicios {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.tarjeta {
  background-color: #f8f9fa;
  border-left: 5px solid #0056b3;
  padding: 1.5rem;
  border-radius: 6px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  transition: transform 0.2s ease;
}

.tarjeta:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.tarjeta h3 {
  color: #0056b3;
  margin-top: 0;
  margin-bottom: 0.8rem;
  font-size: 1.2rem;
}

.tarjeta p {
  margin: 0;
  line-height: 1.5;
  color: #666;
}
</style>