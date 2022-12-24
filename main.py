from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def login(username: str, password: str) -> str:
    with webdriver.Edge() as driver:
        driver.get('https://prereg1.iium.edu.my/')

        frame = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/frameset/frame[1]')))
        driver.switch_to.frame(frame)

        driver.find_element(By.NAME, 'mat').send_keys(username)
        driver.find_element(By.NAME, 'pin').send_keys(password)
        driver.find_element(By.NAME, 'Submit').click()
        return driver.get_cookie('PHPSESSID')['value']


def add_course(course_code: str, section: str, PHPSESSID: str):
    url = 'https://prereg1.iium.edu.my/addcourse.php?'
    payload = {
        'Course_code': course_code,
        'Section': section,
    }
    headers = {'Cookie': f'PHPSESSID={PHPSESSID}'}
    return requests.post(url, headers=headers, data=payload)


if __name__ == '__main__':
    PHPSESSID = login(os.getenv('USERNAME'), os.getenv('PASSWORD'))
    # add_course('MATH 2330', '3', PHPSESSID)
    add_course('MCTA 2313', '1', PHPSESSID)
