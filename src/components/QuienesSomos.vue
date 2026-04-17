<template>
  <div class="home-sio">
    
    <section class="carrusel-sio">
      <div class="slide">
        <div class="overlay-carrusel">
          <h2>Ingeniería Oceánica de Vanguardia</h2>
          <p>Soporte tecnológico avanzado para la comunidad investigadora.</p>
        </div>
      </div>
    </section>

    <section class="contenedor-ancho grid-servicios">
      <div class="tarjeta-sio" @click="$emit('cambiar-pagina', 'servicios')">
        <div class="tarjeta-icono">⚙️</div>
        <h3>Servicios</h3>
        <p>Catálogo de instrumentación, calibración y soporte operativo.</p>
      </div>

      <div class="tarjeta-sio" @click="$emit('cambiar-pagina', 'proyectos')">
        <div class="tarjeta-icono">📂</div>
        <h3>Proyectos</h3>
        <p>Soporte técnico y logístico para campañas oceanográficas.</p>
      </div>

      <div class="tarjeta-sio" @click="$emit('cambiar-pagina', 'idi')">
        <div class="tarjeta-icono">💡</div>
        <h3>Desarrollo I+D+i</h3>
        <p>Diseño de prototipos e innovación tecnológica a medida.</p>
      </div>
    </section>

    <section class="seccion-fichas-tecnicas">
      <div class="contenedor-ancho grid-fichas-bottom">
        <div class="ficha-bottom">
          <h4>Memoria Anual 2025</h4>
          <p>Descubre los hitos y cifras clave de nuestra actividad durante el último año.</p>
          <a href="#" class="link-f">Descargar PDF ➔</a>
        </div>
        <div class="ficha-bottom destacado">
          <h4>Excelencia</h4>
          <p>Compromiso con la innovación tecnológica y los más altos estándares de calidad.</p>
          <a href="#" class="link-f">Saber más ➔</a>
        </div>
        <div class="ficha-bottom">
          <h4>Transparencia</h4>
          <p>Consulta pública de nuestros procesos, licitaciones y normativas internas.</p>
          <a href="#" class="link-f">Acceder ➔</a>
        </div>
      </div>
    </section>

    <section class="seccion-noticias contenedor-ancho">
      <h2 class="titulo-seccion">Actualidad SIO</h2>
      <div class="grid-noticias">
        
        <article class="tarjeta-noticia">
          <div class="img-noticia placeholder-img1"></div>
          <div class="contenido-noticia">
            <span class="fecha-noticia">17 Abril 2026</span>
            <h4>Preparativos campaña Antártida</h4>
            <p>El equipo del SIO finaliza la calibración de los CTDs que zarparán en el buque Hespérides la próxima semana.</p>
            <a href="#">Leer noticia ➔</a>
          </div>
        </article>

        <article class="tarjeta-noticia">
          <div class="img-noticia placeholder-img2"></div>
          <div class="contenido-noticia">
            <span class="fecha-noticia">10 Marzo 2026</span>
            <h4>Nuevo ROV integrado al catálogo</h4>
            <p>Ampliamos nuestra capacidad de exploración submarina con la adquisición de un nuevo vehículo operado remotamente.</p>
            <a href="#">Leer noticia ➔</a>
          </div>
        </article>

        <article class="tarjeta-noticia">
          <div class="img-noticia placeholder-img3"></div>
          <div class="contenido-noticia">
            <span class="fecha-noticia">22 Febrero 2026</span>
            <h4>Colaboración europea en I+D+i</h4>
            <p>El SIO participa en el desarrollo de boyas de deriva de nueva generación para la red de observación del Mediterráneo.</p>
            <a href="#">Leer noticia ➔</a>
          </div>
        </article>

      </div>
    </section>

  </div>
</template>

<style scoped>
/* CARRUSEL */
.carrusel-sio { height: 400px; background: #0a2540 url('https://icm.csic.es/sites/default/files/styles/slider_home/public/2021-04/slider_home_1.jpg') center/cover; position: relative; }
.overlay-carrusel { position: absolute; inset: 0; background: rgba(10, 37, 64, 0.6); display: flex; flex-direction: column; justify-content: center; align-items: center; color: white; text-align: center; padding: 20px; }
.overlay-carrusel h2 { font-size: 3rem; margin-bottom: 10px; font-weight: 300; }
.overlay-carrusel p { font-size: 1.2rem; margin: 0; }

/* 3 TARJETAS PRINCIPALES */
.grid-servicios { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: -50px; position: relative; z-index: 10; padding-bottom: 50px; }
.tarjeta-sio { background: white; padding: 40px 30px; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: center; cursor: pointer; transition: transform 0.3s; border-top: 4px solid transparent; }
.tarjeta-sio:hover { transform: translateY(-10px); border-top-color: #0088cc; }
.tarjeta-icono { font-size: 3rem; margin-bottom: 15px; }
.tarjeta-sio h3 { color: #0a2540; font-size: 1.5rem; margin-bottom: 15px; }
.tarjeta-sio p { color: #666; font-size: 1rem; line-height: 1.5; }

/* FICHAS TÉCNICAS (Memoria) */
.seccion-fichas-tecnicas { background: #f5f7fa; padding: 60px 0; border-top: 1px solid #e1e4e8; border-bottom: 1px solid #e1e4e8; }
.grid-fichas-bottom { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
.ficha-bottom { background: white; padding: 30px; border-radius: 6px; border-top: 4px solid #d1d5db; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
.ficha-bottom.destacado { border-top-color: #0088cc; }
.ficha-bottom h4 { color: #0a2540; font-size: 1.2rem; margin-top: 0; }
.ficha-bottom p { color: #555; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; }
.link-f { font-size: 0.85rem; font-weight: bold; color: #0088cc; text-decoration: none; }
.link-f:hover { text-decoration: underline; }

/* NOTICIAS */
.seccion-noticias { padding: 60px 20px; }
.titulo-seccion { color: #0a2540; font-size: 2rem; margin-bottom: 40px; text-align: center; font-weight: 300; }
.grid-noticias { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
.tarjeta-noticia { background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: 0.3s; }
.tarjeta-noticia:hover { box-shadow: 0 8px 25px rgba(0,0,0,0.1); }
.img-noticia { height: 200px; background-color: #0a2540; background-size: cover; background-position: center; }
/* Imágenes placeholder para las noticias */
.placeholder-img1 { background-image: url('https://images.unsplash.com/photo-1582967788606-a171c1080cb0?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
.placeholder-img2 { background-image: url('https://images.unsplash.com/photo-1605810230434-7631ac76ec81?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }
.placeholder-img3 { background-image: url('https://images.unsplash.com/photo-1544322477-8d2a632236a2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'); }

.contenido-noticia { padding: 25px; }
.fecha-noticia { display: block; color: #0088cc; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; margin-bottom: 10px; }
.contenido-noticia h4 { color: #0a2540; font-size: 1.2rem; margin: 0 0 10px 0; line-height: 1.3; }
.contenido-noticia p { color: #666; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; }
.contenido-noticia a { color: #0a2540; font-weight: bold; font-size: 0.9rem; text-decoration: none; }
.contenido-noticia a:hover { color: #0088cc; }

@media (max-width: 900px) {
  .header-inner { flex-direction: column; gap: 15px; }
  .header-logos-derecha { justify-content: center; }
  .grid-servicios { margin-top: 20px; }
}
</style>