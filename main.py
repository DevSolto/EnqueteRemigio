from selenium import webdriver

from time import sleep

class Enquete:
    def __init__(self) -> None:
        self.link = "https://eleicao.top/?page_id=569"
        self.driver = webdriver.Chrome(executable_path="\\chromedriver.exe")
        self.driver.maximize_window()

    def abrirSite(self):
        sleep(1)
        self.driver.get(self.link)
        sleep(10)

    
enquete = Enquete()

enquete.abrirSite()