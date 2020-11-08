from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.binary_location = CHROME_PATH
driver = webdriver.Chrome(executable_path = CHROMEDRIVER_PATH, options = chrome_options)
driver.get('https://etherscan.io/token/0x8ab3e1faeb44b51e003a8bf1338b090dd5247e50?a=0x313bbb5da55f6087f62dda5329b5e466698c4d48')
driver.implicitly_wait(3);
buttons = driver.find_elements(By.XPATH, '//button')
got_it = buttons[-1]
print(got_it.text)
got_it.click();
driver.implicitly_wait(3);
overview = driver.find_element_by_xpath("//*[@id=\"ContentPlaceHolder1_divSummary\"]/div[1]")
filtered_by = driver.find_element_by_xpath("//*[@id=\"ContentPlaceHolder1_filteredByAddress\"]")
transfers = driver.find_element_by_xpath("//*[@id=\"ContentPlaceHolder1_maintab\"]")
txns = driver.find_element_by_xpath("//*[@id=\"ContentPlaceHolder1_maintab\"]/div[2]/div")
transactions = driver.find_element_by_xpath("//*[@id=\"transactions\"]")
transactions_d = driver.find_element_by_xpath("//*[@id=\"transactions\"]/div[2]")
iframe = driver.find_element_by_xpath("//*[@id=\"tokentxnsiframe\"]")
body = driver.find_element_by_xpath("//*[@id=\"body\"]")
#maindiv = driver.find_element_by_xpath("//*[@id=\"maindiv\"]")
# driver.find_element_by_xpath("//*[@id=\"maindiv\"]/div[2]")
# maindiv = driver.find_element_by_xpath("/html/body/div[2]")
# print(maindiv)
# print(maindiv.get_attribute)
# print(maindiv.get_property)
# print(maindiv.id)
# print(maindiv.tag_name)
# print(maindiv.size)
# print(maindiv.location_once_scrolled_into_view)
# print(maindiv.location)
# print(maindiv.is_selected())
# print(maindiv.is_enabled())
# print(maindiv.is_displayed())

main_div = driver.find_elements(By.ID, '3bada08f-a952-439b-be65-ee0a7504635f')
for child in main_div:
    print(child.get_attribute)
    print(child.get_property)
    print(child.id)
    print(child.tag_name)
    print(child.size)
    print(child.location_once_scrolled_into_view)
    print(child.location)
    print(child.is_selected())
    print(child.is_enabled())
    print(child.is_displayed())

# driver.find_element_by_xpath("//*[@id=\"maindiv\"]/div[2]")

# print(maindiv.text)
# print(overview.text)
# print(filtered_by.text)
# print(transfers.text)
# buttons2 = driver.find_elements(By.XPATH, '//button')
# for button2 in buttons2:
#     print(button2.text)

# driver.find_element_by_xpath("//*[@id=\"maindiv\"]/div[2]/table");
# col = wd.findElements(By.xpath(".//*[@id=\"leftcontainer\"]/table/thead/tr/th"));
# continue_link = driver.find_element_by_link_text('blockscan.com!')
# print(continue_link)
# login_form = driver.find_element_by_xpath("//form[@id='loginForm']")
# login_form = driver.find_element_by_xpath(".//*[@id='maindiv']")

# content = driver.find_element_by_class_name('table')
# print(login_form)
# print(content)

# //*[@id="maindiv"]/div[2]/table
# /html/body/div[2]/div[2]/table

# /html/body/div[2]/div[2]


# generic = driver.find_element_by_xpath("//table[@class='table table-md-text-normal table-hover mb-4']")
# tds = tree.xpath('//table//td[@class="table table-md-text-normal table-hover mb-4"]')

# table_headers = []
# url = 'https://etherscan.io/token/0x8ab3e1faeb44b51e003a8bf1338b090dd5247e50?a=0x313bbb5da55f6087f62dda5329b5e466698c4d48'
# req = Request(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})   # I got this line from another post since "uClient = uReq(URL)" and "page_html = uClient.read()" would not work (I beleive that etherscan is attemption to block webscraping or something?)
# response = urlopen(req, timeout=20).read()
# response_close = urlopen(req, timeout=20).close()
# soup = soup(response, "html.parser")
# for tx in soup.find_all('th'):
#     print(tx)



# light = job_elem.find('thead', class_='thead-light')
# print(light)

# for tx in page_soup.find_all('th'):
#     print(tx)


# Transfers_info_table_1 = page_soup.find("table", {"class": "table-md-text-normal table-hover mb-4"})
# print("Hello")
# print(Transfers_info_table_1)
# df = pd.read_html(str(Transfers_info_table_1))[0]
# print(df)
# df.to_csv("TransferTable.csv",index=False)
