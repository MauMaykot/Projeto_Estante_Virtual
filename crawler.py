from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import csv
from datetime import datetime

driver = webdriver.Chrome(executable_path=r"C:\Users\mauricio.gomes\Desktop\Projeto_Estante_Virtual/chromedriver.exe")
driver.maximize_window()
driver.get('https://www.estantevirtual.com.br/estante/biografias')

filename = "estantevirtual_biografias.csv"
f = open(filename, "w", encoding="utf-8")
headers = "Titulo; Tipo; Editora; Ano; Estante; Peso; ISBN; Idioma; Cadastrado; Descricao; Data\n"
f.write(headers)

#pegar os links das biografias e mudar de pág.#

links = []

while True:

    dados = driver.find_elements_by_xpath('//a[@class="busca-box m-group ga_tracking_event desktop"]')

    for i in dados:

        links.append(i.get_attribute('href'))       
        print(links)

    botao = driver.find_element_by_xpath('//a[@aria-label="próxima"]')
    botao.click()

    sleep(5)    

#pegar os links da biografia específica e mudar de pág.#

links = []

while True:

    dados = driver.find_elements_by_xpath('//a[@aria-label="exemplar"]')

    for i in dados:

        links.append(i.get_attribute('href'))       
        print(links)

    for i in range(10):
        driver.execute_script("window.scrollBy(0,500)","")
        sleep(1)
    try:
        botao = driver.find_element_by_xpath('//a[@aria-label="proxima"]')
        botao.click()
        sleep(8)
    except:
        pass

#ver se está pegando as informações

'''
dados = driver.find_elements_by_xpath('//body[@class="  sticky"]')

for dado in dados:
    nome = dado.find_element_by_xpath('.//h1[@class="livro-titulo col-12"]').text 
    tipo = dado.find_element_by_xpath('.//p[@class="type m-used info-type"]').text
    ano = dado.find_element_by_xpath('.//p[@class="livro-specs info-year"]').text
    estante = dado.find_element_by_xpath('.//p[@class="livro-specs info-shelf"]').text
    peso = dado.find_element_by_xpath('.//p[@class="livro-specs info-weight"]').text
    ISBN = dado.find_element_by_xpath('.//p[@class="livro-specs info-isbn"]').text
    idioma = dado.find_element_by_xpath('.//p[@class="livro-specs info-language"]').text
    cadastrado = dado.find_element_by_xpath('.//p[@class="livro-specs info-time"]').text
    descricao = dado.find_element_by_xpath('.//span[@class="description-text"]').text 
    #print(titulo)
    #print(tipo)
    #print(editora)
    #print(ano)
    #print(estante)
    #print(peso)
    #print(ISBN)
    #print(idioma)
    #print(cadastrado)
    #print(descricao)
'''
# fazer a coleta dos dados

wait = WebDriverWait(driver, 10)

for linkbylink in links:
    driver.get(linkbylink)

    titulo = wait.until(EC.presence_of_element_located(
                            (By.XPATH, './/h1[@class="livro-titulo col-12"]'))).text

    tipo = wait.until(EC.presence_of_element_located(
                            (By.XPATH, './/p[@class="type m-used info-type"]'))).text

    editora = wait.until(EC.presence_of_element_located(
                            (By.XPATH, './/p[@class="livro-specs info-publisher"]'))).text

    ano = wait.until(EC.presence_of_element_located(
                            (By.XPATH, './/p[@class="livro-specs info-year"]'))).text

    estante = wait.until(EC.presence_of_element_located(
                            (By.XPATH, './/p[@class="livro-specs info-shelf"]'))).text

    peso = wait.until(EC.presence_of_element_located(
                            (By.XPATH, './/p[@class="livro-specs info-weight"]'))).text

    ISBN = wait.until(EC.presence_of_element_located(
                            (By.XPATH, './/p[@class="livro-specs info-isbn"]'))).text

    idioma = wait.until(EC.presence_of_element_located(
                            (By.XPATH, './/p[@class="livro-specs info-language"]'))).text

    cadastrado = wait.until(EC.presence_of_element_located(
                            (By.XPATH, './/p[@class="livro-specs info-time"]'))).text

    descricao = wait.until(EC.presence_of_element_located(
                            (By.XPATH, './/span[@class="description-text"]'))).text

    dat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #print("Data: " + dat)

    f.write(titulo + ";" + tipo + ";" + editora + ";" + ano + ";" + estante + ";" + peso + ";" + ISBN + ";" + idioma + ";" + cadastrado + ";" + descricao + ";" + "\n")

    
