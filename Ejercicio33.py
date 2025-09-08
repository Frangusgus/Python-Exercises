print('El costo por día de internación es de 40.000 en pediatría, 30.000 en maternidad y 60.000 en otro')

pediatria = 40000
maternidad = 30000
otro = 60000
internacion = input('Por favor ingrese la categoría de internación entre Pediatría, Maternidad u Otro: ')
diasinternado = int(input('Ahora por favor ingrese la cantidad de días internado: '))

if internacion.lower() == 'pediatría':
    print(f"Su total a pagar es de ${pediatria * diasinternado}")
elif internacion.lower() == 'pediatria':
    print(f"Su total a pagar es de ${pediatria * diasinternado}")
elif internacion.lower() == 'maternidad':
    print(f'Su total a pagar es de ${maternidad * diasinternado}')
elif internacion.lower() == 'otro':
    print(f'Su total a pagar es de ${otro * diasinternado}')