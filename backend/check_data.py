import sqlite3

def check():
    try:
        conn = sqlite3.connect('sio_inventario.db')
        cursor = conn.cursor()
        
        # Comprovem instruments
        cursor.execute("SELECT count(*) FROM instrumentos")
        num_inst = cursor.fetchone()[0]
        
        # Comprovem projectes
        cursor.execute("SELECT count(*) FROM proyectos")
        num_proj = cursor.fetchone()[0]
        
        print(f"--- RESULTAT DE LA BASE DE DADES ---")
        print(f"Instruments trobats: {num_inst}")
        print(f"Projectes trobats: {num_proj}")
        conn.close()
    except Exception as e:
        print(f"Error llegint la base de dades: {e}")

check()