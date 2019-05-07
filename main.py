from Processo import Processo
from SysLib import SysLib
from time import sleep
from os import system, name
from layout import menu, menuMonitor

syslib: SysLib = SysLib()
mem: list = syslib.createMem()

while True:
    try:
        menu()
        op: int = int(input('Digite um código: '))
        if op == 1:
            system('cls' if name == 'nt' else 'clear')
            pid: int = len(mem) + 1
            nome: str = input('Digite o nome do processo: ')
            prioridade: str = input("Digite a prioridade (H ou L): ").upper()
            quantum: int = int(input("Digite o quantum do processo: "))
            dependencia: int = int(input("Digite o pid do processo dependente (0 = sem dependência): "))
            if dependencia == 0:
                processo: Processo = Processo(pid, nome, prioridade, quantum, dependencia, 0)
                syslib.storeProcess(mem, processo)
                sleep(2)
                system('cls' if name == 'nt' else 'clear')
                continue
            dado: int = int(input("Digite o dado de dependência (sem dado = 0): "))
            processo: Processo = Processo(pid, nome, prioridade, quantum, dependencia, dado)
            syslib.storeProcess(mem, processo)
            sleep(2)
            system('cls' if name == 'nt' else 'clear')
            continue
        elif op == 2:
            system('cls' if name == 'nt' else 'clear')
            menuMonitor()
            code: int = int(input("Digite o código de acesso do monitor: "))
            syslib.showProcesses(mem, code)
            sleep(5)
            system('cls' if name == 'nt' else 'clear')
            continue
        elif op == 3:
            system('cls' if name == 'nt' else 'clear')
            print("Iniciando o processo de escalonamento")
            syslib.scheduler(mem)
            sleep(2)
            system('cls' if name == 'nt' else 'clear')
        else:
            system('cls' if name == 'nt' else 'clear')
            syslib.deleteMem(mem)
            sleep(2)
            print("Programa finalizado !!!")
            system('cls' if name == 'nt' else 'clear')
            break
    except (ValueError, EOFError, KeyboardInterrupt):
        system('cls' if name == 'nt' else 'clear')
        syslib.deleteMem(mem)
        print("Programa finalizado !!!")
        break

'''
processo: Processo = Processo(1, "init", "H", 2, 0) 
processo2: Processo = Processo(2, "todo", "L", 2, 3)
processo3: Processo = Processo(3, "nothing", "L", 5, 5, 8) # possui um dado do 8
processo4: Processo = Processo(4, "thang", "H", 2, 6)
processo5: Processo = Processo(5, "teste", "L", 2, 0)
processo6: Processo = Processo(6, 'prior', 'H', 2, 7)
processo7: Processo = Processo(7, 'deep', 'H', 5, 1, 9) # possui um dado do 9
processo8: Processo = Processo(8, 'highlow', 'H', 2, 3)
processo9: Processo = Processo(9, 'lowhigh', 'L', 2, 4)
processo10: Processo = Processo(10, 'p10', 'H', 2, 0)
processo11: Processo = Processo(11, 'p11', 'L', 2, 0)
processo12: Processo = Processo(12, 'p12', 'H', 2, 0)
processo13: Processo = Processo(13, 'p13', 'L', 2, 0)
processo14: Processo = Processo(14, 'p14', 'H', 2, 0)
processo15: Processo = Processo(15, 'p15', 'L', 2, 0)
processo16: Processo = Processo(16, 'p16', 'H', 2, 0)
processo17: Processo = Processo(17, 'p17', 'L', 2, 0)
processo18: Processo = Processo(18, 'p18', 'H', 2, 0)
processo19: Processo = Processo(19, 'p19', 'L', 2, 0)
processo20: Processo = Processo(20, 'p20', 'H', 2, 0)

syslib.storeProcess(mem, processo)
syslib.storeProcess(mem, processo2)
syslib.storeProcess(mem, processo3)
syslib.storeProcess(mem, processo4)
syslib.storeProcess(mem, processo5)
syslib.storeProcess(mem, processo6)
syslib.storeProcess(mem, processo7)
syslib.storeProcess(mem, processo8)
syslib.storeProcess(mem, processo9)
syslib.storeProcess(mem, processo10)
syslib.storeProcess(mem, processo11)
syslib.storeProcess(mem, processo12)
syslib.storeProcess(mem, processo13)
syslib.storeProcess(mem, processo14)
syslib.storeProcess(mem, processo15)
syslib.storeProcess(mem, processo16)
syslib.storeProcess(mem, processo17)
syslib.storeProcess(mem, processo18)
syslib.storeProcess(mem, processo19)
syslib.storeProcess(mem, processo20)

#ordem de execução 
# 1 7 (block) 6 4 9 7 
# 5 3(block) 2 8 3 
# resto sem dependencia é normal

syslib.scheduler(mem) '''
