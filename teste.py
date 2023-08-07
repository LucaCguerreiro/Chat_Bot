from selenium import webdriver
import time

# Inicializa o navegador
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(20)
