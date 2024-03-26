
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time


hasil_scrapping = [] 

file_path = "output_carsome.txt"
daftar_halaman = range(1,8)
base_link = "https://www.carsome.id/beli-mobil-bekas?pageNo="

for halaman in daftar_halaman:
    driver = webdriver.Chrome()
    driver.get(base_link + str(halaman)) 
    driver.implicitly_wait(1)
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/main/div/div/div[1]/div[2]/div[2]/div/div[1]/img').click()
    daftar_mobil = driver.find_elements(By.CLASS_NAME, 'mod-b-card__title')
    for data_mobil in daftar_mobil:
        nama_mobil = data_mobil.find_elements(By.TAG_NAME, 'p')
        nama_mobil = nama_mobil[0].text + ' ' + nama_mobil[1].text
        hasil_scrapping.append(nama_mobil)

    driver.implicitly_wait(1)
    driver.quit()

# Mengekspor hasil berupa file txt
with open(file_path, 'w') as file:
    json.dump(hasil_scrapping, file)