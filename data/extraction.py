# Importar librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("Resultados_BME680.csv")

# Mostrar las primeras filas
df.head()