import pandas as pd
import numpy as np
import re

# se guarda el conjunto de datos
df_ge_crops = pd.read_csv('files/datasets/input/BiotechCropsAllTables2023.csv')

# pd.set_option('display.max_columns', None)

# se llaman las 5 primeras filas del DataFrame y con info() se muestra la información del DataFrame
df_ge_crops.head()
df_ge_crops.info()

# se guarda en una lista el nombre de las columnas
col_names = df_ge_crops.columns

# se emplea un bucle for para iterar sobre la lista con los nombres de las columnas

lower_col_names = [] # se define una nueva lista vacia para guardar los nuevos nombre de las columnas en minúscula

for col in col_names:
    lower_names = col.lower()
    lower_col_names.append(lower_names)


# se cambian el nombre de las columnas "state/year" => 'state', "value" => 'porcentaje' y "table" => '
lower_col_names[1] = 'state'
lower_col_names[3] = 'pct_(%)'
lower_col_names[-1] = 'crop_name'

# Se asignan los nuevos nombres de columna
df_ge_crops.columns = lower_col_names

# * En la documentación de la USDA se indica que hay algunos estados que no tiene datos capturados de los cultivos
# * genéticamente modificados antes del 2005 y se indican con un '.', el '.' se reemplazará con valores nulos
# * También hay estados que tienen un porcentaje de cultivos menores a 1 %, esos se indican con un '*'
# * Por lo tanto, para fines de éste análisis los '*' se reemplazarán con 0.

# se reemplazan los '.' por valores nulos, se define una función

def replace_value(valor):
    '''
    Función que reemplaza los valores de una columna
    '''
    if valor == '.':
        return np.nan
    elif valor == '*':
        return  0
    else:
        return valor
    
# se aplica la función a la función deseada
df_ge_crops['pct_(%)'] = df_ge_crops['pct_(%)'].apply(replace_value)
    
# se revisa la información general del DataFrame
df_ge_crops.info()

# se cambia el tipo de dato de la columna 'pct_(%)' a flotante con to_numeric()
df_ge_crops['pct_(%)'] = pd.to_numeric(df_ge_crops['pct_(%)'])

# se cre una nueva columna para extraer sólo la variedad o modificación genética del cultivo,
# Primero se extrae el texto de interés que indica el tipo de modificación genética o variedad
# patrón regex para múltiples cadenas
pattern = r'(Insect-resistant \(Bt\)|Herbicide-tolerant \(HT\)|Stacked gene varieties|All GE varieties)'

# se usa str.extract() para extraer las cadenas específicas:
# también se crea la columna 'variety' para guardar el texto a extraer
df_ge_crops['variety'] = df_ge_crops['attribute'].str.extract(pattern)

df_ge_crops.head()

# Para el tipo de cultivo se hace lo mismo, se crea una nueva columna solo para el nombre del cultivo
# Primero se extrae el texto de interés que indica el nombre del cultivo
# patrón regex para múltiples cadenas
pattern_crops = r'(\bcorn\b|\bcotton\b|\bsoybean\b)'

# se usa str.extract() para extraer las cadenas específicas:
# también se crea la columna 'crop' para guardar el texto a extraer
df_ge_crops['crop'] = df_ge_crops['crop_name'].str.extract(pattern_crops)

df_ge_crops.head()

# se almacenan las columnas de interés en un nuevo DataFrame

df_final_crops = df_ge_crops[['variety', 'state', 'year', 'pct_(%)', 'crop']]

# se guardan los datos 
df_final_crops.to_csv("files/datasets/output/a01_dataset_ge_crops_cleaned.csv", index=False)






