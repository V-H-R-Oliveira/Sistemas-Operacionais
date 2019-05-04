class Processo(object):
    def __init__(self, pid: int, nome: str, prioridade: str, quantum: int, dependencia: int):
        self.pid = pid
        self.nome = nome
        self.prioridade = prioridade
        self.quantum = quantum
        self.estado = 'P'
        self.dependencia = dependencia
        self.percentual = 0

    def __repr__(self):
        return "PID: {}\nNome: {}\nPrioridade: {}\nQuantum: {}\nEstado:{}\nDependência: {}\nPercentual: {}".format(self.pid, self.nome,
                                                                                                        self.prioridade, self.quantum
                                                                                                        , self.estado, self.dependencia,
                                                                                                        self.percentual)