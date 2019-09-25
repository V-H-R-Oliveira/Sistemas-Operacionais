# -*- coding: utf-8 -*-

import uuid

# a leitura deve ser obrigatória

class Processo(object):
    def __init__(self, escrita):
        self.id = uuid.uuid4()
        self.tamanho = 16
        self.bit_escrita = escrita
        self.base = None
   
    def __repr__(self):
        return "{}".format(self.id)

    # recebe um processo e pergunta via stdin o que 
    # ele deseja ler na memória e caso leia uma página não mapeada,
    # ou seja, páginas que estão com o valor 0, ele retorna page fault

    def ler_Mem(self, memoria, disco): 
        if self in memoria.get_Mem():
            while True:
                paginas = list(map(int, input("[FROM RAM] Quais páginas você deseja acessar: ").split()))
                if len(paginas) == 0:
                    break
                self.__read_Mem(paginas, memoria)
        elif self in disco.get_Disco():
            if disco.swap_out(self, memoria):
                while True:
                    paginas = list(map(int, input("[FROM DISCO] Quais páginas você deseja acessar: ").split()))
                    if len(paginas) == 0:
                        break
                    self.__read_Mem(paginas, memoria)
            else:
                print("\x1B[31m [-] O processo {} não está mapeado na memória... \x1B[0m".format(self.id))
        else:
            print("\x1B[31m [-] O processo {} não está mapeado na memória... \x1B[0m".format(self.id))
    
    def __read_Mem(self, paginas, memoria):
        mapa_bits = memoria.get_Mapa_Bits()
        mem_fisica = memoria.get_Mem()
        c = 0
        
        for i in paginas:
            i += self.base 
            if mapa_bits[i] == 0:
                memoria.page_Fault_Handler(self)
            elif str(self) not in str(mem_fisica[i]):
                print("\x1B[31m [-] O processo {} tentou ler uma região de memória está mapeada para outro processo... \x1B[0m".format(
                    self.id))
                break
            else:
                if self == mem_fisica[i]:
                    print("\x1B[32m [MMU] {} => {} => {} \x1B[0m ".format(
                        "0x" + format(paginas[c], '08x'), "0x" + format(i, '08x'), mem_fisica[i]))
                    c += 1
                else:
                    print("\x1B[32m [MMU] {} => {} => {} \x1B[0m ".format(
                        "0x" + format(paginas[c], '08x'), "0x" + format(i, '08x'), mem_fisica[i][39:])) # pega depois de "=>"
    
    # recebe um processo e pergunta via stdin o que 
    # ele deseja escrever na memória e caso leia uma página não mapeada,
    # ou seja, páginas que estão com o valor 0, ele retorna page fault
    
    def escrever_Mem(self, memoria, disco): # falta verificar se o processo possui permissão de escrita
        if self in memoria.get_Mem() and self.bit_escrita:
            while True:
                paginas = list(map(int, input("[FROM RAM] Quais endereços você deseja escrever: ").split()))
                if len(paginas) == 0:
                    break
                conteudo = list(map(str, input("[FROM RAM] Quais os conteúdos que você deseja escrever nas respectivas páginas: ").split()))
                if len(conteudo) == 0:
                    break
                self.__write_Mem(paginas, conteudo, memoria)
        elif self in memoria.get_Mem() and not self.bit_escrita:
            print("\x1B[31m [-] O processo {} não possui permissão de escrita na memória \x1B[0m".format(
                self.id))
        elif self in disco.get_Disco() and self.bit_escrita:
            if disco.swap_out(self, memoria):
                while True:
                    paginas = list(map(int, input("[FROM DISCO] Quais endereços você deseja escrever: ").split()))
                    if len(paginas) == 0:
                        break
                    conteudo = list(map(str, input("[FROM DISCO] Quais os conteúdos que você deseja escrever nas respectivas páginas: ").split()))
                    if len(conteudo) == 0:
                        break
                    self.__write_Mem(paginas, conteudo, memoria)
            else:
                print("\x1B[31m [-] O processo {} não está mapeado na memória... \x1B[0m".format(self.id))
            
        elif self not in memoria.get_Mem():
            print("\x1B[31m [-] O processo {} não está mapeado na memória... \x1B[0m".format(self.id))
    
    def __write_Mem(self, paginas, conteudo, memoria):
        mapa_bits = memoria.get_Mapa_Bits()
        mem_fisica = memoria.get_Mem()
        j = 0
        c = 0
            
        for i in paginas:
            i += self.base
            if mapa_bits[i] == 0:
                memoria.page_Fault_Handler(self.id)
            elif self != mem_fisica[i]:
                print("\x1B[31m [-] O processo {} tentou escrever na região de memória de outro processo... \x1B[0m".format(
                    self.id))
                break
            else:
                mem_fisica[i] = str(str(self) + " => " + conteudo[j])
                print("\x1B[32m [MMU] {} => {} => {} \x1B[0m ".format(
                        "0x" + format(paginas[c], '08x'), "0x" + format(i, '08x'), conteudo[j]))
                c += 1
                j += 1