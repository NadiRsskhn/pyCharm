from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import  Options

s=Service('C:/Users/Nexus/Downloads/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=s)
o=Options()
o.add_experimental_option("detach", True)

driver.maximize_window()
driver.get("https://guru.qahacking.ru/")
driver.execute_script("window.scrollTo(0,4000)")

driver.find_element(By.NAME, "mod_rscontact_full_name").send_keys("Иванов")
driver.find_element(By.NAME, "mod_rscontact_email").send_keys("demo@mail.ru")
driver.find_element(By.NAME, "mod_rscontact_mobile_phone").send_keys("89999999999")
driver.find_element(By.NAME, "mod_rscontact_subject").send_keys("Здраствуйте. Когда будет в наличии перекус для собачек")
time.sleep(5)
if driver.find_element(By.ID, "mod-rscontact-submit-btn-91"):print("\033[92m{}\033[0m".format("PASS"))
driver.save_screenshot("TC-2.png")