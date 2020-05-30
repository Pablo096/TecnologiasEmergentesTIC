# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:45:17 2020

@author: Pablo
"""

import tkinter as tk
from PIL import ImageTk
import proyectoFinalReglas as rules
from experta import Fact
    
def detectarEnfermedad():    
    sistemaExperto = rules.Consultorio()
    sistemaExperto.reset()
    
    sistemaExperto.declare(Fact(diarrea = str(sintomaDiarrea.get())))
    sistemaExperto.declare(Fact(tos = str(sintomaTos.get())))
    sistemaExperto.declare(Fact(cansancio = str(sintomaCansancio.get())))
    sistemaExperto.declare(Fact(fiebre = str(sintomaFiebre.get())))
    sistemaExperto.declare(Fact(dolorCabeza = str(sintomaDolorCabeza.get())))
    sistemaExperto.declare(Fact(nauseas = str(sintomaNauseas.get())))
    sistemaExperto.declare(Fact(ictericia = str(sintomaIctericia.get())))
    sistemaExperto.declare(Fact(apatia = str(sintomaApatia.get())))
    sistemaExperto.declare(Fact(escalofrios = str(sintomaEscalofrios.get())))
    sistemaExperto.declare(Fact(jaqueca = str(sintomaJaqueca.get())))
    sistemaExperto.declare(Fact(secrecion = str(sintomaSecrecion.get())))
    
    sistemaExperto.run()
    
    enfermedad.config(state = tk.NORMAL)
    medicamentos.config(state = tk.NORMAL)
    especialista.config(state = tk.NORMAL)
    
    enfermedad.delete("1.0", "end")
    enfermedad.insert(tk.INSERT, sistemaExperto.sintoma)
    medicamentos.delete("1.0", "end")
    medicamentos.insert(tk.INSERT, sistemaExperto.medicamentos)
    especialista.delete("1.0", "end")
    especialista.insert(tk.INSERT, sistemaExperto.especialista)
    
    
    enfermedad.config(state = tk.DISABLED)
    medicamentos.config(state = tk.DISABLED)
    especialista.config(state = tk.DISABLED)
 
def limpiar():
    enfermedad.config(state = tk.NORMAL)
    medicamentos.config(state = tk.NORMAL)
    especialista.config(state = tk.NORMAL)
    
    enfermedad.delete("1.0", "end")
    medicamentos.delete("1.0", "end")
    especialista.delete("1.0", "end")
    
    enfermedad.config(state = tk.DISABLED)
    medicamentos.config(state = tk.DISABLED)
    especialista.config(state = tk.DISABLED)
    
    sintomaDiarrea.set(False)
    sintomaTos.set(False)
    sintomaCansancio.set(False)
    sintomaFiebre.set(False)
    sintomaDolorCabeza.set(False)
    sintomaNauseas.set(False)
    sintomaIctericia.set(False)
    sintomaApatia.set(False)
    sintomaEscalofrios.set(False)
    sintomaJaqueca.set(False)
    sintomaSecrecion.set(False)
    
    
raiz = tk.Tk()
raiz.title("Registro Medico")
raiz.geometry("+350+20")
raiz.config(bg="#B2FFFF")

    
sintomaDiarrea = tk.BooleanVar()
sintomaTos = tk.BooleanVar()
sintomaCansancio = tk.BooleanVar()
sintomaFiebre = tk.BooleanVar()
sintomaDolorCabeza = tk.BooleanVar()
sintomaNauseas = tk.BooleanVar()
sintomaIctericia = tk.BooleanVar()
sintomaApatia = tk.BooleanVar()
sintomaEscalofrios = tk.BooleanVar()
sintomaJaqueca = tk.BooleanVar()
sintomaSecrecion = tk.BooleanVar()

l1 = tk.Label(raiz, text="Marque los síntomas que presenta", width=30, bg="#B2FFFF")
l1.grid(row = 0, column = 1, pady = 10)

img1 = ImageTk.PhotoImage(file = "diarrea.jpg")
c1 = tk.Checkbutton(raiz, text = "Diarrea", variable = sintomaDiarrea, image = img1,  width=100, height=100, compound='top', bg="#B2FFFF")
c1.grid(row = 1, column = 0, pady = 5)

img2 = ImageTk.PhotoImage(file = "tos.png")
c2 = tk.Checkbutton(raiz, text = "Tos", variable = sintomaTos, image = img2,  width=100, height=100, compound='top', bg="#B2FFFF")
c2.grid(row = 1, column = 1, pady = 5)

img3 = ImageTk.PhotoImage(file = "cansancio.jpg")
c3 = tk.Checkbutton(raiz, text = "Cansancio", variable = sintomaCansancio, image = img3,  width=100, height=100, compound='top', bg="#B2FFFF")
c3.grid(row = 1, column = 2, pady = 5)

img4 = ImageTk.PhotoImage(file = "fiebre.jpg")
c4 = tk.Checkbutton(raiz, text = "Fiebre", variable = sintomaFiebre, image = img4,  width=100, height=100, compound='top', bg="#B2FFFF")
c4.grid(row = 2, column = 0, pady = 5)

img5 = ImageTk.PhotoImage(file = "dolorCabeza.jpg")
c5= tk.Checkbutton(raiz, text = "Dolor de Cabeza", variable = sintomaDolorCabeza, image = img5,  width=100, height=100, compound='top', bg="#B2FFFF")
c5.grid(row = 2, column = 1, pady = 5)

img6 = ImageTk.PhotoImage(file = "nauseas.jpg")
c6 = tk.Checkbutton(raiz, text = "Náuseas", variable = sintomaNauseas, image = img6,  width=100, height=100, compound='top', bg="#B2FFFF")
c6.grid(row = 2, column = 2, pady = 5) 

img7 = ImageTk.PhotoImage(file = "ictericia.jpg")
c7 = tk.Checkbutton(raiz, text = "Ictericia", variable = sintomaIctericia, image = img7,  width=100, height=100, compound='top', bg="#B2FFFF")
c7.grid(row = 3, column = 0, pady = 5)

img8 = ImageTk.PhotoImage(file = "apatia.jpg")
c8 = tk.Checkbutton(raiz, text = "Apatía", variable = sintomaApatia, image = img8,  width=100, height=110, compound='top',bg="#B2FFFF")
c8.grid(row = 3, column = 1, pady = 5)

img9 = ImageTk.PhotoImage(file = "escalofrios.jpg")
c9 = tk.Checkbutton(raiz, text = "Escalofríos", variable = sintomaEscalofrios, image = img9,  width=100, height=100, compound='top', bg="#B2FFFF")
c9.grid(row = 3, column = 2, pady = 5)

img10 = ImageTk.PhotoImage(file = "jaqueca.jpg")
c10 = tk.Checkbutton(raiz, text = "Jaqueca", variable = sintomaJaqueca, image = img10,  width=100, height=110, compound='top', bg="#B2FFFF")
c10.grid(row = 4, column = 0, pady = 5)

img11 = ImageTk.PhotoImage(file = "secrecion.jpg")
c11 = tk.Checkbutton(raiz, text = "Secreción", variable = sintomaSecrecion, image = img11,  width=100, height=100, compound='top', bg="#B2FFFF")
c11.grid(row = 4, column = 1, pady = 5)


b1 = tk.Button(raiz, text="Aceptar", command = detectarEnfermedad, bg="#BDECB6")
b1.grid(row = 5, column = 0, padx = 5)

b2 = tk.Button(raiz, text="Nuevo Paciente", command = limpiar, bg="#BDECB6")
b2.grid(row = 5, column = 2, padx = 5)

l2 = tk.Label(raiz, text = "Tipo de Enfermedad:", bg="#B2FFFF")
l2.grid(row = 6, column = 0, pady = 2)
enfermedad = tk.Text(raiz, state = tk.DISABLED, height = 1, width=25)
enfermedad.grid(row = 6, column = 1, pady = 2)


l3 = tk.Label(raiz, text="Medicamentos para recetar:", bg="#B2FFFF")
l3.grid(row = 7, column = 0, pady = 2)
medicamentos = tk.Text(raiz, state = tk.DISABLED, height = 1, width=25)
medicamentos.grid(row = 7, column = 1, pady = 2)

l4 = tk.Label(raiz, text="Especialista para Tratar:", bg="#B2FFFF")
l4.grid(row = 8, column = 0, pady = 2)
especialista = tk.Text(raiz, state = tk.DISABLED, height = 1, width=25)
especialista.grid(row = 8, column = 1, pady = 2)

raiz.mainloop()