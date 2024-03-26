from selenium import webdriver
from selenium.webdriver.common.by import By
import json
# import time

# Ini variabel yang akan menampung hasil scrapping
hasil_scrapping = [] 

# Parameter yang dapat diubah2
file_path = "output_olx.txt"
jumlah_muat_lebih = 3
base_link = "https://www.olx.co.id/mobil-bekas_c198"

driver = webdriver.Chrome()
driver.get(base_link) 
driver.implicitly_wait(1)

# Jumlah data yg diambil
count_data = 0

# Jumlah gagal scrapping
count_exception = 0

for muat in range(jumlah_muat_lebih):
    if muat == 0:
        pass
    else:
        tekan_tombol = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/section/div/div/div[5]/div[2]/div/div[2]/ul/li[' + str(jumlah_li) + ']/div/button').click()
    
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        ambil_li = driver.find_elements(By.XPATH, '/html/body/div/div/main/div/div/section/div/div/div[5]/div[2]/div/div[2]/ul/li')
        jumlah_li = len(ambil_li)

        if jumlah_li == 0:
            attempts += 1
            print("gagal mengambil li")
        else:
            break

    print("jumlah", jumlah_li)
    print("muat", muat)
    print("count_data", count_data)
    driver.implicitly_wait(5)
        
    # Looping utk mengambil informasi
    for isi_li in range(count_data, jumlah_li):
        if(count_exception >= 3):
            break
        # Ambil data dan mengolah
        driver.implicitly_wait(1)

        count_data += 1
        print(count_data)

        try:
            geser = 1
            tahun = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/section/div/div/div[5]/div[2]/div/div[2]/ul/li[' + str(isi_li) +']/a/div[1]/div[2]/div[' + str(geser + 1) + ']').text
            nama_mobil = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/section/div/div/div[5]/div[2]/div/div[2]/ul/li[' + str(isi_li) +']/a/div[1]/div[2]/div[' + str(geser + 2) + ']').text
            tahun = tahun[:4]
            # Hasil data 1 mobil
            tahun_nama_mobil = tahun + ' ' + nama_mobil
            hasil_scrapping.append(tahun_nama_mobil)
            # print(tahun_nama_mobil)
            driver.implicitly_wait(1)
            count_exception = 0
        
        except:
            print("scrapping gagal")
            count_exception += 1
    
driver.quit()

# Mengekspor hasil berupa file txt
with open(file_path, 'w') as file:
    json.dump(hasil_scrapping, file)
