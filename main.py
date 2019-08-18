from console import CashMachineConsole, AuthBankAccountConsole
from utils import clear, header
import sys

def main():
    clear()
    header()

    AuthBankAccountConsole.is_auth()
    #CashMachineConsole.call_operation()


if __name__ == '__main__':
    while True:
        main()

        input('Pressione <ENTER> para continuar...')
