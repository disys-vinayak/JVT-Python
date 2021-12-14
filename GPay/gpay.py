class gpay:
    def __init__(self):
        self.__name = ''
        self.__mail = ''
        self.__num = 0
        self.__pin = 0
    
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
        
    