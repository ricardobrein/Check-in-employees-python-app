import locale
import sqlite3
import datetime

# Establecer el locale en español
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')

# Conexión a la base de datos
conn = sqlite3.connect('check_app.db')
c = conn.cursor()

hora_entrada = datetime.time(9, 0)   # Hora de entrada predefinida: 9:00 AM
hora_salida = datetime.time(19, 0)   # Hora de salida predefinida: 7:00 PM


# Función para registrar la entrada del empleado
def register_entradas(id_empleado, checkin_type):
    current_time = datetime.datetime.now()

    # Obtener el nombre del empleado según su ID
    c.execute("SELECT nombre, apellido FROM empleados WHERE id_empleado = ?", (id_empleado,))
    result = c.fetchone()
    if result:
        nombre, apellido = result

        # Insertar el registro en la base de datos
        c.execute("INSERT INTO registro_entradas (id_empleado, employee_name, checkin_type, checkin_time) VALUES (?, ?, ?, ?)",
                  (id_empleado, f"{nombre} {apellido}", checkin_type, current_time))
        conn.commit()
        formatted_time = current_time.strftime("%H:%M:%S, %d de %B de %Y")
        print(f"Registro de {checkin_type} exitoso para el empleado {nombre} {apellido} (ID: {id_empleado}) a las {formatted_time}")
    else:
        print(f"El ID de empleado {id_empleado} no está registrado.")


# Función para registrar la salida del empleado
def register_salidas(id_empleado, checkin_type):
    current_time = datetime.datetime.now()

    # Obtener el nombre del empleado según su ID
    c.execute("SELECT nombre, apellido FROM empleados WHERE id_empleado = ?", (id_empleado,))
    result = c.fetchone()
    if result:
        nombre, apellido = result

        # Insertar el registro en la base de datos
        c.execute("INSERT INTO registro_salidas (id_empleado, employee_name, checkin_type, checkin_time) VALUES (?, ?, ?, ?)",
                  (id_empleado, f"{nombre} {apellido}", checkin_type, current_time))
        conn.commit()
        formatted_time = current_time.strftime("%H:%M:%S, %d de %B de %Y")
        print(f"Registro de {checkin_type} exitoso para el empleado {nombre} {apellido} (ID: {id_empleado}) a las {formatted_time}")
    else:
        print(f"El ID de empleado {id_empleado} no está registrado.")


# Función para obtener los registros de los empleados que llegaron tarde o se fueron antes
def fuera_horario():
    start_time = datetime.datetime.now().replace(hour=hora_entrada.hour, minute=hora_entrada.minute, second=0)
    end_time = datetime.datetime.now().replace(hour=hora_salida.hour, minute=hora_salida.minute, second=0)

    c.execute("SELECT * FROM registro_entradas JOIN registro_salidas ON registro_entradas.id_empleado = registro_salidas.id_empleado WHERE registro_entradas.checkin_time < ? OR registro_entradas.checkin_time > ?",
              (start_time, end_time))
    records = c.fetchall()
    if records:
        print("Registros de empleados que llegaron tarde o se fueron antes:")
        for record in records:
            checkin_time = datetime.datetime.strptime(record[4], "%Y-%m-%d %H:%M:%S.%f")  # Convertir a datetime con fracción de segundos
            formatted_time = checkin_time.strftime("%H:%M, %d de %B de %Y")  # Formato sin segundos
            print(f"ID: {record[1]}, Nombre: {record[2]}, Tipo: {record[3]}, Hora: {formatted_time}")
    else:
        print("No se encontraron registros de empleados que llegaron tarde o se fueron antes.")


# Función para agregar un nuevo empleado
def agregar_empleado(id_empleado, nombre, apellido):
    try:
        # Insertar el empleado en la tabla
        c.execute("INSERT INTO empleados (id_empleado, nombre, apellido) VALUES (?, ?, ?)",
                  (id_empleado, nombre, apellido))
        conn.commit()
        print("Empleado agregado exitosamente.")
    except sqlite3.IntegrityError:
        print("El ID de empleado ya existe en la tabla. No se pudo agregar el empleado.")


# Interfaz de usuario
while True:
    print("1. Registrar Entrada")
    print("2. Registrar Salida")
    print("3. Obtener Registros Anteriores")
    print("4. Agregar un Nuevo Empleado")
    print("5. Salir")
    choice = input("Seleccione una opción: ")

    if choice == '1':
        id_empleado = input("Ingrese el ID del empleado: ")
        register_entradas(id_empleado, 'Entrada')
    elif choice == '2':
        id_empleado = input("Ingrese el ID del empleado: ")
        register_salidas(id_empleado, 'Salida')
    elif choice == '3':
        fuera_horario()
    elif choice == '4':
        id_empleado = input('Ingrese el ID del empleado: ')
        nombre = input('Ingrese el nombre del nuevo empleado: ')
        apellido = input('Ingrese el apellido: ')
        agregar_empleado(id_empleado, nombre, apellido)
    elif choice == '5':
        break
    else:
        print("Opción inválida. Intente nuevamente.")

# Cerrar la conexión a la base de datos
conn.close()