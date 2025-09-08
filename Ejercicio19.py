tv40 = 500000
mouse = 20000
mochila = 40000


print("Bienvenido, tenemos en venta TV de 40 a $500.000 en Electrónica, un Mouse Targa a $20.000 en Computación y una Mochila Gerson a $40.000 en Indumentaria")
print("Hay descuento del 25'%' en electrónica y del 10'%' en Computación y 5'%' en Indumentaria."
"Si quiere comprar la TV escriba Televisor, si quiere el mouse, escriba Mouse y si quiere la mochila, escriba Mochila")

producto = input("Cuál es el producto que desea comprar:")

if producto.lower() == 'televisor':
    print(f'Su compra de la televisión de 40 es de {tv40 * 0.75}')
elif producto.lower() == 'mouse':
    print(f'Su compra del mouse Targa es de {mouse * 0.90}')
elif producto.lower() == 'mochila':
    print(f'Su compra de la mochila Gerson es de {mochila * 0.95}')

