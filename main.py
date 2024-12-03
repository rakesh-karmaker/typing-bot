from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui

from bs4 import BeautifulSoup
import requests



def get_text(driver, url):
    driver.get(url)
    source_code = driver.page_source
    soup = BeautifulSoup(source_code, "html.parser")
    spans = soup.find_all("span", class_="incomplete")
    return "".join([span.text for span in spans])

def main():
    url = "https://humanbenchmark.com/tests/typing"
    driver = webdriver.Firefox()
    text = get_text(driver, url)




pyautogui.write(typing_text, interval=0.035)

print(divs)
