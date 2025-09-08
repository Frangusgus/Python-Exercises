print('Le vamos a solicitar que ingrese el nombre del artículo, su costo unitario y el número de departamento. Se le incrementará el precio final según el departamento. Sólo hay 4 departamentos')

articulo = input('Por favor ingrese el nombre del artículo: ')
costo = int(input('Por favor ingrese el costo unitario: '))
departamento = int(input('Y ahora ingrese el número de departamento: '))

if departamento == 1:
    print(f'Su precio por {articulo} es de ${costo}')
elif departamento == 2:
    print(f'Su precio por {articulo} es de ${costo * 5}')
elif departamento == 3:
    print (f'Su precio por {articulo} es de ${costo * 10}')
elif departamento == 4:
    print (f'Su precio por {articulo} es de ${costo * 15}')