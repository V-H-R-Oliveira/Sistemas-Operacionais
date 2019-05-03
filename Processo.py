class Processo(object):
    def __init__(self, pid: int, nome: str, prioridade: str, quantum: int, estado:str, dependencia: int, percentual:int):
        self.pid = pid
        self.nome = nome
        self.prioridade = prioridade
        self.quantum = quantum
        self.estado = estado
        self.dependencia = dependencia
        self.percentual = percentual

    def __repr__(self):
        return "PID: {}\nNome: {}\nPrioridade: {}\nQuantum: {}\nEstado:{}\nDependência: {}\nPercentual: {}".format(self.pid, self.nome,
                                                                                                        self.prioridade, self.quantum
                                                                                                        , self.estado, self.dependencia,
                                                                                                        self.percentual)