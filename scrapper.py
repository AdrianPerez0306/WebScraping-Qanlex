import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrapper_generic import Scrapper

################################################
#   CONFIGURACIONES
################################################
JURISDICCION = 'COM - Camara Nacional de Apelaciones en lo Comercial'
PALABRA_CLAVE = 'residuos'

#Estos XPATH son los usados para el ejercicio propuesto. Luego para navegacion se pueden
# crear sus respectivos XPATH, para un mejor manejo de hacia donde se navega.
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
    'BUTTON_NEXT': '//*[@id="j_idt118:j_idt208:j_idt215"]'
}

#Este scrapper esta orientado a lo pedido en el ejercicio.
class ScrapperTareaQanlex(Scrapper):
    def __init__(self, driver:webdriver.Chrome) -> None:
        super().__init__(driver)
        self.driver = driver

    def navigate_to_data(self):
        #SE usan metodos privados para tener un mejor control del comportamiento
        self.click_button(XPATHS_TAREA['porParte'])
        self.__enfrentar_captcha()
        self.__fill_inputs()
        self.click_button(XPATHS_TAREA['consultar'])
    
    def extract_data(self):
        table = self.driver.find_element(By.XPATH, XPATHS_TAREA['TABLE'])
        rows = table.find_elements(By.CSS_SELECTOR, 'tbody tr')
        current, total = 0, len(rows)
        # self.process_data(rows)
        # flag = True
        while current<total:
            table = self.driver.find_element(By.XPATH, XPATHS_TAREA['TABLE'])
            rows = table.find_elements(By.CSS_SELECTOR, 'tbody tr')
            time.sleep(1)
            rows[current].find_element(By.TAG_NAME, 'a').click()
            time.sleep(1)
            self.driver.back()
            # self.find_by_XPATH(XPATHS_TAREA['BUTTON_BACK']).click()
            current+=1
        
        self.find_by_XPATH(XPATHS_TAREA['BUTTON_NEXT']).click()
        time.sleep(3)
        table_2 = self.driver.find_element(By.XPATH, XPATHS_TAREA['TABLE'])
        rows_2 = table_2.find_elements(By.CSS_SELECTOR, 'tbody tr')
        time.sleep(3)
        current, total = 0, len(rows_2)
        while current<total:
            table_2 = self.driver.find_element(By.XPATH, XPATHS_TAREA['TABLE'])
            rows_2 = table_2.find_elements(By.CSS_SELECTOR, 'tbody tr')
            time.sleep(1)
            rows_2[current].find_element(By.TAG_NAME, 'a').click()
            time.sleep(1)
            self.find_by_XPATH(XPATHS_TAREA['BUTTON_BACK']).click()
            current+=1

    def process_pagination(self):
        pass

    ###############
    #   PRIVATES
    ###############
    def __enfrentar_captcha(self):
        self.__switch_html_frame(0)
        self.click_button(XPATHS_TAREA['captcha'])
        time.sleep(8)
        self.driver.switch_to.default_content()


    def __switch_html_frame(self, nro_frame: int):
        self.driver.switch_to.frame(nro_frame)


    def __fill_inputs(self):
        self.fill_input(JURISDICCION, XPATHS_TAREA['INPUTS']['JURISDICCION'])
        self.fill_input(PALABRA_CLAVE, XPATHS_TAREA['INPUTS']['PALABRA_CLAVE'])

    def __fill_inputs(self):
        self.fill_input(JURISDICCION, XPATHS_TAREA['INPUTS']['JURISDICCION'])
        self.fill_input(PALABRA_CLAVE, XPATHS_TAREA['INPUTS']['PALABRA_CLAVE'])

    # def process_data(self, rows):
    #     for row in rows:
    #         # data = row.find_elements(By.TAG_NAME, 'td')
    #         # main_data = [data[i].text for i in range(len(data))]
    #         # data = row.find_elements(By.TAG_NAME, 'td')
    #         # raw_data = [data[i].text for i in len(data)]
            
    #         # print(main_data)
    
