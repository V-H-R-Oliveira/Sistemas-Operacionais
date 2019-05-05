from Processo import Processo
from SysLib import SysLib
from time import sleep
import os

def menu():
    print('---------------------------------')
    print('0 - Sair do programa')
    print('1 - Cadastrar um processo')
    print('2 - Acessar monitor')
    print('3 - Escalonar processos')
    print('---------------------------------')
    print()

def menuMonitor():
    print('---------------------------------')
    print('1 - Exibir os processos na memória')
    print('2 - Exibir os processos nas filas múltiplas')
    print('---------------------------------')
    print()

syslib: SysLib = SysLib()
mem = syslib.createMem()

while True:
    try:
        menu()
        op: int = int(input('Digite um código: '))
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            pid = len(mem) + 1
            nome: str = input('Digite o nome do processo: ')
            prioridade: str = input("Digite a prioridade (H ou L): ").upper()
            quantum: int = int(input("Digite o quantum do processo: "))
            dependencia: int = int(input("Digite o pid do processo dependente (0 = sem dependência): "))
            processo: Processo = Processo(pid, nome, prioridade, quantum, dependencia)
            syslib.storeProcess(mem, processo)
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            menuMonitor()
            code: int = int(input("Digite o código de acesso do monitor: "))
            syslib.showProcesses(mem, code)
            sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Iniciando o processo de escalonamento")
            syslib.scheduler(mem)
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            syslib.deleteMem(mem)
            sleep(2)
            print("Programa finalizado !!!")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    except (ValueError, EOFError, KeyboardInterrupt):
        os.system('cls' if os.name == 'nt' else 'clear')
        syslib.deleteMem(mem)
        print("Programa finalizado !!!")
        break
'''
processo: Processo = Processo(1, "init", "H", 2, 0) 
processo2: Processo = Processo(2, "todo", "L", 2, 3) 
processo3: Processo = Processo(3, "nothing", "L", 2, 5) 
processo4: Processo = Processo(4, "thang", "H", 2, 6) 
processo5: Processo = Processo(5, "teste", "L", 2, 0) 
processo6: Processo = Processo(6, 'prior', 'H', 2, 7)
processo7: Processo = Processo(7, 'deep', 'H', 2, 1)
processo8: Processo = Processo(8, 'highlow', 'H', 2, 3)
processo9: Processo = Processo(9, 'lowhigh', 'L', 2, 4)

syslib.storeProcess(mem, processo)
syslib.storeProcess(mem, processo2)
syslib.storeProcess(mem, processo3)
syslib.storeProcess(mem, processo4)
syslib.storeProcess(mem, processo5)
syslib.storeProcess(mem, processo6)
syslib.storeProcess(mem, processo7)
syslib.storeProcess(mem, processo8)
syslib.storeProcess(mem, processo9)

syslib.scheduler(mem)

'''