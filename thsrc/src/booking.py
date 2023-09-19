# -*- coding: utf-8 -*-
import requests
from requests.adapters import HTTPAdapter
from request import Flow
import sys
import time
from request_data import SelectTrainData, SubmitTrainData, ConfirmBill
from file_operation import JsonOperation, FileOperation
from PIL import Image


class Booking:
    def __init__(self):
        self.requestsSession = requests.session()
        self.requestsSession.mount("https://", HTTPAdapter(max_retries=3))

    def booking_flow(self):
        send = Flow()
        config = JsonOperation()
        file = FileOperation()
        print('-----Start booking-----')

        '''
        Flow 1
        Trying to access the THSRC booking page
        It will keep trying to load the page while the server is busy
        '''
        jsessionid, rv, radio = send.first_page(self.requestsSession)
        if rv != '0000':
            print("failed at first")
            sys.exit()
        if radio is None:
            print('cannot get radio from submitFirst')
            sys.exit()

        print('first_page : ' + str(radio))
        print('first_page     OK\n')

        #  open captcha.jpg
        img_path = file.get_captcha_img_path()
        img = Image.open(img_path)
        img.show()
        print("系統會自動打開圖片,請輸入圖形驗證瑪 : ")
        captcha = input()

        station_start, station_end, date, times = config.read_config_content()  # get config information
        html_data = SelectTrainData(station_start, station_end, date, times, radio, captcha)
        data_dict = html_data.get_select_train_data()
        time.sleep(2)

        '''
        Flow 2
        Access the select train page using the parameters from the config file
        '''
        page_select_train, rv, radio = send.select_train(self.requestsSession, jsessionid, data_dict)
        if rv != '0000':
            print("failed at select train")
            sys.exit()
        if radio is None:
            print('圖形驗證碼可能輸入錯誤, 請再重新執行一次')
            sys.exit()

        print('select_train : ' + str(radio))
        print('select_train     OK\n')

        html_data = SubmitTrainData(radio)
        data_dict = html_data.get_submit_train_data()
        time.sleep(2)

        '''
        Flow 3
        Submit the first train on the select train page because you cannot choose your desired train for now
        '''
        page_submit_train, rv, radio = send.submit_train(self.requestsSession, data_dict)
        if rv != '0000':
            print("failed at submit train")
            sys.exit()
        if radio is None:
            print('cannot get radio from submit_train')
            sys.exit()

        print('submit_train : ' + str(radio))
        print('submit_train     OK\n')

        html_data = ConfirmBill(radio)
        data_dict = html_data.get_confirm_bill_data()
        time.sleep(2)
        '''
        Flow 4
        Confirm the final bill
        '''
        page_confirm_bill, rv = send.confirm_bill(self.requestsSession, data_dict)
        if rv != '0000':
            print("failed at submit train")
            sys.exit()

        print("-----Booking done-----")

