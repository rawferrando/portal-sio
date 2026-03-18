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

      <div class="tarjeta-servicio bg-tanques">
        <div class="contenido-tarjeta">
          <h3>Tanques y Laboratorio</h3>
          <p>Infraestructuras y espacios experimentales equipados para la simulación y prueba de equipos en condiciones controladas.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-embarcaciones">
        <div class="contenido-tarjeta">
          <h3>Embarcaciones y Logística</h3>
          <p>Apoyo operativo con embarcaciones propias para trabajos costeros, fondeos y recuperación de plataformas de observación.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-calibracion">
        <div class="contenido-tarjeta">
          <h3>Calibración y Verificación</h3>
          <p>Técnicas de verificación y control riguroso para garantizar la máxima calidad y precisión de los datos oceanográficos.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-desarrollo">
        <div class="contenido-tarjeta">
          <h3>Desarrollo a Medida</h3>
          <p>Diseño de soluciones de ingeniería personalizadas, desde el mecanizado de piezas hasta la adaptación de hardware de muestreo.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-auv">
        <div class="contenido-tarjeta">
          <h3>Vehículos Autónomos y Gliders</h3>
          <p>Operación, mantenimiento y despliegue de plataformas autónomas para misiones de observación de larga duración.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-datamanagement">
        <div class="contenido-tarjeta">
          <h3>Gestión de Datos Oceanográficos</h3>
          <p>Procesamiento, visualización y aseguramiento de la calidad (*QA*) de grandes volúmenes de datos científicos.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-comms">
        <div class="contenido-tarjeta">
          <h3>Comunicaciones en Tiempo Real</h3>
          <p>Sistemas de comunicación remota para boyas, landers y plataformas fijos vía satélite (Iridium) o radiofrecuencia.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-training">
        <div class="contenido-tarjeta">
          <h3>Formación Técnica Especializada</h3>
          <p>Cursos prácticos en el ICM para investigadores en el manejo de instrumentación, mantenimiento y seguridad en el mar.</p>
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

/* Grid de las tarjetas (Se ajusta dinámicamente: 4 columnas en grande, 3 en mediano, 2 o 1 en móvil) */
.grid-servicios {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
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
.contenido-tarjeta h3 { color: white; border: none; padding: 0; margin: 0 0 10px 0; font-size: 1.25rem; }
.contenido-tarjeta p { color: #e0e0e0; margin: 0; font-size: 0.9rem; line-height: 1.5; }

/* IMÁGENES DE FONDO (Originales) */
.bg-proyectos { background-image: url('https://images.unsplash.com/photo-1583212292454-1fe6229603b7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
.bg-despliegue { background-image: url('https://images.unsplash.com/photo-1518861053457-37c22e4dcb32?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
.bg-analisis { background-image: url('https://images.unsplash.com/photo-1582719471384-894fbb16e074?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
.bg-instrumentacion { background-image: url('https://images.unsplash.com/photo-1622322080352-794dc2d6505c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
.bg-tanques { background-image: url('https://images.unsplash.com/photo-1581093458791-9f3c3900df4b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
.bg-embarcaciones { background-image: url('https://images.unsplash.com/photo-1566324866657-31131103c800?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
.bg-calibracion { background-image: url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
.bg-desarrollo { background-image: url('https://images.unsplash.com/photo-1581092160607-ee22621dd758?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }

/* 👇 NUEVAS IMÁGENES DE FONDO PARA LAS 4 TARJETAS 👇 */
.bg-auv { background-image: url('https://images.unsplash.com/photo-1626002760611-667950c051a3?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); } /* Un Glider naranja bajo el agua */
.bg-datamanagement { background-image: url('https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); } /* Un circuito y datos abstractos */
.bg-comms { background-image: url('https://images.unsplash.com/photo-1516110833967-0b5716ca1387?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); } /* Una antena satelital/torre costera */
.bg-training { background-image: url('https://images.unsplash.com/photo-1581094396009-8488e085c8e3?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); } /* Dos personas trabajando sobre instrumentación en un taller */
</style>