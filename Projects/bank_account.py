from datetime import datetime
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        self.transactions=[]
        self.is_active=True

    def credit(self, amount):
        if not self.is_active:
            print("The account is inactive.")
            return
        if amount<=0:
            print("Enter a value greater than 0")
            return
        self.balance+=amount
        self.transactions.append(["Credit", amount, datetime.now()])
        print(f"Credit of ${amount} deposited.") 
    
    def debit(self, amount):
        if not self.is_active:
            print("The account is inactive.")
            return
        if amount<=0:
            print("Enter a value greater than 0")
            return
        self.balance-=amount
        self.transactions.append(["Debit", amount, datetime.now()])
        print(f"${amount} debitted from your account.")

    def get_balance(self):
        if not self.is_active:
            print("The account is inactive.")
            return
        elif self.balance < 0:
            print("There is no balance in your account.")
            return
        else:
            print(f"Current balance: ${self.balance}")


    def get_transactions(self):
        if not self.is_active:
            print("The account is inactive.")
            return
        elif len(self.transactions) == 0:
            print("There/'s no transaction record in you account")
            return
        else:
            for transaction in self.transactions:
                print(f"{transaction[0]} {transaction[1]} on {transaction[2]}")
    
    def delete_account(self):
        self.is_active=False
        print("Your account has been deactivated")
        return
    
acc = BankAccount("DK", 1000)
acc.credit(500)
acc.debit(200)
acc.get_balance()
acc.get_transactions()
acc.delete_account()
acc.credit(100)  
