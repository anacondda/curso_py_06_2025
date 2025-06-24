palabrotas = {"idiota":"@",
              "imbecil":"#",
              "hijo puta":"$",
              "coño":"%"
              }

frase = input ("Introduce una palabra, por favor ")
mi_lista = frase.split(" ")
print (mi_lista)
las_palabrotas = palabrotas.keys()
frase_limpia =""
for palabra in mi_lista:
    if palabra in las_palabrotas:
        print(palabrotas.get(palabra)) 
        frase_limpia = frase.replace(palabra,palabrotas.get(palabra))
        
print (frase_limpia)