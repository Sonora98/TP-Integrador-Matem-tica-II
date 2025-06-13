#TP Ingregrador II Matemática

#   &&&&&=A.OPERACIONES CON DNI=&&&&&

#   ==DEFINICION DE FUNCIONES==

#Conjuntos
def generar_conjuntos(DNI):
    return set(DNI)

#Operaciones: union, interseccion, diferencias, diferencia_simetrica
def operaciones_conjuntos(DNI1, DNI2, DNI3):
    conjunto1 = generar_conjuntos(DNI1)
    conjunto2 = generar_conjuntos(DNI2)
    conjunto3 = generar_conjuntos(DNI3)

    union = conjunto1 | conjunto2 | conjunto3
    interseccion = conjunto1 & conjunto2 & conjunto3
    diferencia1 = conjunto1 - conjunto2
    diferencia2 = conjunto2 - conjunto3
    diferencia3 = conjunto3 - conjunto1
    diferencia_simetrica = conjunto1 ^ conjunto2 ^ conjunto3

    return {
        "union": union,
        "interseccion": interseccion,
        "diferencia1": diferencia1,
        "diferencia2": diferencia2,
        "diferencia3": diferencia3,
        "diferencia_simetrica": diferencia_simetrica
    }
    
#conteo de frecuencia de cada dígito
def contar_frecuencia(DNI):
    frecuencias = {}

    for digito in DNI:
        if digito in frecuencias:
            frecuencias[digito] += 1
        else:
            frecuencias[digito] = 1

    return frecuencias

#sumar dígitos DNI
def suma_digitos(DNI):
    num = int(DNI)    
    suma=0

    for digito in range (0, len(DNI)):
        suma += digito
    
    return suma
  












#  ==PROGRAMA PRINCIPAL==

#Inputs
DNI1 = input("Intregrante N°1. Ingrese su número de DNI: ")
DNI2 = input("Intregrante N°2. Ingrese su número de DNI: ")
DNI3 = input("Intregrante N°3. Ingrese su número de DNI: ")

#llamados
print("Conjunto1:", generar_conjuntos(DNI1))
print("Conjunto2:", generar_conjuntos(DNI2))
print("Conjunto3:", generar_conjuntos(DNI3))
print(operaciones_conjuntos(DNI1, DNI2, DNI3))

frec1 = contar_frecuencia(DNI1)
frec2 = contar_frecuencia(DNI2)
frec3 = contar_frecuencia(DNI3)
print("Frecuencia de cada dígito (DNI1):")
for digito, cantidad in frec1.items():
    print(f"Dígito {digito}: {cantidad} vez/veces")
    
print("Frecuencia de cada dígito (DNI2):")
for digito, cantidad in frec2.items():
    print(f"Dígito {digito}: {cantidad} vez/veces")

print("Frecuencia de cada dígito (DNI3):")
for digito, cantidad in frec3.items():
    print(f"Dígito {digito}: {cantidad} vez/veces")

print(f"La suma de los dígitos del DNI1({DNI1}) es: {suma_digitos(DNI1)}")
print(f"La suma de los dígitos del DNI2({DNI2}) es: {suma_digitos(DNI2)}")
print(f"La suma de los dígitos del DNI3({DNI3}) es: {suma_digitos(DNI3)}")




#   &&&&&=B.OPERACIONES CON AÑOS DE NACIMIENTO=&&&&&

#   ==DEFINICION DE FUNCIONES==

def par_impar(AÑO1, AÑO2, AÑO3):
    años = [AÑO1, AÑO2, AÑO3]
    par = 0
    impar = 0

    for i in años:
        if i % 2 == 0:
            par += 1
        else:
            impar += 1
    
    print("La cantidad de integrantes nacidos en años pares es: ", par, "\nLa cantidad de integrantes nacidos en años impares es: ", impar)

def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False









#  ==PROGRAMA PRINCIPAL==

#inputs
AÑO1 = int(input("Intregrante N°1. Ingrese su año de nacimiento(YYYY): "))
AÑO2 = int(input("Intregrante N°2. Ingrese su año de nacimiento(YYYY): "))
AÑO3 = int(input("Intregrante N°3. Ingrese su año de nacimiento(YYYY): "))

#llamados
par_impar(AÑO1, AÑO2, AÑO3)

if AÑO1>=2000 and AÑO2>=2000 and AÑO3>=2000:
    print("Grupo Z")

if es_bisiesto(AÑO1) or es_bisiesto(AÑO2) or es_bisiesto(AÑO3):
    print("Tenemos un año especial")


























