from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
#menus desplegables
from selenium.webdriver.support.ui import Select
#mantener el navegador abierto
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#webdriver.Chrome(options = chrome_options)


url = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path='/home/pablo/Documents/web scraping/chromedriver_linux64/chromedriver'

service = Service(path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url)

all_matches_button = driver.find_element(By.XPATH, value='//label[@analytics-event="All matches"]') #@atributs='valor' label -- tag  // = nodo
all_matches_button.click()

#dropdown
dropdown = Select(driver.find_element(By.ID, value = 'country'))
#visible_text = texto visible
#by_index = indice
dropdown.select_by_visible_text('Argentina')

#varios elementos
matches = driver.find_elements(By.TAG_NAME, value='tr')


partidos = []

for match in matches:
    partido = []
    detalle_td = match.find_elements(By.TAG_NAME, value='td')
    for i in detalle_td:
        partido.append(i.text)
    partidos.append(partido)

driver.quit()


#[0] = fecha
#[1] = equipo 1
#[2] = resultado
#[3] = equipo 2
fechas= []
equipo1 = []
resultados = []
equipo2 = []
for i in partidos:
    #fecha = pd.to_datetime(i[0], format='%d-%m-%Y')
    fechas.append(i[0])
    equipo1.append(i[1])
    resultados.append(i[2])
    equipo2.append(i[3])

#pandas

df = pd.DataFrame({
    'fechas': fechas,
    'equipo1' : equipo1,
    'resultado' : resultados,
    'equipo2' : equipo2
    })

df.to_csv('partidos.csv', index=False) #sin indice
