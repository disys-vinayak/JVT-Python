import gpay


class PhonePay(gpay.GPay):
    def __init__(self):
        super().__init__()


obj = PhonePay()
obj.create_account('Name', 'mail@.com', '1234567890', '123456789012', '1234567890')
obj.add_balance(100000.1)
obj.add_friend('ABC', '123456789012')
obj.transfer_money('ABC', '123456789012', 5000.2)
