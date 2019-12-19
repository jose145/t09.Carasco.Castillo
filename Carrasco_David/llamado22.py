import os
import libreria_Carrasco

gasto_mensual=libreria_Carrasco.gasto_mensual(float(os.sys.argv[1]),float(os.sys.argv[2]),float(os.sys.argv[3]),
                                              float(os.sys.argv[4]))

print("El gasto es",gasto_mensual)
