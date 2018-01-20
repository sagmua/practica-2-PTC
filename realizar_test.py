#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.10
# In conjunction with Tcl version 8.6
#    Jan 18, 2018 07:38:17 PM
import sys
import support
import os
from test import *
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root,top
    root = Tk()
    support.set_Tk_var()
    top = New_Toplevel_1 (root)
    support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    support.set_Tk_var()
    top = New_Toplevel_1 (w)
    support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        
        self.test_realizar = Test()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("1440x799+-1+23")
        top.title("New Toplevel 1")
        top.configure(background="#d9d9d9")
        self.top = top
        
        self.lista_archivos = ttk.Combobox(top, state="readonly")
        self.lista_archivos["values"] = self.ficheros_examenes()      
        
        self.lista_archivos.place(relx=0.81, rely=0.1, relheight=0.04
                , relwidth=0.18)
        
        self.lista_archivos.configure(takefocus="")
        self.variables =[]
    

        self.Text1 = Text(top)
        self.Text1.place(relx=0.15, rely=0.08, relheight=0.25, relwidth=0.53)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=768)
        self.Text1.configure(wrap=WORD)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.16, rely=0.04, height=24, width=145)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Pregunta''')
        self.Label1.configure(width=145)

        self.label_pena = Label(top)
        self.label_pena.place(relx=0.4, rely=0.04, height=24, width=151)
        self.label_pena.configure(background="#d9d9d9")
        self.label_pena.configure(foreground="#000000")
        self.label_pena.configure(text='''penalizacion''')
        self.label_pena.configure(width=151)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.36, rely=0.04, height=24, width=39)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Tipo:''')
        
        self.Label6 = Label(top)
        self.Label6.place(relx=0.81, rely=0.05, height=24, width=60)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Examen:''')

        self.Text2 = Text(top)
        self.Text2.place(relx=0.15, rely=0.44, relheight=0.5, relwidth=0.54)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=778)
        self.Text2.configure(wrap=WORD)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Label4 = Label(top)
        self.Label4.place(relx=0.16, rely=0.41, height=24, width=85)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Respuestas:''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.76, rely=0.43, height=24, width=187)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Selecciona la/s respuesta/s:''')

        self.boton_siguiente = Button(top, command = self.siguiente)
        self.boton_siguiente.place(relx=0.63, rely=0.95, height=32, width=77)
        self.boton_siguiente.configure(activebackground="#d9d9d9")
        self.boton_siguiente.configure(activeforeground="#000000")
        self.boton_siguiente.configure(background="#d9d9d9")
        self.boton_siguiente.configure(foreground="#000000")
        self.boton_siguiente.configure(highlightbackground="#d9d9d9")
        self.boton_siguiente.configure(highlightcolor="black")
        self.boton_siguiente.configure(text='''Siguiente''')
        self.boton_siguiente.configure(width=77)
        
        
        self.check_respuestas = []
        
        '''
        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.76, rely=0.46, relheight=0.03
                , relwidth=0.13)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text=)
        self.Checkbutton1.configure(variable=support.che50)
        self.Checkbutton1.configure(width=185)
        self.Checkbutton1.deselect()
        '''

    def ficheros_examenes(self):
        path = '.'
        ficheros = []
    
        #listamos todos los ficheros:
        lstDir = os.walk(path)
        #nos quedamos sólo con los que son solución:
        for root, dirs, files in lstDir:
            for f in files:
                if '.xml' in f and 'sol' not in f and '_done' not in f:
                    ficheros.append(f)
        
        return ficheros
    
    def siguiente(self):
        examen = self.lista_archivos.get()
        if self.test_realizar.is_empty() and examen!= '':
            self.test_realizar.cargar_a_realizar(examen)
            primera_pregunta = self.test_realizar.preguntas[0]
            primera_respuestas, num_r = self.test_realizar.get_respuesta(0)
            #rellenamos la pregunta:
            self.Text1.delete(1.0, END)
            self.Text1.insert(END, self.test_realizar.preguntas[0])            
            
            #rellenamos las respuestas:
            self.Text2.delete(1.0, END)
            self.Text2.insert(END, primera_respuestas)
            self.crear_lista_respuestas(num_r)
            self.label_pena['text'] = self.test_realizar.penalizaciones[0]
            
            print(self.test_realizar.penalizaciones[0])
        else:
            print(self.test_realizar.num_preguntas)
            print(self.test_realizar.siguiente)
            #si es ya no hay mas preguntas terminamos:
            respuestas = self.obtener_respuesta()
            print(respuestas)
            self.test_realizar.aniadir_elegida(respuestas)
            
            if self.test_realizar.siguiente == self.test_realizar.num_preguntas:
                
                self.Text1.delete(1.0, END)
                self.Text1.insert(END, 'TEST FINALIZADO, XML GENERADO') 
                self.Text2.delete(1.0, END)
                self.Text2.insert(END, 'TEST FINALIZADO, XML GENERADO') 
                
                
                nuevo = examen[:len(examen)-4]
                self.test_realizar.genera_resultado_alumno(nuevo)
                
            else:
                
                
                #rellenamos la pregunta:
                self.Text1.delete(1.0, END)
                self.Text1.insert(END, self.test_realizar.preguntas[self.test_realizar.siguiente]) 
                
                #ahora la respuesta:
                primera_respuestas, num_r = self.test_realizar.get_respuesta(self.test_realizar.siguiente)
                self.Text2.delete(1.0, END)
                self.Text2.insert(END, primera_respuestas)
                self.crear_lista_respuestas(num_r)
                self.label_pena['text'] = self.test_realizar.penalizaciones[self.test_realizar.siguiente]
            
            
    
    def crear_lista_respuestas(self, num):
        for i in self.check_respuestas:
            i.destroy()
        self.check_respuestas.clear()
        self.variables.clear()
        y_ini = 0.46
        for i in range(num):
            
            self.check_respuestas.append(Checkbutton(self.top))
            self.check_respuestas[i].deselect()
            self.check_respuestas[i].place(relx=0.76, rely=y_ini, relheight=0.03
                    , relwidth=0.13)
            self.check_respuestas[i].configure(activebackground="#d9d9d9")
            self.check_respuestas[i].configure(activeforeground="#000000")
            self.check_respuestas[i].configure(background="#d9d9d9")
            self.check_respuestas[i].configure(foreground="#000000")
            self.check_respuestas[i].configure(highlightbackground="#d9d9d9")
            self.check_respuestas[i].configure(highlightcolor="black")
            self.check_respuestas[i].configure(justify=LEFT)
            self.check_respuestas[i].configure(text=str(i+1))
            self.variables.append(IntVar())
            self.check_respuestas[i].configure(variable=self.variables[i])
            self.check_respuestas[i].configure(width=185)
            
            y_ini += 0.05 
            
    def obtener_respuesta(self):
        respuestas = []
        i =0
        for r in self.check_respuestas:
            if self.variables[i].get():
                respuestas.append(i)
            i+=1
        
        return respuestas
    



if __name__ == '__main__':
    vp_start_gui()

