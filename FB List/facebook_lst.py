import re

class Facebook:
    __accounts = {}
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
        if not num.isdecimal():
            flag += 1
            raise ValueError('Number must only be in digits')

        if flag == 0:
            return num

    def validate_password(self, password):
        flag = 0
        special = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        digits = re.compile('1234567890')
        alphabets = re.compile('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
        if type(password) is not str:
            flag += 1
            raise TypeError('Password must be string')
        if special.search(password) == None and digits.search(digits) == None and alphabets.search(alphabets) == None:
            flags += 1
            raise ValueError('Password must contain letters, numbers and special characters')
        

    ############### VALIDATION CODE END ###########################################

    ################### ACCOUNT CODE START ########################################

    def create_account(self, name: str, num: str, mail: str, password: str):
        self.__name = self.validate_name(name)
        self.__phone = self.validate_phone(num)
        self.__mail = self.validate_mail(mail)
        self.__password = self.validate_password(password)
        Facebook.__accounts[self.__mail] = self.__password
        print('Account Created')
        
    def login(self, mail: str, password: str):
        checked_mail = self.validate_mail(mail)
        checked_password = self.validate_password(password)
        if checked_mail in Facebook.__accounts.keys():
            if Facebook.__accounts[checked_mail] == checked_password:
                print('Logged In')
            else:
                print('Mail and Password do not match')
        else:
            print('Mail does not exist')
            
    def add_friend(self, friend: str):
        name = self.validate_name(friend)
        if name in self.__friends:
            raise ValueError(f'{name} already in Friends List')
        else:
            self.__friends.append(friend)
        
    def add_group(self, group_name: str):
        name = self.validate_name(group_name)
        if name in self.__groups.keys():
            raise ValueError(f'{name} already in Groups List')
        else:
            self.__groups[name] = []
            
    
    def add_group_member(self,group_name: str, member_name: str):
        group = self.validate_name(group_name)
        member = self.validate_name(member_name)
        if group not in self.__groups.keys():
            raise ValueError(f'{group} does not Exist. Please add group')
        elif member in self.__groups.values():
            raise ValueError(f'{member} already exist in group')
        else:
            self.__groups[group].append(member)
        
    def show_friends(self):
        print('Friends List:')
        for friend in self.__friends:
            print('  ', friend)
    
    def show_group(self):
        print('Group: ')
        for group in self.__groups.keys():
            print(f'  {group}: ')
            for member in self.__groups[group]:
                print('    ', member)
    
    ############################## ACCOUNT CODE END ###############################################
        

fb = Facebook()
fb.create_account('Vinayak', '1234567890', 'vinayak@mail.com', 'password@123')
fb.login('vinayak@mail.com', 'password@123')
fb.add_friend('FriendA')
fb.add_friend('FriendB')
fb.add_group('Pizza')
fb.add_group_member('Pizza', 'PizzaA')
fb.show_friends()
fb.show_group()


