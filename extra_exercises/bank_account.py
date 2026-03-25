class Bank_account():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class person(Bank_account):
    def __init__(self, first_name, last_name, amount, password):
        super().__init__(first_name, last_name)
        self.account_name = first_name[0:2] + last_name[0:2]
        self.password = password
    def login(self, login_name, login_pass):
        if login_name == self.account_name and login_pass == self.password:
            return True

kund1 = person('John', 'Doe', 1203, '123abc')

print(f'Välkommen {kund1.first_name}')
print('Welcome to Python Bank!')
banking = kund1.login(input('Account name:'), input(f'Password: '))

while banking == True:
    input(f'What would you like')