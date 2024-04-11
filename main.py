from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

for i in range(0,20):


    navegador.get("https://eleicao.top/?page_id=569")

    sleep(1)

    navegador.find_element(by=By.CLASS_NAME, value="totalpoll-question-choices-item-container").click()

    navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/main/div/div/section[2]/div[2]/div/div/div[2]/div/div/div/div/form/div[4]/button[2]").click()
    sleep(5)

    navegador.delete_all_cookies() 
