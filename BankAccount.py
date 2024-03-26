class BankAccount:
    #creates a list of accounts for use with the classmethod later
    all_accounts = []

    #constructs BankAccount object
    def __init__(self, int_rate, balance=0):
        self.int_rate=int_rate
        self.balance=balance
        #appens constructed object onto list from earlier
        BankAccount.all_accounts.append(self)

    #increased account balance by specified amount
    def deposit(self, amount):
        self.balance=self.balance+amount
        return self
    
    #decrease account balance by specified amount
    def withdraw(self, amount):
        if(self.balance>=amount):
            self.balance=self.balance-amount
        else:
            print("Insuficiant funds: Charging a $5 fee")
            #charges fee for overdrawing the account
            self.balance=self.balance-(amount+5)
        return self
    
    #displays info on a single account
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    #yields interest
    def yield_interest(self):
        if(self.balance>0):
            self.balance=self.balance*(1+self.int_rate)
        return self
    
    #displays all accounts
    @classmethod
    def displayaccounts(cls):
        i=0
        #loops through all_accounts list form line 3
        for account in cls.all_accounts:
            i=i+1
            print(f"Account {i} Balance: ${account.balance}")

class User:
    #constructor for user objects
    def __init__(self, name, email, int_rate, balance):
        self.name = name
        self.email = email
        #this is a list of account for said user. the balance and interest rate will have to be specified for the account created when the user is created
        self.account = [BankAccount(int_rate, balance)]

    #makes deposite into specifed account(account_number) of specified amount(amount)
    def make_deposit(self, account_number, amount):
        #uses account_number to access the account in the account list of account objects
        self.account[account_number].deposit(amount)
        return self
    
    #makes withdraws from specifed account(account_number) a specified amount(amount)
    def make_withdraw(self, account_number, amount):
        #uses account_number to access the account in the account list of account objects
        self.account[account_number].withdraw(amount)
        return self

    #method that opens a new account for the user with sepcified interest rate and balance
    def open_account(self, int_rate, balance):
        #appends BankAccount object with specified attributes onto the account list of the user
        self.account.append(BankAccount(int_rate, balance))
        return self

    #displays balance for specified account(account_number)
    def display_user_balance(self, account_number):
        #uses account_number to specifed index of account to be displayed form users account list
        self.account[account_number].display_account_info()

    #displays all accounts for user
    def display_all_accounts(self):
        #loops through users account list
        for i in self.account:
            i.display_account_info()

    #transfers specifed amount of money from the specifed account of one user to the speficed account of another specified user
    def transfer_money(self, amount, account_number, other_user, other_user_account_number):
        self.make_withdraw(account_number, amount)
        other_user.make_deposit(other_user_account_number, amount)


Zach = User("Zach", "zach@mail.com", .01, 100)
Zach.open_account(.01, 200)
Zach.make_deposit(0, 200)
Zach.make_withdraw(1, 100)
Zach.display_user_balance(0)
Zach.display_all_accounts()

Frank = User("Frank", "frank@mail.com", .01, 2000)

print("1------------------------")
Zach.display_user_balance(1)
Frank.display_user_balance(0)
Frank.transfer_money(500,0,Zach,1)
print("3------------------------")
Frank.display_user_balance(0)
Zach.display_user_balance(1)
print("2------------------------")


account1=BankAccount(.01, 100)
account2=BankAccount(.01, 200)

account1.deposit(10).deposit(10).deposit(20).withdraw(40).yield_interest().display_account_info()
print("----------------------")
account2.deposit(100).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(101).yield_interest().display_account_info()
print("----------------------")
BankAccount.displayaccounts()