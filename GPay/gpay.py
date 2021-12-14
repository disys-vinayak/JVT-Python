class gpay:
    def __init__(self):
        self.__name = ''
        self.__mail = ''
        self.__num = 0
        self.__pin = 0
        self.__pan = ''
    
    def enter_mail(self, mail: str):
        if not isinstance(mail, str):
            raise TypeError('Mail should be string')
        else:
            self.__mail = mail
            print('Mail Connected')
            
    def enter_num(self, num: int):
        if isinstance(num, int):
            if len(num) == 10:
                self.__num = num
                print('Phone connected')
            else:
                raise ValueError('Num should be 10 digits long')
        else:
            raise TypeError('Num should be int')
    
    def enter_num(self, name: str):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError('Name should be string')
        
    def enter_pan(self, pan: str):
        if isinstance(pan, str):
            if len(pan) == 10:
                self.__pan = pan
            else:
                raise ValueError('PAN should be 10 digits long')
        else:
            raise TypeError('PAN should be string')
        
    
       
