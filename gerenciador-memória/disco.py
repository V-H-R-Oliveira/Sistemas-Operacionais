# -*- coding: utf-8 -*-

from processo import Processo
import sys

class Disco(object):
    def __init__(self):
        self.__disco = [] 
        self.__mem_size = 512 # 16 kb * 32
        self.__mapa_bits_disco = [] # 0 = livre, 1 = ocupado
        
    def __repr__(self):
        return "[INFO] Memória secundária: {}\n".format(self.__disco)
    
    def get_Disco(self):
        return self.__disco

    def get_Mapa_Bits_Disco(self):
        return self.__mapa_bits_disco
    
    def init_Disco(self): 
        for i in range(self.__mem_size):
            self.__disco.append(0) 
            self.__mapa_bits_disco.append(0)

        print("\x1B[32m [+] Memória secundária foi alocada com sucesso... \x1B[0m")
    
    def clear_Disco(self):
        self.__disco.clear()
        self.__mapa_bits_disco.clear()
        print("\x1B[32m [+] Memória secundária foi desalocada... \x1B[0m")
        
    def dump_Disco(self):
        c = 0
        pag_index = 0
        
        if(len(self.__disco) != 0):
            for i in range(self.__mem_size):
                if i % 4 == 0:
                    print("\t ------------------------------------")
                    print("\t \x1B[96m [PAGINA] Página {} \x1B[0m".format("0x" + format(pag_index, '04x')))
                    print("\t ------------------------------------")
                    print()
                    pag_index += 1
                
                if c < 4:
                    print("\t \x1B[32m [+] endereço nº {} contém o processo ou o conteúdo {} \x1B[0m".format(
                        "0x" + format(i, '08x'), self.__disco[i]))
                    c += 1
                else:
                    c = 0
                    print("\t \x1B[32m [+] endereço nº {} contém o processo ou o conteúdo {} \x1B[0m".format(
                        "0x" + format(i, '08x'), self.__disco[i]))
        else:
            print("\x1B[31m [-] A memória se encontra desalocada \x1B[0m")
            
    def dump_Mapa_bits(self): # debug
        c = 0
        bloco = 0
        
        if(len(self.__disco) != 0):
            for i in range(self.__mem_size):
                if i % 4 == 0:
                    print("\t ------------------------------------")
                    print("\t \x1B[96m [BLOCO DISCO] Bloco {} \x1B[0m".format("0x" + format(bloco, '04x')))
                    print("\t ------------------------------------")
                    print()
                    bloco += 1
                
                if c < 4:
                    print("\t \x1B[32m [+] endereço nº {} contém o bit {} \x1B[0m".format(
                        "0x" + format(i, '08x'), self.__mapa_bits_disco[i]))
                    c += 1
                else:
                    c = 0
                    print("\t \x1B[32m [+] endereço nº {} contém o bit {} \x1B[0m".format(
                        "0x" + format(i, '08x'), self.__mapa_bits_disco[i]))
        else:
            print("\x1B[31m [-] O mapa de bits se encontra desalocado \x1B[0m")
    
    def __area_Livre(self):
        try:
            return self.__mapa_bits_disco.index(0)
        except ValueError:
            print("\x1B[31m [-] Memória está cheia... \x1B[0m")
            return None
                    
    def __encontrar_Processo(self, processo):
        try:
            return self.__disco.index(processo)
        except ValueError:
            print("\x1B[31m [-] Processo não se encontra mapeado na memória \x1B[0m")    
            return None  
        
    def swap_out(self, processo, memoria):
        pos_processo = self.__encontrar_Processo(processo)
        limite = pos_processo + 16
        c = 0
        
        if pos_processo is not None:
            for i in range(pos_processo, limite):
                if self.__mapa_bits_disco[i] == 1:
                    c += 1
                else:
                    print("\x1B[31m [-] O processo não está mapeado corretamente... \x1B[0m")
                    return False
            if c == 16:
                print(" \x1B[32m [INFO DISCO] Posição {} até {} serão desmapeadas e o processo {} será removido \x1B[0m".format(
                    pos_processo, limite, processo.id))
                for i in range(pos_processo, limite):
                    self.__disco[i] = 0
                    self.__mapa_bits_disco[i] = 0
                memoria.mapear_processo(processo)
            return True
        else:
            return False
                
    def swap_in(self, processo): 
        pos_livre = self.__area_Livre()
        limite = pos_livre + 16 
        c = 0
        
        if pos_livre is not None:
            for i in range(pos_livre, limite):
                if self.__mapa_bits_disco[i] == 0:
                    c += 1
                else:
                    print("\x1B[31m [-] Não possui espaço contínuo suficiente para armazenar o processo... \x1B[0m")
                    return False
            if c == 16:
                print("\x1B[32m [INFO DISCO] Posição {} até {} serão ocupadas pelo processo {} \x1B[0m".format(
                    pos_livre, limite, processo.id))
                for i in range(pos_livre, limite):
                    self.__disco[i] = processo
                    self.__mapa_bits_disco[i] = 1
            return True
        else:
            return False
        
    def page_Fault_Handler(self, processo):
        print("\x1B[31m [PAGE FAULT] O processo {} tentou acessar uma região de memória que não se encontra mapeada... \x1B[0m".format(
            processo))
        sys.exit(1)
