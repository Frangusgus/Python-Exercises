salario = 40
extra = 80
print("En su salario, se le paga 40$ por hora, vamos a calcular cuánto debe cobrar este mes. Si laburó más de 160 horas se le paga el doble por las horas extras")
horas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))



if horas <= 160:
    print(f'Su salario mensual es de ${horas * salario} pesos')
elif horas > 160:
    print(f'Su salario mensual es de ${((horas - 160) * extra) + (salario * 160)} pesos')


