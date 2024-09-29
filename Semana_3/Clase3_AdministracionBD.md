## Sistemas Gestores de Bases de Datos (SGBD)🗄️💻

En esta clase, el profesor introduce los **Sistemas Gestores de Bases de Datos (SGBD)**, tanto tradicionales como en la nube. Se enfoca en las ventajas de la nube, comparando AWS (Amazon Web Services) y Azure (Microsoft).

Se destaca la importancia de las certificaciones en la nube y se anima a los estudiantes a explorar las opciones gratuitas de AWS y Azure para practicar. La actividad de la semana consiste en comparar AWS y Azure, respondiendo a preguntas específicas sobre sus características y beneficios.

---

## Temas Tratados en la Clase 📑

**1. Sistemas Gestores de Bases de Datos (SGBD) 🗃️**

* **Definición:** Software para crear, manejar y acceder a una base de datos.
* **Componentes:**
  * **Lenguaje de Definición de Datos (DDL):** Define la estructura de la base de datos (tablas, columnas, relaciones).
  * **Lenguaje de Manipulación de Datos (DML):** Permite acceder, insertar, modificar y eliminar datos.
* **Tipos:**
  * **Relacionales (SQL):** Datos estructurados en tablas con filas y columnas. Ejemplos: MySQL, PostgreSQL, SQL Server.
  * **No relacionales (NoSQL):**  Datos no estructurados o semi-estructurados. Ejemplos: MongoDB, Cassandra, Redis.

**2.  Centros de Datos Tradicionales 🏢 vs.  Nube ☁️**

* **Centros de Datos Tradicionales:** Infraestructura física propia de la empresa.

  * **Desventajas:** Costosos (implementación, administración, mantenimiento), difíciles de predecir la demanda, alcances limitados.
* **Computación en la Nube:** Servicios de almacenamiento y procesamiento a través de Internet.

  * **Proveedores:** AWS (Amazon), Azure (Microsoft), Google Cloud Platform (GCP).
  * **Ventajas:** Reducción de costos, escalabilidad, flexibilidad, seguridad, mantenimiento simplificado.

**3. Microsoft Azure  💙**

* **Definición:** Plataforma en la nube de Microsoft con más de 200 servicios, incluyendo máquinas virtuales, almacenamiento, bases de datos, redes, IA y desarrollo de aplicaciones.
* **Ventajas:**  Amplia gama de servicios, altos estándares de seguridad,  integración con el ecosistema Microsoft,  opciones de trabajo híbrido (nube y local).
* **Desventajas:**  Menor adopción que AWS, complejidad para nuevos usuarios,  costos potencialmente menos transparentes.

**4. Amazon Web Services (AWS) 🧡**

* **Definición:**  Plataforma en la nube de Amazon con la mayor cantidad de servicios y la mayor base de clientes.
* **Ventajas:** Amplio ecosistema,  madurez, escalabilidad,  innovación constante,  amplia red global de centros de datos.
* **Desventajas:**  Curva de aprendizaje pronunciada,  costos potencialmente elevados si no se gestionan adecuadamente.

**5. Ejemplos de Servicios de AWS y Azure  🧰**

* **AWS:** EC2 (máquinas virtuales), S3 (almacenamiento), RDS (bases de datos relacionales), Lambda (ejecución de código), DynamoDB (bases de datos NoSQL), CloudFront (red de entrega de contenido).
* **Azure:**  Virtual Machines, Azure Storage, Azure SQL Database, Azure Cosmos DB, Azure Virtual Network, Azure Machine Learning.

---

## Ejercicios Prácticos  🏋️‍♀️

**1. Crear una base de datos MySQL en AWS RDS:**

1. **Crear una cuenta de AWS:**  Sigue las instrucciones en [https://aws.amazon.com/](https://aws.amazon.com/). Aprovecha el nivel gratuito.
2. **Accede a la consola de RDS:** Busca "RDS" en la barra de búsqueda y selecciónalo.
3. **Crea una instancia de base de datos:**
   * Elige el motor de base de datos:  MySQL.
   * Selecciona la plantilla:  "Producción" o "Gratis".
   * Configura la instancia: Nombre, usuario administrador, contraseña, tipo de instancia, almacenamiento.
4. **Conéctate a tu base de datos:** Utiliza un cliente MySQL como MySQL Workbench.
5. **Crea una tabla:**
   ```sql
   CREATE TABLE Productos (
       ID INT PRIMARY KEY AUTO_INCREMENT,
       Nombre VARCHAR(255) NOT NULL,
       Precio DECIMAL(10,2) NOT NULL
   );
   ```

**2. Crear una instancia de máquina virtual con Azure:**

1. **Crear una cuenta de Azure:** Visita [https://azure.microsoft.com/es-es/free/](https://azure.microsoft.com/es-es/free/).
2. **Accede al portal de Azure:** Inicia sesión con tu cuenta.
3. **Crea una máquina virtual:**
   * Haz clic en "Crear un recurso"  > "Compute" > "Máquina virtual".
   * Elige una imagen:  Windows Server o Linux.
   * Selecciona un tamaño de máquina virtual.
   * Configura la máquina virtual: Nombre de usuario, contraseña, grupo de recursos.
4. **Conéctate a tu máquina virtual:** Utiliza una herramienta de conexión remota como Escritorio remoto (para Windows) o SSH (para Linux).

---

## Recursos Adicionales 📚

* **Documentación de Microsoft Azure:** [https://docs.microsoft.com/es-es/azure/?product=featured](https://docs.microsoft.com/es-es/azure/?product=featured)
* **Documentación de Amazon Web Services:** [https://docs.aws.amazon.com/?nc2=h_ql_doc_do](https://docs.aws.amazon.com/?nc2=h_ql_doc_do)
* **Tutoriales de AWS:** [https://aws.amazon.com/es/getting-started/](https://aws.amazon.com/es/getting-started/)
* **Tutoriales de Azure:** [https://docs.microsoft.com/es-es/learn/browse/?products=azure](https://docs.microsoft.com/es-es/learn/browse/?products=azure)

**Consejos Finales 🎉**

* **Experimenta:** La mejor forma de aprender es usando las plataformas. Aprovecha las opciones gratuitas.
* **Certificaciones:**  Una certificación en AWS o Azure puede impulsar tu carrera.
* **Mantente actualizado:**  La tecnología en la nube evoluciona rápidamente.

¡Espero que esta guía te ayude a dominar la administración de bases de datos en la nube! 🚀
