class Swiggy():
    __restaurant_lst = {
        'Saravana': {
            'rating': 3.9,
            'distance': 6.8,
            'veg': 'yes',
            'menu': {'dosa': 90, 'masala dosa': 115, 'vada': 60, 'vada sambar': 85, 'idli': 80}
        },

        'KFC': {
            'rating': 3.8,
            'distance': 4.3,
            'veg': 'no',
            'menu': {'popcorn chicken': 150, 'bucket': 500, 'burger': 200}
        }
    }

    def __init__(self):
        self.__restaurant_choice = ''
        self.__total_cost = 0
        self.__items = {}

    def validate_choice(self, choice, choice_type):
        if type(choice) is not choice_type:
            raise TypeError('Choice must be ', choice_type)
        else:
            return choice

    def show_restaurant_list(self):
        for restaurants in Swiggy.__restaurant_lst.items():
            print(restaurants)

    def show_menu(self, restaurant):
        checked_restaurant = self.validate_choice(restaurant, str)
        if restaurant in Swiggy.__restaurant_lst.keys():
            print(Swiggy.__restaurant_lst[restaurant]['menu'])
        else:
            raise ValueError('Restaurant does not exist')

    def order_food(self, restaurant: str, order: dict):
        checked_restaurant = self.validate_choice(restaurant, str)
        checked_order = self.validate_choice(order, dict)
        menu = Swiggy.__restaurant_lst[checked_restaurant]['menu']
        for item in checked_order.items():
            if item[0] in menu:
                self.__total_cost += menu[item[0]] * item[1]

        print('Bill: \n')
        for item in checked_order.items():
            print(item)
        print('Total Cost: ', self.__total_cost)


user_1 = Swiggy()
user_1.show_restaurant_list()
user_1.show_menu('KFC')
user_order = {'popcorn chicken': 2, 'bucket': 3, 'burger': 1}
user_1.order_food('KFC', user_orderorder)
