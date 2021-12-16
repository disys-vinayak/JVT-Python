import random
import time


class GPay:
    __accounts = {}

    def __init__(self):
        self.__name = ''
        self.__mail = ''
        self.__phone = 0
        self.__pan = ''
        self.__bank_id = ''
        self.__friend_bank_id = {}
        self.__gpay_balance = 0
        self.__transaction_lst = []
        self.__logged_in = 'n'
        random.seed(time.time())

    ######################################### VALIDATION CODE START ################################################################

    def validate_name(self, name):
        flag = 0
        if type(name) is not str:
            flag += 1
            raise TypeError('Name must be string')

        if not str.isalpha(name):
            flag += 1
            raise ValueError('Name must only consist of characters')

        if flag == 0:
            return name

    def validate_mail(self, mail):
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

    def validate_phone(self, num):
        flag = 0
        if type(num) is not str:
            flag += 1
            raise TypeError('Phone Number must be string')

        if len(num) != 10:
            flag += 1
            raise ValueError('Phone number must be 10 digits long')

        if flag == 0:
            return num

    def validate_pan(self, pan):
        flag = 0
        if type(pan) is not str:
            flag += 1
            raise TypeError('PAN must be ')

        if len(pan) != 10:
            flag += 1
            raise ValueError('PAN should be 10 digits long')

        if flag == 0:
            return pan

    def validate_pin(self, pin):
        flag = 0
        if type(pin) is not str:
            flag += 1
            raise TypeError('PIN should be str')

        if len(pin) != 4:
            flag += 1
            raise ValueError('PIN should be 4 digits')

        if flag == 0:
            return pin

    def validate_bank_id(self, bank_id):
        flag = 0
        if type(bank_id) is not str:
            flag += 1
            raise TypeError('Bank Id should be string')

        if len(bank_id) != 12:
            flag += 1
            raise ValueError('Bank Id should be 12 digits long')

    def validate_money(self, money):
        if type(money) is not float:
            raise TypeError('Money should be in float')
        else:
            return money

    def check_log_in(self):
        if self.__logged_in == 'n':
            raise ValueError('Not Logged In. Please Log In')

    ##################################VALIDATION CODE END ############################################################################

    ########################### ACCOUNT CODE START ################################################################
    def create_transaction(self, name, bank_id, money):
        random.seed(time.time())
        transaction_id = str(random.randint(0000000000, 9999999999))
        transaction = {'transaction_id': transaction_id, 'name': name, 'bank_id': bank_id, 'money': money}
        self.__transaction_lst.append(transaction)

    def create_account(self, name: str, mail: str, num: str, bank_id: str, pan: str, pin: str):
        self.__name = self.validate_name(name)
        self.__phone = self.validate_phone(num)
        self.__mail = self.validate_mail(mail)
        self.__bank_id = self.validate_bank_id(bank_id)
        self.__pan = self.validate_pan(pan)
        GPay.__accounts[self.__phone] = self.validate_pin(pin)
        print('Created Account')

    def login(self, phone: str, pin: str):
        checked_phone = self.validate_phone(phone)
        checked_pin = self.validate_pin(pin)
        if checked_phone in GPay.__accounts.keys():
            if GPay.__accounts[checked_phone] == checked_pin:
                self.__logged_in = 'y'
                print('Logged In')
            else:
                raise ValueError('Phone number and Password do not match')
        else:
            raise ValueError('Account Does not Exist. Please Sign Up')


    def add_balance(self, money: float):
        self.check_log_in()
        self.__gpay_balance += self.validate_money(money)
        print('Added Balance \n Remaining balance', self.__gpay_balance)

    def add_friend(self, friend_name: str, friend_bank_id: str):
        self.check_log_in()
        name = self.validate_name(friend_name)
        bank_id = self.validate_bank_id(friend_bank_id)
        self.__friend_bank_id[name] = bank_id
        print('Added Friend')

    def transfer_money(self, friend_name: str, friend_bank_id: str, money: float):
        self.check_log_in()
        name = self.validate_name(friend_name)
        bank_id = self.validate_bank_id(friend_bank_id)
        money = self.validate_money(money)
        if name in self.__friend_bank_id.keys():
            if self.__friend_bank_id[name] == bank_id:
                if self.__gpay_balance >= money:
                    self.__gpay_balance -= money
                    self.create_transaction(name, bank_id, money)
                    print('Money Transferred\n Remaining Balance: ', self.__gpay_balance)
                else:
                    raise ValueError('Not Enough Money')
            else:
                raise ValueError('Bank Id and Name do not Match')
        else:
            raise ValueError('Name not found')
