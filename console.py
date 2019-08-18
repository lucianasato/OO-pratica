class CashMachineConsole:

    @staticmethod
    def get_menu_options_type():
        print("1 - Saldo")
        print("2 - Saque")
        return input('Escolha uma das opcoes acima: ')

    @staticmethod
    def call_operation():
        option_typed = CashMachineConsole.get_menu_options_type()