import threading
import time
import random
from os import getcwd

file = open(getcwd() + '/output.txt', 'a')
TAM = 1000
regiaoCritica = []

sem = threading.Semaphore()
index = 0

def produzir(name: str):
  global index
  if len(regiaoCritica) < TAM:
    sem.acquire()
    if index > len(regiaoCritica):
        index -= len(regiaoCritica)
    qtd = [x for x in range(10)]
    for i in range(10):
      print("Processo {} inclui posição {}".format(name, index))
      file.write("Processo {} inclui posição {}\n".format(name, index))
      index += 1
      time.sleep(2)
    regiaoCritica.extend(qtd)
    sem.release()
    time.sleep(1)
  else:
    print("Processo {} esperando alguém consumir o buffer".format(name))
    file.write("Processo {} esperando alguém consumir o buffer\n".format(name))

def consumir(name: str):
  global index
  if len(regiaoCritica) > 0:
    sem.acquire()
    for i in range(10):
        valor = regiaoCritica.pop(0)
        print("Processo {} remove posição {}".format(name, valor))
        file.write("Processo {} remove posição {}\n".format(name, valor))
        index -= 1
        time.sleep(2)
    sem.release()
    time.sleep(1)
  else:
      print("Processo {} esperando a produção de algum item".format(name))
      file.write("Processo {} esperando a produção de algum item\n".format(name))


def main():
    t1 = threading.Thread(target=produzir, args=("Produtor 1",))
    t2 = threading.Thread(target=produzir, args=("Produtor 2",))
    t3 = threading.Thread(target=produzir, args=("Produtor 3",))
    t4 = threading.Thread(target=produzir, args=("Produtor 4",))
    t5 = threading.Thread(target=produzir, args=("Produtor 5",))
    t6 = threading.Thread(target=consumir, args=("Consumidor 1",))
    t7 = threading.Thread(target=consumir, args=("Consumidor 2",))
    t8 = threading.Thread(target=consumir, args=("Consumidor 3",))
    t9 = threading.Thread(target=consumir, args=("Consumidor 4",))
    t10 = threading.Thread(target=consumir, args=("Consumidor 5",))
    lista = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
    lista2 = [x for x in range(9)]

    for i in range(200):
        random.shuffle(lista2) # embaralha o ordem de começo da thread
        for i in lista2:
            try:
                lista[i].start()
                lista[i].join()
                del lista[i] # deleta a thread após ela fazer o seu serviço
            except IndexError:
                continue # caso não exista o index desejado, ele começa no próximo index
    file.close()

if __name__ == '__main__':
    main()