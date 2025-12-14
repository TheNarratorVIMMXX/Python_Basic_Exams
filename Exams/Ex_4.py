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
""" ======================================================== Módulos Importados ============================================================= """

# Dependencias
from typing import Union                                                                                   # Tipos de Datos Avanzados

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Posible Solución de Examen ============================================================= """

# Función: Mostrar el Resumen de Ejercicio 
def show_exercise_summary(total_minutes: int, total_calories: Union[int, float], total_sessions: int) -> None:
    
    """
        - Función: Mostrar el Resumen de Ejercicio
        - Argumentos:
            - total_minutes (int): Total de Minutos Ejercitados
            - total_calories (Union[int, float]): Total de Calorías Quemadas
            - total_sessions (int): Cantidad de Sesiones Registradas
        - Retorno: Ninguno
        - Objetivo: Mostrar el Resumen de Información del Ejercicio
    """

    # Mostrar Resumen de Ejercicio
    print("\n========== RESUMEN DE EJERCICIO SEMANAL ==========")                                                # Título Resumen
    print(f"Total de Minutos Ejercitados: {total_minutes} minutos")                                              # Total de Minutos
    print(f"Total de Calorías Quemadas: {round(total_calories, 2)} kcal")                                        # Total de Calorías
    print(f"Promedio de Calorías por Sesión: {round(total_calories / total_sessions, 2)} kcal")                  # Promedio de Calorías por Sesión
    print(f"Cantidad de Sesiones Registradas: {total_sessions}")                                                 # Cantidad de Sesiones
    print("==================================================\n")                                                # Línea Final Resumen




# Contadores
sum_minutes = 0                                                                                                  # Sumatoria para el Total de Minutos
sum_calories = 0                                                                                                 # Sumatoria para el Total de Calorías
count_sessions = 0                                                                                               # Contador de Sesiones Registradas


# Bucle Principal
while count_sessions < 3:

    # Lectura de Datos
    print(f"\n--- Sesión de Ejercicio {count_sessions + 1} ---")
    exercise_type = input("Ingresa el Tipo de Ejercicio (Cardio/Fuerza/Resistencia): ")                          # Tipo de Ejercicio
    while exercise_type != "Cardio" and exercise_type != "Fuerza" and exercise_type != "Resistencia":            # Validación Tipo
        print("ERROR. El Tipo de Ejercicio debe ser: Cardio, Fuerza o Resistencia")
        exercise_type = input("Ingresa el Tipo de Ejercicio (Cardio/Fuerza/Resistencia): ")
    
    minutes = int(input("Ingresa los Minutos de Duración: "))                                                    # Minutos de Duración
    while minutes <= 0:                                                                                          # Validación Minutos
        print("ERROR. Los Minutos deben ser Mayor a 0")
        minutes = int(input("Ingresa los Minutos de Duración: "))
    
    calories = float(input("Ingresa las Calorías Quemadas Aproximadas: "))                                       # Calorías Quemadas
    while calories <= 0:                                                                                         # Validación Calorías
        print("ERROR. Las Calorías deben ser Mayor a 0")
        calories = float(input("Ingresa las Calorías Quemadas Aproximadas: "))

    # Actualización de Contadores
    sum_minutes += minutes                                                                                       # Total de Minutos
    sum_calories += calories                                                                                     # Total de Calorías
    count_sessions += 1                                                                                          # Contador de Sesiones


# Llamada a la Función para Mostrar el Resumen
show_exercise_summary(sum_minutes, sum_calories, count_sessions)

# -----------------------------------------------------------------------------------------------------------------------------------------