# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

""" Examen 1: Rifa Benéfica Escuela """

# NOTE: Fecha de Realización: 22/10/2025
# NOTE: Autor: Magallanes López Carlos Gabriel
# NOTE: Correo: cgmagallanes23@gmail.com

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Redacción de Examen ============================================================= """

"""

- Descripción:
    
	Imagina que organizas una Rifa Benéfica para una Escuela. Tienes una Lista de 5 Participantes y 1 Premio. 
	Debes seleccionar un Ganador Aleatorio, le pedirás un Número del 1 - 10 al Participante (Número de Rifa) y generarás un número al Azar, 
	si el Número de Rifa del Participante es igual que el Aleatorio ganará el Premio de la Rifa. Solo puede haber un Ganador del Premio.
	Para competir los Estudiantes deben de tener un Promedio Mayor o Igual 9 Total en las 3 Materias de Lengua y Comunicación, Matemáticas y Ecología. 

	
- Requerimientos:
    
	- Pedir al Participante su Nombre
	- Usar Bucle While y la Sentencia Break para Determinar el Participante Ganador
    - Los Rangos de para la Entrada de la Calificación deben de ser del 1 - 10, si no cumple con la condición volver pedir la Calificación
    - El Rango del Número de Rifa debe de ser del 1 - 10, si no cumple volver a pedir el el Número de Rifa
    - Imprimir un Mensaje en donde venga el Nombre del Ganador y una Felicitación con Concatenación de C (%)
	- Si no hay ningún Ganador mostrar un Mensaje que diga "Ningún Participante ganó la Rifa" 
"""

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

# Dependencias
import random                                                                                  # Módulo de Funciones de Aleatoriedad

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Posible Solución de Examen ============================================================= """

# Contadores
i = 0                                                                                          # Variable de Control para el Bucle
lost = 0                                                                                       # Contador de Participaciones que no ganaron Premio


# Bucle Principal 
while i < 5:
    
    # Entrada de Datos del Usuario
    name = input("Ingresa el Nombre del Participante: ")                                       # Nombre
    calif_math = int(input("Ingresa tu Calificación en Matemáticas: "))                        # Calificación de Matemáticas
    while calif_math < 1 or calif_math > 10:                                                   # Validación Rango 1 - 10
        print("ERROR. El Rango de Calificación es del 1 - 10")
        calif_math = int(input("Ingresa tu Calificación en Matemáticas: "))  
    calif_spanish = (int(input("Ingresa tu Calificación en Lengua y Comunicación: ")))         # Califcación de Lengua y Comunicacióm
    while calif_spanish < 1 or calif_spanish > 10:                                             # Validación Rango 1 - 10
        print("ERROR. El Rango de Calificación es del 1 - 10")
        calif_spanish = (int(input("Ingresa tu Calificación en Lengua y Comunicación: ")))         
    calif_ecology = int(input("Ingresa tu Calificación en Ecología: "))                        # Califcicaión Ecología 
    while calif_ecology < 1 or calif_ecology > 10:                                             # Validación Rango 1 - 10
        print("ERROR. El Rango de Calificación es del 1 - 10") 
        calif_ecology = int(input("Ingresa tu Calificación en Ecología: "))                        
    
    
    # Determinar Participación en Rifa
    sumatory = calif_math + calif_ecology + calif_spanish                                      # Sumatoria de Calificaciones
    prom = sumatory / 3                                                                        # Promedio de Califcaciones
    if prom >= 9:                                                                              # Promedio Mayor o Igual a 9
        selected_num = int(input("Ingresa un Número al Azar en el Rango del 1 - 10: "))        # Nïmero de Rifa del Participante
        while selected_num < 1 or selected_num > 10:                                           # Validación del Rango 1 - 10
            print("ERROR. El Rango del Número a Elegir es del 1 - 10")
            selected_num = int(input("Ingresa un Número al Azar en el Rango del 1 - 10: "))   
        rand_num = random.randint(1, 10)                                                       # Número al Azar
        print("El Numero al Azar seleccionado es: %d" %(rand_num))                             # Mensaje Número al Azar
        if selected_num == rand_num:                                                           # Coincidencia                              
            print("Has Ganado el Premio de la Rifa %s !!!!" %(name))                           # Mensaje Ganador
            break                                                                              # Salida del Bucle
        else:  
            lost += 1                                                                          # Sumar Contador de Participaciones Perdida
            print("Lo Sentimos, no obtuviste el Premio de la Rifa")                            # Mensaje Perdedor
    else: 
        lost += 1                                                                              # Sumar Contador de Participaciones Perdida
        print("Necesitas un Promedio Mayor o Igual a 9 para participar en la Rifa")            # Mensaje de Descalificación por Promedio
        

    # Actualizamos la Variable de Control del Bucle
    i += 1


# Si se Perdieron todas las Participaciones imrpimimos Mensaje Perdedor 
if lost == 5: print("Ningún Participante Ganó la Rifa")

# -----------------------------------------------------------------------------------------------------------------------------------------
