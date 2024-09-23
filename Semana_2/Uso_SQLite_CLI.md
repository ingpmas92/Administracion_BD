### Cómo Usar SQLite CLI

Aquí te explico cómo usar esta consola para trabajar con una base de datos SQLite persistente:

1. **Abrir una Base de Datos Existente o Crear una Nueva:**
   - Para abrir una base de datos existente o crear una nueva, usa el comando `.open` seguido del nombre del archivo de base de datos. Si el archivo no existe, SQLite lo creará.
   - Por ejemplo:
     ```sh
     .open lego.db
     ```

2. **Verificar la Base de Datos Abierta:**
   - Una vez que hayas abierto (o creado) la base de datos, puedes empezar a ejecutar comandos SQL. Puedes verificar que la base de datos está abierta ejecutando el siguiente comando para mostrar las tablas existentes:
     ```sh
     .tables
     ```

3. **Crear una Tabla:**
   - Para crear una nueva tabla, puedes usar el comando SQL estándar. Por ejemplo:
     ```sql
     CREATE TABLE bricks (
         id INTEGER PRIMARY KEY,
         color TEXT NOT NULL,
         size TEXT NOT NULL
     );
     ```

4. **Insertar Datos:**
   - Para insertar datos en la tabla, usa el comando `INSERT INTO`:
     ```sql
     INSERT INTO bricks (color, size) VALUES ('red', '2x4');
     INSERT INTO bricks (color, size) VALUES ('blue', '2x2');
     ```

5. **Consultar Datos:**
   - Para consultar los datos de la tabla, usa el comando `SELECT`:
     ```sql
     SELECT * FROM bricks;
     ```

6. **Guardar y Cerrar la Base de Datos:**
   - Los cambios se guardan automáticamente cuando cierras SQLite. Puedes salir de la consola de SQLite usando el comando `.exit` o `Ctrl+D`:
     ```sh
     .exit
     ```

### Ejemplo Paso a Paso

1. **Abre la Consola de SQLite:**
   - Ejecuta el archivo `.exe` de SQLite, lo que abre una consola interactiva.

2. **Abre (o crea) tu base de datos:**
   ```sh
   .open lego.db
   ```

3. **Crea una tabla:**
   ```sql
   CREATE TABLE bricks (
       id INTEGER PRIMARY KEY,
       color TEXT NOT NULL,
       size TEXT NOT NULL
   );
   ```

4. **Inserta algunos datos:**
   ```sql
   INSERT INTO bricks (color, size) VALUES ('red', '2x4');
   INSERT INTO bricks (color, size) VALUES ('blue', '2x2');
   ```

5. **Consulta los datos:**
   ```sql
   SELECT * FROM bricks;
   ```

6. **Cierra la consola:**
   ```sh
   .exit
   ```

### Recursos Adicionales

Si prefieres trabajar con una interfaz gráfica en lugar de la línea de comandos, considera usar **DB Browser for SQLite**, que ofrece una interfaz visual para gestionar tus bases de datos SQLite. Puedes descargarlo desde [DB Browser for SQLite](https://sqlitebrowser.org/dl/).

