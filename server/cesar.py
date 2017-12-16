#!/usr/bin/python3
# fonction qui va chiffrer notre chaine de caractères à l'aide d'une clé
# la clé est passée en parametre de la fonction
def cesar_crypt(string, key):
	for i in range(len(string)):
		string[i].isupper()
		Upper = list().append(i)
		string[i].islower()
		Upper = list().append(0)

	string = string.lower()

	result = ''
	for i in range(len(string)):
		result = result + chr((ord(string[i]) + key-ord('a')) % 26 + ord('a'))
	return result


# fonction pour dechiffrer la clé
def cesar_decrypt(string,key):
	for i in range(len(string)):
		string[i].islower()
		lower = list().append(i)

	string= string.lower()

	result = ''
	for i in range(len(string)):
		result = result + chr((ord(string[i]) - key - ord('a')) % 26 + ord('a'))
	return result
