# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 17:15:53 2018

@author: samuel
"""

class Test:
    def __init__(self, nombre_test = ''):
        self.nombre_test = nombre_test
        self.num_preguntas = 0
        self.preguntas = []
        self.respuestas = []
        
        
    def aniadir_pregunta(self, texto):
        self.preguntas.append(texto)
        self.num_preguntas += 1
    
    def aniadir_respuesta(self, texto, valoracion):
        respuesta = (texto, valoracion)
        
        if len(self.respuestas) == self.num_preguntas:
            self.respuestas.append([respuesta])
        else:
            self.respuestas[self.num_preguntas].append(respuesta)
            
    
    def print_respuestas(self):
        for i in self.respuestas:
            print(i)
    def print_preguntas(self):
        for i in self.preguntas:
            print(i)
        


if __name__ == '__main__':
    
    test = Test('el primero')
    
    