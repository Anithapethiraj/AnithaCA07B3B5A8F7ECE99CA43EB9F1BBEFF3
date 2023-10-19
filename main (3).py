class Bankaccount:

  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=initial_balance
  def deposit(self,amount):
    if amount > 0:
      self.__account_balance+=amount
      print("Deposited amount:₹{}.New balance ₹{}".format(amount,self.__account_balance))
    else:
      print("Invalid deposit amount.please deposit a positive amount")
  def withdraw(self,amount):
    if amount >0 and amount <=self.__account_balance:
      self.__account_balance-=amount
      print("Withdraw ₹{}.New balance:₹{}".format(amount,self.__account_balance))
    else:
      print("Insufficient balance")
  def display_balance(self):
    print("Account balance for {}(Account #{}): ₹{}".format( self.__account_holder_name,self.__account_number,self.__account_balance))

account=Bankaccount(account_number="1234567890",account_holder_name="Akshaya Rathinam",initial_balance=500.00)
account.display_balance()
account.deposit(500.00)
account.withdraw(500.00)