<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['volver'])

// CONFIGURACIÓN DEL CALENDARIO (Datos predefinidos)
// Puedes añadir más campañas aquí con este formato.
const campañas = ref([
  { inicio: '2026-04-10', fin: '2026-04-12', nombre: 'Muestreo de Agua', tipo: 'investigacion' },
  { inicio: '2026-04-22', fin: '2026-04-25', nombre: 'Mantenimiento Boyas', tipo: 'mantenimiento' },
  { inicio: '2026-05-05', fin: '2026-05-15', nombre: 'Despliegue Fondeos', tipo: 'investigacion' }
])

// Mes actual para el calendario (abril de 2026)
const mesActual = ref(new Date(2026, 3, 1)) 

const nombreMes = computed(() => {
  return mesActual.value.toLocaleString('es-ES', { month: 'long', year: 'numeric' })
})

const diasDelMes = computed(() => {
  const año = mesActual.value.getFullYear()
  const mes = mesActual.value.getMonth()
  const primerDia = new Date(año, mes, 1).getDay()
  const ultimoDia = new Date(año, mes + 1, 0).getDate()
  
  let dias = []
  // Ajuste para que el lunes sea el primer día
  const offset = primerDia === 0 ? 6 : primerDia - 1
  
  for (let i = 0; i < offset; i++) dias.push({ vacio: true })
  
  for (let d = 1; d <= ultimoDia; d++) {
    const fechaStr = `${año}-${String(mes + 1).padStart(2, '0')}-${String(d).padStart(2, '0')}`
    const campaña = campañas.value.find(c => fechaStr >= c.inicio && fechaStr <= c.fin)
    dias.push({ dia: d, fecha: fechaStr, campaña })
  }
  return dias
})
</script>

<template>
  <div class="pelagia-hub">
    <div class="fondo-pelagia"></div>

    <div class="contenedor-ancho contenido-hub">
      <div class="migas-pan" @click="$emit('volver')" style="cursor: pointer; color: #8cc63f; font-weight: bold; margin-bottom: 20px;">
        &larr; Volver a Servicios
      </div>

      <h1 class="titulo-seccion">Embarcación SIO: "Pelagia"</h1>
      <p class="subtitulo">Nuestra unidad de apoyo costero basada en el Port Olímpic de Barcelona.</p>

      <div class="grid-detalles">
        <div class="seccion-bloque ficha-tecnica">
          <h2 class="titulo-fija">📊 Especificaciones</h2>
          <ul>
            <li><strong>Eslora:</strong> 7,5 metros</li>
            <li><strong>Motorización:</strong> 200 HP fueraborda</li>
            <li><strong>Capacidad:</strong> 6 personas (incl. patrón)</li>
            <li><strong>Equipamiento:</strong> Grúa para despliegue de instrumentos, GPS diferencial y sonda.</li>
          </ul>
        </div>

        <div class="seccion-bloque servicios-mar">
          <h2 class="titulo-fija">🌊 Operaciones Habituales</h2>
          <p>Realizamos despliegues de fondeos, mantenimiento de boyas, muestreos de agua y sedimentos, y apoyo a buceo científico.</p>
        </div>
      </div>

      <div class="separador"></div>

      <h2 class="titulo-seccion" style="font-size: 1.8rem;">Disponibilidad y Reservas</h2>
      
      <div class="grid-calendario-reservas">
        <div class="seccion-bloque calendario-contenedor">
          <div class="header-calendario">
            <h3 style="margin-top:0; color:#012169; text-transform: capitalize;">{{ nombreMes }}</h3>
          </div>
          <div class="dias-semana">
            <span>Lun</span><span>Mar</span><span>Mié</span><span>Jue</span><span>Vie</span><span>Sáb</span><span>Dom</span>
          </div>
          <div class="grid-dias">
            <div v-for="(d, i) in diasDelMes" :key="i" :class="['celda', { 'ocupado': d.campaña, 'vacio': d.vacio }]">
              <span class="num-dia">{{ d.dia }}</span>
              <div v-if="d.campaña" class="dot-campaña"></div>
            </div>
          </div>
        </div>

        <div class="seccion-bloque info-campañas">
          <h3 style="margin-top: 0; color: #012169;">Campañas Programadas</h3>
          <div class="lista-items">
            <div v-for="(c, i) in campañas" :key="i" class="item-reserva">
              <div class="fecha-badge">{{ c.inicio.split('-')[2] }}/{{ c.inicio.split('-')[1] }}</div>
              <div class="detalles">
                <strong>{{ c.nombre }}</strong>
                <span>{{ c.tipo === 'investigacion' ? '🔬 Investigación' : '🛠️ Mantenimiento' }}</span>
              </div>
            </div>
          </div>
          <button class="btn-reserva">Solicitar Reserva de la Pelagia</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pelagia-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }

.fondo-pelagia { 
  position: absolute; top: 0; left: 0; width: 100%; height: 550px; 
  /* Puedes poner la foto real de la Pelagia si la tienes en la carpeta public */
  background-image: linear-gradient(rgba(1, 33, 105, 0.7), rgba(1, 33, 105, 0.9)), url('/Pelagia.jpg');
  background-size: cover; background-position: center; z-index: 0; 
}

.contenido-hub { position: relative; z-index: 10; padding-top: 120px; }
.titulo-seccion { color: white; font-size: 2.5rem; margin-bottom: 10px; font-weight: bold; display: inline-block; position: relative; padding-bottom: 8px;}
.titulo-seccion::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 4px; background-color: #8cc63f; }
.subtitulo { color: #e0e6ed; margin-bottom: 40px; font-size: 1.1rem; }

/* REGLAS PARA LAS CAJAS BLANCAS (COMPACTAS Y SIN HUECOS) */
.seccion-bloque { 
  background: white; 
  border-radius: 12px; 
  padding: 35px; 
  box-shadow: 0 10px 30px rgba(0,0,0,0.15); 
  display: flex;
  flex-direction: column;
  min-height: auto; /* Evita que sobre espacio en blanco por debajo */
}

.titulo-fija { color: #012169; margin-top: 0; font-size: 1.4rem; margin-bottom: 15px; border-bottom: 2px solid #eee; padding-bottom: 10px;}

.grid-detalles { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 40px; }

/* ESTILOS DE LOS TEXTOS INTERNOS COMPACTADOS */
.ficha-tecnica ul { list-style: none; padding: 0; margin: 0; }
.ficha-tecnica li { margin-bottom: 8px; color: #444; border-bottom: 1px solid #f4f7f9; padding-bottom: 8px; font-size: 0.95rem; line-height: 1.3;}
.ficha-tecnica li:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }

.servicios-mar p { color: #666; line-height: 1.4; font-size: 0.95rem; margin: 0; }

.separador { height: 2px; background: rgba(255,255,255,0.2); margin: 20px 0 40px 0; }

/* CALENDARIO Y RESERVAS */
.grid-calendario-reservas { display: grid; grid-template-columns: 1.5fr 1fr; gap: 30px; }

.header-calendario { text-align: center; margin-bottom: 15px; }
.dias-semana { display: grid; grid-template-columns: repeat(7, 1fr); text-align: center; font-weight: bold; color: #012169; margin-bottom: 10px; font-size: 0.9rem; }
.grid-dias { display: grid; grid-template-columns: repeat(7, 1fr); gap: 5px; }
.celda { aspect-ratio: 1; border: 1px solid #eee; display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; border-radius: 4px; font-size: 0.95rem; }
.celda.vacio { border: none; }
.celda.ocupado { background: #eef7ff; border-color: #0086c0; color: #012169; font-weight: bold; }
.dot-campaña { width: 6px; height: 6px; background: #8cc63f; border-radius: 50%; margin-top: 4px; }

.lista-items { display: flex; flex-direction: column; gap: 0; margin-top: 10px; }
.item-reserva { display: flex; gap: 15px; padding: 12px 0; border-bottom: 1px solid #f0f0f0; margin-bottom: 0 !important; }
.item-reserva:last-child { border-bottom: none; }
.fecha-badge { background: #012169; color: white; padding: 5px 10px; border-radius: 6px; font-weight: bold; font-size: 0.9rem; height: fit-content; }
.detalles { display: flex; flex-direction: column; line-height: 1.3;}
.detalles span { font-size: 0.85rem; color: #666; margin-top: 3px;}

.btn-reserva { margin-top: 20px; width: 100%; padding: 12px; background: #8cc63f; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; transition: background 0.3s; }
.btn-reserva:hover { background: #7ab332; }

@media (max-width: 992px) { 
  .grid-detalles, .grid-calendario-reservas { grid-template-columns: 1fr; } 
}
</style>