<script setup>
import { ref, computed, onMounted } from 'vue'

// Usamos el enlace de EXPORTACIÓN directa, que funciona perfecto con tu permiso de "Cualquiera con el enlace"
const csvUrl = 'https://docs.google.com/spreadsheets/d/1h1j4rXGvF-3SVUQa-g9Jwuhx5C-yK2JgMRFescdzAHY/export?format=csv'

const cargando = ref(true)
const errorCarga = ref(false)
const instrumentos = ref([])
const categoriaActiva = ref('Física')

const categorias = computed(() => {
  const cats = new Set(instrumentos.value.map(inst => inst.tipo))
  return Array.from(cats)
})

const cargarDatos = async () => {
  try {
    const urlSinCache = csvUrl + '&t=' + new Date().getTime()
    const respuesta = await fetch(urlSinCache)
    
    if (!respuesta.ok) throw new Error('Error en la descarga del CSV')
    
    const textoCsv = await respuesta.text()
    
    const filas = parseCSV(textoCsv)
    const cabeceras = filas[0].map(h => h ? h.toLowerCase().trim() : '')
    
    const idxId = cabeceras.indexOf('id')
    const idxCat = cabeceras.indexOf('categoria')
    const idxSubcat = cabeceras.indexOf('subcategoria')
    const idxNombre = cabeceras.indexOf('nombre')
    const idxMarca = cabeceras.indexOf('marca')
    const idxEstado = cabeceras.indexOf('estado')
    const idxCalibracion = cabeceras.indexOf('ultima_calibracion')
    const idxDesc = cabeceras.indexOf('descripcion')
    const idxParams = cabeceras.indexOf('parametros_tecnicos')

    const nuevosInstrumentos = []
    
    for (let i = 1; i < filas.length; i++) {
      const fila = filas[i]
      if (!fila || fila.length < 2 || !fila[idxNombre]) continue 
      
      nuevosInstrumentos.push({
        id: fila[idxId] || i,
        tipo: fila[idxCat] || 'General',
        subcategoria: fila[idxSubcat] || 'Sin Subcategoría',
        nombre: fila[idxNombre],
        marca: fila[idxMarca] || '',
        estado: fila[idxEstado] || 'Disponible',
        ultimaCalibracion: fila[idxCalibracion] || 'N/A',
        descripcionCompleta: fila[idxDesc] || 'No hi ha descripció disponible.',
        parametros: fila[idxParams] || 'No hi ha paràmetres tècnics especificats.'
      })
    }
    
    instrumentos.value = nuevosInstrumentos
    if (categorias.value.length > 0 && !categorias.value.includes(categoriaActiva.value)) {
      categoriaActiva.value = categorias.value[0]
    }
    cargando.value = false
  } catch (error) {
    errorCarga.value = true
    cargando.value = false
  }
}

const parseCSV = (str) => {
  const arr = []
  let quote = false
  let col, c
  for (let row = col = c = 0; c < str.length; c++) {
    let cc = str[c], nc = str[c+1]
    arr[row] = arr[row] || []
    arr[row][col] = arr[row][col] || ''
    if (cc == '"' && quote && nc == '"') { arr[row][col] += cc; ++c; continue; }
    if (cc == '"') { quote = !quote; continue; }
    if (cc == ',' && !quote) { ++col; continue; }
    if (cc == '\r' && nc == '\n' && !quote) { ++row; col = 0; ++c; continue; }
    if (cc == '\n' && !quote) { ++row; col = 0; continue; }
    arr[row][col] += cc
  }
  return arr
}

onMounted(() => cargarDatos())

const instrumentosAgrupados = computed(() => {
  const filtrados = instrumentos.value.filter(inst => inst.tipo === categoriaActiva.value)
  const grupos = {}
  filtrados.forEach(inst => {
    if (!grupos[inst.subcategoria]) grupos[inst.subcategoria] = []
    grupos[inst.subcategoria].push(inst)
  })
  return grupos
})

// === ACORDEÓN ===
const instrumentoExpandido = ref(null)

const toggleAcordeon = (id) => {
  instrumentoExpandido.value = instrumentoExpandido.value === id ? null : id
}

// === GESTIÓN DE RESERVA Y CALENDARIO ===
const equipoSeleccionado = ref(null)
const diasSeleccionados = ref([])

const nombreInvestigador = ref('')
const dniInvestigador = ref('')
const institucionInvestigador = ref('')

const verDetalles = (equipo) => {
  equipoSeleccionado.value = equipo
  diasSeleccionados.value = [] 
  nombreInvestigador.value = ''
  dniInvestigador.value = ''
  institucionInvestigador.value = ''
}

const cambiarCategoria = (cat) => {
  categoriaActiva.value = cat
  equipoSeleccionado.value = null
  instrumentoExpandido.value = null 
}

const fechaHoy = new Date()
const mesActual = ref(fechaHoy.getMonth())
const anioActual = ref(fechaHoy.getFullYear())
const nombresMeses = ['Gener', 'Febrer', 'Març', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Setembre', 'Octubre', 'Novembre', 'Desembre']

const nombreMes = computed(() => nombresMeses[mesActual.value])
const diasEnMes = computed(() => new Date(anioActual.value, mesActual.value + 1, 0).getDate())

const cambiarMes = (direccion) => {
  let nuevoMes = mesActual.value + direccion
  if (nuevoMes > 11) { nuevoMes = 0; anioActual.value++ }
  else if (nuevoMes < 0) { nuevoMes = 11; anioActual.value-- }
  mesActual.value = nuevoMes
  diasSeleccionados.value = [] 
}

const esOcupado = (n) => {
  return n > 10 && n < 15 && equipoSeleccionado.value?.estado === 'En Uso'
}

const toggleDia = (n) => {
  if (esOcupado(n)) return
  const index = diasSeleccionados.value.indexOf(n)
  if (index > -1) diasSeleccionados.value.splice(index, 1) 
  else diasSeleccionados.value.push(n) 
}

const diasOrdenadosTexto = computed(() => {
  if (diasSeleccionados.value.length === 0) return 'Cap dia seleccionat'
  const diasStr = [...diasSeleccionados.value].sort((a, b) => a - b).join(', ')
  return `Dies ${diasStr} de ${nombreMes.value} de ${anioActual.value}`
})

// === GENERADOR DE DOCUMENTO PDF ===
const generarDocumento = () => {
  if (diasSeleccionados.value.length === 0) {
    alert("Si us plau, selecciona primer els dies al calendari.")
    return
  }
  if (!nombreInvestigador.value || !dniInvestigador.value) {
    alert("Si us plau, emplena el teu Nom i DNI per generar el document.")
    return
  }

  const ventana = window.open('', 'PRINT', 'height=800,width=800');
  const fechaHoyStr = new Date().toLocaleDateString('ca-ES', { year: 'numeric', month: 'long', day: 'numeric' });

  ventana.document.write(`
    <html>
      <head>
        <title>Responsabilitat_SIO_${equipoSeleccionado.value.nombre.replace(/\s+/g, '_')}</title>
        <style>
          body { font-family: 'Helvetica', 'Arial', sans-serif; padding: 50px; line-height: 1.6; color: #222; }
          .header { margin-bottom: 50px; text-align: right; }
          .destinatario { font-weight: bold; margin-bottom: 40px; }
          .title { font-weight: bold; font-size: 1.3em; text-align: center; margin-bottom: 40px; text-decoration: underline;}
          .signature-box { margin-top: 80px; border-top: 1px solid #000; width: 350px; padding-top: 10px; color: #555; }
        </style>
      </head>
      <body>
        <div class="header">Barcelona, ${fechaHoyStr}</div>
        <div class="destinatario">A l'atenció del Servei d'Enginyeria Oceanogràfica (SEO)<br>Institut de Ciències del Mar (ICM-CSIC)</div>
        <div class="title">DOCUMENT DE RESPONSABILITAT D'EQUIPAMENT SIO</div>
        <p>Per mitjà d'aquest document, jo <strong>${nombreInvestigador.value.toUpperCase()}</strong>, amb DNI/Passaport número <strong>${dniInvestigador.value.toUpperCase()}</strong>, en representació de la institució/grup <strong>${institucionInvestigador.value || '_______________________'}</strong>,</p>
        <p>Sol·licito la reserva de l'equipament tecnològic:</p>
        <p style="text-align: center; font-weight: bold; font-size: 1.2em; margin: 20px 0; padding: 10px; border: 1px solid #ccc; background-color: #f9f9f9;">
          ${equipoSeleccionado.value.nombre} ${equipoSeleccionado.value.marca ? `(${equipoSeleccionado.value.marca})` : ''}
        </p>
        <p>El període de préstec sol·licitat i bloquejat al calendari del Servei d'Enginyeria Oceanogràfica correspon a: <strong>${diasOrdenadosTexto.value}</strong>.</p>
        <p>Accepto la responsabilitat sobre l'equip esmentat i assumeixo el compromís de reemborsar el cost íntegre de l'equip en cas de pèrdua, així com el cost de la seva reparació en cas de danys, durant el període de préstec al nostre grup.</p>
        <p style="margin-top: 40px;">Cordialment,</p>
        <div class="signature-box">Signat digitalment per:<br><strong>${nombreInvestigador.value.toUpperCase()}</strong></div>
        <script>window.onload = function() { setTimeout(function() { window.print(); }, 500); }<\/script>
      </body>
    </html>
  `);
  ventana.document.close();
}
</script>

<template>
  <div class="servicios-hub">
    <div class="fondo-servicios"></div>

    <div class="contenido-hub">
      <h1 class="titulo-seccion">Instrumentación Oceanográfica</h1>
      <p class="subtitulo">Catálogo técnico, calibraciones y gestión de préstamos del SIO.</p>

      <div v-if="cargando" class="alerta-estado carga">⏳ Connectant amb la Base de Dades del SIO...</div>
      <div v-else-if="errorCarga" class="alerta-estado error">❌ Error de connexió. No s'ha pogut carregar el catàleg d'instruments.</div>

      <div v-else>
        <div class="tabs-sio">
          <button v-for="cat in categorias" :key="cat" :class="['tab-btn', { activa: categoriaActiva === cat }]" @click="cambiarCategoria(cat)">
            {{ cat }}
          </button>
        </div>

        <div class="grid-layout">
          <!-- ZONA IZQUIERDA: CATÁLOGO CON ACORDEÓN -->
          <div class="seccion-bloque ficha-wiki">
            <div v-if="Object.keys(instrumentosAgrupados).length === 0" style="color: #666; font-style: italic;">No hi ha instruments catalogats en aquesta secció.</div>

            <div v-for="(lista, subcat) in instrumentosAgrupados" :key="subcat" class="bloque-subcat">
              <h3 class="titulo-subcat">{{ subcat }}</h3>
              <ul class="lista-wiki">
                <li v-for="inst in lista" :key="inst.id">
                  <div class="item-header">
                    <span class="punto-azul">•</span>
                    <span class="enlace-wiki" @click="verDetalles(inst)" title="Click para reservar">{{ inst.nombre }}</span>
                    <span class="marca-wiki">({{ inst.marca }})</span>
                  </div>
                  <div class="caja-gris-wiki">
                    <div v-if="inst.ultimaCalibracion"><strong>- Última calibració:</strong> {{ inst.ultimaCalibracion }}</div>
                    
                    <button class="btn-acordeon" @click="toggleAcordeon(inst.id)">
                      <span v-if="instrumentoExpandido === inst.id">▲ Ocultar informació tècnica</span>
                      <span v-else>▼ Veure informació tècnica i manuals</span>
                    </button>
                    
                    <div v-show="instrumentoExpandido === inst.id" class="contenido-acordeon">
                      <div class="bloque-info-wiki">
                        <h4>Descripció General</h4>
                        <p class="texto-wiki">{{ inst.descripcionCompleta }}</p>
                      </div>
                      <div class="bloque-info-wiki">
                        <h4>Especificacions Tècniques / Manuals</h4>
                        <p class="texto-wiki parametros-wiki">{{ inst.parametros }}</p>
                      </div>
                      
                      <button class="btn-acordeon btn-cerrar-acordeon" @click="toggleAcordeon(inst.id)">
                        ▲ Ocultar informació tècnica
                      </button>
                    </div>

                  </div>
                </li>
              </ul>
            </div>
          </div>

          <!-- ZONA DERECHA: GESTIÓN DE RESERVAS -->
          <div class="seccion-bloque ficha-gestion">
            
            <div v-if="equipoSeleccionado" class="detalles-equipo">
              <div class="cabecera-estado">
                <h2 class="titulo-fija">{{ equipoSeleccionado.nombre }}</h2>
                <span :class="['badge-grande', equipoSeleccionado.estado.toLowerCase().replace(' ', '-')]">
                  {{ equipoSeleccionado.estado }}
                </span>
              </div>
              
              <div class="calendario-mini">
                <h3 class="titulo-mini">Pàs 1: Selecciona els dies de reserva</h3>
                
                <div class="controles-mes">
                  <button @click.prevent="cambiarMes(-1)" class="btn-mes">◀</button>
                  <span class="mes-actual">{{ nombreMes }} {{ anioActual }}</span>
                  <button @click.prevent="cambiarMes(1)" class="btn-mes">▶</button>
                </div>

                <div class="grid-dias">
                  <div v-for="n in diasEnMes" :key="n" @click="toggleDia(n)" :class="['dia', { ocupado: esOcupado(n), seleccionado: diasSeleccionados.includes(n), disponible: !esOcupado(n) }]">
                    {{ n }}
                  </div>
                </div>
                <p class="leyenda">* Gris: Disponible | Blau: Ocupat | Verd: La teva selecció</p>
              </div>

              <div class="generador-doc-box">
                <h3 class="titulo-mini">Pàs 2: Generar Document de Responsabilitat</h3>
                <p class="txt-p" style="font-size: 0.85rem; margin-bottom: 15px;">Emplena les teves dades per generar el document amb les dates de reserva ja incloses. Desa'l com a PDF per signar-lo.</p>
                
                <div class="form-grupo">
                  <label>Nom i Cognoms:</label>
                  <input type="text" v-model="nombreInvestigador" placeholder="Ex: Eve Galimany Sanromà" class="input-form">
                </div>
                <div class="form-grupo" style="display: flex; gap: 10px;">
                  <div style="flex: 1;">
                    <label>DNI / Passaport:</label>
                    <input type="text" v-model="dniInvestigador" placeholder="Ex: 38110059W" class="input-form">
                  </div>
                  <div style="flex: 1;">
                    <label>Institució (Opcional):</label>
                    <input type="text" v-model="institucionInvestigador" placeholder="Ex: ICATMAR" class="input-form">
                  </div>
                </div>
                
                <button @click="generarDocumento" class="btn-generar" :disabled="diasSeleccionados.length === 0">
                  📄 Generar i Desar PDF
                </button>
              </div>

              <form action="https://formsubmit.co/sio@icm.csic.es" method="POST" enctype="multipart/form-data" class="formulario-reserva">
                <h3 class="titulo-mini">Pàs 3: Envia la Sol·licitud</h3>
                
                <input type="hidden" name="_subject" :value="'Nova Reserva SIO: ' + equipoSeleccionado.nombre">
                <input type="hidden" name="_template" value="table">
                <input type="hidden" name="Equip_Sol·licitat" :value="equipoSeleccionado.nombre">
                <input type="hidden" name="Dies_Reserva" :value="diasOrdenadosTexto">
                <input type="hidden" name="Investigador" :value="nombreInvestigador">

                <div class="form-grupo">
                  <label>Correu Electrònic (Per confirmar la reserva):</label>
                  <input type="email" name="email" required placeholder="exemple@icm.csic.es" class="input-form">
                </div>

                <div class="form-grupo">
                  <label>Adjunta el PDF Generat i Signat Digitalment:</label>
                  <input type="file" name="Document_Signat" accept="application/pdf" required class="input-form file-input">
                </div>

                <button 
                  type="submit" 
                  :class="['btn-submit', { 'btn-desactivado': diasSeleccionados.length === 0 }]"
                  :disabled="diasSeleccionados.length === 0"
                >
                  📤 Enviar Sol·licitud de Reserva
                </button>
              </form>
              
              <button class="btn-cerrar" @click="equipoSeleccionado = null">Tancar Detalls</button>
            </div>

            <div v-else>
              <h2 class="titulo-fija">Préstecs SIO</h2>
              <p class="txt-p">Feu clic a l'enllaç blau de qualsevol instrument a l'esquerra per veure la seva fitxa tècnica completa i disponibilitat.</p>
              <hr style="border: 0; border-top: 1px solid #eee; margin: 25px 0;">
              <h3 class="titulo-mini">Com funciona?</h3>
              <ol style="color: #666; font-size: 0.9rem; line-height: 1.6; padding-left: 20px;">
                <li>Selecciona un instrument de la llista.</li>
                <li>Fes clic als dies del calendari que necessitis.</li>
                <li>Emplena el teu Nom i DNI per generar el document en PDF.</li>
                <li>Signa el PDF al teu ordinador i adjunta'l al formulari final.</li>
              </ol>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* ESTILOS GLOBALES UNIFICADOS */
.servicios-hub { position: relative; min-height: 100vh; padding-bottom: 80px; background-color: #f4f7f9; }
.fondo-servicios { 
  position: absolute; top: 0; left: 0; width: 100%; height: 550px; 
  background-image: linear-gradient(rgba(1, 33, 105, 0.75), rgba(1, 33, 105, 0.9)), url('/instrumentacion.jpg');
  background-size: cover; background-position: center; z-index: 0; 
}
.contenido-hub { position: relative; z-index: 10; padding-top: 120px; max-width: 1300px; margin: 0 auto; padding-left: 20px; padding-right: 20px; }
.titulo-seccion { color: white; font-size: 2.2rem; font-weight: bold; position: relative; display: inline-block; padding-bottom: 8px; margin-bottom: 15px; }
.titulo-seccion::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 4px; background-color: #8cc63f; }
.subtitulo { color: #e0e6ed; font-size: 1.1rem; margin-bottom: 25px; max-width: 800px; }

/* ALERTAS ESTADO */
.alerta-estado { text-align: center; padding: 20px; border-radius: 8px; font-weight: bold; margin-bottom: 30px; font-size: 1.2rem; }
.alerta-estado.carga { background: rgba(255, 255, 255, 0.9); color: #012169; border: 2px solid #0086c0; }
.alerta-estado.error { background: #ffebee; color: #c62828; border: 2px solid #ef5350; }

/* TABS */
.tabs-sio { display: flex; gap: 10px; margin-bottom: 25px; overflow-x: auto; }
.tab-btn { padding: 10px 20px; background: rgba(255, 255, 255, 0.1); border: 1px solid white; color: white; border-radius: 8px; cursor: pointer; font-weight: bold; transition: 0.3s; white-space: nowrap; }
.tab-btn.activa { background: #8cc63f; border-color: #8cc63f; color: #012169; }

/* GRID PRINCIPAL */
.grid-layout { display: grid; grid-template-columns: 1.8fr 1.3fr; gap: 30px; }
.seccion-bloque { background: white; border-radius: 12px; padding: 35px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); min-height: auto; }
.titulo-fija { color: #012169; margin-top: 0; font-size: 1.4rem; margin-bottom: 20px; border-bottom: 2px solid #eee; padding-bottom: 10px; }

/* ESTILO LISTADO (ZONA IZQUIERDA) */
.bloque-subcat { margin-bottom: 30px; }
.titulo-subcat { font-size: 1.1rem; color: #333; margin-bottom: 15px; border-bottom: 1px solid #ddd; padding-bottom: 5px; }
.lista-wiki { list-style: none; padding-left: 0; margin: 0; }
.item-header { margin-bottom: 8px; font-size: 0.95rem; }
.punto-azul { color: #0056b3; margin-right: 8px; font-size: 1.2rem; line-height: 0; }
.enlace-wiki { color: #0056b3; font-weight: 500; cursor: pointer; text-decoration: none; font-size: 1.05rem; }
.enlace-wiki:hover { text-decoration: underline; }
.marca-wiki { color: #666; font-size: 0.9rem; margin-left: 5px; }
.caja-gris-wiki { background-color: #f1f3f4; border-radius: 6px; padding: 10px 15px; margin-left: 15px; margin-bottom: 20px; font-family: 'Consolas', 'Courier New', Courier, monospace; font-size: 0.85rem; color: #202124; line-height: 1.6; }

/* ESTILOS ACORDEÓN E IMAGEN */
.btn-acordeon { background: none; border: none; color: #0086c0; font-family: inherit; font-size: 0.85rem; font-weight: bold; cursor: pointer; padding: 5px 0 0 0; display: block; margin-top: 5px; text-align: left; }
.btn-acordeon:hover { text-decoration: underline; }
.btn-cerrar-acordeon { width: 100%; text-align: center; margin-top: 15px; padding-top: 12px; border-top: 1px dashed #ddd; color: #666; font-size: 0.8rem; }
.btn-cerrar-acordeon:hover { color: #d32f2f; text-decoration: none; }
.contenido-acordeon { background: white; border-left: 3px solid #8cc63f; padding: 15px; margin-top: 10px; border-radius: 0 6px 6px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.05); animation: fadeIn 0.3s; }

.bloque-info-wiki { margin-bottom: 15px; }
.bloque-info-wiki h4 { color: #012169; font-size: 0.95rem; margin: 0 0 5px 0; font-family: system-ui, -apple-system, sans-serif; }
.texto-wiki { margin: 0; white-space: pre-line; color: #555; font-size: 0.9rem; }
.parametros-wiki { background: #f8f9fa; padding: 10px; border-radius: 4px; font-family: monospace; font-size: 0.8rem; border: 1px dashed #ccc; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(-5px); } to { opacity: 1; transform: translateY(0); } }

/* PANEL DERECHO (GESTIÓN) */
.cabecera-estado { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-bottom: 15px;}
.cabecera-estado .titulo-fija { border-bottom: none; margin-bottom: 0; padding-bottom: 0; font-size: 1.3rem;}
.badge-grande { padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; }
.badge-grande.disponible { background: #e6f4ea; color: #1e7e34; }
.badge-grande.en-uso { background: #fff4e5; color: #b45d00; }
.badge-grande.mantenimiento { background: #fdeaea; color: #c53030; }
.txt-p { font-size: 0.95rem; color: #666; line-height: 1.5; margin-bottom: 20px; }

/* ESTILOS NUEVOS DEL CALENDARIO */
.calendario-mini { margin-bottom: 20px; }
.titulo-mini { font-size: 1.1rem; color: #012169; margin-bottom: 10px; font-weight: bold; }
.controles-mes { display: flex; justify-content: space-between; align-items: center; background: #012169; color: white; padding: 8px 15px; border-radius: 6px 6px 0 0; }
.btn-mes { background: transparent; border: none; color: white; font-size: 1.2rem; cursor: pointer; transition: transform 0.2s; }
.btn-mes:hover { transform: scale(1.2); }
.mes-actual { font-weight: bold; font-size: 1rem; }
.grid-dias { display: grid; grid-template-columns: repeat(7, 1fr); gap: 5px; padding: 10px; background: #f9f9f9; border: 1px solid #eee; border-radius: 0 0 6px 6px; }
.dia { padding: 8px; text-align: center; font-size: 0.85rem; border-radius: 4px; font-weight: bold; transition: 0.2s; user-select: none; }
.dia.disponible { background: white; color: #666; cursor: pointer; border: 1px solid #ddd;}
.dia.disponible:hover { border-color: #8cc63f; background: #f0f7e6; }
.dia.ocupado { background: #0086c0; color: white; cursor: not-allowed; opacity: 0.6; }
.dia.seleccionado { background: #8cc63f; color: #012169; border: 1px solid #012169; transform: scale(1.05); }
.leyenda { font-size: 0.75rem; color: #999; margin-top: 10px; text-align: center; }

/* GENERADOR DE DOCUMENTO Y FORMULARIO RESERVA */
.generador-doc-box { background-color: #eef5fa; padding: 20px; border-radius: 8px; border: 1px dashed #0086c0; margin-bottom: 20px; }
.formulario-reserva { background-color: #f8f9fa; padding: 20px; border-radius: 8px; border: 1px solid #e0e0e0; margin-top: 15px; }
.form-grupo { margin-bottom: 15px; }
.form-grupo label { display: block; font-size: 0.85rem; color: #333; margin-bottom: 5px; font-weight: bold; }
.input-form { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; font-size: 0.95rem; box-sizing: border-box; font-family: inherit;}
.file-input { background: white; font-size: 0.85rem; cursor: pointer; }

.btn-generar { width: 100%; background-color: #0086c0; color: white; border: none; padding: 12px; border-radius: 6px; font-weight: bold; cursor: pointer; transition: 0.2s; margin-top: 5px; }
.btn-generar:hover:not(:disabled) { background-color: #006b99; }
.btn-generar:disabled { background-color: #a0cadd; cursor: not-allowed; }

.btn-submit { width: 100%; background-color: #012169; color: white; border: none; padding: 15px; border-radius: 8px; font-size: 1rem; font-weight: bold; cursor: pointer; transition: 0.3s; margin-top: 10px; }
.btn-submit:hover:not(.btn-desactivado) { background-color: #0056b3; transform: translateY(-2px); }
.btn-desactivado { background-color: #ccc; cursor: not-allowed; }

.btn-cerrar { margin-top: 30px; width: 100%; background: #eee; color: #555; border: none; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: bold; transition: 0.2s; }
.btn-cerrar:hover { background: #e0e0e0; color: #333; }

@media (max-width: 992px) { 
  .grid-layout { grid-template-columns: 1fr; } 
}
</style>