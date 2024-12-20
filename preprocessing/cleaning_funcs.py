import ast
import copy
import re

def empty_to_null(lista):
    if len(lista) == 0:
        return None
    else:
        return lista
    


def parse_list_string_structured(row):
    #   La libreria ast a.k.a Abstract Syntax Tree ayuda a transformarlo a formato lista
    #   sin complicaciones
    try:
        return ast.literal_eval(row)  # Convierte el string a una lista real
    except (ValueError, SyntaxError):
        return row  # Devuelve el valor original si no se puede convertir
    

def clean_string_newline(string:str) -> list[str]:
    #Los string que contienen un \n son problematicos. 
    # Los reemplazo por algo facil de cambiar
    clean_string = re.sub("\\n", "-", string).split(':-')
    return copy.deepcopy(clean_string)

# Función para limpiar cada elemento en una lista
def clean_list(row):
    row_aux = []
    for sublist in row:
        lista_aux = []
        for string in sublist:
            string_cleaned = clean_string_newline(string)
            if(len(string_cleaned)==2):
                lista_aux.append(string_cleaned[1])
            if(len(string_cleaned)==1):
                lista_aux.append(string_cleaned[0])
        
        row_aux.append(lista_aux)

    return row_aux  # Devolver sin cambios si no es una lista