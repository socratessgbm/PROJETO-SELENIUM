from selenium import webdriver

import time



navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("https://ri.magazineluiza.com.br/")
time.sleep(1)
navegador.find_element_by_xpath('/html/body/form/div[7]/a').click()
navegador.find_element_by_xpath('/html/body/form/header/div/div/div/div[2]/ul/li[1]/a').click()
time.sleep(1)
navegador.find_element_by_xpath('/html/body/form/div[10]/div/div/div/div/ul[1]/li[1]/a').click()