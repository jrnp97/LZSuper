from __future__ import absolute_import
from celery import current_app

import os
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

BASE_DIR = os.path.dirname(__file__)

driver = WebDriver(executable_path=os.path.join(BASE_DIR, 'driver', 'chromedriver'))
wait_driver = WebDriverWait(driver=driver, timeout=30)
app = current_app


@app.task(name='google')
def google(keywords):

    url = "http://www.google.com"
    try:
        print("Start SeoRobot Google")
        driver.get(url)  # Url de la pagina a Buscar
        driver.find_element_by_name('q').send_keys(keywords, Keys.ENTER)
        links = driver.find_elements_by_css_selector('.rc > .r a')

    finally:
        time.sleep(10)
        print("Finished SeoRobot Google")
        driver.quit()

    return dict([(i, _.get_attribute('href')) for i, _ in enumerate(links, 1) ])


@app.task(name='yahoo')
def yahoo(keywords):
    url = "https://www.yahoo.com"
    return "Executing yahoo"


@app.task(name='bing')
def bing(keywords):

    url = "http://www.bing.com"

    try:
        print("Start SeoRobot Bing")
        driver.get(url)  # Url de la pagina a Buscar
        driver.find_element_by_name('q').send_keys(keywords, Keys.ENTER)
        links = driver.find_elements_by_css_selector('.b_algo a')

    finally:
        time.sleep(10)
        print("Finished SeoRobot Bing")
        driver.quit()

    return  dict([(i, _.get_attribute('href')) for i, _ in enumerate(links, 1)])


@app.task(name='duckduck')
def duck(keywords):
    url = "https://www.duckduckgo.com"
    try:
        print("Start SeoRobot DuckDuck")
        driver.get(url)  # Url de la pagina a Buscar
        driver.find_element_by_name('q').send_keys(keywords, Keys.ENTER)
        links = driver.find_elements_by_css_selector('.result__title a')

    finally:
        print("Finished SeoRobot DuckDuck")
        time.sleep(10)
        driver.quit()

    return dict([(i, _.get_attribute('href')) for i, _ in enumerate(links, 1)])




