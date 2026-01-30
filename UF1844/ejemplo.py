MAX_INTENTOS = 5
clave = 'manolito'
intentos = 0

while intentos < MAX_INTENTOS:
    user_pass = input("Introduzca la clave: ")
    if clave != user_pass:
        print("Clave incorrecta")
        intentos += 1
    else:
        print("Bienvenido. Has entrado.")
        break

if intentos == MAX_INTENTOS:
    print("Expulsado del sistema")