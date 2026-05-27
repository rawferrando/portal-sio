<script setup>
import { ref } from 'vue'

const emit = defineEmits(['cambiar-pagina'])

// Lógica para el calendario
const diasSeleccionados = ref([])

// Simulamos algunos días ocupados para que se vea el calendario funcionando
const esOcupado = (dia) => {
  return [2, 5, 14, 15, 22].includes(dia) 
}

const toggleDia = (dia) => {
  if (esOcupado(dia)) return
  const index = diasSeleccionados.value.indexOf(dia)
  if (index > -1) {
    diasSeleccionados.value.splice(index, 1)
  } else {
    diasSeleccionados.value.push(dia)
  }
}
</script>

<template>
  <div class="servicios-hub">
    
    <div class="hero-bg-tanques" style="background: var(--icm-navy); padding: 60px 0; color: white;">
      <div class="contenedor-ancho">
        <button @click="emit('cambiar-pagina', 'servicios')" class="btn-volver" style="background: transparent; color: white; border: 1px solid white; padding: 5px 15px; border-radius: 4px; cursor: pointer; margin-bottom: 20px;">
          ⬅ Volver a Servicios
        </button>
        <h1 style="font-size: 2.5rem; margin-bottom: 10px; border-bottom: 4px solid var(--icm-blue); display: inline-block; padding-bottom: 5px;">Tanques de Pruebas</h1>
        <p style="font-size: 1.2rem; opacity: 0.9;">Instalaciones experimentales para ensayos controlados, calibración y biología.</p>
      </div>
    </div>

    <div class="contenido-hub contenedor-ancho" style="margin-top: 40px; margin-bottom: 60px;">
      <div class="grid-layout" style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
        
        <div class="seccion-bloque ficha-wiki" style="background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
          <h2 style="color: var(--icm-navy); border-bottom: 2px solid var(--icm-blue); padding-bottom: 10px;">Ficha Técnica</h2>
          
          <div class="caja-desc" style="margin-top: 20px;">
            <h3 style="color: var(--icm-blue);">Descripción General</h3>
            <p style="line-height: 1.6; color: #444;">
              El SIO dispone de tanques de pruebas de alta capacidad diseñados para la calibración de sensores, ensayos de fatiga de materiales y simulaciones de condiciones marinas controladas.
            </p>
            
            <h3 style="color: var(--icm-blue); margin-top: 25px;">Especificaciones Principales</h3>
            <ul style="line-height: 1.8; color: #444;">
              <li><strong>Volumen total:</strong> [Añadir litros/m3]</li>
              <li><strong>Control de Temperatura:</strong> Rango de [X] ºC a [Y] ºC</li>
              <li><strong>Control de Salinidad:</strong> Sistema automatizado</li>
              <li><strong>Iluminación:</strong> Espectro regulable para fotosíntesis</li>
              <li><strong>Filtración:</strong> Filtros UV y biológicos integrados</li>
            </ul>
          </div>
        </div>

        <div class="seccion-bloque ficha-gestion" style="background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 2px solid #eef2f5;">
          
          <div class="cabecera-estado" style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; padding-bottom: 15px; margin-bottom: 20px;">
            <h2 class="titulo-fija" style="margin: 0; color: var(--icm-navy);">Solicitud de Uso</h2>
            <span class="badge-grande disponible" style="background: #e6f4ea; color: #1e8e3e; padding: 5px 12px; border-radius: 20px; font-weight: bold; font-size: 0.9rem;">OPERATIVA</span>
          </div>

          <p style="font-size: 0.9rem; color: #666; margin-bottom: 10px; font-weight: bold;">Paso 1: Descarga la normativa de los tanques.</p>
          
          <div class="descarga-box-pequena" style="background: #f8f9fa; border: 1px dashed #ccc; padding: 15px; text-align: center; border-radius: 6px; margin-bottom: 30px;">
            <span style="display: block; margin-bottom: 10px;">📄 Normativa_Tanques.pdf</span>
            <a href="Normativa_Tanques.pdf" download="Normativa_Tanques.pdf" class="link-dl-mini" style="background: var(--icm-blue); color: white; padding: 8px 15px; text-decoration: none; border-radius: 4px; display: inline-block;">
              ⬇ Descargar Normativa
            </a>
          </div>

          <div class="calendario-mini">
            <h3 class="titulo-mini" style="font-size: 1rem; color: var(--icm-navy); margin-bottom: 15px;">Paso 2: Selecciona los días de uso</h3>
            
            <div class="grid-dias" style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 5px; text-align: center;">
              <div 
                v-for="n in 31" 
                :key="n"
                @click="toggleDia(n)"
                :class="['dia', { ocupado: esOcupado(n), seleccionado: diasSeleccionados.includes(n), disponible: !esOcupado(n) }]"
                style="padding: 10px 0; border-radius: 4px; font-size: 0.9rem; cursor: pointer; transition: all 0.2s;"
                :style="esOcupado(n) ? 'background: #ffebee; color: #c62828; cursor: not-allowed;' : (diasSeleccionados.includes(n) ? 'background: var(--icm-blue); color: white;' : 'background: #f1f3f4; color: #333;')"
              >
                {{ n }}
              </div>
            </div>
            
            <button v-if="diasSeleccionados.length > 0" style="width: 100%; margin-top: 20px; background: var(--icm-navy); color: white; border: none; padding: 12px; border-radius: 4px; cursor: pointer; font-weight: bold;">
              Solicitar {{ diasSeleccionados.length }} días seleccionados
            </button>

          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped>
/* Los estilos heredan de App.vue, pero por si necesitas ajustes específicos para los tanques, puedes ponerlos aquí */
@media (max-width: 768px) {
  .grid-layout {
    grid-template-columns: 1fr !important;
  }
}
</style>