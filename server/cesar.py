def CesarCrypt(ch,n):
    result = ''
    for i in range(len(ch)):
        result = result + chr((ord(ch[i]) + n-ord('a')) % 26 + ord('a'))
    return result

str_origin = raw_input("Entrer un message : ")

for i in range(len(str_origin)):
	str_origin[i].isupper()
	Upper = list().append(i)
	str_origin[i].islower()
	Upper = list().append(0)

str_origin= str_origin.lower()
int_cle = int(input("Entrer la cle : "))
str_cryp=CesarCrypt(str_origin,int_cle)
print(str_cryp)

def decrypte(ch,n):
	result = ''
	for i in range(len(ch)):
		result = result + chr((ord(ch[i]) - n - ord('a')) % 26 + ord('a'))
	return result
str_cryp1 = raw_input("Entrer un message : ")

for i in range(len(str_cryp1)):
	str_origin[i].islower()
	lower = list().append(i)
	
	for i in range(len(Upper))
		

str_origin= str_origin.lower()




int_cle1 = int(input("Entrer la cle : "))
str_origin1 = decrypte(str_cryp1,int_cle1)
print(str_origin1)
