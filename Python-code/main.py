from Processo import  Processo
from time import sleep
from random import randint

READY = 'P'
RUNNING = 'R'
BLOCKED = 'B'
FINISHED = 'F'

# kernel operation

# alloc memory - default = 2048
def allocMemory() -> list:
    return list()
# free memory
def freeMemory(mem: list):
    del mem

# add process to memory
def allocProcess(mem: list, processo: Processo) -> bool:
    if len(mem) <= 2048:
        mem.append(processo)
        return True
    print("Não existe espaço na memória")
    return False

# free process to memory
def freeProcess(mem: list, pid: int) -> bool:
    if len(mem) == 0:
        print("Memória vazia")
        return False
    for item in mem:
        if item.pid == pid:
            print("Item encontrado e pronto a ser removido", end='\n')
            mem.remove(item)
            return True

    print("O processo não se encontra na memória", end='\n')
    return False


# Process scheduler

def escalonador(mem: list):
    # primeiro - ordena os processo por prioridade

    fila, fila2 = [], []

    for p in mem:
        if p.prioridade == 'H':
            fila.append(p)
        elif p.prioridade == 'L':
            fila2.append(p)

    # organizar antes de executar


    # execução dos processos
    while True:
        # executa primeiro a fila prioritária, depois a fila não prioritária

        if len(fila) > 0:
            for proc in fila:
                print("----------------------------------------")
                print("Processo [{}] - {}".format(proc.pid, proc.nome))

                if proc.dependencia != 0: # com dependência
                    #proc.estado = 'B'
                    continue

                for d in fila:
                    if d.dependencia == proc.pid:
                        d.dependencia = 0
                        d.estado = READY
                proc.estado = READY

                while proc.quantum >= 0:
                    proc.percentual += 1
                    sleep(randint(1,3))
                    print("#" * proc.percentual)
                    proc.quantum -= 1

                print()
                freeProcess(mem, proc)
                fila.remove(proc)
        elif len(fila2) > 0:
            for prc in fila2:
                print("----------------------------------------", end="\n")
                print("Processo [{}] - {}".format(prc.pid, prc.nome), end="\n")

                if prc.dependencia != 0: # com dependência
                    #prc.estado = 'B'
                    continue

                for d in fila2:
                    if d.dependencia == prc.pid:
                        d.dependencia = 0
                        d.estado = READY
                prc.estado = READY

                while prc.quantum >= 0:
                    prc.percentual += 1
                    sleep(randint(1, 3))
                    print("#" * prc.percentual)
                    prc.quantum -= 1
                prc.estado = FINISHED

                print()
                if prc.estado == FINISHED:
                    print('Processo finalizado')
                    freeProcess(mem, prc)
                    fila2.remove(prc)
        else:
            break


# system monitor
# code 0 -> see all processes
# code 1 -> see ready processes
# code 2 -> see blocked processes

def monitor(mem: list, cod: int):
    if len(mem) == 0:
        print("Memória está vazia")
        return False

    # switch codes
    if cod == 0:
        print('Todos os processos na memória:')
        for process in mem:
            print("--------------")
            print("PID:", process.pid)
            print("Nome:", process.nome)
            print("Prioridade:", process.prioridade)
            print("Quantum:", process.quantum)
            print('Estado:', process.estado)
            print("Dependência:", process.dependencia)
            print("Percentual", process.percentual)
            print('-----------------')
    if cod == 1:
        pass
    if cod == 2:
        print("Processos bloqueados:")
        for process in mem:
            if process.estado == 'B':
                print("--------------")
                print("PID:", process.pid)
                print("Nome:", process.nome)
                print("Prioridade:", process.prioridade)
                print("Quantum:", process.quantum)
                print('Estado:', process.estado)
                print("Dependência:", process.dependencia)
                print("Percentual", process.percentual)
                print('-----------------')

mem = allocMemory()

processo: Processo = Processo(1, "init", "H", 2, 'P', 0, 0)
processo2: Processo = Processo(2, "todo", "L", 2, 'B', 3, 0)
processo3: Processo = Processo(3, "nothing", "L", 2, 'B', 5, 0)
processo4: Processo = Processo(4, "thang", "H", 2, 'P', 6, 0)
processo5: Processo = Processo(5, "teste", "L", 2, 'P', 0, 0)
processo6: Processo = Processo(6, 'prior', 'H', 2, 'B', 1, 0)


allocProcess(mem, processo)
allocProcess(mem, processo2)
allocProcess(mem, processo3)
allocProcess(mem, processo4)
allocProcess(mem, processo5)
allocProcess(mem, processo6)

escalonador(mem)

freeMemory(mem)
