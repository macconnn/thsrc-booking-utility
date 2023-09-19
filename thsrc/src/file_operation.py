import os
import json


class JsonOperation:
    @staticmethod
    def read_config_content():
        current_directory = os.path.dirname(__file__) + "/resources/config"
        with open(current_directory, 'r') as file:
            result = json.load(file)

        station_start = result["station_start"]
        station_end = result["station_end"]
        date = result["date"]
        times = result["times"]
        return station_start, station_end, date, times


class FileOperation:
    @staticmethod
    def get_captcha_img_path():
        current_directory = os.path.dirname(__file__) + "/resources/captcha.jpg"
        return current_directory
