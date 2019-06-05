class Processo(object):
    def __init__(self, pid: int, nome: str, prioridade: str, quantum: int, dependencia: int, dado: int = 0):
        self.pid = pid
        self.nome = nome
        self.prioridade = prioridade
        self.quantum = quantum
        self.estado = 'P'
        self.dependencia = dependencia
        self.percentual = 0
        self.dado = dado # irá ser o pid do processo dependente

    def __repr__(self):
        return "PID: {}\nNome: {}\nPrioridade: {}\nQuantum: {}\nEstado:{}\nDependência: {}\nPercentual: {}\nDado: {}"\
            .format(self.pid, self.nome, self.prioridade, self.quantum, self.estado, self.dependencia, self.percentual, self.dado)