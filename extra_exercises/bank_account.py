class Bank_account():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        

class Person(Bank_account):
    def __init__(self, first_name, last_name, amount, password):
        super().__init__(first_name, last_name)
        self.account_name = first_name[0:2] + last_name[0:2]
        self.password = password
        self.amount = amount
    def login(self, login_name, login_pass):
        if login_name == self.account_name and login_pass == self.password:
            return True
        else:
            return False
    def withdrawal(self, withraw_amount):
        self.amount -= withraw_amount
        print(f'Your new balance is: {self.amount} \n')
    def deposits(self, deposit_amount):
        self.amount += deposit_amount
        print(f'Your new balance is: {self.amount} \n')

kund1 = Person('John', 'Doe', 1203, '123abc')
kund2 = Person('Julia', 'Krigare', 63589, '123456')
banking = None

customers = [kund1, kund2]
loggedin = False
print(f'Welcome to Python Bank! Please log in. \n')
while loggedin == False:
    startup_choice = input(f'What do you want to do? \n 1. Log in. \n 2. Check accounts \n 3. Open new account \n')
    try:
        if int(startup_choice) == 1:
            input_name = input('Account name:')
            input_pass = input(f'Password: ')
            #Trying to login
            for c in customers:
                if c.login(input_name, input_pass) == True:
                    banking = c
                    loggedin = True
                    break
        elif int(startup_choice) == 2:
            for c in customers:
                print(f'{c.first_name} \n')
        elif int(startup_choice) == 3:
            new_account_name = input('Name: ')
            new_account_lname = input('Last name: ')
            new_account_pass = input('Password: ')
            kund3 = Person(new_account_name, new_account_lname,0 , new_account_pass)
            customers.append(kund3)
    except ValueError:
        print('Value error')
        continue



print(f'Välkommen {banking.first_name}')

while loggedin == True:
    choice = input(f'What would you like to do? \n 1.Check account balance \n 2. Deposit \n 3. Withdraw \n 4. Logout \n')
    try:
        if int(choice) == 1:
            print(f'Account Balance {banking.amount} \n')
        elif int(choice) == 2:
            banking.deposits(int(input('Deposit amount: ')))
        elif int(choice) == 3:
            banking.withdrawal(int(input('Withdrawal Amount: ')))
        elif int(choice) == 4:
            print('Goodbye!')
            break
    except ValueError:
        continue
