from scrapper.scrapper import ScrapperTareaQanlex
from selenium import webdriver

PATH:str = '/home/the14th/Downloads/'

if __name__ == "__main__":
    URL = "https://scw.pjn.gov.ar/scw/home.seam"
    driver = webdriver.Chrome()
    scrapper = ScrapperTareaQanlex(driver)
    scrapper.connect_to(URL)
    scrapper.navigate_to_data()
    scrapper.extract_data()
    scrapper.disconnect()
    scrapper.expedientes.show_info()
    scrapper.expedientes.save_to_csv()

