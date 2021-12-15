class Swiggy:
    __restaurants = []
    def __init__(self):
        self.user_choice = ''
        
    def get_choice(self, choice: str):
        if not isintance(choice, str):
            raise TypeError('Choice should be in string')
    def enter_restaurant
        