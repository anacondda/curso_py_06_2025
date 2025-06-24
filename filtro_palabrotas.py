palabrotas = {"idiota":"@",
              "imbecil":"#",
              "hijo puta":"$",
              "coño":"%"
              }

palabra = input ("Introduce una palabra, por favor ")
las_palabrotas = palabrotas.keys()
if palabra in las_palabrotas:
    print(palabrotas.get(palabra))  
    