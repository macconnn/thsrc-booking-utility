import requests
from bs4 import BeautifulSoup
import time
from file_operation import FileOperation


class Flow:
    def __init__(self):
        self.htmlHeader: dict = {
            'Host': '',
            'user-agent': '',
            'Accept-Encoding': '',
            'Accept': '',
            'Accept-Language': ''
        }

    def first_page(self, requests_session: requests.session()):
        rv = '0000'
        captcha_img = None
        JSESSIONID = ""
        count = 0
        file = FileOperation()

        while True:
            count += 1
            print("The THSRC server is busy right now.\nPlease wait while we try to establish a connection.({})"
                  .format(count))
            response = requests_session.get('https://irs.thsrc.com.tw/IMINT/', headers=self.htmlHeader, allow_redirects=True)

            if response.status_code != 200:
                print("connect error")
                rv = '0001'
                break

            else:
                cookies = requests_session.cookies
                cookie_name = 'JSESSIONID'

                if cookie_name in cookies:
                    JSESSIONID = cookies[cookie_name]
                soup = BeautifulSoup(response.text, "lxml")
                captcha_img = soup.select('.captcha-img')
                if captcha_img:
                    print('connect success')
                    break
                time.sleep(2)

        back_dynamic_url = captcha_img[0]['src']
        font_dynamic_url = 'https://irs.thsrc.com.tw'
        captcha_url = font_dynamic_url + back_dynamic_url
        print("captcha url : {}".format(captcha_url))

        #  save img captcha image to /resources/captcha.jpg
        jpg = requests_session.get(captcha_url, headers=self.htmlHeader, allow_redirects=True)
        img_path = file.get_captcha_img_path()
        with open(img_path, 'wb') as f:
            f.write(jpg.content)
            f.close()

        page = BeautifulSoup(response.content, features='html.parser')
        radio = _get_submit_first_radio(page)
        return JSESSIONID, rv, radio

    def select_train(self, requests_session: requests, JSESSIONID, data: dict):
        rv = '0000'
        url = 'https://irs.thsrc.com.tw/IMINT/;jsessionid=' + JSESSIONID + '?wicket:interface=:0:BookingS1Form::IFormSubmitListener'
        response = requests_session.post(url, headers=self.htmlHeader, data=data, allow_redirects=True)
        if response.status_code != 200:
            print("connect error")
            rv = '0001'
        else:
            print('connect success')

        page = BeautifulSoup(response.content, features='html.parser')
        radio = _get_select_train_radio(page)
        return response.text, rv, radio

    def submit_train(self, requests_session: requests.session(), data: dict):
        rv = '0000'
        url = 'https://irs.thsrc.com.tw/IMINT/?wicket:interface=:1:BookingS2Form::IFormSubmitListener'
        response = requests_session.post(url, headers=self.htmlHeader, data=data, allow_redirects=True)

        if response.status_code != 200:
            print("connect error")
            rv = '0001'
        else:
            print('connect success')

        page = BeautifulSoup(response.content, features='html.parser')
        radio = _get_submit_train_radio(page)
        return response.text, rv, radio

    def confirm_bill(self, requests_session: requests.session(), data: dict):
        rv = '0000'
        url = 'https://irs.thsrc.com.tw/IMINT/?wicket:interface=:2:BookingS3Form::IFormSubmitListener'
        response = requests_session.post(url, headers=self.htmlHeader, data=data, allow_redirects=True)

        if response.status_code != 200:
            print("connect error")
            rv = '0001'
        else:
            print('connect success')
        print(response.url)
        return response.text, rv


def _get_submit_first_radio(page: BeautifulSoup) -> str:
    value = None
    input_elements = page.find_all('input',
                               {'name': 'bookingMethod'})
    for input_element in input_elements:
        data_target = input_element.get('data-target')
        if data_target == 'search-by-time':
            value = input_element.get('value')
    return value


def _get_select_train_radio(page: BeautifulSoup) -> str:
    input_elements = page.find_all('input',
                               {'name': 'TrainQueryDataViewPanel:TrainGroup'})
    for input_element in input_elements:
        value = input_element.get('value')
        return value


def _get_submit_train_radio(page: BeautifulSoup) -> str:
    input_elements = page.find_all('input',
                               {'name': 'TicketMemberSystemInputPanel:TakerMemberSystemDataView:memberSystemRadioGroup'})

    for input_element in input_elements:
        value = input_element.get('value')
        return value
