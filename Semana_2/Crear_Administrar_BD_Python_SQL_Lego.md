### Paso a Paso para Crear y Administrar una Base de Datos de Juguetes LEGO

#### 1. **Crear la Base de Datos**

Primero, creamos la base de datos y la tabla `juguetes_lego`, que contendrá la información de los juguetes de LEGO. Usaremos Python y SQLite, como en el ejemplo anterior:

```python
import sqlite3

# Conectar a la base de datos (crea la base de datos si no existe)
conn = sqlite3.connect('lego_toys.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla de juguetes LEGO
cursor.execute('''
CREATE TABLE IF NOT EXISTS juguetes_lego (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL
)
''')

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Base de datos y tabla 'juguetes_lego' creada exitosamente.")
```

#### Explicación:
1. **Tabla `juguetes_lego`**: Creamos una tabla con las siguientes columnas:
   - `id`: Identificador único para cada juguete (llave primaria).
   - `nombre`: El nombre del juguete de LEGO (ej. "Millennium Falcon").
   - `tipo`: El tipo de juguete, como **"Star Wars"**, **"Harry Potter"**, etc.
   - `cantidad`: La cantidad disponible en el inventario.
   - `precio`: El precio del juguete.

#### 2. **Insertar Datos en la Base de Datos**

Vamos a insertar algunos juguetes LEGO en la base de datos.

```python
# Conectar a la base de datos
conn = sqlite3.connect('lego_toys.db')
cursor = conn.cursor()

# Insertar algunos juguetes LEGO
cursor.execute("INSERT INTO juguetes_lego (nombre, tipo, cantidad, precio) VALUES (?, ?, ?, ?)", ('Millennium Falcon', 'Star Wars', 5, 159.99))
cursor.execute("INSERT INTO juguetes_lego (nombre, tipo, cantidad, precio) VALUES (?, ?, ?, ?)", ('Hogwarts Castle', 'Harry Potter', 3, 129.99))
cursor.execute("INSERT INTO juguetes_lego (nombre, tipo, cantidad, precio) VALUES (?, ?, ?, ?)", ('Bugatti Chiron', 'Technic', 2, 349.99))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Juguetes LEGO insertados correctamente.")
```

#### Explicación:
1. Hemos insertado tres juguetes LEGO con sus nombres, tipo (tema), cantidad y precio.
   - **Millennium Falcon** de la serie **Star Wars**.
   - **Hogwarts Castle** de **Harry Potter**.
   - **Bugatti Chiron** de **Technic**.

#### 3. **Consultar Datos desde la Base de Datos**

Ahora vamos a consultar los datos que acabamos de insertar.

```python
# Conectar a la base de datos
conn = sqlite3.connect('lego_toys.db')
cursor = conn.cursor()

# Seleccionar todos los juguetes LEGO
cursor.execute("SELECT * FROM juguetes_lego")

# Obtener y mostrar todos los registros
juguetes = cursor.fetchall()

for juguete in juguetes:
    print(juguete)

# Cerrar la conexión
conn.close()
```

#### Explicación:
1. Seleccionamos todos los juguetes LEGO usando `SELECT * FROM juguetes_lego`.
2. Imprimimos cada juguete de la base de datos.

#### 4. **Actualizar Datos en la Base de Datos**

Imagina que se vende un **Millennium Falcon**, por lo que debemos reducir la cantidad disponible. Aquí te muestro cómo actualizar la cantidad de un juguete.

```python
# Conectar a la base de datos
conn = sqlite3.connect('lego_toys.db')
cursor = conn.cursor()

# Actualizar la cantidad de Millennium Falcon
cursor.execute("UPDATE juguetes_lego SET cantidad = ? WHERE nombre = ?", (4, 'Millennium Falcon'))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Cantidad de Millennium Falcon actualizada.")
```

#### Explicación:
1. Usamos el comando `UPDATE` para modificar la cantidad de **Millennium Falcon** a 4, ya que se ha vendido uno.

#### 5. **Eliminar Datos de la Base de Datos**

Ahora, vamos a eliminar un juguete de la base de datos. Supongamos que ya no tenemos más unidades del **Bugatti Chiron** y lo eliminamos del inventario.

```python
# Conectar a la base de datos
conn = sqlite3.connect('lego_toys.db')
cursor = conn.cursor()

# Eliminar el Bugatti Chiron
cursor.execute("DELETE FROM juguetes_lego WHERE nombre = ?", ('Bugatti Chiron',))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Bugatti Chiron eliminado.")
```

#### Explicación:
1. Usamos `DELETE` para eliminar el juguete **Bugatti Chiron** de la base de datos, ya que no tenemos más unidades en el inventario.

#### 6. **Funciones Adicionales: Consultas y Reportes**

Como parte de la administración de una base de datos de juguetes LEGO, es probable que quieras obtener información más específica, como el juguete más caro o el total de juguetes en inventario. Vamos a hacer un par de consultas más avanzadas:

##### a) **Obtener el juguete más caro:**

```python
# Conectar a la base de datos
conn = sqlite3.connect('lego_toys.db')
cursor = conn.cursor()

# Seleccionar el juguete más caro
cursor.execute("SELECT nombre, precio FROM juguetes_lego ORDER BY precio DESC LIMIT 1")

# Obtener el resultado
juguete_mas_caro = cursor.fetchone()
print(f"El juguete más caro es: {juguete_mas_caro[0]} con un precio de ${juguete_mas_caro[1]}")

# Cerrar la conexión
conn.close()
```

##### b) **Obtener el total de unidades en inventario:**

```python
# Conectar a la base de datos
conn = sqlite3.connect('lego_toys.db')
cursor = conn.cursor()

# Calcular el total de unidades en inventario
cursor.execute("SELECT SUM(cantidad) FROM juguetes_lego")

# Obtener el resultado
total_unidades = cursor.fetchone()[0]
print(f"El total de unidades en inventario es: {total_unidades}")

# Cerrar la conexión
conn.close()
```

#### Explicación:
1. En la primera consulta, usamos `ORDER BY precio DESC` para ordenar por precio de mayor a menor, y `LIMIT 1` para obtener solo el juguete más caro.
2. En la segunda consulta, usamos `SUM(cantidad)` para sumar todas las cantidades de los juguetes y obtener el total de unidades en inventario.

### Conclusión:
Este ejemplo adapta la creación y administración de una base de datos al tema de **juguetes LEGO**. Puedes seguir añadiendo funcionalidades, como categorías de productos, proveedores, o realizar consultas más avanzadas para generar reportes de inventario, ventas, etc. ¡Este es solo el punto de partida para una base de datos más completa!