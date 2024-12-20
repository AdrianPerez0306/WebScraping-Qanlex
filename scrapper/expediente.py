import pandas as pd
from config import PATH

#Cada expediente tiene id, JURISDICCION, DEPENDENCIA, situacion_actual, caratula, {actuaciones -> oficina, fecha, tipo, detalle, a_fs}
column_names = ['id', 'jurisdiccion', 'dependencia', 'situacion_actual', 'caratula', 'actuaciones', 'intervinientes']


class DataExpediente:
    def __init__(self):
        self.data = []

    def show_info(self):
        for value in self.data:
            print('\n')
            print(value)
    
    def save_to_csv(self):
        pd.DataFrame(self.data, columns=column_names).to_csv(f'{PATH}expedientes.csv', index=False)
