from pypal import Pypal


def main():
    ruru_a = Pypal('RuruYeh', money = 1000, withdraw_limit = 700)
    tater_a = Pypal('Tater', money = 20000, withdraw_limit=5000)

    ruru_a.withdraw(1000)
    print(ruru_a.get_money())
    ruru_a.set_name('DIDIYEH')
    ruru_a.withdraw(700)
    ruru_a.withdraw(700)

    tater_a.withdraw(4000)
    print(tater_a.get_money())
    tater_a.set_name('Pauvid')
    tater_a.withdraw(7000)





if __name__ =='__main__':
    main()

