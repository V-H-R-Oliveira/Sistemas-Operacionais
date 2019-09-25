# -*- coding: utf-8 -*-

from memoria import Memoria
from processo import Processo
from disco import Disco
from menu import menu 

if __name__ == "__main__":
    menu()
    mem = Memoria()
    disco = Disco()
    processo = Processo(escrita=True)
    processo2 = Processo(escrita=True)
    processo3 = Processo(escrita=True)
    processo4 = Processo(escrita=False)
    
    mem.init_Mem()
    disco.init_Disco()
    
    if mem.mapear_processo(processo):
        print("[+] O processo 1 foi mapeado para a memória")
    
    if mem.mapear_processo(processo2):
        print("[+] O processo 2 foi mapeado para a memória")
    
    if mem.unmmap_processo(processo, disco):
         print("[+] O processo 1 foi desmapeado da memória")
    
    if mem.mapear_processo(processo3):
        print("[+] O processo 3 foi mapeado para a memória")
    
    if mem.mapear_processo(processo4):
        print("[+] O processo 4 foi mapeado para a memória")

    processo.escrever_Mem(mem, disco)
    processo.ler_Mem(mem, disco)
    
    mem.unmmap_processo(processo2, disco)
    processo2.ler_Mem(mem, disco)
    
    processo3.ler_Mem(mem, disco)
    
    processo3.escrever_Mem(mem, disco)
    processo2.escrever_Mem(mem, disco)
    
    mem.dump_Mem()
    disco.dump_Disco()
    
    mem.clear_Full_Mem()
    disco.clear_Disco()
  
