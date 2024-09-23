import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('lego.db')
cursor = conn.cursor()

# Crear la tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS bricks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT NOT NULL,
    size TEXT NOT NULL
)
''')

# Insertar datos
cursor.execute('INSERT INTO bricks (color, size) VALUES (?, ?)', ('red', '2x4'))
cursor.execute('INSERT INTO bricks (color, size) VALUES (?, ?)', ('blue', '2x2'))
cursor.execute('INSERT INTO bricks (color, size) VALUES (?, ?)', ('green', '1x2'))

# Consultar datos
cursor.execute('SELECT * FROM bricks')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Cerrar la conexión
conn.commit()
conn.close()