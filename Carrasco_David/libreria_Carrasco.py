#1funcion
#fuerza MRUV de distancia
def formula_distancia(velocidad_inicial,tiempo,aceleracion):
    distancia=((velocidad_inicial*tiempo)+(aceleracion*tiempo*tiempo)//2)
    return distancia
#fin_funcion



#funcion 02
#boleta para 2 productos
def boleta(nombre,producto01,producto02,costo_producto01,costo_producto02):
    print("Restauran \"El Fogon de mi Abuelo\"")
    print("#"*30)
    print("Cliente:",nombre)
    print("Producto" +"Costo".rjust(20))
    print(producto01 +str(costo_producto01).rjust(20))
    print(producto02 +str(costo_producto02).rjust(20))
    total=costo_producto01+costo_producto02
    print("Total:", total)
    return total
#fin_funcion



#funcion 03
#verificador de edad
def comparacion_edades(edad1,edad2):
    msg=""
    while(edad1<0 or edad1>100):
        print("Primera edad invalidad")
        edad1=int(input("Ingrese edad valida"))
    while(edad2<0 or edad2>100):
        print("Segunda edad invalidad")
        edad2=int(input("Ingrese edad valida"))

    if(edad1==edad2):
        msg="Tienen la misma edad"
    else:
        msg="sus edades no son iguales"

    print("La edad:", edad1)
    print("La edad:", edad2)
    return msg
#fin_funcion




#funcion 04
#Energia electrica
def energia_electrica(variacion_voltaje,intensidad,tiempo):
    energia=variacion_voltaje*intensidad*tiempo
    return energia
#fin_funcion




#funcion 05
#energia cinetica
def energia_cinetica(masa,velocidad):
    cinetica=masa*velocidad*velocidad
    return cinetica
#fin_funcion



#funcion 06
#formula del empuje
def empuje(densidad_liquida,volumen_sumergida):
    resulatado=densidad_liquida*volumen_sumergida
    return resulatado
#fin_funcion



#funcion 07
#formula de dilatacion
def dilaticion_lineal(longitud_inicial,coeficiente_dilatacion,variacion_temperatura):
    resultado=longitud_inicial*coeficiente_dilatacion*variacion_temperatura
    return resultado
#fin_funcion



#funcion 08
#contador de palabras
def contador(palabra):
    cad=palabra.split(" ")
    suma=0
    for i in cad:
        suma+=1
    return suma
#fin_funcion




#funcion 09
#contador de letras
def contador_letras(palabra):
    suma=0
    for i in palabra:
        if(i==" "):
            suma-=1
        suma+=1
    return suma
#fin_funiciones



#funcion 10

#Sacar promedio de notas
def promedio_notas(nombre_alumno,nota01,nota02,nota03):
    promedio=(nota01+nota02+nota03)//3
    print("El Alumno es:",nombre_alumno)
    print("1er nota:",nota01)
    print("2da nota:",nota02)
    print("3er nota:",nota03)
    return promedio
#fin_funcion




#funcion 11
#verificador de contraseñas
def verificador(contra):
    msg=""
    print(contra)
    while(len(contra)<8):
        print("La contra debe tener al menos 8 caracteres")
        contra=input("Ingrese contraseña:")
    #fin_while
    for i in contra:
        if(i=="@" or i.isdigit()==True):
            msg="La contraseña es correcta"
        else:
            msg="La contraseña es incorrecta"
            #fin_for
    return msg
#fin_funcion


#funcion 12
def area_rombo(diagonal_mayor,diagonal_menor,altura):
    area=(diagonal_mayor+diagonal_menor)*altura//2
    return area
#fin_funcion



#funcion 13
#formula de fuerza
def fuerza(masa,aceleracion):
    resultado=masa*aceleracion
    return resultado
#fin_funcion



#funcion 14
def potencia(trabajo,tiempo):
    resultado=trabajo//tiempo
    return resultado
#fin_funcion




#funcion 15
#densidad
def densidad(masa,volumen):
    resultado=masa//volumen
    return resultado
#fin funcion


#funcion 16
def trabajo(fuerza,distancia):
    resultado=fuerza*distancia
    return resultado
#fin funcion


#funcion 17
#capicuas
def capicua(numero):
    msg=""
    if(isinstance(numero,int)==True):
        cad=str(numero)
        if(cad==cad[::-1]):
            msg="el numero es capicua"
        else:
            msg="el numero no es capicua"
        return msg
    else:
        msg="Variable no es un entero"
        return msg
#fin_funcion



#funcion 18

#termometro
def termometro(temperatura):
    msg=""
    while(temperatura<0 or temperatura>100):
        print("Es la temperatura de una persona")
        temperatura=int(input("Ingrese temperatura:"))
        #fin while

    if(temperatura>30 and  temperatura<=40):
        if(temperatura>34 and temperatura<=37):
            msg="Ud esta con temperatura normal"

        else:
            msg="Ud esta enfermo"
        #fin_if
    else:
        msg="temperatura invalida"
    return msg
#fin funcion



#funcion 19
#verificador de contraseñas
def verificador_contra(contra,repetir_contra):
    msg=""
    while(repetir_contra!=contra):
        print("Contraseña incorrecta")
        repetir_contra=input("Ingrese contraseña correcta:")
        #fin_while

    if(repetir_contra==contra):
        msg="contraseña correcta"
    return msg
#fin_funcion



#funcion 20
#programa para que el usuario ponga su edad y su salario y si cumpke con el requesito pueda tributar
def tributo(edad, salario):
    msg=""
    while(edad<=0 or edad>100):
        print("Edad invalidad")
        edad=int(input("Ingrese edad:"))

    if(edad>=19 and salario>=1000):
        msg="Ud debe tributar"
    else:
        msg="Ud todavia no tributa"
    return msg
#fin funcion



#funcion 21
#crear un programa donde al introducir el sexo de la persona este puede
#indicar el grupo a donde le pertenece y tambien que pida el nombre

def grupos(nombre,sexo):
    msg=""
    while(sexo.lower()!="femenino" and sexo.lower()!="masculino"):
        print("Sexo incorrecto")
        sexo=input("Ingrese sexo:")
        #fin_while
    if(sexo.lower()=="femenino"):
        msg="Ud es del grupo \"A\""
    else:
        msg="Ud es del grupo \"B\""

    print(nombre)
    return msg
#fin funcion



#funcion 22
def gasto_mensual(semana1,semana2,semana3,semana4):
    gasto=semana1+semana2+semana3+semana4
    if(gasto>=200):
        print("Ud esta excedido")
    return gasto




#funcion 23
#hacer in programa que al introducir un numeero muestre los numeros pares desde el 0 hasta el numero
#e indicar cuantos numero hay
def contador_pares(numero):
    suma=0
    for i in range(0,numero,2):
        print(i,end=",")
        suma+=1
    return suma
#fin funcion





#funcion 24
#el area lateral de un prisma recto
def area_prisma(perimeto_base,arista_lateral):
    resultado=perimeto_base*arista_lateral
    return resultado
#fin funcion


#funcion 25
#area total de un prisma recto
def area_total(area_lateral,area_base ):
    resultado=area_lateral+2*area_base
    return resultado
