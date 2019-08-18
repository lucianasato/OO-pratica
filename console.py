import sys, getpass

from auth import AuthBankAccount

class AuthBankAccountConsole:

    @staticmethod
    def is_auth():
        account_number_typed = str(raw_input('Digite sua conta: '))
        password_typed = getpass.getpass('Digite sua senha: ')

        AuthBankAccount.authenticate(account_number_typed, password_typed)


class CashMachineConsole:

    @staticmethod
    def call_operation():
        option_typed = CashMachineConsole.get_menu_options_type()
        CashMachineOperation.do_operation(option_typed)

    @staticmethod
    def get_menu_options_type():
        print("1 - Saldo")
        print("2 - Saque")
        return input('Escolha uma das opcoes acima: ')


class CashMachineOperation:

    @staticmethod
    def do_operation(option):
        if option == 1:
            ShowBalanceOperation.do_operation()
        elif option == 2:
            WithDrawOperation.do_operation()


class ShowBalanceOperation:

    @staticmethod
    def do_operation():
        print('Mostrar Saldo')


class WithDrawOperation:

    @staticmethod
    def do_operation():
        print('Sacar dinheiro')