from selenium import webdriver
from selenium.webdriver.common.by import By

# Scrapper generico, las tareas basicas siempre son 
# connect, disconnect, find_byXPATH, navegar, extraer-datos
class Scrapper():
    def __init__(self, driver:webdriver.Chrome) -> None:
        self.driver = driver

    def connect_to(self, URL):
        try:
            self.driver.get(URL)
        except:
            print('ERROR')

    def disconnect(self):
        self.driver.quit()

    def navigate_to_data(self):
        pass

    def extract_data(self):
        pass

    def find_by_XPATH(self, _XPATH:str):
        return self.driver.find_element(
            by=By.XPATH,
            value=_XPATH
        )
    
    def fill_input(self, input:str, XPATH:str):
        input_field = self.find_by_XPATH(XPATH)
        input_field.send_keys(input)

    def click_button(self, XPATH:str):
        button = self.find_by_XPATH(XPATH)
        button.click()
