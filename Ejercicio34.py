refacciones = int(input("Ingrese los importes de ventas por refacciones: "))
servicios = int(input("Ingrese los importes de ventas por servicios: "))
vehiculos = int(input("Ingrese el importe de ventas por vehiculos: "))

total = refacciones + servicios + vehiculos

if total >= 50000: 
    print(f'El precio total es de ${total} y el promedio de ${(total + 3) / 3}. Se alcanzó el objetivo de $50.000')
else:
    print(f'El precio total es de ${total} y el promedio de ${(total + 3) / 3}')