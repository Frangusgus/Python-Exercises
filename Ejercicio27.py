num = int(input("Escriba un número para ver si es par o impar:"))

if num % 2 != 0:
    print(f'{num} es impar')
elif num % 2 == 0:
    print(f'{num} es par')