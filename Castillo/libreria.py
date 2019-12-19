#Ejercicio 26
def area_cuadrado(lado):
    area= (lado*lado)
    return area
#fin_def


#Ejercicio 27
def area_rectangulo(base,altura):
    area= (base*altura)
    return area
#fin_def



#Ejercicio 28
def area_triangulo_equilatero(lado):
    area= ((lado*lado*1.73)/4)
    return area
#fin_def



#Ejercicio 29
def potencia(trabajo,tiempo):
    potencia= (trabajo/tiempo)
    return potencia
#fin_def


#Ejercicio 30
def densidad(masa,volumen):
    densidad= (masa/volumen)
    return densidad
#fin_def

#Ejercicio 31
def area_del_triangulo(altura,base):
    area_del_triangulo=pedir_entero
    resultado= (altura*base)/2
    return resultado
#Fin_def



#Ejercicio 32
def trabajo_de_cuerpo(fuerza,distancia):
    trabajo_de_cuerpo=pedir_entero
    trabajo= (fuerza*distancia)
    return trabajo
#Fin_def



#Ejercicio 33
def energia_potencial_gravitatoria(masa,gravedad,altura):
    energia_potencial_gravitatoria=pedir_entero
    energia= (masa*gravedad*altura)
    return energia
#Fin_def


#Ejercicio 34
def pedir_promedio(n1,n2,n3):
    promedio= n1+n2+n3
    return promedio
#fin_def


#Ejercicio 35
def pedir_nombre(nombre):
    nombre=str(nombre)
    return nombre
#fin_def
1111

#Ejercicio 36
def area_rombo(D1,d2):
    area= (D1*d2)/2
    return area
#fin_def


#Ejercicio 37
def area_trapecio(base1,base2,altura):
    area= ((base1+base2)*altura)/2
    return area
#fin_def


#Ejercicio 38
def area_circulo(radio):
    area= ((radio*radio*3.14))
    return area
#fin_def


#Ejercicio 39
def energia_cinetica(masa,velocidad):
    energia_cinetica=((masa*velocidad*velocidad)/2)
    return energia_cinetica
#fin_def

#Ejercicio 40
def area_paralelogramo(base,altura):
    area= (base*altura)
    return area
#fin_def


#Ejercicio 41
def pedir_IMC(talla,peso):
    IMC=((peso)/(talla*talla))
    return IMC
#fin_def

#Ejercicio 42
def pedir_distancia(velocidad,tiempo):
    distancia=(velocidad*tiempo)
    return distancia
#fin_def

#Ejercicio 43
def pedir_volumen_prisma(area_base,altura):
    volumen_prisma=(area_base*altura)
    return volumen_prisma
#fin_def

#Ejercicio 44
def pedir_volumen_paralelepipedo(largo,ancho,grosor):
    volumen_paralelepipedo=(largo*ancho*grosor)
    return volumen_paralelepipedo
#fin_def

#Ejercicio 45
def pedir_area_paralelepipedo(largo,ancho,grosor):
    area_paralelepipedo=(2*((largo*ancho)+(largo*grosor)+(ancho*grosor)))
    return area_paralelepipedo
#fin_def


#Ejercicio 46
def pedir_volumen_piramide(area_base,altura):
    volumen_piramide=(int((area_base*altura)/3))
    return volumen_piramide
#fin_def


#Ejercicio 47
def pedir_area_cubo(lado):
    area_cubo=(6*(lado*lado))
    return area_cubo
#fin_def


#Ejercicio 48
def pedir_area_cilindro(radio,generatriz):
    area_cilindro=(2*(3.14)*radio*(generatriz+radio))
    return area_cilindro
#fin_def


#Ejercicio 48
def pedir_area_esfera(radio):
    area_esfera=(4*(3.14)*radio*radio)
    return area_esfera
#fin_def


#Ejercicio 46
def pedir_volumen_cono(radio,altura):
    volumen_cono=(int(((3.14)*radio*radio*altura)/3))
    return volumen_cono
#fin_def
