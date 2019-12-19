import libreria
import os

#Calcular el IMC de una persona
IMC=libreria.pedir_IMC(float(os.sys.argv[1]),float(os.sys.argv[2]))
print ("El IMC de una persona es: " , IMC)
