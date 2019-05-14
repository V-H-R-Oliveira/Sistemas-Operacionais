from time import sleep
from random import randint

class Kernel(object):
    #flags
    READY = 'P'
    RUNNING = 'R'
    BLOCKED = 'B'
    FINISHED = 'F'

    # create memory
    def allocMemory(self) -> list:
        return list()

    # free memory
    def freeMemory(self, mem: list):
        del mem

    # add process to memory
    def allocProcess(self, mem: list, processo) -> bool:
        if len(mem) <= 2048:
            mem.append(processo)
            return True
        print("Não existe espaço na memória")
        return False

    # free process to memory
    def freeProcess(self, mem: list, pid: int) -> bool:
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

    #filas múltiplas
    def filasMultiplas(self, mem) -> tuple:
        fila, fila2 = [], []

        # salva nas filas sem gerenciar depedendências
        for p in mem:
            if p.prioridade == 'H':
                fila.append(p)
            if p.prioridade == 'L':
                fila2.append(p)

        # gerenciamento de dependências
        for ph in fila:
            for pl in fila2:
                if ph.dependencia == pl.pid:
                    ph.prioridade = 'L'
                    fila2.append(ph)
                    fila.remove(ph)

        # gerenciamento de dependências
        for pl in fila2:
            for ph in fila:
                if pl.dependencia == ph.pid:
                    pl.prioridade = 'H'
                    fila.append(pl)
                    fila2.remove(pl)

        return fila, fila2

    # Process scheduler
    def escalonador(self, mem: list):

        fila, fila2 = self.filasMultiplas(mem)

        while True:
            if len(fila) > 0:
                print('Fila prioritária: ')
                print()
                for proc in fila:
                    print("----------------------------------------")
                    print("Processo [{}] - {} - estado {}".format(proc.pid, proc.nome, proc.estado))

                    if proc.dependencia != 0:  # com dependência
                        proc.estado = self.BLOCKED
                        print("Processo [{}] - {} - estado {}".format(proc.pid, proc.nome, proc.estado))
                        continue

                    for d in fila:
                        if d.dependencia == proc.pid:
                            d.dependencia = 0
                            d.estado = self.READY

                    if proc.estado == self.BLOCKED:
                        proc.estado = self.READY
                        print("Processo [{}] - {} - estado {}".format(proc.pid, proc.nome, proc.estado))

                    proc.estado = self.RUNNING

                    if proc.estado == self.RUNNING:
                        print("Processo [{}] - {} - estado {}".format(proc.pid, proc.nome, proc.estado))

                        if proc.dado != 0:
                            blockP: int = randint(1, proc.quantum) # irá executar até block
                            tempP: int = blockP # guarda para executar posteriormente
                            while proc.quantum > blockP:
                                proc.percentual += 1
                                sleep(randint(1, 3))
                                print("+" * proc.percentual)
                                proc.quantum -= 1
                            proc.estado = self.BLOCKED
                            print(
                                "Processo [{}] - {} - estado {} - Precisa do {} do processo {} - percentual {}%".format(
                                    proc.pid,
                                    proc.nome,
                                    proc.estado,
                                    tempP,
                                    proc.dado,
                                    proc.percentual))
                            proc.quantum = tempP # atualiza o quantum
                            proc.dado = 0
                            continue
                        if proc.dado == 0:
                            while proc.quantum > 0:
                                proc.percentual += 1
                                sleep(randint(1, 3))
                                print("#" * proc.percentual)
                                proc.quantum -= 1
                            proc.estado = self.FINISHED
                    print()
                    if proc.estado == self.FINISHED:
                        print('Processo finalizado')
                        self.freeProcess(mem, proc.pid)
                        fila.remove(proc)
            elif len(fila2) > 0:
                print('Fila não prioritária: ')
                print()
                for prc in fila2:
                    print("----------------------------------------", end="\n")
                    print("Processo [{}] - {} - estado {}".format(prc.pid, prc.nome, prc.estado), end="\n")

                    if prc.dependencia != 0:  # com dependência
                        prc.estado = self.BLOCKED
                        print("Processo [{}] - {} - estado {}".format(prc.pid, prc.nome, prc.estado))
                        continue

                    for d in fila2:
                        if d.dependencia == prc.pid:
                            d.dependencia = 0
                            d.estado = self.READY

                    if prc.estado == self.BLOCKED:
                        prc.estado = self.READY
                        print("Processo [{}] - {} - estado {}".format(prc.pid, prc.nome, prc.estado))
                    prc.estado = self.RUNNING

                    if prc.estado == self.RUNNING:
                        print("Processo [{}] - {} - estado {}".format(prc.pid, prc.nome, prc.estado))

                        if prc.dado != 0:
                            block: int = randint(1, prc.quantum) # irá executar até block
                            temp = block # guarda para executar posteriormente
                            while prc.quantum > block:
                                prc.percentual += 1
                                sleep(randint(1, 3))
                                print("*" * prc.percentual)
                                prc.quantum -= 1
                            prc.estado = self.BLOCKED
                            print("Processo [{}] - {} - estado {} - Precisa do {} do processo {} - percentual {}%"
                                  .format(prc.pid, prc.nome, prc.estado, temp, prc.dado, prc.percentual))
                            prc.quantum = temp # atualiza o quantum
                            prc.dado = 0
                            continue
                        if prc.dado == 0:
                            while prc.quantum > 0:
                                prc.percentual += 1
                                sleep(randint(1, 3))
                                print("#" * prc.percentual)
                                prc.quantum -= 1
                            prc.estado = self.FINISHED
                    print()
                    if prc.estado == self.FINISHED:
                        print('Processo finalizado')
                        self.freeProcess(mem, prc.pid)
                        fila2.remove(prc)
            else:
                break

    # system monitor
    # code 1 - all processes
    # code 2 - queue content
    def monitor(self, mem: list, code: int):
        if len(mem) == 0:
            print("Memória está vazia")
            return False
        if code == 1:
            print('Todos os processos na memória:')
            for process in mem:
                print("--------------")
                print("PID:", process.pid)
                print("Nome:", process.nome)
                print("Prioridade:", process.prioridade)
                print("Quantum:", process.quantum)
                print('Estado:', process.estado)
                print("Dependência:", process.dependencia)
                print("Dado:", process.dado)
                print("Percentual", process.percentual)
                print('-----------------')
                print()
        elif code == 2:
            fila, fila2 = self.filasMultiplas(mem)
            print('----------------------------------------')
            print('Apenas o PID dos processos')
            print("Fila prioritária:", [x.pid for x in fila])
            print("Fila não prioritária: ", [x.pid for x in fila2])
            print('----------------------------------------')
            print()
        else:
            print('Código inválido')
            return False
