from selenium import webdriver

import time

class Cookie:
    def __init__(self):
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"
        self.SITE_MAP = {
            "buttons": {
                "biscoito":{
                    "xpath":"/html/body/div[2]/div[2]/div[15]"
                }
            }
        }

        self.driver = webdriver.Chrome(executable_path=r"C:\\12 - ProjetoSelenium\\chromedriver.exe")
        self.driver.maximize_window()

    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)

    def clicar_no_cookie(self):
        self.driver.find_element_by_xpath(self.SITE_MAP["buttons"] ["biscoito"] ["xpath"]).click()

biscoito = Cookie()
biscoito.abrir_site()