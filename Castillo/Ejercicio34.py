import libreria
import os

#Sacar el promedio de tres notas de matematica
promedio=libreria.pedir_promedio(int(os.sys.argv[1]),int(os.sys.argv[2]),int(os.sys.argv[3]))
print("El promedio del niño es: " , promedio)
