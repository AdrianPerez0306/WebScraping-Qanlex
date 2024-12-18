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

    def find_by_XPATH(self, XPATH:str):
        return self.driver.find_element(
            by=By.XPATH,
            value=XPATH
        )
