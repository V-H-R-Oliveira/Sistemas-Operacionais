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
            syslib.showProcesses(mem)
            sleep(2)
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
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    except (ValueError, EOFError, KeyboardInterrupt):
        os.system('cls' if os.name == 'nt' else 'clear')
        syslib.deleteMem(mem)
        print("Programa finalizado !!!")
        break

'''
processo: Processo = Processo(1, "init", "H", 2, 'P', 0, 0)
processo2: Processo = Processo(2, "todo", "L", 2, 'P', 3, 0)
processo3: Processo = Processo(3, "nothing", "L", 2, 'P', 5, 0)
processo4: Processo = Processo(4, "thang", "H", 2, 'P', 6, 0)
processo5: Processo = Processo(5, "teste", "L", 2, 'P', 0, 0)
processo6: Processo = Processo(6, 'prior', 'H', 2, 'P', 7, 0)
processo7: Processo = Processo(7, 'deep', 'H', 2, 'P', 1, 0)
'''