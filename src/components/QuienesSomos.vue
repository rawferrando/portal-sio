<template>
  <div class="quienes-somos">
    <h2>Quiénes Somos</h2>
    <p>El <strong>Servicio de Ingeniería Oceanográfica</strong> del Instituto de Ciencias del Mar ofrece soporte técnico especializado a grupos de investigación y proyectos en el ámbito de las ciencias del mar.</p>
    <p>Nuestro objetivo es proporcionar soluciones técnicas adaptadas a las necesidades específicas de cada cliente, además de ofrecer asesoramiento experto basado en años de experiencia en el sector. Contamos con un equipo altamente cualificado y una amplia gama de instrumentación y recursos, lo que nos permite innovar, desarrollar y personalizar equipos, así como diseñar, desplegar e implementar sistemas avanzados de adquisición de datos, tanto fijos como móviles. También ofrecemos herramientas y técnicas de verificación específicas para garantizar la calidad de los datos obtenidos en los estudios oceanográficos.</p>

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
          <p>Diseño, despliegue y mantenimiento de líneas de instrumentación fondeadas.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-analisis">
        <div class="contenido-tarjeta">
          <h3>Análisis y Caracterización</h3>
          <p>Caracterización de agua marina con perfilador vertical y análisis de salinidad.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-instrumentacion clicable" @click="$emit('cambiar-pagina', 'instrumentacion')">
        <div class="contenido-tarjeta">
          <h3>Instrumentación Científica</h3>
          <p>Gestión del catálogo completo de sondas CTD, salinómetros y sensores disponibles.</p>
          <span class="enlace-falso">🔍 Buscar Equipos y Reservar ➔</span>
        </div>
      </div>

      <div class="tarjeta-servicio bg-tanques">
        <div class="contenido-tarjeta">
          <h3>Tanques y Laboratorio</h3>
          <p>Infraestructuras experimentales equipadas para simulación en condiciones controladas.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-embarcaciones">
        <div class="contenido-tarjeta">
          <h3>Embarcaciones y Logística</h3>
          <p>Apoyo operativo con embarcaciones propias y drones para trabajos costeros.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-calibracion">
        <div class="contenido-tarjeta">
          <h3>Calibración y Verificación</h3>
          <p>Técnicas de control riguroso para garantizar la precisión de los datos oceanográficos.</p>
        </div>
      </div>

      <div class="tarjeta-servicio bg-desarrollo">
        <div class="contenido-tarjeta">
          <h3>Desarrollo a Medida</h3>
          <p>Diseño de soluciones de ingeniería personalizadas y mecanizado de piezas.</p>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.quienes-somos { margin-bottom: 40px; animation: fadeIn 0.5s ease-in-out; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

h2 { color: #005596; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-top: 30px; }

/* 👇 AQUÍ AÑADIMOS EL TEXT-ALIGN: JUSTIFY 👇 */
p { line-height: 1.6; color: #444; font-size: 1.05rem; text-align: justify; }

.titulo-ofrecemos { margin-top: 50px; margin-bottom: 30px; }

/* Grid de las tarjetas */
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
  min-height: 250px;
  display: flex;
  align-items: flex-end;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background-color: #005596; 
  background-size: cover;
  background-position: center;
}

.tarjeta-servicio:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}

/* Capa de degradado oscuro */
.tarjeta-servicio::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(to top, rgba(0, 30, 60, 0.95) 0%, rgba(0, 30, 60, 0.2) 100%);
  transition: background 0.3s ease;
}
.tarjeta-servicio:hover::before {
  background: linear-gradient(to top, rgba(0, 30, 60, 0.98) 0%, rgba(0, 30, 60, 0.4) 100%);
}

/* Textos dentro de la tarjeta */
.contenido-tarjeta {
  position: relative;
  z-index: 1;
  padding: 25px;
  color: white;
  width: 100%;
}
.contenido-tarjeta h3 { color: white; border: none; padding: 0; margin: 0 0 10px 0; font-size: 1.25rem; text-shadow: 1px 1px 3px rgba(0,0,0,0.5); }

/* Para que los textos de las tarjetas no se justifiquen y queden feos, les forzamos alineación a la izquierda */
.contenido-tarjeta p { color: #e2eef7; margin: 0; font-size: 0.9rem; line-height: 1.5; text-align: left; }

/* Efecto clicable para la tarjeta 4 */
.clicable { cursor: pointer; border: 2px solid transparent; }
.clicable:hover { border: 2px solid #66b2ff; }
.enlace-falso { display: inline-block; margin-top: 15px; color: #66b2ff; font-weight: bold; font-size: 0.95rem; background: rgba(0,0,0,0.3); padding: 5px 10px; border-radius: 4px; }

/* Imágenes locales */
.bg-proyectos { background-image: url('../assets/proyectos.jpg'); }
.bg-despliegue { background-image: url('../assets/despliegue.jpg'); }
.bg-analisis { background-image: url('../assets/analisis.jpg'); }
.bg-instrumentacion { background-image: url('../assets/instrumentacion.jpg'); }
.bg-tanques { background-image: url('../assets/tanques.jpg'); }
.bg-embarcaciones { background-image: url('../assets/embarcacion.jpg'); }
.bg-calibracion { background-image: url('../assets/calibracion.jpg'); }
.bg-desarrollo { background-image: url('../assets/desarrollo.jpg'); }
</style>

<style scoped>
.quienes-somos { margin-bottom: 40px; animation: fadeIn 0.5s ease-in-out; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

h2 { color: #005596; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-top: 30px; }
p { line-height: 1.6; color: #444; font-size: 1.05rem; }
.titulo-ofrecemos { margin-top: 50px; margin-bottom: 30px; }

/* Grid de las tarjetas */
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
  min-height: 250px;
  display: flex;
  align-items: flex-end;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background-color: #005596; /* Color de respaldo por si tarda en cargar la foto */
  background-size: cover;
  background-position: center;
}

.tarjeta-servicio:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}

/* Capa de degradado oscuro */
.tarjeta-servicio::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(to top, rgba(0, 30, 60, 0.95) 0%, rgba(0, 30, 60, 0.2) 100%);
  transition: background 0.3s ease;
}
.tarjeta-servicio:hover::before {
  background: linear-gradient(to top, rgba(0, 30, 60, 0.98) 0%, rgba(0, 30, 60, 0.4) 100%);
}

/* Textos dentro de la tarjeta */
.contenido-tarjeta {
  position: relative;
  z-index: 1;
  padding: 25px;
  color: white;
  width: 100%;
}
.contenido-tarjeta h3 { color: white; border: none; padding: 0; margin: 0 0 10px 0; font-size: 1.25rem; text-shadow: 1px 1px 3px rgba(0,0,0,0.5); }
.contenido-tarjeta p { color: #e2eef7; margin: 0; font-size: 0.9rem; line-height: 1.5; }

/* Efecto clicable para la tarjeta 4 */
.clicable { cursor: pointer; border: 2px solid transparent; }
.clicable:hover { border: 2px solid #66b2ff; }
.enlace-falso { display: inline-block; margin-top: 15px; color: #66b2ff; font-weight: bold; font-size: 0.95rem; background: rgba(0,0,0,0.3); padding: 5px 10px; border-radius: 4px; }

/* 👇 AQUÍ ESTÁ EL TRUCO: Cargar imágenes desde la carpeta local assets 👇 */
.bg-proyectos { background-image: url('../assets/proyectos.jpg'); }
.bg-despliegue { background-image: url('../assets/despliegue.jpg'); }
.bg-analisis { background-image: url('../assets/analisis.jpg'); }
.bg-instrumentacion { background-image: url('../assets/instrumentacion.jpg'); }
.bg-tanques { background-image: url('../assets/tanques.jpg'); }
.bg-embarcaciones { background-image: url('../assets/embarcacion.jpg'); }
.bg-calibracion { background-image: url('../assets/calibracion.jpg'); }
.bg-desarrollo { background-image: url('../assets/desarrollo.jpg'); }
</style>