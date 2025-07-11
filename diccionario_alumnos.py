alumnos = { 
            "alumno1" :{"nombre":"Pedro",
             "edad" : 22,
             "cursos" : ["ingles","frances","ia generativa","basico de python"],
            },
            
            "alumno2":{"nombre":"Juan",
            "edad" : 21,
            "cursos" : ["frances"],
            },
            "alumno3" : {"nombre":"Lidia",
            "edad" : 20,
            "cursos" : ["ia generativa","basico de python"],
            }    
          }


def nun_alumnos_por_asignatura():
    #se crea un nuevo diccionario con cada asignatura como clave 
    #y el numero de alumnos como valor
    alumnos_asignaturas = {}
    for clave , valor  in  alumnos.items():
        un_alumno = valor
        mis_cursos = un_alumno["cursos"]
        for curso in mis_cursos:
            if curso in alumnos_asignaturas:
                alumnos_asignaturas[curso] += 1
            else:
                alumnos_asignaturas[curso] = 1
    print ("Alumnos por asignatura :\n")
    for clave , valor in alumnos_asignaturas.items():
        print (f"Asignatura: {clave}, nº alumnos {valor}")
    input("Presiona Enter para continuar...")

def alumno_y_asignaturas():
    lista_nombres = []
    for values in alumnos.values():
        mi_di = values
        asignaturas = ", ".join(mi_di["cursos"])
        print(f"- Nombre: {mi_di["nombre"]}, asignaturas: {asignaturas}")
    input("Presiona Enter para continuar...")

while  True:
    print (f"""
    GESTOR DE ALUMNOS
    1.- Numero de alumnos por cada asignatura
           
    2.- Nombre de alumno y sus cursos
    3.- Media de notas por alumno
    0.- Salir
    """)
    opcion = input("Indique tipo informe ") 
    
    if opcion == "1":
        nun_alumnos_por_asignatura()
    elif opcion == "2":
        alumno_y_asignaturas()
    elif opcion == "3":
        print (opcion)
    elif opcion == "0":
        break
        print ("Fin") #si no pongo este print, la opción funciona
    else:
        print ("Opcion debe ser 1,2,3,0")

   