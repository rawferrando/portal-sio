import sqlite3

try:
    conn = sqlite3.connect('sio_inventario.db')
    # Añadimos la columna nueva a la tabla existente
    conn.execute('ALTER TABLE instrumentos ADD COLUMN numero_serie TEXT DEFAULT ""')
    conn.commit()
    conn.close()
    print("✅ Columna 'numero_serie' añadida correctamente a la base de datos.")
except Exception as e:
    print(f"Error (quizás ya la habías añadido): {e}")