print("Vamos a ver si un número es mayor, menor o igual que el otro")
num1=int(input("Escriba el primer número, por favor:"))
num2=int(input("Ahora escriba el siguiente número, por favor:"))
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num1} es menor que {num2}")
else:
    print ("Ambos números son iguales")
