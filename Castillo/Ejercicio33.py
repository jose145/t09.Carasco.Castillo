import libreria
import os

#Calcular la energia potencial gravitatoria de un cuerpo
energia_potencial_grav = libreria.energia_potencial_gravitatoria(int(os.sys.argv[1]), int(os.sys.argv[2]), int(os.sys.argv[3]))
print("la energia potencial gravitatoria de un cuerpo es: " , energia_potencial_grav)



