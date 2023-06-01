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
            if self.limitUsed < 0:
                refundLimit = self.limitUsed + money
                if refundLimit > 0:
                    self.limit += (self.limitUsed * -1)
                    self.balance += refundLimit
                    self.limitUsed = 0
                else:
                    self.limit += money
            else:
                self.balance += money

    def withdraw(self, money):
      if self.status == False:
            print("A conta está desativada!")
      else:
        if money > self.balance:
            if money > self.balance + self.limit:
                print("Saldo insuficiente")
            else:
                withdrawBalance = money - self.balance
                self.limitUsed = self.balance - money
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
cc.deposit(1000)
cc.includeLimit(500)
cc.consultBalance()
cc.withdraw(1500)
cc.consultBalance()
cc.deposit(3150)
cc.consultBalance()
