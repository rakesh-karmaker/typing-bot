from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui

from bs4 import BeautifulSoup
import requests

url = "https://humanbenchmark.com/tests/typing"


def get_text(driver):
    driver.get(url)
    source_code = driver.page_source
    soup = BeautifulSoup(source_code, "html.parser")
    spans = soup.find_all("span", class_="incomplete")
    return "".join([span.text for span in spans])



driver = webdriver.Firefox()
driver.get(url)
source_code = driver.page_source
soup = BeautifulSoup(source_code, "html.parser")
spans = soup.find_all("span", class_="incomplete")
typing_text = "".join([span.text for span in spans])
pyautogui.write(typing_text, interval=0.035)

print(divs)
