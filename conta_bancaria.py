class BankAccount:

    def __init__(self, number, balance, name, typeAccount, limit, limitUsed, status=False):
        self.number = number
        self.balance = balance
        self.name = name
        self.typeAccount = typeAccount
        self.status = status
        self.limit = limit
        self.limitUsed = limitUsed

    def deposit(self, money):
        if self.status == False:
            print("A conta está desativada!")
        else:
            if self.limitUsed > 0:
                print(self.limitUsed)
            else:
                self.balance = money

    def withdraw(self, money):
        if money > self.balance:
            if money > self.balance + self.limit:
                print("Saldo insuficiente")
            else:
                withdrawBalance = money - self.balance
                withdrawLimit = self.limit - withdrawBalance
                self.balance = 0
                self.limit -= withdrawBalance
        else:
            self.balance -= money

    def activateAccount(self):
        if self.status == False:
            self.status = True
        else:
            "A conta já está ativa!"

    def deactivateAccount(self):
        if self.status == True:
            self.status = False
        else:
            print("A conta já está desativada!")

    def consultBalance(self):
        if self.status == False:
            print("A conta está desativada!")
        else:
            print(f'O seu saldo é R$ {self.balance}')
            print(f'Cheque especial R$ {self.limit}')

    def includeLimit(self, money):
        if self.status == False:
            print("A conta está desativada!")
        else:
            self.limit = money

cc = BankAccount('001', 0, 'Victor', 'Conta Corrente', 0, 0)

cc.activateAccount()
cc.consultBalance()
cc.deposit(133)
cc.includeLimit(500)
cc.consultBalance()
cc.withdraw(217)
cc.consultBalance()
cc.deposit(50)
cc.consultBalance()