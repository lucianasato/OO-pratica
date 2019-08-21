class BankAccount:
    def __init__(self, account_number, name, password, value, admin):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.value = value
        self.admin = admin

    def check_account_number(self, account_number):
        return account_number == self.account_number

    def check_account_password(self, account_password):
        return account_password == self.password

class CashMachine:

    def __init__(self, money_slips):
        self.money_slips = money_slips
        self.money_slips_user = {}
        self.value_remaining = 0

accounts_list = [
    BankAccount('0001', 'Fulano 1', '123', 100, False),
    BankAccount('0002-02', 'Fulano 2', '123456', 50, False),
    BankAccount('1111-11', 'Fulano 3', '123456', 1000, True),
]