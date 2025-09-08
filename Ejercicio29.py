print("Vamos a ver cuál de los tres números que ingreses es el mayor:")
num1=int(input("Escriba el primer número, por favor:"))
num2=int(input("Ahora escriba el segundo número, por favor:"))
num3=int(input("Ahora escriba el tercer número, por favor:"))

if num1 > num2 and num3:
    print (f'{num1} es el número mayor')
elif num2 > num3:
    print (f'{num2} es el número mayor')
else:
    print (f'{num3} es el número mayor')