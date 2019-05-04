from Kernel import Kernel

class SysLib(object):
    def __init__(self):
        self.__kernel = Kernel()

    def createMem(self) -> list:
        return self.__kernel.allocMemory()

    def storeProcess(self, mem: list, processo) -> bool:
        return self.__kernel.allocProcess(mem, processo)

    def removeProcess(self, mem: list, pid: int) -> bool:
        return self.__kernel.freeProcess(mem, pid)

    def deleteMem(self, mem: list):
        return self.__kernel.freeMemory(mem)

    def scheduler(self, mem: list):
        return self.__kernel.escalonador(mem)

    def showProcesses(self, mem: list):
        return self.__kernel.monitor(mem)