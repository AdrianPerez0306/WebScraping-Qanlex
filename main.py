
from scrapper import ScrapperTareaQanlex
from selenium import webdriver

if __name__ == "__main__":
    URL = "https://scw.pjn.gov.ar/scw/home.seam"
    driver = webdriver.Chrome()
    scrapper = ScrapperTareaQanlex(driver)
    scrapper.connect_to(URL)
    scrapper.navigate_to_data()
    scrapper.extract_data()
    scrapper.disconnect()


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