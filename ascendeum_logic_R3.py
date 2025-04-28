from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

time_cal = []
j=10

for i in range(1,j+1):
    start_time = time.time()
    driver = webdriver.Chrome()

    driver.get("https://mathup.com")

    WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div/div[1]/div/div/div[3]/div[1]/div[2]/div/div[2]/div[1]')))

    driver.close()

    end_time = time.time()

    total_time = end_time - start_time

    time_cal.append(total_time)

    print (time_cal)

avg_time = sum(time_cal)/j
print ("Average loading time of mathup page -- "+str(avg_time))
    
    
    
