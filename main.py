from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#to get dynamic values
import time

service = Service('C:\\Users\\Fabio\\Desktop\\Coding\\Python\\ScrapingTextSelenium\\driver\\chromedriver.exe')

def get_driver():
    #Set Options for browsing
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com/")
    return driver

def clean_text(text):
    """Extract only the temperature from quote"""
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    #use sleep to get info from the page
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)

print(main())