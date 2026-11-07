# Parte 1
import pandas as pd
import numpy

df = pd.read_csv("datos_actividad_pandas.csv")
print("Tabla: ")
print(df)

# Parte 2
print("Resumen tecnico: ")
print(df.info())

print("Resumen estadistico: ")
print(df.describe())

# Parte 3
print("Selecciona las columnas:")

#columna1 = input("Columna 1:")
#columna2 = input("Columna 2:")

columnas = df[['categoria', 'precio_unitario']]

print("Columnas seleccionadas:")
print(columnas.head())

condicion = df[df['precio_unitario'] >= 100]
print("Productos con precio mayor o igual a 100")
print(condicion)

condicionDoble = df[(df['categoria'] == 'Deportes') |  (df['categoria'] == 'Hogar')]
print("Productos que sean de hogar o deportes")
print(condicionDoble)

# Parte 4

#------------------------Contar Valores faltantes------------------------# 
print("Valores faltantes: ")
print(df.isnull().sum())
#------------------------eliminar o reemplazar justificando------------------------#
medianaDePrecio = df['precio_unitario'].median()
df['precio_unitario'] = df['precio_unitario'].fillna(medianaDePrecio)
#   Si no hay descuento registrado, asumimos que fue 0.0 (sin descuento).
#   Si no hay calificación, podemos rellenarla con la mediana o un valor neutral.
df['descuento_aplicado'] = df['descuento_aplicado'].fillna(0.0)
df['calificacion_cliente'] = df['calificacion_cliente'].fillna(df['calificacion_cliente'].median())

# Detectar y eliminar registros duplicados
print("\n--- Cantidad de filas duplicadas antes de limpiar ---")
print(df.duplicated().sum())

# Eliminamos los duplicados del DataFrame
df = df.drop_duplicates()

print(f"--- Cantidad de filas después de eliminar duplicados: {len(df)} ---")

# parte 5

df['ventaTotal'] = df['precio_unitario'] * df['cantidad']

promedioPrecio = df['precio_unitario'].mean()
minPrecio = df['precio_unitario'].min()
maxPrecio = df['precio_unitario'].max()
precioTotal = df['ventaTotal'].sum()

print("#----Promedio de Precios----#")
print(promedioPrecio)
print("#----Precios minimos----#")
print(minPrecio)
print("#----Precios maximos----#")
print(maxPrecio)
print("#----Suma Total de precios----#")
print(precioTotal)

resumCategorias = df.groupby('categoria').agg(
    promedioDeVentas = ('ventaTotal','mean'),
    totalVentas = ('ventaTotal', 'sum'),
    cantidadProductos = ('id_producto', 'count')
)

print("analisis agrupado de las categorias")
print(resumCategorias)