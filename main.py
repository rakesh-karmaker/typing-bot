from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import keyboard

from bs4 import BeautifulSoup
import requests



def get_text(driver, url):
    source_code = driver.page_source
    soup = BeautifulSoup(source_code, "html.parser")
    spans = soup.find_all("span", class_="incomplete")
    return "".join([span.text for span in spans])


# def get_text(driver, url):
#     source_code = driver.page_source
#     soup = BeautifulSoup(source_code, "html.parser")
#     spans = soup.find_all("span", class_="dash-letter")
#     text = ""
#     for span in spans:
#         print(span.text)
#         if span.text == "&nbsp;":
#             print("space")
#             text += " "
#         else:
#             text += span.text
#     return " ".join(text.split())

def main():
    url = "https://humanbenchmark.com/tests/typing"
    # url = "https://www.nitrotype.com/race"
    driver = webdriver.Firefox()
    driver.get(url)
    keyboard.wait("enter")
    text = get_text(driver, url)
    write_test(text)
    print(text)



def write_test(text):
    pyautogui.typewrite(text, interval=0.1)


if __name__ == "__main__":
    main()