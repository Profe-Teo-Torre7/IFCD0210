# Calcular el precio con IVA de un producto
precio_producto = 32
porcentaje_iva = 0.21
#precio_total = precio_producto + precio_producto * porcentaje_iva
precio_total = precio_producto * (1 + porcentaje_iva)
print("El precio total es: " + str(precio_total))
# ----------------------------------------

# Convertir de grados Celsius a Fahrenheit
# F = C * 1.8 + 32

grados_celsius = -17
grados_fh = grados_celsius * 1.8 + 32
#print(grados_celsius, '-->',grados_fh)
mensaje = str(grados_celsius) + " Grados Celsius son " + str(grados_fh) + " Grados Fh"
print(mensaje)

# -------------------------------

# Calcular el índice de masa corporal
# IMC = Peso(kg) / altura ** 2
# imc < 18: Bajo
# 18 < imc < 25: Normal
# > 25: Sobrepeso

peso = 57
altura = 1.77
imc = peso / altura ** 2
print(imc)


