from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
textInput = input()

chromeOption = webdriver.ChromeOptions()
chromeOption.add_argument("--start-maximized")
driver = webdriver.Chrome(options = chromeOption)
driver.get("https://www.sheypoor.com")

WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="advanced-search"]/form/div/div[1]/div/input')))
searchInput = driver.find_element(By.XPATH,'//*[@id="advanced-search"]/form/div/div[1]/div/input')
searchInput.click()
searchInput.send_keys(textInput)
searchInput.send_keys(Keys.ENTER)
time.sleep(5)
blocks = driver.find_elements(By.CLASS_NAME,"content")
links= []
for div in blocks:
    a = div.find_element(By.TAG_NAME,"a")
    href = a.get_attribute("href")
    links.append(href)
imgLinks = []
searchInput = WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'.item-image.ratio-4-3')))
for im in searchInput:
    imElm = im.find_element(By.TAG_NAME,'img')
    imAtr = imElm.get_attribute('src')
    imgLinks.append(imAtr)
imgTitle = []
for title in searchInput:
    titleElm = title.find_element(By.TAG_NAME,'img')
    titleAtr = titleElm.get_attribute('title')
    imgTitle.append(titleAtr)

file = open("links.txt",'w',encoding='utf-8')

imgLinks = imgLinks[:10:]
for i in range(len(imgLinks)):
    file.write(imgTitle[i]+"\n"+links[i]+"\n"+imgLinks[i]+"\n")
    file.write("\n")
file.close()

for idx,img in enumerate(imgLinks):
    session = requests.Session()
    session.max_redirects = 1000
    response = session.get(img)
    with open('digi{}.png'.format(idx), 'wb') as file:
            file.write(response.content)





