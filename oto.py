from selenium import webdriver
from selenium.webdriver.common.by import By
import json

# Ini variabel yang akan menampung hasil scrapping
hasil_scrapping = []

# Parameter yang dapat diubah-ubah
file_path = "output.txt"
daftar_halaman = range(1, 3)
base_link = "https://www.oto.com/mobil-bekas?page="

options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # Menjalankan browser di background

with webdriver.Firefox(options=options) as driver:
    for halaman in daftar_halaman:
        driver.get(base_link + str(halaman))
        driver.implicitly_wait(3)

        daftar_mobil = driver.find_elements(By.XPATH, '/html/body/main/div/div[2]/ul[1]/li')
        for mobil in daftar_mobil:
            try:
                # XPath yang mengindikasikan informasi merek, tahun, dan jenis kendaraan perlu disesuaikan
                # dengan struktur aktual dari halaman web yang Anda inginkan.
                # Berikut adalah contoh umum untuk bagaimana Anda bisa mendapatkan informasi ini.
                # Anda perlu menyesuaikan './/div[@class="some-class"]' dengan kelas yang akurat dari elemen.
                nama_mobil = mobil.find_element(By.XPATH, './/div[@class="some-class"]/a').text
                # Asumsi XPath untuk tahun dan jenis kendaraan (anda harus menyesuaikannya)
                tahun = mobil.find_element(By.XPATH, './/div[@class="year-class"]').text
                jenis_kendaraan = mobil.find_element(By.XPATH, './/div[@class="type-class"]').text

                # Contoh pencarian sederhana berdasarkan merek, tahun, dan jenis.
                # Anda perlu mengganti "SomeBrand", "SomeYear", "SomeType" dengan nilai yang sesuai.
                if "SomeBrand" in nama_mobil and "SomeYear" in tahun and "SomeType" in jenis_kendaraan:
                    hasil_scrapping.append({
                        "nama": nama_mobil,
                        "tahun": tahun,
                        "jenis": jenis_kendaraan
                    })
            except Exception as e:
                print(f"Error when processing page {halaman}:", e)

# Mengekspor hasil berupa file txt
with open(file_path, 'w') as file:
    json.dump(hasil_scrapping, file)