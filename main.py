from console import CashMachineConsole
from utils import clear, header

def main():
    clear()
    header()
    CashMachineConsole.call_operation()

if __name__ == '__main__':
    while True:
        main()

        input("Pressione <ENTER> para continuar...")