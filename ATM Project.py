"""
Purpose: To practice implementing and using python classes
Authors: Phan Anh Le
Date: April 28, 2023
CS111
"""
class BankAccount:
    def __init__(self, balance):
        '''
        Purpose: Takes the initial balance from the user.

        Parameters:
            self: instance variable.
            balance: initial amount of money in your account.
        '''
        self._balance = balance

    def check_balance(self):
        '''
        Purpose: Returns the amount of money in your balance.

        Parameter:
            self: instance variable.

        Return: amount of money in your balance.
        '''
        return self._balance
    
    def withdraw(self, amount):
        '''
        Purpose: Decrease the amount of money in the account by a certain amount.

        Parameters:
            self: instance variable.
            amount: amount of money to withdraw.
        
        Return: amount of money in your balance.
        '''
        if not isinstance (amount, int) or amount <= 0: #makes sure that input is a number, and that it is not negative
            print ("Invalid amount of money, please try again.")
            return self._balance
        
        if amount > self._balance:       #if the balance is too small to take out a certain amount
            print("Insufficient funds. Please try again.")
            return self._balance
        else: 
            self._balance = self._balance - amount 
            fifty = amount//50                      #this will, starting with the largest bill, check how many of that bill fit, then subtract and move to the next.
            amount = amount - fifty*50 
            twenty = amount//20
            amount = amount - twenty*20
            ten = amount//10
            amount = amount - ten*10
            five = amount//5
            amount = amount - five*5
            one = amount//1             #then it prints how many of each bill adds up to the amount they wanted to withdraw
            print("You will recieve: " + str(fifty) + " (50 Dollar Bills), " + str(twenty) + " (20 Dollar Bills), " + str(ten) + " (10 Dollar Bills), " +str(five) + " (5 Dollar Bills), " + str(one) + " (1 Dollar Bills) ")
            return self._balance
    
    def deposit(self, amount):
        '''  
        Purpose: Increase the amount of money in the account by a certain amount.

        Parameters:
            self: instance variable.
            amount: amount of money to deposit.
        
        Return: amount of money in your balance.
        '''
        if not isinstance (amount, int) or amount <= 0: #checks to see if the input is an integer and greater than 0
            print ("Invalid amount of money, please try again.")
            return self._balance
        self._balance = self._balance + amount  # adds the amount to the balance
        return self._balance


def ATM():
    '''
    Purpose: Simulate an ATM interface for a bank account.

    This function allows users to interact with their bank account. Users can check their balance, withdraw money, deposit money, and log out.

    Return value: None
    '''
    val = 0
    while val != 1:        #making sure it loops until the input is appropriate
        try:
            start_amount = int(input("What is the accounts balance?: ")) 
            if start_amount >= 0:            #making sure the starting amount is greater or equals to 0
                val = val + 1
            else: 
                print("Invalid amount of money, please try again.")
        except:
            print("Invalid amount of money, please try again.")

    account = BankAccount(start_amount)
    log = 0
    while log != 1:  #loops until logout, which will make log = 1 and end the loop
        try:
            choice = int(input("What would you like to do? 1: Check your balance, 2: Withdraw from your balance, 3: Deposit, 4: Log Out: "))  #if the input is not an integer, tell the user and try again
            if 0 < choice < 5:   #if the integer is not 1-4, tell the user and try again
                if choice == 1:
                    print("Your balance is:", account.check_balance())
                elif choice == 2:
                    try: 
                        amount = int(input("How much would you like to withdraw?: "))
                        print("Your balance is:", account.withdraw(amount))
                    except ValueError:
                        print("Invalid amount of money, please try again.")
                elif choice == 3:       
                    try: 
                        amount = int(input("How much would you like to deposit?: "))
                        print("Your balance is:", account.deposit(amount))
                    except ValueError:
                        print("Invalid amount of money, please try again.") 
                elif choice == 4:
                    print("Logging out of ATM. Thank you for using this service.")
                    log = log + 1    #ends the loop
            else:
                print("Invalid choice, please indicate your option from 1-4")
        except ValueError:
            print("Invalid choice, please enter a number.")
                
def main():
    '''
    Purpose: Calls main function to run the code

    Return Value: None
    '''
    ATM()
    
if __name__ == "__main__":
    main()




            
