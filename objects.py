class BankAccount:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def greet_customer(self):
        print('Hello {}, your balance is ${}'.format(self.name, self.balance))

    def withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print('You have withdrawn ${}, your balance is now ${}.'.format(amount, self.balance))
        else:
            print('You don\'t have enough money in your account! Get a job!')

    def deposit(self, amount):
        self.balance += amount
        print('You have deposited ${} into your account. Your balance ilss now ${}'.format(amount, self.balance))


class RestrictB(BankAccount):
    def __init__(self, bal, name, padding):
        BankAccount.__init__(self, bal, name)
        self.padding = padding

    def withdrawal(self, amount):
        if self.balance - amount - self.padding >= 0:
            self.balance -= amount
            print('You have withdrawn ${}, your balance is now ${}.'.format(amount, self.balance))
        else:
            print('You don\'t have enough money in your account! Get a job!')

chris = RestrictB(150, 'Chris', 50)
katie = BankAccount(2000, 'Katie')

chris.greet_customer()
katie.greet_customer()

chris.withdrawal(20)
chris.deposit(10)
chris.withdrawal(91)
