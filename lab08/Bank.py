class Bank:
    def __init__(self, __balance: float):
        self.__balance = __balance
        if __balance < 0:
            print("Неможлививй баланс")

    def deposit_money(self, money):
        if not isinstance(money, (int, float)):
            return "ви ввели не число"
        if money < 0:
            return "Ви не можете покласти від'ємну суму"
        self.__balance = self.__balance + money
        return f"Ви поклали {money} грн. Ваш рахунок {self.__balance}"

    def withdraw_money(self, money):
        your_balance = self.__balance
        if not isinstance(money, (int, float)):
            return "ви ввели не число"
        if your_balance < money:
            return "Недостатньо коштів на рахунку"
        else:
            self.__balance = your_balance - money
            return f"Ви зняли {money} грн. Ваш рахунок {self.__balance}"

    def get_balance(self):
        return self.__balance


balance1 = Bank(400)
balance2 = Bank(1200)
balance3 = Bank(100)
print("Ваш баланс:", balance1.get_balance())
print(balance2.deposit_money(321.234))
print(balance3.withdraw_money(150))
print(balance3.withdraw_money(50))

