import copy
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from expediente import DataExpediente
from scrapper_generic import Scrapper
from selenium.webdriver.remote.webelement import WebElement

################################################
#   CONFIGURACIONES
################################################
JURISDICCION = 'COM - Camara Nacional de Apelaciones en lo Comercial'
PALABRA_CLAVE = 'residuos'

#Estos XPATH son los usados para el ejercicio propuesto. Luego para navegacion se pueden
# crear sus respectivos XPATH, para un mejor control de navegacion.
# Esto podria generar el inconveniente de repetir varios XPATH, segun la cantidad de tareas independientes
XPATHS_TAREA = {
    "porParte":'//*[@id="formPublica:porParte:header:inactive"]',
    "captcha":'/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]',
    'consultar':'//*[@id="formPublica:buscarPorParteButton"]',
    'INPUTS': {
        'JURISDICCION':'//*[@id="formPublica:camaraPartes"]',
        'TIPO':'', # POr el momento este campo no es usado
        'PALABRA_CLAVE':'//*[@id="formPublica:nomIntervParte"]'
    },
    
    'TABLE': '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/form/table/tbody',
    'BUTTON_BACK': '/html/body/div[1]/div[2]/form/div/div[1]/div/div/a',
    'BUTTON_NEXT': '//*[@id="j_idt118:j_idt208:j_idt215"]',
    'ROW_DATA':'/html/body/div[1]/div[2]/form/div/div[2]', #
    'TABLE_ACTUACIONES':'/html/body/div[1]/div[2]/form/div/div[3]/div/div[3]/div/div[1]/table[2]/tbody', #TABLA CON TBODY, TR(td, td, td), TR(td, td, td)
    'BUTTON_INTERVINIENTE':'/html/body/div[1]/div[2]/form/div/div[3]/div/div[1]/table/tbody/tr/td[6]/span',
    'TABLE_INTERVINIENTE':'//*[@id="expediente:participantsTable"]' #TABLA CON THEAD, TBODY, TOBODY, TBODY
}

#Este scrapper esta orientado a lo pedido en el ejercicio.
class ScrapperTareaQanlex(Scrapper):
    def __init__(self, driver:webdriver.Chrome) -> None:
        super().__init__(driver)
        self.driver = driver
        self.expedientes = DataExpediente()
        self.data_row_aux = [] #Solo para almacenar cada expediente, y luego agregarlo a <self.expediente>

    def navigate_to_data(self):
        #SE usan metodos privados para tener un mejor control del comportamiento
        self.click_button(XPATHS_TAREA['porParte'])
        self.__enfrentar_captcha()
        self.__fill_inputs()
        self.click_button(XPATHS_TAREA['consultar'])
    
    def extract_data(self):
        ############################################################################
        #   CODIGO QUE FUNCIONA. 
        #   Idea: Los datos Expediente, Caratula, Dependencia, Situacion, Ult.Actividad 
        #       ya se encuentran incluidos en la parte de detalle. Como ya hay que 
        #       acceder a detalle y extraer mas datos, primero se accede al detalle y 
        #       luego se extraen todos los datos. 
        #       Un ejemplo de flujo de ejecucion es el siguiente:
        #           - La primera vez que se accede a los datos, se busca la tabla(+1)
        #           - Luego se clikea en detalle y se accede a cada informacion del expediente
        #           - Una vez obtenida la info, debo volver a buscar las tablas, para evitar un StaleElementError
        #   PROBLEMA: Se busca constantemente el <WebElementent>:Table, para evitar un
        #        StaleElementError, por perder la referencia al <WebElementent>:Table.
        #        Esto puede no ser muy optimo. En los Docs de Selenium se menciona el tema. S
        #       https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/
        ############################################################################
        while self.__exist_table():
            current, total = self.__extract_table_len()
            self.__iterate_table(current, total)
            self.__more_data()
            time.sleep(3)
        

    ###############
    #   PRIVATES
    ###############
    def __enfrentar_captcha(self):
        self.__switch_html_frame(0)
        self.click_button(XPATHS_TAREA['captcha'])
        time.sleep(10)
        self.driver.switch_to.default_content()


    def __switch_html_frame(self, nro_frame: int):
        #Los elementos fuera del frame original html, necesitan su contexto
        self.driver.switch_to.frame(nro_frame)


    def __fill_inputs(self):
        self.fill_input(JURISDICCION, XPATHS_TAREA['INPUTS']['JURISDICCION'])
        self.fill_input(PALABRA_CLAVE, XPATHS_TAREA['INPUTS']['PALABRA_CLAVE'])


    def __get_tableRows(self) -> list[WebElement]:
        #Para algunos casos no sirve el CSS_SELECTOR
        table = self.driver.find_element(By.XPATH, XPATHS_TAREA['TABLE'])
        rows = table.find_elements(By.CSS_SELECTOR, 'tbody tr')
        return rows
    
    def __extract_table_len(self):
        try:
            #Si existe la tabla continua, sino no existen datos
            rows = self.__get_tableRows()
            return 0, len(rows)
        except:
            self.driver.quit()

    def __exist_table(self) -> bool:
        try:
            #Si las puede encontrar, existen
            rows = self.__get_tableRows()
            return True
        except:
            return False


    def __iterate_table(self, current:int, total:int):
        while current<total:
            rows = self.__get_tableRows()
            self.__click_detail(rows[current]) #Navego hacia el detalle dentro de la tabla, y ahi extraigo datos
            self.__get_rowData() #Datos generales
            self.__get_extraData() #Datos en otras tablas dentro del general
            print(self.data_row_aux)
            self.__save_values()
            self.driver.back()
            current+=1

    def __click_detail(self, row:WebElement):
        time.sleep(1)
        button_detail = row.find_element(By.TAG_NAME, 'a')
        button_detail.click()
        time.sleep(1)

    def __more_data(self):
        #Si existe el boton, hay mas datos. Si no hay mas datos, termina
        try:
            button_more = self.find_by_XPATH(XPATHS_TAREA['BUTTON_NEXT'])
            button_more.click()
            time.sleep(3)
        except:
            self.disconnect()

    def __get_rowData(self):
        table = self.find_by_XPATH(XPATHS_TAREA['ROW_DATA'])
        spans = table.find_elements(By.TAG_NAME, 'span')
        data = [spans[i].text for i in range(len(spans))]
        self.data_row_aux.extend(data[1:])


    def __iterate_actuaciones(self):
        #No necesito navegar, ya que es la opcion por default
        try:
            aux_list = []
            table = self.find_by_XPATH(XPATHS_TAREA['TABLE_ACTUACIONES']) #TABLA CON tbody > tr(td, td, td), tr(td, td, td)
            rows = table.find_elements(By.TAG_NAME, 'tr')
            for row in rows:
                data_cells = row.find_elements(By.TAG_NAME, 'td')
                data = [data_cells[i].text for i in range(1, len(data_cells))]
                aux_list.append(data)

            self.data_row_aux.append(aux_list)
        except:
            #Si no existe la tabla agrego un valor vacio, para posicionar 
            # correctamente segun las columnas del Dataframe()
            self.data_row_aux.append([])



    def __iterate_intervinientes(self):
        #TABLA CON tbody(tr), tbody(tr), tbody(tr)
        try:
            aux_list = []
            #Necesito navegar si o si
            self.click_button(XPATHS_TAREA['BUTTON_INTERVINIENTE'])
            time.sleep(1) #Da tiempo a que cargue la tabla
            table = self.driver.find_element(By.XPATH, XPATHS_TAREA['TABLE_INTERVINIENTE'])
            rows = table.find_elements(By.CSS_SELECTOR, 'tbody tr')
            for row in rows:
                data_cells = row.find_elements(By.TAG_NAME, 'td')
                data = [data_cells[i].text for i in range(len(data_cells))]
                #En este caso, debido a la estructura de las tablas, a veces aparecen listas vacias
                if data!=['']:
                    aux_list.append(data)

            self.data_row_aux.append(aux_list)
        except:
            #Si no existe la tabla agrego un valor vacio, para posicionar 
            # correctamente segun las columnas del Dataframe()
            self.data_row_aux.append([])



    def __get_extraData(self):
        # Las distintas tablas extras tienen estructuras diferentes, por lo que 
        #   cuesta mas abstraer. Por el momento quedan 2 iteraciones para las tablas
        #   Expediente -> Actuaciones y Expediente -> Intervinientes  
        self.__iterate_actuaciones()
        self.__iterate_intervinientes()

    def __save_values(self):
        #Si no hago deepcopy, todos los indices siempre hacen referencia al ultimo valor
        row_copy = copy.deepcopy(self.data_row_aux) 
        self.expedientes.data.append(row_copy)
        self.data_row_aux.clear()
        
    
