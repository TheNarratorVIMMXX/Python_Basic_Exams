# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

""" Examen 3: Control de Ventas Semanal de una Cafetería """

# NOTE: Fecha de Realización: 27/10/2025
# NOTE: Autor: Magallanes López Carlos Gabriel
# NOTE: Correo: cgmagallanes23@gmail.com

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Redacción de Examen ============================================================= """

"""

- Descripción:
    
    Eres el encargado de una Cafetería y necesitas llevar el Control de Ventas de la Semana. Debes Registrar 
    las Ventas de 7 Días (Lunes a Domingo), donde por cada Día se Registrará: el Nombre del Día, la Cantidad 
    de Cafés Vendidos, el Precio Unitario del Café y la Cantidad de Postres Vendidos con su Precio Unitario. 
    Al finalizar el Registro calcularás el Ingreso Promedio por Día de toda la Semana.
	
- Requerimientos:
    
    - Usar una Función con Retorno para Calcular el Ingreso Promedio por Día de la Semana, 
      recuerda Redondear a 2 Decimales el Ingreso Promedio
    - Usar Bucle For para el Registro de los 7 Días de la Semana
    - Imprimir el Mensaje de Salida usando .format() del Ingreso Promedio por Día
    - Debe haber Validaciones para Rangos de los Datos, si no se cumple con la Validación volver a pedir la Entrada del Dato:
        
        - La Cantidad de Cafés Vendidos no puede ser Menor a 0
        - El Precio Unitario del Café no debe ser Menor a $15.0
        - La Cantidad de Postres Vendidos no puede ser Menor a 0
        - El Precio Unitario del Postre no debe ser Menor a $25.0
"""

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

# Dependencias
from typing import Union                                                                                   # Tipos de Datos Avanzados

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Posible Solución de Examen ============================================================= """

# Función: Calcular el Ingreso Promedio por Día
def prom_daily_income(total_weekly_income: Union[int, float]) -> Union[int, float]: 
    
    """
        - Función: Calcular el Ingreso Promedio por Día
        - Argumentos:
            - total_weekly_income (Union[int, float]): Total de Ingresos de la Semana
        - Retorno:
            - Union[int, float]: Ingreso Promedio por Día Redondeado a 2 Decimales
        - Objetivo: Calcular el Ingreso Promedio por Día Redondeado a 2 Decimales
    """

    # Cálculo de Ingreso Promedio por Día
    prom_income = total_weekly_income / 7
    
    # Retorno de Ingreso Promedio Redondeado a 2 Decimales
    return round(prom_income, 2)




# Sumatoria para el Total de Ingresos de Todos los Días
sum_daily_income = 0          


# Bucle Principal
for i in range(7):

    # Lectura de Datos
    day_name = input("Ingresa el Nombre del Día: ")                                                        # Nombre del Día
    coffee_quantity = int(input("Ingresa la Cantidad de Cafés Vendidos: "))                                # Cantidad de Cafés
    while coffee_quantity < 0:                                                                              # Validación Cantidad de Cafés
        print("ERROR. La Cantidad de Cafés debe ser Mayor o Igual a 0")
        coffee_quantity = int(input("Ingresa la Cantidad de Cafés Vendidos: "))
    coffee_price = float(input("Ingresa el Precio Unitario del Café: "))                                   # Precio del Café         
    while coffee_price < 15.0:                                                                              # Validación Precio del Café
        print("ERROR. El Precio del Café debe ser Mayor o Igual a $15.0")               
        coffee_price = float(input("Ingresa el Precio Unitario del Café: "))
    dessert_quantity = int(input("Ingresa la Cantidad de Postres Vendidos: "))                             # Cantidad de Postres
    while dessert_quantity < 0:                                                                             # Validación Cantidad de Postres
        print("ERROR. La Cantidad de Postres debe ser Mayor o Igual a 0")
        dessert_quantity = int(input("Ingresa la Cantidad de Postres Vendidos: "))
    dessert_price = float(input("Ingresa el Precio Unitario del Postre: "))                                # Precio del Postre
    while dessert_price < 25.0:                                                                             # Validación Precio del Postre
        print("ERROR. El Precio del Postre debe ser Mayor o Igual a $25.0")
        dessert_price = float(input("Ingresa el Precio Unitario del Postre: "))

    # Cálculo de Ingreso del Día
    daily_income = (coffee_quantity * coffee_price) + (dessert_quantity * dessert_price)
    
    # Actualización de Contadores
    sum_daily_income += daily_income       # Total de Ingresos de la Semana


# Impresión de Mensaje
print("El Ingreso Promedio por Día de la Semana es de: ${}".format(prom_daily_income(sum_daily_income)))

# -----------------------------------------------------------------------------------------------------------------------------------------