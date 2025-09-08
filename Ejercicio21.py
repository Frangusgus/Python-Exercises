print('Esto es un semáforo, la letra A representa el color Verde, la letra B representa Amarillo y la C representa Rojo')

semaforo = input('Elija por favor una letra entre A, B y C para asignar el color al semáforo:')
                        
if semaforo.lower() == 'a':
    print('El semáforo está en verde')
elif semaforo.lower() == 'b':
    print('El semáforo está en amarillo')
elif semaforo.lower() == 'c':
    print('El semáforo está en rojo')