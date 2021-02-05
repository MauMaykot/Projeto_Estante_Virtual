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

wait = WebDriverWait(driver, 20)

links_biografias = []
links_biografias_especificas = []

#pegar os links das biografias e mudar de pág.#

#while True:

dados = driver.find_elements_by_xpath('//a[@class="busca-box m-group ga_tracking_event desktop"]')

for i in dados:

    links_biografias.append(i.get_attribute('href'))       
    print(links_biografias)

    #botao = driver.find_element_by_xpath('//a[@aria-label="próxima"]')
    #botao.click()

    #sleep(5)    

#pegar os links da biografia específica e mudar de pág.#

dados = driver.find_elements_by_xpath('//a[@aria-label="exemplar"]')

for linkbylink_biografias in links_biografias:
    driver.get(linkbylink_biografias)

    #while True:

    for i in dados:

        links_biografias_especificas.append(i.get_attribute('href'))       
        print(links_biografias_especificas)

        #for i in range(10):
            #driver.execute_script("window.scrollBy(0,500)","")
            #sleep(1)
        #try:
            #botao = driver.find_element_by_xpath('//a[@aria-label="proxima"]')
            #botao.click()
            #sleep(8)
        #except:
            #pass

# fazer a coleta dos dados

for linkbylink_biografias_especificas in links_biografias_especificas:
    driver.get(linkbylink_biografias_especificas)
    try:
        titulo = wait.until(EC.presence_of_element_located(
                                (By.XPATH, './/h1[@class="livro-titulo col-12"]'))).text
        print(titulo)
    except:
        pass

    try:
        tipo = wait.until(EC.presence_of_element_located(
                                (By.XPATH, './/p[@class="type m-used info-type"]'))).text
        print(tipo)
    except:
        pass

    try:
        editora = wait.until(EC.presence_of_element_located(
                                (By.XPATH, './/p[@class="livro-specs info-publisher"]'))).text
        print(editora)
    except:
        pass

    try:
        ano = wait.until(EC.presence_of_element_located(
                                (By.XPATH, './/p[@class="livro-specs info-year"]'))).text
        print(ano)
    except:
        pass

    try:
        estante = wait.until(EC.presence_of_element_located(
                                (By.XPATH, './/p[@class="livro-specs info-shelf"]'))).text
        print(estante)
    except:
        pass

    try:
        peso = wait.until(EC.presence_of_element_located(
                                (By.XPATH, './/p[@class="livro-specs info-weight"]'))).text
        print(peso)
    except:
        pass

    try:
        ISBN = wait.until(EC.presence_of_element_located(
                                (By.XPATH, './/p[@class="livro-specs info-isbn"]'))).text
        print(ISBN)
    except:
        pass

    try:
        idioma = wait.until(EC.presence_of_element_located(
                                (By.XPATH, './/p[@class="livro-specs info-language"]'))).text
        print(idioma)
    except:
        pass

    try:
        cadastrado = wait.until(EC.presence_of_element_located(
                                (By.XPATH, './/p[@class="livro-specs info-time"]'))).text
        print(cadastrado)
    except:
        pass

    try:
        descricao = wait.until(EC.presence_of_element_located(
                                (By.XPATH, './/span[@class="description-text"]'))).text
        print(descricao)
    except:
        pass

    try:
        dat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Data: " + dat)
    except:
        pass

    f.write(titulo + ";" + tipo + ";" + editora + ";" + ano + ";" + estante + ";" + peso + ";" + ISBN + ";" + idioma + ";" + cadastrado + ";" + descricao + ";" + "\n")

    
