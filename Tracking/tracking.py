class App:
    __permission_lst = ['camera', 'microphone', 'contacts', 'gps', 'sms', 'log']
    def __init__(self):
        self.__name = ''
        self.__hours = 0.0 
        self.__size = 0.0
        self.__permissions = []
        self.__extra = {}
        
    def validate_name(self, name):
        flag = 0
        if type(name) is not str:
            flag += 1
            raise TypeError('App Name must be in string')
        
        if flag == 0:
            return name
    
    def validate_hours(self, hours):
        flag = 0
        if type(hours) is int:
            hours = float(hours)
        if type(hours) is not float:
            flag += 1
            raise TypeError('Hours must be in float')
        if hours > 24.0:
            flag += 1
            raise ValueError('Hours Per Day cannot be over 24')
        if hours < 0.0:
            flag += 1
            raise ValueError('Hours Per Day cannot be less than 0')
        
        if flag == 0:
            return hours
        
    def validate_size(self, size):
        flag = 0
        if type(size) is int:
            size = float(size)
        if type(size) is not float:
            flag += 1
            raise TypeError('Size must be in float')
        if size < 0.0:
            flag += 1
            raise ValueError('Size cannot be less than 0')
        
        if flag == 0:
            return size
        
    def validate_permission(self, permission):
        flag = 0
        if type(permission) is not str:
            flag += 1
            raise TypeError('Permission must be string')
        if len(permission) < 1:
            flag += 1
            raise ValueError('Permission cannot be less than 1 character long')
        if permission not in App.__permission_lst:
            flag += 1
            raise ValueError('Permission does not exist')
        
        if flag == 0:
            return permission
        
    ########################## VALIDATION CODE END ###########################################################
    
    ############################ ACCOUNT CODE START #############################################################
        
    def create_app(self, name: str, size: float):
        self.__name = self.validate_name(name)
        self.__size = self.validate_size(size)
        print('App Created')
    
    def add_hours(self, hours: float):
        self.__hours += self.validate_hours(hours)
        print('Hours Added')
        print(f'Hours: {self.__hours}')
    
    def add_permission(self, permission: str):
        if permission in self.__permissions:
            raise ValueError('Permission already activated')
        else:
            self.__permissions.append(permission)
            print('Permission Added')
    
    def add_extra(self, attribute: str, value: str):
        checked_attribute = self.validate_name(attribute)
        checked_value = self.validate_name(value)
        if checked_attribute in self.__extra.keys():
            raise ValueError('Attribute already exists')
        else:
            self.__extra[checked_attribute] = checked_value
            print('Extra Attribute Added')
            
    def show_status(self):
        print('Name: ', self.__name)
        print('Hours: ', self.__hours)
        print('Size: ', self.__size, ' GB')
        print('Permissions: ', self.__permissions)
        print('Extra Attributes: ', self.__extra)
        
whatsapp = App()
whatsapp.create_app('Whatsapp', 1.8)
whatsapp.add_hours(2)
whatsapp.add_permission('camera')
whatsapp.add_permission('contacts')
whatsapp.add_extra('photos', '765')
whatsapp.show_status()
