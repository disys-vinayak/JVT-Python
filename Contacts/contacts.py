class Contacts:
    def __init__(self):
        self.__num = ''
        self.__name = ''
        self.__contacts = {}

    ################## VALIDATION CODE START ###############################################

    def validate_num(self, num):
        flag = 0
        if type(num) is not str:
            flag += 1
            raise TypeError('Number should be in string')

        if len(num) != 10:
            raise ValueError('Number should be 10 digits long')

        if flag == 0:
            return num

    def validate_name(self, name):
        flag = 0
        if type(name) is not str:
            flag += 1
            raise TypeError('Name should be string')

    ################ VALIDATION CODE END ########################################################

    def create_account(self, name: str, num: str):
        self.__name = self.validate_name(name)
        self.__num = self.validate_num(num)

    def add_contacts(self, name: str, num: str):
        checked_name = self.validate_name(name)
        checked_num = self.validate_num(num)
        if checked_name in self.__contacts.keys():
            raise ValueError('Name already in contacts')
        else:
            self.__contacts[checked_name] = checked_num
            print('New Contact Entered')

    def modify_contact(self, name: str, num: str):
        checked_name = self.validate_name(name)
        checked_num = self.validate_num(num)
        if checked_name not in self.__contacts.keys():
            raise ValueError('Contact does not exist')
        else:
            self.__contacts[checked_name] = checked_num
            print('Contact Modified')

    def delete_contact(self, name: str):
        checked_name = self.validate_name(name)
        if checked_name not in self.__contacts.keys():
            raise ValueError('Contact does not exist')
        else:
            del self.__contacts[name]