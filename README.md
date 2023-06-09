# Check-in-python-app

### Esta es una app de python sencilla que se conecta a una base de datos SQLite y permite registar la entrada y salida de los empleados.

Motivación: Practicar deliberada de Python y la conexión a bases SQL.

En el cuaderno de jupyter teneos la creacion de la Base de datos y las tablas, cree 3 tablas para insertar los registros de entrada y salida de los empleados. Además cree 20 registros ficticios para relaizar pruebas.

## Explicando un poco el código de la App

Importar modulos necesarios (Sqlite3, datetime, locale)
Nos conectamos a la base de datos e intanciamos un cursor.

Antes que nada, he puesto un locale de hora para presentar las horas de los registros en el formato español, luego nos conectamos a la base de datos SQLite para empezar a crear funciones que interactuen con ella.
**Funciones**
1. Una Primera función escribir registros de entrada del empleado, introduciendo solo el ID del cliente.
2. La segunda es para registrar la salida de la misma manera.
3. La siguiente obtiene los registros de empleados que llegaron despues de la hora predefinida en las **variables globales** de entrada y salida de la empresa.
4. Por supuesto teniamos que crear una funcion para agregar un nuevo empleado que te solicitara el ID que desees asignarle, Nombre y apellido.

Por ultimo tenemos nuestra funcion main que es un bucle para invocar cualquiera de las funciones anteriores.


### Gracias por leer :) 
