import pandas as pd
import os

path = '/home/the14th/Downloads/'
os.chdir(path)
df_expedientes = pd.read_csv('expedientes.csv')

################################################
#   Todos los datos a minuscula
################################################
df_expedientes = df_expedientes.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)

################################################
#   Normalizacion de los datos a 1FN
################################################
df_expedientes[['jurisdiccion_acronimo', 'id', 'anio']] = df_expedientes['id'].apply(
    lambda x: pd.Series([x.split()[0], x.split()[1].split('/')[0], x.split()[1].split('/')[1]])
)

# Solo me interesan los ids, ya que palabras como juzgados o secretaria son redundantes
# ya que se entienden segun la columna
df_expedientes[['juzgado_id', 'secretaria_id']] = df_expedientes['dependencia'].apply(
    lambda x: pd.Series([
        x.split()[2],              # The juzgado_id is the third last part
        x.split()[-1]               # The secretaria_id is the last part (after 'nº')
    ])
)
df_expedientes.drop(columns=['dependencia'], inplace=True)
df_expedientes.rename(columns={'jurisdiccion':'jurisdiccion_aclaracion'}, inplace=True)

#Elimino palabras innecesarias como 'en ', ya que la 1FN requiere solo 1 dato
df_expedientes['situacion_actual'] = df_expedientes['situacion_actual'].str.replace(r'en (despacho|letra)', r'\1', regex=True)
df_expedientes.rename(columns={'situacion_actual':'estado'}, inplace=True)

#Guardar los datos en un csv
df_expedientes.to_csv(f'{path}expedientes_clean.csv', index=False)