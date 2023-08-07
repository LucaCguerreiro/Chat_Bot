from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import openai


dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/zap")
driver = webdriver.Chrome(chrome_options=chrome_options2)
driver.get('https://web.whatsapp.com/')
#######API DO EDITACODIGO##########################################
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

api = requests.get("https://editacodigo.com.br/index/api-whatsapp/9M1ujEdimQDYACbr5mXeUlVM8FMIj44z" ,  headers=agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()	

##########################################
time.sleep(10)

def bot():

    try:
        ####Pegar a mensagem do cliente e clicar nela ###
        bolinha = driver.find_element(By.CLASS_NAME,bolinha_notificacao)
        bolinha = driver.find_elements(By.CLASS_NAME,bolinha_notificacao)
        clica_bolinha = bolinha[-1]
        acao_bolinha =  webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()

        ###### Mensagem do cliente ########
        todas_as_mensagens = driver.find_elements(By.CLASS_NAME,msg_cliente)
        todas_as_msg_texto = [e.text for e in todas_as_mensagens]
        msg = todas_as_msg_texto[-1]

        ###### Processa a mensagenm na API da Ia
        chave_api = 'API DO CHAT GPT'
        editacodigo = '9M1ujEdimQDYACbr5mXeUlVM8FMIj44z'
        sistema = 'explique tudo sobre o hotel Copacabana Palace. Endereço: Av. Atlântica, 1111 - Copacabana, Rio de Janeiro - RJ, 22021-111. Telefone: (21) 2548-1111, reservas por email: reserva@email.com, aceitamos todas as formas de pagamento. OBS: responda com no maximo com 15 palavras'
        resposta = requests.get("https://editacodigo.com.br/gpt/index.php", params={'pagina': editacodigo,'sistema': sistema, 'chave_api': chave_api, 'mensagem_usuario': msg}, headers=agent)
        time.sleep(3)
        resposta = resposta.text

        ###### Envia a mensagem para o cliente ######
        campo_de_texto = driver.find_element(By.XPATH, caixa_msg)
        campo_de_texto.click()
        time.sleep(3)
        campo_de_texto.send_keys(resposta, Keys.ENTER)
        time.sleep(2)



        ######### Volta para a tela inicial ##########
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    except:
        print('buscando novas notificações')

while True:

    bot()      