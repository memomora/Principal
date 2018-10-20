#Ejemplos de uso del if en python

esta_lloviendo = True
tenemos_hambre = False
python_es_genial = True
ayer_pagaron = False
vamos_a_la_playa = False

#Funcion para solicitar datos por consola input(mensage)
#la funcion input siempre devuelve un string. Tenemos
#que convertirlo a numero antes de hacer operaciones
#numericas

numero_digitado = float(input("Digite un numero: "))

if esta_lloviendo and tenemos_hambre:
    #este codigo esta dentro del if
    print("Esta lloviendo y tenemos hambre")
elif numero_digitado > 12 and python_es_genial or vamos_a_la_playa:
    print("Python es genial o vamos a la playa")
else:
    print("Esto se ejecuta si ninguna condicion anterior es verdadera")

