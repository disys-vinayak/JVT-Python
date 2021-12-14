import random
import time


class gpay:
    __pin = {}

    def __init__(self):
        self.__name = ''
        self.__mail = ''
        self.__phone = 0
        self.__pan = ''
        self.__bank_id = ''
        self.__friend_bank_id = []
        self.__gpay_balance = 0
        self.__transaction_lst = []
        random.seed(time.time())

    ######################################### VALIDATION CODE START ################################################################

    def validate_name(name):
        flag = 0
        if type(name) is not str:
            flag += 1
            raise TypeError('Name must be string')

        if flag == 0:
            return name

    def validate_mail(mail):
        flag = 0
        if type(mail) is not str:
            flag += 1
            raise TypeError('Mail should be string')

        if '@' not in mail:
            flag += 1
            raise ValueError('There should be @ in mail')

        if '.com' not in mail:
            raise ValueError('There should be .com in mail-5')

        if flag == 0:
            return mail

    def validate_phone(num):
        flag = 0
        if type(num) is not int:
            flag += 1
            raise TypeError('Phone Number must be int')

        if len(num) != 10:
            flag += 1
            raise ValueError('Phone number must be 10 digits long')

        if flag == 0:
            return num

    def validate_pan(pan):
        flag = 0
        if type(pan) is not string:
            flag += 1
            raise TypeError('PAN must be ')

        if len(pan) != 10:
            flag += 1
            raise ValueError('PAN should be 10 digits long')

        if flag == 0:
            return pan

    ##################################VALIDATION CODE END ############################################################################

    def create_transaction_id():
        return random.randint(0000000000, 9999999999)

    def enter_mail(self, mail: str):
        self.__mail = self.validate_mail(mail)

    def enter_num(self, phone: int):
        self.__phone = self.validate_phone(phone)

    def enter_pan(self, pan: str):
        if isinstance(pan, str):
            if len(pan) == 10:
                self.__pan = pan
            else:
                raise ValueError('PAN should be 10 digits long')
        else:
            raise TypeError('PAN should be string')

    def enter_pin(self, pin: str):
        if type(pin) is str:
            if len(pin) == 4:
                gpay.__pin[self.__bank_id] = pin
                print('PIN Entered')
            else:
                raise ValueError('PIN should be 4 digits long')
        else:
            raise TypeError('PIN should be string')
