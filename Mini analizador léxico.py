"""
@author: Orlando
"""

import re 

Identificador = re.compile(r'[a-zA-Z]+[\w]*') #Funcion para identificar cadenas
 
Real = re.compile(r'[\d]+\.[\d]+') #Funcion para identificar reales

linea = []  #Espacio para guardar nuestra cadena

while (linea != 'exit'): #Ciclo para usar la función con 'exit' finaliza
    linea = input("Cadena a analizar: ") #Ingresamos nuestra cadena
    print("Contenido de la linea:" , "\n" , linea) 
    tokens=linea.split(' ') #Separamos la linea de texto usando los espacios
    for token in tokens: #Recorremos la linea de texto
        
        if Identificador.match(linea): #Si es identificador entra aquí
            print (token, "es un identificador del tipo: 0")
        if Real.match(linea):  #Si es real entra aquí
            print (token, "es un real del tipo: 3") 
            
            
    print("\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+") 
