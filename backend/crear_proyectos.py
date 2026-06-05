import sqlite3

def crear_tabla():
    # Nos conectamos a la misma base de datos que ya tienes
    conn = sqlite3.connect('sio_inventario.db')
    cursor = conn.cursor()

    # Creamos la tabla 'proyectos'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS proyectos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        categoria TEXT,
        estado TEXT,
        descripcion TEXT,
        investigador_principal TEXT,
        wiki_url TEXT,
        fecha_fin DATE,
        es_publico BOOLEAN DEFAULT 1
    )
    ''')

    # Vamos a inyectar un par de proyectos de prueba de tu captura para que haya datos
    cursor.execute('''
        INSERT INTO proyectos (titulo, categoria, estado, descripcion, investigador_principal) 
        VALUES ('PROTEO', 'Divulgación Científica', 'Solicitado', 'Desarrollo de sistema hardware open-source para extracción y monitorización de oxígeno.', 'Raül Ferrando')
    ''')
    cursor.execute('''
        INSERT INTO proyectos (titulo, categoria, estado, descripcion) 
        VALUES ('ALBARANES', 'Infraestructura', 'En Curso', 'Gestión de infraestructura y recursos técnicos marinos.')
    ''')

    conn.commit()
    conn.close()
    print("✅ ¡Tabla 'proyectos' creada y rellenada con datos de prueba!")

if __name__ == '__main__':
    crear_tabla()