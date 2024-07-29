#Se debe crear un conversor de grados C to F y viseversa
grados = float(input("Ingrese la temperatura a convertir:"))
escala = str(input("Es en Fahrenheit(F) o Celsius(C):")).lower()

if escala == "c":
    print(((grados * 9/5) + 32))
elif escala == "f":
    print(((grados - 32) * 5/9))
else:
    print("Escala incorrecta")