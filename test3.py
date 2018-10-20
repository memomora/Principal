suma_total = 0
numero_actual = 0

while numero_actual <= 100:
    suma_total = suma_total + numero_actual
    numero_actual += 1
    #en este punto vuelve a evaluar la condicion
    #inicial del while

print("La suma de los numero del 0 al 100 es: {}, y su mitad es: {}".format(suma_total,suma_total/2))




