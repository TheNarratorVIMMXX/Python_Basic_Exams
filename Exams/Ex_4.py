# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

""" Examen 4B: Control de Ejercicio Semanal """

# NOTE: Fecha de Realización: 27/10/2025
# NOTE: Autor: Magallanes López Carlos Gabriel
# NOTE: Correo: cgmagallanes23@gmail.com

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Redacción de Examen ============================================================= """

"""

- Descripción:
    
    Estás llevando un Registro de tu Rutina de Ejercicio Semanal. El Programa debe permitir al Usuario 
    Registrar exactamente 3 Sesiones de Ejercicio Diferentes. Por cada Sesión deberás Registrar: el Tipo 
    de Ejercicio (Cardio, Fuerza o Resistencia), los Minutos de Duración y las Calorías Quemadas Aproximadas. 
    Después de Registrar las 3 Sesiones se mostrará el Total de Minutos Ejercitados, el Total de Calorías 
    Quemadas y el Promedio de Calorías por Sesión.
	
- Requerimientos:
    
    - Usar una Función sin Retorno para Mostrar el Resumen Final de Ejercicio (Total de Minutos, 
      Total de Calorías y Promedio de Calorías por Sesión), recuerda Redondear a 2 Decimales el Promedio
    - Usar Bucle While para el Registro de las 3 Sesiones de Ejercicio
    - La Función debe Imprimir el Mensaje con F-String del Resumen Completo
    - Debe haber Validaciones para Rangos de los Datos, si no se cumple con la Validación volver a pedir la Entrada del Dato:
        
        - Los Minutos de Duración deben ser Mayor a 0
        - Las Calorías Quemadas deben ser Mayor a 0
        - El Tipo de Ejercicio debe ser solamente: Cardio, Fuerza o Resistencia
"""

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Posible Solución de Examen ============================================================= """

# Contadores
sum_minutes = 0           # Sumatoria para el Total de Minutos
sum_calories = 0          # Sumatoria para el Total de Calorías
count_sessions = 0        # Contador de Sesiones Registradas

# Función para Mostrar el Resumen de Ejercicio (Sin Retorno)
def show_exercise_summary(total_minutes: int, total_calories: int | float, total_sessions: int):
    avg_calories = total_calories / total_sessions
    print("\n========== RESUMEN DE EJERCICIO SEMANAL ==========")
    print(f"Total de Minutos Ejercitados: {total_minutes} minutos")
    print(f"Total de Calorías Quemadas: {round(total_calories, 2)} kcal")
    print(f"Promedio de Calorías por Sesión: {round(avg_calories, 2)} kcal")
    print(f"Cantidad de Sesiones Registradas: {total_sessions}")
    print("==================================================\n")

# Bucle Principal
while count_sessions < 3:

    # Lectura de Datos
    print(f"\n--- Sesión de Ejercicio {count_sessions + 1} ---")
    exercise_type = input("Ingresa el Tipo de Ejercicio (Cardio/Fuerza/Resistencia): ")                    # Tipo de Ejercicio
    while exercise_type != "Cardio" and exercise_type != "Fuerza" and exercise_type != "Resistencia":      # Validación Tipo
        print("ERROR. El Tipo de Ejercicio debe ser: Cardio, Fuerza o Resistencia")
        exercise_type = input("Ingresa el Tipo de Ejercicio (Cardio/Fuerza/Resistencia): ")
    
    minutes = int(input("Ingresa los Minutos de Duración: "))                                               # Minutos de Duración
    while minutes <= 0:                                                                                     # Validación Minutos
        print("ERROR. Los Minutos deben ser Mayor a 0")
        minutes = int(input("Ingresa los Minutos de Duración: "))
    
    calories = float(input("Ingresa las Calorías Quemadas Aproximadas: "))                                  # Calorías Quemadas
    while calories <= 0:                                                                                    # Validación Calorías
        print("ERROR. Las Calorías deben ser Mayor a 0")
        calories = float(input("Ingresa las Calorías Quemadas Aproximadas: "))

    # Actualización de Contadores
    sum_minutes += minutes          # Total de Minutos
    sum_calories += calories        # Total de Calorías
    count_sessions += 1             # Contador de Sesiones

# Llamada a la Función para Mostrar el Resumen
show_exercise_summary(sum_minutes, sum_calories, count_sessions)

# -----------------------------------------------------------------------------------------------------------------------------------------