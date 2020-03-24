# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:11:01 2020

@author: Pablo
"""
import tkinter as tk
import random 


def generarCoordenadasVisualizacion(coordOriginales, direccion, distanciaVis ):
    global tamCasilla
    coordVisualizacion = []
    
    for i in range(distanciaVis):
        for j in range(-i,i+1):
            if direccion == 'D':
                x,y = coordOriginales[0]+j*tamCasilla, coordOriginales[1]+(i*tamCasilla)
                coordVisualizacion.append([ x, y, x+tamCasilla,y+tamCasilla ])
            
            elif direccion == 'U':
                x,y = coordOriginales[0]-j*tamCasilla, coordOriginales[1]-(i*tamCasilla)
                coordVisualizacion.append([ x, y, x-tamCasilla,y-tamCasilla ])
           
            elif direccion == 'L':
                x,y = coordOriginales[0]-(i*tamCasilla), coordOriginales[1]-j*tamCasilla
                coordVisualizacion.append([ x, y, x-tamCasilla,y+tamCasilla ])
            
            else:
                x,y = coordOriginales[0]+(i*tamCasilla), coordOriginales[1]+j*tamCasilla
                coordVisualizacion.append([ x, y, x+tamCasilla,y-tamCasilla ])                      
            
    return coordVisualizacion
    


def verificarCoordenadas(coordNuevas, CoordLeones, Coordimpalas): 
    aceptado = 1
    
    if CoordLeones != Coordimpalas:       
        for leon in CoordLeones:
            if coordNuevas[0] == leon[0] and coordNuevas[1] == leon[1]:
                aceptado = 0
                break
                 
        for impala in Coordimpalas:
            if coordNuevas[0] == impala[0] and coordNuevas[1] == impala[1]:
                aceptado = 0
                break
    
    return aceptado
            
def verificarVisualizacion(coordVision, CoordLeones, Coordimpalas, direccion):
    global tamCasilla
    visualizacion = [0,-1]
    
    indexLeon = 0
    for coordLeon in CoordLeones:
        if direccion == 'L':
            if coordVision[0] == coordLeon[0]+tamCasilla and coordVision[1] == coordLeon[1] and coordVision[2] == coordLeon[0] and coordVision[3] == coordLeon[1]+tamCasilla:
                visualizacion[0] = 1
                visualizacion[1] = indexLeon
                break
            
        elif direccion == 'R':
            if coordVision[0] == coordLeon[0] and coordVision[1] == coordLeon[1]+tamCasilla and coordVision[2] == coordLeon[0]+tamCasilla and coordVision[3] == coordLeon[1]:
                visualizacion[0] = 1
                visualizacion[1] = indexLeon
                break
            
        elif direccion == 'U':
            if coordVision[0] == coordLeon[0]+tamCasilla and coordVision[1] == coordLeon[1]+tamCasilla and coordVision[2] == coordLeon[0] and coordVision[3] == coordLeon[1]:
                visualizacion[0] = 1
                visualizacion[1] = indexLeon
                break
            
        elif direccion == 'D':
             if coordVision[0] == coordLeon[0] and coordVision[1] == coordLeon[1] and coordVision[2] == coordLeon[0]+tamCasilla and coordVision[3] == coordLeon[1]+tamCasilla:
                visualizacion[0] = 1
                visualizacion[1] = indexLeon
                break
            
        indexLeon += 1          
      
    indexImpala = 0
    for coordimpala in Coordimpalas:
        if direccion == 'L':
            if coordVision[0] == coordimpala[0]+tamCasilla and coordVision[1] == coordimpala[1] and coordVision[2] == coordimpala[0] and coordVision[3] == coordimpala[1]+tamCasilla:
                visualizacion[0] = 2
                visualizacion[1] = indexImpala
                break
            
        elif direccion == 'R':
            if coordVision[0] == coordimpala[0] and coordVision[1] == coordimpala[1]+tamCasilla and coordVision[2] == coordimpala[0]+tamCasilla and coordVision[3] == coordimpala[1]:
                visualizacion[0] = 2
                visualizacion[1] = indexImpala
                break
            
        elif direccion == 'U':
            if coordVision[0] == coordimpala[0]+tamCasilla and coordVision[1] == coordimpala[1]+tamCasilla and coordVision[2] == coordimpala[0] and coordVision[3] == coordimpala[1]:
                visualizacion[0] = 2
                visualizacion[1] = indexImpala
                break
            
        elif direccion == 'D':
             if coordVision[0] == coordimpala[0] and coordVision[1] == coordimpala[1] and coordVision[2] == coordimpala[0]+tamCasilla and coordVision[3] == coordimpala[1]+tamCasilla:
                visualizacion[0] = 2
                visualizacion[1] = indexImpala
                break
            
        indexImpala += 1
        
    
    return visualizacion

def moverPersonajes():    
    global contPasosLargoLeon, contPasosAltoLeon
    global coordImpalaXHuir, coordImpalaYHuir

    #CAZAR IMPALA
    if cazarImpala:   
        if contPasosLargoLeon > 0:
            contPasosLargoLeon -= 1
            
            if avanceLargoLeon == 1:
                Pantalla.move(leones[indiceLeon],tamCasilla,0) 
              #  Pantalla.after(200,moverPersonajes)
    
            elif avanceLargoLeon == -1:
                Pantalla.move(leones[indiceLeon],-tamCasilla,0) 
              #  Pantalla.after(200,moverPersonajes)
    
        if contPasosLargoLeon == 0 and contPasosAltoLeon > 0:
            contPasosAltoLeon -= 1
                       
            if avanceAltoLeon == 1:
                Pantalla.move(leones[indiceLeon],0,tamCasilla) 
              #  Pantalla.after(200,moverPersonajes)
       
            elif avanceAltoLeon == -1:
                Pantalla.move(leones[indiceLeon],0,-tamCasilla) 
              #  Pantalla.after(200,moverPersonajes)
                  
        if contPasosLargoLeon == 0 and contPasosAltoLeon == 0:
            if not salvado:
                Pantalla.create_rectangle(coordImpalaXCazar,coordImpalaYCazar,coordImpalaXCazar+tamCasilla,coordImpalaYCazar+tamCasilla, fill="red")
            
                
                    
     # HUIR IMPALA
    if huirImpala: 
        if (coordImpalaXHuir > 0 or coordImpalaXHuir < tamTablero) and (coordImpalaYHuir > 0 or coordImpalaYHuir < tamTablero):
            if direccionImpala == 'R':
                coordImpalaXHuir += tamCasilla/2
                Pantalla.move(impalas[indiceImpala],tamCasilla/2,0) 
              #  Pantalla.after(200,moverPersonajes)
            elif direccionImpala == 'L':
                coordImpalaXHuir -= tamCasilla/2
                Pantalla.move(impalas[indiceImpala],-tamCasilla/2,0) 
              #  Pantalla.after(200,moverPersonajes)
            elif direccionImpala == 'U':
                coordImpalaYHuir += tamCasilla/2
                Pantalla.move(impalas[indiceImpala],0,tamCasilla/2) 
               # Pantalla.after(200,moverPersonajes)
            elif direccionImpala == 'D':
                coordImpalaYHuir -= tamCasilla/2
                Pantalla.move(impalas[indiceImpala],0,-tamCasilla/2) 
               # Pantalla.after(200,moverPersonajes)
            
    
    Pantalla.after(200,moverPersonajes)
      
          
               
            
raiz = tk.Tk()
raiz.title("Leones e impalas")
raiz.geometry("+150+50")

# Frames
frameBotones = tk.Frame(raiz)
frameBotones.pack(side="right")

frameCanvas = tk.Frame(raiz)
frameCanvas.pack()


tamTablero = 600
numCasillas = 10 #tamaño de tablero
tamCasilla = tamTablero/numCasillas

Pantalla = tk.Canvas(frameCanvas, width=tamTablero, height=tamTablero, bg="#212121")
Pantalla.pack()

botonComenzar = tk.Button(frameBotones, text="Comenzar", command = moverPersonajes)
botonComenzar.pack(padx="10")


coordenadas = []
for i in range(numCasillas):
    coordenadas.append(int(i*tamCasilla))

# horizontal (eje X)  vertical (eje Y)
# Esq. superior Izq (0,0)
# create_line(coord_x(origen),coord_y(origen),coord_x(destino),coord_y(destino) )
    
for i in coordenadas:
    Pantalla.create_line(tamTablero,i,0,i,fill="#FAFAFA")
    Pantalla.create_line(i,tamTablero,i,0,fill="#FAFAFA")

distanciaVision = 3    #tamaño de vision            
coordenadasLeones = []
coordenadasimpalas = [] 
listaAux = []
contLeones = 0
contimpalas = 0                       

#while contLeones < 2 or contimpalas < 5:
#    if contLeones < 2:
#        coord_x_leon = random.choice(coordenadas) 
#        coord_y_leon = random.choice(coordenadas)  
#        listaAux.append(coord_x_leon)
#        listaAux.append(coord_y_leon)
#        if verificarCoordenadas(listaAux,coordenadasLeones, coordenadasimpalas) == 1:
#            coordenadasLeones.append(listaAux)
#            contLeones += 1
#        listaAux = []
#        
#    if contimpalas < 5:
#        coord_x_impala = random.choice(coordenadas) 
#        coord_y_impala = random.choice(coordenadas) 
#        listaAux.append(coord_x_impala)
#        listaAux.append(coord_y_impala)
#        if verificarCoordenadas(listaAux,coordenadasLeones, coordenadasimpalas) == 1:
#            coordenadasimpalas.append(listaAux)
#            contimpalas += 1
#        listaAux = []

coordenadasLeones = [[60,60]]
coordenadasimpalas = [[180,60]]

tamanoLeon = ['Chico','Mediano','Grande']
colorLeon = ['Amarilla','Naranja','Negra']
edadImpala = ['Niño','Joven','Adulto','Anciano']
saludImapala = ['Enfemo','Saludable']


leones = []
impalas = []
atributosLeones = []
atributosImpalas = []

for leon in coordenadasLeones:
    leones.append(Pantalla.create_rectangle(leon[0],leon[1],leon[0]+tamCasilla,leon[1]+tamCasilla, fill="yellow"))
    listaAux = []
    listaAux.append(random.randint(0,2))
    listaAux.append(random.randint(0,2))
    atributosLeones.append(listaAux)
    
    
    
for impala in coordenadasimpalas:
    impalas.append(Pantalla.create_rectangle(impala[0],impala[1],impala[0]+tamCasilla,impala[1]+tamCasilla, fill="blue"))
    listaAux = []
    listaAux.append(random.randint(0,3))
    listaAux.append(random.randint(0,1))
    atributosImpalas.append(listaAux)
    
    
contador = 0
cazarImpala = False
dirrecciones = ['L','R','U','D']
coordImpalaXCazar, coordImpalaYCazar = 0,0

for leon in coordenadasLeones: 
    direccion = random.choice(dirrecciones)
   
    leonAux = leon
    if direccion == 'R':
        leonAux = [leon[0]+tamCasilla, leon[1]+tamCasilla]
        
    elif direccion == 'U':
        leonAux = [leon[0]+tamCasilla,leon[1]]
        
    elif direccion == 'D':
        leonAux = [leon[0],leon[1]+tamCasilla]

    coordenadasVision = generarCoordenadasVisualizacion(leonAux, direccion, distanciaVision )

    for coordenadaVision in coordenadasVision:
        Pantalla.create_rectangle(coordenadaVision[0],coordenadaVision[1],coordenadaVision[2],coordenadaVision[3], outline="yellow", width=2)               
       
        visualizacion = verificarVisualizacion(coordenadaVision, coordenadasLeones, coordenadasimpalas, direccion)
        
        if visualizacion[0] == 1 or visualizacion[0] == 2:
            cadena = "Soy el león número "+str(contador+1)+" y mi tamaño es: "+tamanoLeon[atributosLeones[contador][0]]+" y mi color de melena es: "+colorLeon[atributosLeones[contador][1]]
            tk.Label(frameBotones, text=cadena, fg="black",bg="yellow").pack()
            
            if visualizacion[0] == 1:
                if atributosLeones[contador][0] > atributosLeones[visualizacion[1]][0]  and atributosLeones[contador][0] > atributosLeones[visualizacion[1]][1]:
                    cadena = "Veo otro león con tamaño: "+tamanoLeon[atributosLeones[visualizacion[1]][0]]+" y su melena es: "+colorLeon[atributosLeones[visualizacion[1]][1]]+" por lo tanto voy a PELEAR..."
                    tk.Label(frameBotones, text=cadena, fg="black",bg="yellow").pack()
                
                elif atributosLeones[contador][0] < atributosLeones[visualizacion[1]][0]  and atributosLeones[contador][0] < atributosLeones[visualizacion[1]][1]:
                    cadena = "Veo otro león con tamaño: "+tamanoLeon[atributosLeones[visualizacion[1]][0]]+" y su melena es: "+colorLeon[atributosLeones[visualizacion[1]][1]]+" por lo tanto voy a HUIR..."
                    tk.Label(frameBotones, text=cadena, fg="black",bg="yellow").pack()
                
                else:
                    cadena = "Veo otro león con tamaño: "+tamanoLeon[atributosLeones[visualizacion[1]][0]]+" y su melena es: "+colorLeon[atributosLeones[visualizacion[1]][1]]+" por lo tanto voy a HACER NADA..."
                    tk.Label(frameBotones, text=cadena, fg="black",bg="yellow").pack()
 
            
            elif visualizacion[0] == 2:
                if (atributosLeones[contador][0] > 0 and atributosLeones[contador][1] > 0) and (atributosImpalas[visualizacion[1]][0] == 0 or atributosImpalas[visualizacion[1]][1] == 0 or atributosImpalas[visualizacion[1]][1] == 3):
                    cadena = "Veo un impala que es: "+edadImpala[atributosImpalas[visualizacion[1]][0]]+" y su salud es: "+saludImapala[atributosImpalas[visualizacion[1]][1]]+" por lo tanto voy a CAZARLO..."
                    tk.Label(frameBotones, text=cadena, fg="black",bg="yellow").pack()
                    
                    if not cazarImpala:
                        avanceLargoLeon = 1
                        avanceAltoLeon = 1
                        coordXLeon, coordYLeon = leon[0],leon[1]
                        coordImpalaXCazar, coordImpalaYCazar = coordenadasimpalas[visualizacion[1]][0], coordenadasimpalas[visualizacion[1]][1]                       
    
                        if  coordImpalaXCazar - coordXLeon  < 0:
                            avanceLargoLeon = -1
                        if  coordImpalaYCazar - coordYLeon < 0:
                            avanceAltoLeon = -1
                        
                        contPasosLargoLeon = int(abs( (coordImpalaXCazar - coordXLeon)/tamCasilla ))
                        contPasosAltoLeon = int(abs( (coordImpalaYCazar - coordYLeon)/tamCasilla ))
                        
                        cazarImpala = True
                        indiceLeon = contador                        
                    
                else:
                    cadena = "Veo un impala que es: "+edadImpala[atributosImpalas[visualizacion[1]][0]]+" y su salud es: "+saludImapala[atributosImpalas[visualizacion[1]][1]]+" por lo tanto voy a HUIR DE ÉL..."
                    tk.Label(frameBotones, text=cadena, fg="black",bg="yellow").pack()
 
    contador += 1


contador = 0    
huirImpala = False
salvado = False

for impala in coordenadasimpalas:
    direccion = random.choice(dirrecciones)
    
    impalaAux = impala
    if direccion == 'R':
        impalaAux = [impala[0]+tamCasilla, impala[1]+tamCasilla]
    
    elif direccion == 'U':
        impalaAux = [impala[0]+tamCasilla,impala[1]]
      
    elif direccion == 'D':
        impalaAux = [impala[0],impala[1]+tamCasilla]
            
     
    coordenadasVision = generarCoordenadasVisualizacion(impalaAux, direccion, distanciaVision )

    for coordenadaVision in coordenadasVision:
        Pantalla.create_rectangle(coordenadaVision[0],coordenadaVision[1],coordenadaVision[2],coordenadaVision[3], outline="blue", width=2)
        
        visualizacion = verificarVisualizacion(coordenadaVision, coordenadasLeones, coordenadasimpalas, direccion)

        if visualizacion[0] == 1 or visualizacion[0] == 2:
            cadena = "Soy el impala número "+str(contador+1)+" y soy un: "+edadImpala[atributosImpalas[contador][0]]+" y estoy: "+saludImapala[atributosImpalas[contador][1]]
            tk.Label(frameBotones, text=cadena, fg="black", bg="#67a1cf").pack()
        
            if visualizacion[0] == 1:
                if (atributosLeones[visualizacion[1]][0] > 0 and atributosLeones[visualizacion[1]][1] > 0) and (atributosImpalas[contador][0] == 0 or atributosImpalas[contador][1] == 0 or atributosImpalas[contador][1] == 3):
                    cadena = "Veo un león con tamaño: "+tamanoLeon[atributosLeones[visualizacion[1]][0]]+" y su melena es: "+colorLeon[atributosLeones[visualizacion[1]][1]]+" por lo tanto voy a HUIR..."
                    tk.Label(frameBotones, text=cadena, fg="black", bg="#67a1cf").pack()
                    
                    if not huirImpala:
                        if direccion == 'R':
                            direccionImpala = 'L'
                        elif direccion == 'L':
                            direccionImpala = 'R'
                        elif direccion == 'D':
                            direccionImpala = 'U'
                        elif direccion == 'U':
                            direccionImpala = 'D'
                            
                        coordImpalaXHuir = impala[0]
                        coordImpalaYHuir = impala[1]
                        
                        if coordImpalaXCazar == coordImpalaXHuir and coordImpalaYCazar == coordImpalaYHuir:
                            salvado = True
                        
                        huirImpala = True
                        indiceImpala = contador     
                             
                else:    
                    cadena = "Veo un león con tamaño: "+tamanoLeon[atributosLeones[visualizacion[1]][0]]+" y su melena es: "+colorLeon[atributosLeones[visualizacion[1]][1]]+" por lo tanto voy a CAZARLO..."
                    tk.Label(frameBotones, text=cadena, fg="black", bg="#67a1cf").pack()

            elif visualizacion[0] == 2:
                if  atributosImpalas[visualizacion[1]][0] == 0 or atributosImpalas[visualizacion[1]][1] == 0 or atributosImpalas[visualizacion[1]][1] == 3:
                    cadena = "Veo otro impala que es: "+edadImpala[atributosImpalas[visualizacion[1]][0]]+" y su salud es: "+saludImapala[atributosImpalas[visualizacion[1]][1]]+" por lo tanto voy a AYUDARLO..."
                    tk.Label(frameBotones, text=cadena, fg="black", bg="#67a1cf").pack()
                
                else: 
                    cadena = "Veo otro impala que es: "+edadImpala[atributosImpalas[visualizacion[1]][0]]+" y su salud es: "+saludImapala[atributosImpalas[visualizacion[1]][1]]+" por lo tanto voy a HACER NADA..."
                    tk.Label(frameBotones, text=cadena, fg="black", bg="#67a1cf").pack()

    contador += 1
        

raiz.mainloop()