from selenium import webdriver
from selenium.webdriver.common.by import By
import json

# Ini variabel yang akan menampung hasil scrapping
hasil_scrapping = [] 

# Parameter yang dapat diubah2
file_path = "output.txt"
daftar_halaman = range(1,5)
base_link = "https://www.mobil123.com/mobil-dijual/indonesia?type=used&page_number="

for halaman in daftar_halaman:

    driver = webdriver.Chrome()
    driver.get(base_link + str(halaman) + "&page_size=25") 
    driver.implicitly_wait(3)

    daftar_mobil = driver.find_elements(By.XPATH, '/html/body/main/div[3]/div/div/div/div/section/article')
    for isi in range(len(daftar_mobil)):
        driver.implicitly_wait(3)
        nama_mobil = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/div/div/section/article[' + str(isi + 1) + ']/div/div/h2/a')
        hasil_scrapping.append(nama_mobil.text)

    driver.implicitly_wait(3)
    driver.quit()

# Mengekspor hasil berupa file txt
with open(file_path, 'w') as file:
    json.dump(hasil_scrapping,file)