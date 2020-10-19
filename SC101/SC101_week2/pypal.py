
WITHDRAW_LIMIT = 1000
INITIAL_MONEY = 0


class Pypal:
    def __init__(self, name, money=INITIAL_MONEY, withdraw_limit = WITHDRAW_LIMIT):
        self.__n = name
        self.__m = money
        self.__w_l = withdraw_limit


    def withdraw(self, amount):
        if amount > self.__w_l:
            print('Exceed Limit')
        elif self.__m - amount >= 0:
             self.__m -= amount
             print(f'{self.__n}:{self.__m}')
        else:
            print('Illegal')

    def set_name(self, new_name):
        print(f'Name change from {self.__n} to {new_name}')
        self.__n = new_name


    def get_money(self):
        return self.__m

