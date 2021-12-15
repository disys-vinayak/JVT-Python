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
