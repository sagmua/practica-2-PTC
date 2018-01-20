# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 17:15:53 2018

@author: samuel
"""

#Para generar los xml:
from xml.etree.ElementTree import * 
from xml.etree import ElementTree
from xml.dom import minidom

class Test:
    def __init__(self, nombre_test = ''):
        self.nombre_test = nombre_test
        self.num_preguntas = 0
        self.preguntas = []
        self.respuestas = []
        self.penalizaciones = []
        self.elegidas = []
        self.siguiente=0
        
        
    def aniadir_pregunta(self, texto):
        self.preguntas.append(texto)
        self.num_preguntas += 1
        
    def is_empty(self):
        return len(self.preguntas)==0
    
    
        
    
    def aniadir_respuesta(self, texto, valoracion):
        respuesta = (texto, valoracion)
        
        if len(self.respuestas) == self.num_preguntas:
            self.respuestas.append([respuesta])
        else:
            self.respuestas[self.num_preguntas].append(respuesta)
            
            
    def cargar_xml(self, archivo):
        
        tree = parse(archivo)
        root = tree.getroot()
        for pregunta in root:
            print(pregunta.tag)
            enunciado = pregunta[0].text
            opciones = pregunta[1]
            for opcion in opciones:
                self.aniadir_respuesta(opcion[0].text, opcion[1].text)
            
            self.aniadir_pregunta(enunciado)
            
    
    def cargar_a_realizar(self, archivo):
        tree = parse(archivo)
        root = tree.getroot()
        for pregunta in root:
            print(pregunta.tag)
            enunciado = pregunta[0].text
            self.penalizaciones.append(pregunta[1].text)
            opciones = pregunta[2]
            for opcion in opciones:
                self.aniadir_respuesta(opcion[0].text, 'unknow')
            
            self.aniadir_pregunta(enunciado)
            
        self.print_preguntas()
        self.print_respuestas()
            
            
    def generar_xml(self, nombre_examen='examen', con_valoracion=True):
        root = Element('examen')
        
        for i in range(self.num_preguntas):
            pregunta_i = SubElement(root, 'pregunta')
            pregunta_i.set('id', str(i+1))
            enunciado = SubElement(pregunta_i, 'enunciado')
            enunciado.text = self.preguntas[i]
            
            
            if not con_valoracion:
                valoraciones = []
                penalizacion = 'no-penalizado'
                for r in self.respuestas[i]:
                    valoraciones.append(int(r[1]))
                
                if sum(1 for number in valoraciones if number < 0)>0:
                    penalizacion = 'penalizado'
                
                if sum(1 for number in valoraciones if number > 0)>1:
                    penalizacion = 'varias-validas'
                
                pen = SubElement(pregunta_i, 'tipo')
                pen.text = penalizacion
                
                
            opciones = SubElement(pregunta_i, 'opciones')
                
            
            for respuesta in self.respuestas[i]:
                print(respuesta)
                opcion = SubElement(opciones, 'opcion')
                texto = SubElement(opcion, 'texto')
                texto.text = respuesta[0]
                if con_valoracion:
                    valoracion = SubElement(opcion, 'valoracion')
                    valoracion.text = respuesta[1]
                
            
                
        
        print(self.prettify(root))
        test_xml = self.prettify(root)
        
        fichero = nombre_examen
        if con_valoracion:
            fichero = fichero+ "_sol.xml"
        else:
            fichero = fichero + ".xml"
        
        f=open(fichero,"w")
        f.write(test_xml)
        f.close()
        
        if con_valoracion:
            self.generar_xml(con_valoracion=False, nombre_examen=nombre_examen)
            
    def cargar_resultado_alumno(self, nombre):
        tree = parse(nombre)
        root = tree.getroot()
        for pregunta in root:
            print(pregunta.tag)
    
            opciones = pregunta[0]
            elegidas = []
            for opcion in opciones:
                elegidas.append(opcion[0].text)
            
            self.elegidas.append(elegidas)
            print(elegidas)
        
        
    def genera_resultado_alumno(self, nombre):
        
        root = Element('examen')
        
        for i in range(self.num_preguntas):
            pregunta_i = SubElement(root, 'pregunta')
            pregunta_i.set('id', str(i+1))
            opciones = SubElement(pregunta_i, 'soluciones_elegidas')
                
            
            for respuesta in self.elegidas[i]:
                print(respuesta)
                opcion = SubElement(opciones, 'solucion')
                texto = SubElement(opcion, 'texto')
                texto.text = str(respuesta)
  
        #print(tostring(root))
        
        test_xml = self.prettify(root)
        
        fichero = nombre+'_done.xml'
        
        
        f=open(fichero,"w")
        f.write(test_xml)
        f.close()
        
        
        
        
        
    def aniadir_elegida(self, r):
        self.elegidas.append(r)
        self.siguiente+=1
        if self.siguiente > self.num_preguntas:
            print('FIN TEST')
     
     
    def prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
            
    
    def print_respuestas(self):
        for i in self.respuestas:
            print(i)
    def print_preguntas(self):
        for i in self.preguntas:
            print(i)
    
    def get_respuesta(self, index):
        respuesta = self.respuestas[index]
        respuestas = ''
        j=1
        for i in respuesta:
            respuestas += ('\n' + str(j) + '.-    ')
            respuestas += i[0]
            j+=1
        
        j=j-1
        return respuestas, j
    
    def obtener_nota(self):
        sumatoria = 0
        i = 0
        for respuesta in self.respuestas:
            for ele in self.elegidas[i]:
                valoracion = respuesta[int(ele)][1]
                sumatoria+= 1* (float(valoracion)/100.0)
            i+=1
        
        sumatoria = sumatoria*10/self.num_preguntas
        if sumatoria<0:
            sumatoria=0
        elif sumatoria>10:
            sumatoria=10
        
        return sumatoria
            
            
            
        


if __name__ == '__main__':
    
    test = Test('el primero')
    examen = 'examen.xml'
    print()
    