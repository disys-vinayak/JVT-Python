import re   
   
   
class Swiggy():
    __restaurant_lst = {
        'Saravana': {
            'rating': 3.9,
            'time': 25,
            'veg': 'yes',
            'menu': {'dosa': 90, 'masala dosa': 115, 'vada': 60, 'vada sambar': 85, 'idli': 80}
        },

        'KFC': {
            'rating': 3.8,
            'time': 30,
            'veg': 'no',
            'menu': {'popcorn chicken': 150, 'bucket': 500, 'burger': 200}
        }
    }
    
    __accounts = {'admin': 'password'}
    
    __payment = ['cash', 'netbanking', 'swiggy wallet', 'upi', 'card']

    def __init__(self):
        self.__name = ''
        self.__password = ''
        self.__restaurant_choice = ''
        self.__logged_in = 'n'
        self.__total_cost = 0
        self.__items = {}
    
    ####################### VALIDATION CODE START #############################

    def validate_choice(self, choice, choice_type):
        if type(choice) is not choice_type:
            raise TypeError('Choice must be ', choice_type)
        else:
            return choice
        
    def validate_name(self, name):
        if type(name) is not str:
            raise TypeError('Name must be str')
        else:
            return name
    
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
        
    def check_log_in(self):
        if self.__logged_in == 'n':
            raise ValueError('Not Logged In. Please Log In')
        
    ################################ VALIDATION CODE END ###############################################
        
    def create_account(self, name: str, password: str):
        checked_name = self.validate_name(name)
        checked_password = self.validate_password(password)
        if checked_name in Swiggy.__accounts.keys():
            raise ValueError('Account already exists')
        else:
            Swiggy.__accounts[checked_name] = checked_password
            
    def login(self, name: str, password: str):
        self.__name = self.validate_name(name)
        self.__password = self.validate_password(password)
        if self.__name in Swiggy.__accounts.keys():
            if Swiggy.__accounts[self.__name] == self.__password:
                self.__logged_in = 'y'
            else:
                raise ValueError('Name and Password do not match')
        else:
            raise ValueError('Account does not Exist')

    def show_restaurant_list(self):
        self.check_log_in()
        for restaurants in Swiggy.__restaurant_lst.items():
            print(restaurants)

    def show_menu(self, restaurant: str):
        self.check_log_in()
        checked_restaurant = self.validate_choice(restaurant, str)
        if restaurant in Swiggy.__restaurant_lst.keys():
            print(Swiggy.__restaurant_lst[restaurant]['menu'])
        else:
            raise ValueError('Restaurant does not exist')

    def order_food(self, restaurant: str, order: dict, payment: str):
        self.check_log_in()
        checked_restaurant = self.validate_choice(restaurant, str)
        checked_order = self.validate_choice(order, dict)
        checked_payment = self.validate_choice(payment, str)
        if checked_payment not in Swiggy.__payment:
            raise ValueError('Payment option not available')
        menu = Swiggy.__restaurant_lst[checked_restaurant]['menu']
        for item in checked_order.items():
            if item[0] in menu:
                self.__total_cost += menu[item[0]] * item[1]

        print('Bill: \n')
        for item in checked_order.items():
            print(item)
        print('Total Cost: ', self.__total_cost)
        print('Payment Method: ', checked_payment)


user_1 = Swiggy()
user_1.create_account('Vinayak', 'password@123')
user_1.login('Vinayak', 'password@123')
user_1.show_restaurant_list()
user_1.show_menu('KFC')
user_order = {'popcorn chicken': 2, 'bucket': 3, 'burger': 1}
user_1.order_food('KFC', user_order, 'cash')  
