print("Bienvenido a la tienda. Cada producto vale $30.000. Se puede pagar en efectivo, con QR o con tarjeta")
print("Si usted paga en efectivo tendrá un 15'%' de descuento. Si supera los 3 productos comprados tiene, además, un 5'%' de descuento sin importar el medio de pago")

precio = 30000
cantidad = int(input("Cuántos desea comprar?: "))
medio = str(input("Con qué desea pagar? Escriba Tarjeta, Efectivo o QR: "))

if cantidad <= 3 and medio.lower() == 'efectivo':
    print (f"Su total a pagar es ${(precio*cantidad) * 0.80}")
elif cantidad > 3 and medio.lower() == 'efectivo':
    print(f"Su total a pagar es ${(precio*cantidad) * 0.75}")
elif cantidad > 3 and medio.lower() == 'qr' or 'tarjeta':
    print(f"Su total a pagar es ${(precio*cantidad) * 0.95}")
    
