import re

class Facebook:
    __account = {}
    def __init__(self):
        self.__name = ''
        self.__phone = ''
        self.__mail = ''
        self.__friends = []
        self.__groups = {}

    ############################## VALIDATION CODE START #########################################
    def validate_name(self, name):
        flag = 0
        if type(name) is not str:
            flag += 1
            raise TypeError('Name must be string')
        if not name.isalpha():
            flag += 1
            raise ValueError('Name must only contain alphabets ')

        if flag == 0:
            return name


    def validate_mail(self, mail):
        flag = 0
        if type(mail) is not str:
            flag += 1
            raise TypeError('Mail must be string')
        if '@' not in mail:
            flag += 1
            raise ValueError('Mail must contain @')
        if '.com' not in mail:
            flag += 1
            raise ValueError('Mail must contain .com')

        if flag == 0:
            return mail

    def validate_phone(self, num):
        flag = 0
        if type(num) is not str:
            flag += 1
            raise TypeError('Number must be string')
        if len(num) != 10:
            flag += 1
            raise ValueError('Number must be 10 digits long')
        if not num.isdigits():
            flag += 1
            raise ValueError('Number must only be in digits')

        if flag == 0:
            return num

    def validate_password(self, password):
        flag = 0
        if type(password) is not str:
            flag += 1
            raise TypeError('Password must be string')
        if not ('')

    ############### VALIDATION CODE END ###########################################

    ################### ACCOUNT CODE START ########################################

    def create_account(self, name: str, num: str, mail: str):
        self.__name = self.validate_name(name)
        self.__phone = self.validate_phone(num)
        self.__mail = self.validate_mail(mail)


        print('Account Created')

