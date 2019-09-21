import random

class noh:
    def iniciaNoh(self, value):
       self.value = value
       self.prox = None
       self.back = None 
    def printa(self):
       print(self.value)
       if self.prox != None:
           self.prox.printa()
    def addNohRec (self, value):
       if self.value > value:
          no = noh()
          no.iniciaNoh(self.value)
          no.prox = self.prox
          self.value = value
          self.prox = no
       elif self.prox == None:
          no = noh()
          no.iniciaNoh(value)
          no.back = self
          self.prox = no
       else:
          self.prox.addNohRec(value)
           
class Lista:
    def iniciaDesc(self, nome=None):
       self.name = nome
       self.quantidade = 0
       no = noh()
       no.iniciaNoh(None)
       self.inicio = no
       self.fim = None
    def escreve(self):
       print(self.name,'-', self.quantidade)
       self.inicio.printa()
    def adicionaNoh(self, value):
       if self.quantidade == 0:
          no = noh()
          no.iniciaNoh(value)
          self.inicio = no
       else:
          self.inicio.addNohRec(value)
       self.quantidade += 1  

lista = Lista()
lista.iniciaDesc('Cagão')

for i in range(0, 30):
    lista.adicionaNoh(random.randrange(0, 1000))

lista.escreve()
