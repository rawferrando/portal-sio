from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
# Esto permite que tu web en Vue se conecte sin problemas de seguridad
CORS(app)

# Función para conectarnos a la base de datos
def conectar_bd():
    conexion = sqlite3.connect('sio_inventario.db')
    conexion.row_factory = sqlite3.Row 
    return conexion

# Ruta principal: GET para leer, POST para escribir
@app.route('/api/instrumentos', methods=['GET', 'POST'])
def gestionar_instrumentos():
    
    # Si la web pide LEER los instrumentos
    if request.method == 'GET':
        try:
            conexion = conectar_bd()
            instrumentos = conexion.execute('SELECT * FROM instrumentos').fetchall()
            conexion.close()
            lista_instrumentos = [dict(fila) for fila in instrumentos]
            return jsonify(lista_instrumentos)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Si la web pide GUARDAR un instrumento nuevo
    if request.method == 'POST':
        try:
            nuevo_equipo = request.json
            
            conexion = conectar_bd()
            cursor = conexion.cursor()
            
            cursor.execute('''
                INSERT INTO instrumentos 
                (categoria, subcategoria, nombre, marca, estado, ultima_calibracion, descripcion, parametros_tecnicos, numero_serie)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                nuevo_equipo.get('categoria', 'Física'),
                nuevo_equipo.get('subcategoria', 'General'),
                nuevo_equipo.get('nombre', 'Sense Nom'),
                nuevo_equipo.get('marca', ''),
                nuevo_equipo.get('estado', 'Disponible'),
                nuevo_equipo.get('ultima_calibracion', ''),
                nuevo_equipo.get('descripcion', ''),
                nuevo_equipo.get('parametros_tecnicos', ''),
                nuevo_equipo.get('numero_serie', '')
            ))
            
            conexion.commit()
            conexion.close()
            
            return jsonify({"mensaje": "Equip desat correctament al SIO!"}), 201
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500


# Ruta para modificar: PUT para editar, DELETE para borrar
@app.route('/api/instrumentos/<int:id>', methods=['PUT', 'DELETE', 'OPTIONS'])
def modificar_instrumento(id):
    
    # Si es una petición OPTIONS (Preflight de CORS), respondemos OK
    if request.method == 'OPTIONS':
        return '', 200

    # Si la web pide ELIMINAR
    if request.method == 'DELETE':
        conn = sqlite3.connect('sio_inventario.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM instrumentos WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return '', 204

    # Si la web pide ACTUALIZAR / EDITAR
    if request.method == 'PUT':
        try:
            datos = request.json
            conn = sqlite3.connect('sio_inventario.db')
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE instrumentos 
                SET nombre = ?, marca = ?, categoria = ?, subcategoria = ?, 
                    ultima_calibracion = ?, descripcion = ?, parametros_tecnicos = ?, numero_serie = ?
                WHERE id = ?
            ''', (
                datos.get('nombre'), 
                datos.get('marca'), 
                datos.get('categoria'), 
                datos.get('subcategoria'), 
                datos.get('ultima_calibracion'), 
                datos.get('descripcion'), 
                datos.get('parametros_tecnicos'),
                datos.get('numero_serie'), 
                id
            ))
            
            conn.commit()
            conn.close()
            return jsonify({'mensaje': 'Instrumento actualizado correctamente'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("🚀 Arrancando el motor del SIO en http://localhost:5000 ...")
    app.run(debug=True, port=5000)