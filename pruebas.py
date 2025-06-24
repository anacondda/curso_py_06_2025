""""
vocales = ["a","e","i","o","u"]
print(vocales[:2:-1])


d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(d1)
print (d1["Nombre"])
"""
mapa_traducciones = {
    "a":"@",
    "e":"#",
    "i":"$",
    "o":"%",
    "u":"&"
}

contraseña=input("Introduce tu contraseña: ")

#for letra in contraseña:
#    if letra in mapa_traducciones.keys():
#        contraseña = contraseña.replace(letra,mapa_traducciones[letra])

#print (f"contraseña transformada {contraseña}")

print (mapa_traducciones.items())
