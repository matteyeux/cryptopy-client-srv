def CesarCrypt(ch,n):
    result = ''
    for i in range(len(ch)):
        result = result + chr((ord(ch[i]) + n-ord('A')) % 26 + ord('A'))
    return result

str_origin = input("Entrer un message : ")
int_cle = int(input("Entrer la clé : "))
str_cryp=CesarCrypt(str_origin,int_cle)
print(str_cryp)

