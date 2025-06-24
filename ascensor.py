import keyboard

origen = 0
destino = 0
maximo_piso = 20
minimo_piso = -2
funcionando = True

def subir(pasos,destino):
    subo_piso = 0
    for i in range(pasos):
        subo_piso +=  1
    resul = True if subo_piso == destino else false
    if subo_piso == destino:
        resul = True
    else:
        resul = False

    return resul 


def bajar(piso,destino):
    print (piso,destino)
    return True

while True:
    if keyboard.is_pressed('esc'):
        funcionado = False
    
    destino = int(input ("Piso: "))
    pisos = destino - origen

    if destino > origen:
        resultado = subir(pisos,destino)
    elif destino < origen:
        resultado = bajar(pisos,destino)
    else:
        print ("ya estas en ese piso")

    if resultado == False:
       print ("Hay que llamar al tecnico")
    else:
       print ("Abrir puertas")
       