# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

""" Examen 2:  Inventario de la Tienda """

# NOTE: Fecha de Realización: 23/10/2025
# NOTE: Autor: Magallanes López Carlos Gabriel
# NOTE: Correo: cgmagallanes23@gmail.com

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Redacción de Examen ============================================================= """

"""

- Descripción:
    
	Imagina que estáas haciendo el Inventario de la Tienda. Necsitas Registrar 10 Artículos, su Nombre, su Costo al Público, 
    el Costo al que fue Adquirido del Proveedor y la Cantidad del Producto. Después de Registrar la Información de los Productos
    calcularás el Costo Total de Adquisición de el Proveedor de todos los Productos de la Tienda. 
	
- Requerimientos:
    
    - Usar una Función con Retorno para Calcular el Promedio por Producto del Costo Total de Adquisición de 
      Todos los Productos del Proveedor, recuerda Redondear a 2 el Precio Promedio por Producto con el Proveedor
    - Usar Bucle For para el Registro de los 10 Artículos
    - Imprimir el Mensaje de Salida con F-String del Costo Promedio por Producto con el Proveedor
    - Debe haber Validaciones para Rangos de los Datos, si no se cumple con la Validación volver a pedir la Entrada del Dato:
        
        - El Costo al Público no debe ser Menor a $0.5
        - El Costo de Adquisición del Proveedor no debe ser Menor $0.5
        - La Cantidad de Producto no puede ser Menor a 1
"""

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

# Dependencias
from typing import Union                                                                                   # Tipos de Datos Avanzados

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Posible Solución de Examen ============================================================= """

# Función: Calcular el Precio Promedio del Proveedor por Producto
def prom_price_per_product(
        
    total_provider_amount: Union[int, float], 
    total_cant_products: Union[int, float]
    
) -> Union[int, float]: 
    
    """
        - Función: Calcular el Precio Promedio del Proveedor por Producto
        - Argumentos:
            - total_provider_amount (Union[int, float]): Total del Costo de Adquisición de Productos
            - total_cant_products (Union[int, float]): Total de Cantidad de Productos
        - Retorno:
            - Union[int, float]: Precio Promedio por Producto con el Proveedor Redondeado a 2 Decimales
        - Objetivo: Calcular el Precio Promedio por Producto con el Proveedor Redondeado a 2 Decimales
    """

    # Cálculo de Precio Promedio
    prom_price = total_provider_amount / total_cant_products
    
    # Retorno de Precio Promedio Redondeado a 2 Decimales
    return round(prom_price, 2)




# Contadores
sum_provider_price = 0                                                                                     # Total de Costo de Adquisición de Productos
sum_product_amount = 0                                                                                     # Sumatoria de la Cantidad Total de Productos


# Bucle Principal
for i in range(10):

    # Lectura de Datos
    name = input("Ingresa el Nombre del Producto: ")                                                       # Nombre
    public_price = float(input("Ingresa el Costo al Público del Producto: "))                              # Precio a Público
    while public_price < 0.5:                                                                              # Validación Precio a Público
        print("ERROR. El Precio debe ser Mayor a 0")
        public_price = float(input("Ingresa el Costo al Público del Producto: ")) 
    provider_price = float(input("Ingresa el Costo de Adquisición del Producto con el Proveedor: "))       # Precio de Proveedor         
    while provider_price < 0.5:                                                                            # Validación Precio de Proveedor
        print("ERROR. El Precio debe ser Mayor a 0")               
        provider_price = float(input("Ingresa el Costo de Adquisición del Producto con el Proveedor: "))
    product_amount = int(input("Ingresa la Cantida del Producto en Tienda: "))                             # Cantidad de Producto
    while product_amount < 0:                                                                              # Validació Cantidad de Producto
        print("ERROR. La Cantidad de Producto debe de ser Mayor a 0")
        product_amount = int(input("Ingresa la Cantida del Producto en Tienda: ")) 

    # Actualización de Contadores
    sum_provider_price += product_amount * provider_price                                                  # Total del Precio Pagado al Proveedor
    sum_product_amount += product_amount                                                                   # Total de Cantidad de Productos


# Impresión de Mensaje
print(f"El Costo Promedio por Producto con el Proveedor es de: ${prom_price_per_product(sum_provider_price, sum_product_amount)}")

# -----------------------------------------------------------------------------------------------------------------------------------------
