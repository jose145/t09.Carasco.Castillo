import os
import libreria_Carrasco

energia=libreria_Carrasco.energia_electrica(float(os.sys.argv[1]),float(os.sys.argv[2]),float(os.sys.argv[3]))
print("La energia es:", energia)
