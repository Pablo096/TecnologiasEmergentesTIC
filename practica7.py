# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:45:51 2020

@author: Pablo
"""


# SEGUNDO SISTEMA EXPERTO 
from experta import Rule, Fact, KnowledgeEngine, AND
from random import choice


class Cajero(KnowledgeEngine):
        
    @Rule( AND(
              Fact(transaccionValida='si'), Fact(tipo='extraccion')
              )                 
         )
    def realizarExtraccion(self):
        print("Pedir Monto")
        print("Descontar Monto de la Cuenta")
        print("Generar Comprobante")
        
        
        
    @Rule( AND(
              Fact(transaccionValida='si'), Fact(tipo='depositar')
              )                 
         )
    def realizarDeposito(self):
        print("Pedir Monto")
        print("Sumar Monto a la Cuenta")
        print("Generar Comprobante")
        
    @Rule( AND(
              Fact(transaccionValida='si'), Fact(tipo='saldo')
              )                 
         )
    def consultarSaldo(self):
        print("Obtener Saldo")
        print("Generar Comprobante")

        
    @Rule( Fact(transaccionValida='no') )
    def transaccionNoExitosa(self):
        print("Error: La operación no se puede realizar")


engine = Cajero()
engine.reset()

#engine.declare(Fact(transaccionValida = choice(['si','no'])))
#engine.declare(Fact(tipo = choice(['extraccion','depositar', 'saldo'])))

engine.declare(Fact(transaccionValida = 'no'))
engine.declare(Fact(tipo ='saldo'))


engine.run()