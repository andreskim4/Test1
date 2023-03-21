from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest


def test_selenium1():
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    driver.get('https://inscripciones.fadu.uba.ar/inicial.php')

    """time.sleep(3)
    elem = driver.find_element(By.CLASS_NAME, "a.__web-inspector-hide-shortcut__")  # Find the search box
    elem.enter() """

    time.sleep(20)
    elem1 = driver.find_element(By.NAME, 'fUsuario')  # Find the search box
    elem1.click()
    elem1.send_keys("")

    elem2 = driver.find_element(By.NAME, 'bClave')  # Find the search box
    elem2.click()
    elem2.send_keys("")
    elem2.enter
    time.sleep(5)
    #texto = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div/a/h3').text
    #assert "luis" in texto
    driver.quit() 
