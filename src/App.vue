<script setup>
import { ref } from 'vue'
import QuienesSomos from './components/QuienesSomos.vue'
import Instrumentacion from './components/Instrumentacion.vue'

const vistaActual = ref('inicio')

const irAInstrumentacion = () => { 
  vistaActual.value = 'instrumentacion'
  window.scrollTo(0, 0)
}

const volverAInicio = () => { 
  vistaActual.value = 'inicio' 
  window.scrollTo(0, 0)
}
</script>

<template>
  <div class="app-container">
    <header class="main-header">
      <div class="contenedor-cabecera">
        
        <div class="logo-area">
          <img src="./assets/logo-sio.jpg" alt="Logo SIO ICM-CSIC" class="imagen-logo" />
        </div>
        
        <nav class="menu-principal">
          <div class="selector-idiomas">
            <button class="btn-idioma">CAT</button>
            <button class="btn-idioma active">CAS</button>
            <button class="btn-idioma">ENG</button>
          </div>
          
          <div class="area-privada-wrapper">
            <button class="btn-intranet" @click="alert('Área Privada: En desarrollo')">
              👤 Área Privada
            </button>
          </div>
        </nav>
      </div>
    </header>

    <main class="main-content">
      <QuienesSomos 
        v-if="vistaActual === 'inicio'" 
        @ir-a-instrumentacion="irAInstrumentacion" 
      />
      <Instrumentacion 
        v-else-if="vistaActual === 'instrumentacion'" 
        @volver="volverAInicio" 
      />
    </main>

    <footer class="main-footer">
      <p>&copy; 2026 SIO - Instituto de Ciencias del Mar (CSIC)</p>
    </footer>
  </div>
</template>

<style>
body { margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f9; color: #333; }
.app-container { display: flex; flex-direction: column; min-height: 100vh; }
.main-content { flex: 1; padding: 40px 20px; box-sizing: border-box; width: 100%; max-width: 1200px; margin: 0 auto; }

/* AZUL BLINDADO */
.main-header {
  background-color: #005596; 
  color: white;
  padding: 15px 0;
  display: flex;
  justify-content: center;
  border-bottom: 3px solid #003366;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
.contenedor-cabecera { width: 100%; max-width: 1200px; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; }
.logo-area { display: flex; align-items: center; }
.imagen-logo { height: auto; max-height: 65px; width: auto; display: block; }
.menu-principal { display: flex; align-items: center; gap: 20px; }
.selector-idiomas { display: flex; gap: 5px; }
.btn-idioma { background: none; border: none; color: white; font-size: 0.85rem; cursor: pointer; padding: 3px 6px; border-radius: 3px; transition: background 0.2s; }
.btn-idioma:hover { background-color: rgba(255,255,255,0.1); }
.btn-idioma.active { background-color: white; color: #005596; font-weight: bold; }
.area-privada-wrapper { position: relative; }
.btn-intranet { background-color: white; color: #005596; border: none; padding: 10px 18px; border-radius: 4px; cursor: pointer; font-weight: bold; display: flex; align-items: center; gap: 5px; transition: background 0.2s; }
.btn-intranet:hover { background-color: #e2eef7; }
.main-footer { background-color: #333; color: #ccc; padding: 20px; text-align: center; font-size: 0.9rem; margin-top: auto; }
</style>