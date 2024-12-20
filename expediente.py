import pandas as pd

#Cada expediente tiene id, JURISDICCION, DEPENDENCIA, situacion_actual, caratula, {actuaciones -> oficina, fecha, tipo, detalle, a_fs}
column_names = ['id', 'jurisdiccion', 'dependencia', 'situacion_actual', 'caratula', 'actuaciones', 'intervinientes']
path = '/home/the14th/Downloads/'

#ALgunos datos se extraen del scrapper de la forma
# <Tipo:\nABCD>, para estos casos ,debido a  las distintas estructuras de las tablas,
#  se limpia con <pandas>

# expediente = {
#     'info':[],
#     'id': pd.Series(dtype='str'),
#     'jurisdiccion': pd.Series(dtype='str'),
#     'dependencia': pd.Series(dtype='str'),
#     'situacion_actual': pd.Series(dtype='str'),
#     'caratula': pd.Series(dtype='str')
# }
# df_expediente_types = {
#     'id': pd.Series(dtype='str'),
#     'jurisdiccion': pd.Series(dtype='str'),
#     'dependencia': pd.Series(dtype='str'),
#     'situacion_actual': pd.Series(dtype='str'),
#     'caratula': pd.Series(dtype='str')
# }

# df_exp_actuaciones_types = {
#     'oficina': pd.Series(dtype='str'),
#     'fecha': pd.Series(dtype='str'),
#     'tipo': pd.Series(dtype='str'),
#     'detalle': pd.Series(dtype='str'),
#     'a_fs': pd.Series(dtype='str')
# }

# df_exp_intervinientes_types = {
#     'tipo': pd.Series(dtype='str'),
#     'nombre': pd.Series(dtype='str'),
#     'tomo': pd.Series(dtype='str'),
#     'i_e_j': pd.Series(dtype='str')
# }

class DataExpediente:
    def __init__(self):
        self.data = []

    def show_info(self):
        for value in self.data:
            print('\n')
            print(value)
    
    def save_to_csv(self):
        pd.DataFrame(self.data, columns=column_names).to_csv(f'{path}expedientes.csv', index=False)
