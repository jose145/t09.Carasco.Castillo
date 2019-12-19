import libreria
import os

#Calcular el volumen de un prisma
volumen_prisma=libreria.pedir_volumen_prisma(int(os.sys.argv[1]),int(os.sys.argv[2]))
print ("El volumen de un prisma es: " , volumen_prisma)
