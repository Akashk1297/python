class Bank:
    def __init__(self,name,customerId,accountNo,accountType,bankName,balance,amount,transactionType):
        self.name=name
        self.customerId=customerId
        self.accountNo=accountNo
        self.accountType=accountType
        self.bankName=bankName
        self.balance=balance
        self.amount=amount
        self.transactionType=transactionType

    @staticmethod
    def showDetails():
        print(name, customerId)


    def transaction(self):
        if self.transactionType == 'debit':
            if self.balance > self.amount:
                self.balance=self.balance-self.amount
            else:
                raise ValueError('Insufficient balance to debit amount.')
        elif self.transactionType == 'credit':
            self.balance=self.balance+self.amount
        else:
            ValueError('Transaction type not supported: ', self.transactionType)

        return self.balance

name='akash'
customerId='cus123'
accountNo='sbi123'
accountType='savings'
bankName='sbi'
balance=1000.01
amount=123.14
transactionType='credit'
p1=Bank(name,customerId,accountNo,accountType,bankName,balance,amount,transactionType)
print(p1.transaction())

print(p1.showDetails)

transactionType='debit'
p2=Bank(name,customerId,accountNo,accountType,bankName,balance,amount,transactionType)
print(p2.transaction())

balance=200.01
amount=323.14
transactionType='debit'
p3=Bank(name,customerId,accountNo,accountType,bankName,balance,amount,transactionType)
print(p3.transaction())

