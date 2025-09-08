print("Por favor ingresá las longitudes del tríángulo que querés clasificar:")
cat1 = int(input("Ingresá el primer lado:"))
cat2 = int(input("Ingresá el segundo lado:"))
hipo = int(input("Ingresá el tercer lado:"))

if cat1 == cat2 == hipo:
    print("Es un Equilátero")
elif (cat1 == cat2) or (cat2 == hipo) or (hipo == cat1):
    print("Es un Isósceles")
elif cat1 != cat2 != hipo:
    print("Es un Escaleno")