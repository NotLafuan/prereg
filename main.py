from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import lxml.html
import os
from datetime import datetime
import time

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class Prereg:
    def login(self, username: str, password: str) -> None:
        with webdriver.Edge() as driver:
            driver.get('https://prereg1.iium.edu.my/')

            frame = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/frameset/frame[1]')))
            driver.switch_to.frame(frame)

            driver.find_element(By.NAME, 'mat').send_keys(username)
            driver.find_element(By.NAME, 'pin').send_keys(password)
            driver.find_element(By.NAME, 'Submit').click()
            self.PHPSESSID = driver.get_cookie('PHPSESSID')['value']

    def add_course(self, course_code: str, section: str, print_output: bool = True):
        try:
            url = 'https://prereg1.iium.edu.my/addcourse.php?'
            payload = {
                'Course_code': course_code,
                'Section': section,
            }
            headers = {'Cookie': f'PHPSESSID={self.PHPSESSID}'}
            response = requests.post(url, headers=headers, data=payload)
            if print_output:
                print(f'COURSE CODE: {course_code} | SECTION: {section}')
                tree: lxml.html.HtmlElement = lxml.html.fromstring(
                    response.text)
                output: lxml.html.HtmlElement = tree.xpath(
                    '/html/body/p[2]')[0]
                print(output.text_content())
                print()
            return response
        except Exception as e:
            print(e)


def wait_until(hour: int, minute: int, second: int):
    try:
        now = datetime.now()
        while now.hour != hour or now.minute != minute or now.second != second:
            print(f'\r{now.strftime("%H:%M:%S")}', end='', flush=True)
            time.sleep(1)
            now = datetime.now()
        print(f'\r{now.strftime("%H:%M:%S")}')
    except KeyboardInterrupt:
        time.sleep(1)


if __name__ == '__main__':
    wait_until(hour=0, minute=0, second=10)
    prereg = Prereg()
    prereg.login(os.getenv('USER'), os.getenv('PASS'))
    prereg.add_course('MCTA 3331', '1')
    prereg.add_course('MCTA 3203', '1')
    prereg.add_course('MCTA 3352', '2')
    prereg.add_course('MCTA 3351', '1')
    prereg.add_course('MCTA 3371', '1')
    prereg.add_course('UNGS 2380', '12')
