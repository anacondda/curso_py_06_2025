from datetime import datetime

#valores
nombre ="Ana"
so = "windows 11"
herramienta = "Python"
dia = str(datetime.now())
evento = "clase especial"
saludo = "Saludos"
#mail
mail =f"""
Titulo
------
"Estimado/a {nombre}, le cominicamos que el proximo {dia} 
tendra lugar {evento} de {herramienta}, para todos 
aquellos alumnos con so {so}

{saludo}
"""
print (mail)