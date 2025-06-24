
def validar (mi_direccion):
    valido = False
    print (mi_direccion)
    if mi_direccion.count("@") != 1:
        valido = False
    else:
        cortar_mail = mi_direccion.split("@")
        #print(cortar_mail)
        #nombre
        if (cortar_mail[0].isalpha()) or ".":
            #if (cortar_mail[1].isalpha()) or cortar_mail[0] == ".":
            
        else:
            return False
        
        if cortar_mail[1].count(".") >= 1:
            return True
        else:
            return False

        



mails_validos = ["ejemplo@ejemplo.com","ejemplo@ejemplo.es","mi.ejemplo@ejemplo.ai","ejemplo+alias@ejemplo.com","nomber_apellido-otroapellido@ejemplo.com","1234567890@ejemplo.us"]
mails_invalidos = ["ejemplo@.com","ejemplo@es", "@ejemplo.comi","ejemplo@","ejemplo","ejemplo@.ejemplo.es","ejemplo@ejemplo..com"]
#for mail in mails_validos:
    #print(validar(mail))
for mail in mails_invalidos:
    print (f"direccion: {mail} {validar(mail)}")

