#De referencia utilicé el cuadro tarifario de Edesur Tarifa 1 R pero cerrándolo en números enteros

consumo = int(input("Escriba aquí su consumo: "))

if consumo > 0 and consumo <= 150:
    print(f'El monto a pagar de su consumo es de ${1186 + (consumo * 102)} pesos')
elif consumo > 150 and consumo <= 400:
    print(f'El monto a pagar de su consumo es de ${2491 + (consumo * 103)} pesos')
elif consumo > 400 and consumo <= 500:
    print(f'El monto a pagar de su consumo es de ${8154 + (consumo * 111)} pesos')
elif consumo > 500 and consumo <= 600:
    print(f'El monto a pagar de su consumo es de ${13298 + (consumo * 113)} pesos')
elif consumo > 600 and consumo <= 700:
    print(f'El monto a pagar de su consumo es de ${28752 + (consumo * 122)} pesos')
else:
    print(f'El monto a pagar de su consumo es de ${43630 + (consumo * 133)} pesos')