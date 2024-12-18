# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver

# # Obtener la respuesta inicial
# response = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
# if response.status_code == 200:
#     print("API OK")
# else:
#     'PROBLEMAS'

# # print(response)
# #Parsea a beatifoul soup
# soup = BeautifulSoup(response.content, 'html.parser')



# print(soup.find(id="formPublica"))
# print(soup.form.formPublica)
# # print(soup.find(id="formPublica:porParte"))
# # print(soup.prettify())

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
from scrapper_generic import Scrapper

################################################
#   CONFIGURACIONES
################################################

URL = "https://scw.pjn.gov.ar/scw/home.seam"
JURISDICCION = 'COM - Camara Nacional de Apelaciones en lo Comercial'
PALABRA_CLAVE = 'residuos'

#Estos XPATH son los usados para el ejercicio propuesto. Luego para navegacion se pueden
# crear sus respectivos XPATH, para un mejor manejo de hacia donde se navega.
# Esto podria generar el inconveniente de repetir varios XPATH, segun la cantidad de tareas independientes
XPATHS_TAREA = {
    'porParte':'',
    'captcha':'',
    'consultar':'',
    'INPUTS': {
        'JURISDICCION':'',
        'TIPO':'',
        'PALABRA_CLAVE':''
    }
}

def navigate_porParte(driver):
    button_porParte = driver.find_element(
        by=By.ID,
        value="formPublica:porParte:header:inactive"
    )
    button_porParte.click()
    
def clickear_captcha(driver):
    button_captcha = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]"
    )
    button_captcha.click()

def completar_input_select(input:str, driver):
    input_field = driver.find_element(
        by=By.XPATH,
        value='//*[@id="formPublica:camaraPartes"]'
    )
    input_field.send_keys(input)

def completar_input_text(input:str, driver):
    input_field = driver.find_element(
        by=By.XPATH,
        value='//*[@id="formPublica:nomIntervParte"]'
    )
    input_field.send_keys(input)


class ScrapperTareaQanlex(Scrapper):
    def __init__(self, driver:webdriver.Chrome) -> None:
        super().__init__(driver)
        self.driver = driver


    def navigate_to_data(self):
        self.__navigate_porParte()
        self.__enfrentar_captcha()
        self.__fill_inputs()
        self.__consult_data()
        
    def click_captcha(self):
        self.find_by_XPATH(XPATHS_TAREA['captcha']).click

    def __enfrentar_captcha(self):
        self.__switch_html_frame(0)
        clickear_captcha(self.driver)
        self.driver.switch_to.default_content()


    def __navigate_porParte(self):
        self.find_by_XPATH(XPATHS_TAREA['porParte'])


    def __switch_html_frame(self, nro_frame: int):
        self.driver.switch_to.frame(nro_frame)


    def __fill_inputs(self):
        completar_input_select(JURISDICCION, self.driver)
        completar_input_text(PALABRA_CLAVE, self.driver)

    
    def __consult_data(self):
        button = self.find_by_XPATH('//*[@id="formPublica:buscarPorParteButton"]')
        button.click()


    def extract_data(self):
        pass


    def __private_method():
        pass


if __name__ == "__main__":
    driver = webdriver.Chrome()
    scrapper = ScrapperTareaQanlex(driver)
    scrapper.connect_to(URL)
    scrapper.navigate_to_data()
    scrapper.extract_data()
    scrapper.disconnect()