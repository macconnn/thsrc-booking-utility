class SelectTrainData:
    def __init__(self, start, end, date, times, radio, captcha):
        self.start = start
        self.end = end
        self.date = date
        self.times = times
        self.radio = radio
        self.captcha = captcha

    def get_select_train_data(self):
        result: dict = {
            'BookingS1Form:hf:0': '',
            'selectStartStation': self.start,
            'selectDestinationStation': self.end,
            'trainCon:trainRadioGroup': '0',
            'tripCon:typesoftrip': '0',
            'seatCon:seatRadioGroup': '0',
            'bookingMethod': self.radio,
            'toTimeInputField': self.date,
            'toTimeTable': self.times,
            'toTrainIDInputField': '',
            'backTimeInputField': self.date,
            'backTimeTable': '',
            'backTrainIDInputField': '',
            'ticketPanel:rows:0:ticketAmount': '1F',
            'ticketPanel:rows:1:ticketAmount': '0H',
            'ticketPanel:rows:2:ticketAmount': '0W',
            'ticketPanel:rows:3:ticketAmount': '0E',
            'ticketPanel:rows:4:ticketAmount': '0P',
            'homeCaptcha:securityCode': self.captcha
        }

        return result


class SubmitTrainData:
    def __init__(self, radio):
        self.radio = radio

    def get_submit_train_data(self):
        result: dict = {
            'TrainQueryDataViewPanel:TrainGroup': self.radio,
            'BookingS2Form:hf:0': ''
        }

        return result


class ConfirmBill:
    def __init__(self, radio):
        self.radio = radio

    def get_confirm_bill_data(self):
        result: dict = {
            'BookingS3FormSP:hf:0': '',
            'diffOver': '1',
            'isSPromotion': '1',
            'passengerCount': '1',
            'isGoBackM': '',
            'backHome': '',
            'TgoError': '1',
            'idInputRadio': '0',
            'dummyId': '',
            'dummyPhone': '',
            'email': '@gmail.com',
            'TicketMemberSystemInputPanel:TakerMemberSystemDataView:memberSystemRadioGroup': self.radio,
            'agree': 'on'
        }

        return result
