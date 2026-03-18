<template>
  <div class="quienes-somos">
    <h2>Quiénes Somos</h2>
    <p>El <strong>Servicio de Ingeniería Oceanográfica</strong> del Instituto de Ciencias del Mar ofrece apoyo técnico especializado a grupos de investigación y proyectos en el ámbito de las ciencias del mar.</p>
    <p>Nuestro objetivo es proporcionar soluciones técnicas adaptadas a las necesidades específicas de cada cliente, así como ofrecer asesoramiento experto basado en años de experiencia en el sector. Disponemos de un equipo altamente cualificado y de una amplia gama de instrumentación y recursos, lo que nos permite innovar, desarrollar y personalizar equipos, así como diseñar, desplegar e implementar sistemas avanzados de adquisición de datos, tanto fijos como móviles. También ofrecemos herramientas y técnicas de verificación específicas para garantizar la calidad de los datos obtenidos en los estudios oceanográficos.</p>

    <h2 class="titulo-ofrecemos">¿Qué ofrecemos?</h2>
    
    <div class="grid-servicios">
      
      <div class="tarjeta-servicio bg-proyectos">
        <div class="contenido-tarjeta">
          <h3>Proyectos de Investigación</h3>
          <p>Aportamos experiencia técnica especializada, innovación tecnológica y soporte logístico en todas las fases del proyecto.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-despliegue">
        <div class="contenido-tarjeta">
          <h3>Despliegue y Mantenimiento</h3>
          <p>Diseño, despliegue, mantenimiento de líneas de instrumentación y alquiler de espacio en instalaciones experimentales.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-analisis">
        <div class="contenido-tarjeta">
          <h3>Análisis y Caracterización</h3>
          <p>Caracterización de agua marina con perfilador vertical y servicio de análisis de salinidad del agua.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-instrumentacion">
        <div class="contenido-tarjeta">
          <h3>Instrumentación Científica</h3>
          <p>Gestión del catálogo completo de sondas CTD, salinómetros y sensores disponibles para campañas.</p>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.quienes-somos { margin-bottom: 40px; }
h2 { color: #005596; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-top: 30px; }
p { line-height: 1.6; color: #444; font-size: 1.05rem; }
.titulo-ofrecemos { margin-top: 50px; margin-bottom: 30px; }

/* Grid de las tarjetas */
.grid-servicios {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 25px;
}

/* Estructura base de la tarjeta */
.tarjeta-servicio {
  position: relative;
  border-radius: 10px;
  overflow: hidden;
  min-height: 240px;
  display: flex;
  align-items: flex-end; /* Empuja el texto hacia abajo */
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background-size: cover;
  background-position: center;
}

/* Efecto al pasar el ratón */
.tarjeta-servicio:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

/* Capa de degradado oscuro sobre la imagen para que el texto se lea bien */
.tarjeta-servicio::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(to top, rgba(0, 40, 80, 0.95) 0%, rgba(0, 40, 80, 0.3) 100%);
}

/* Textos dentro de la tarjeta */
.contenido-tarjeta {
  position: relative;
  z-index: 1;
  padding: 25px;
  color: white;
}
.contenido-tarjeta h3 { color: white; border: none; padding: 0; margin: 0 0 10px 0; font-size: 1.4rem; }
.contenido-tarjeta p { color: #e0e0e0; margin: 0; font-size: 0.95rem; line-height: 1.5; }

/* IMÁGENES DE FONDO DE EJEMPLO (Se pueden cambiar luego) */
.bg-proyectos { background-image: url('https://images.unsplash.com/photo-1583212292454-1fe6229603b7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
.bg-despliegue { background-image: url('https://images.unsplash.com/photo-1518861053457-37c22e4dcb32?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
.bg-analisis { background-image: url('https://images.unsplash.com/photo-1582719471384-894fbb16e074?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
.bg-instrumentacion { background-image: url('https://images.unsplash.com/photo-1622322080352-794dc2d6505c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
</style>