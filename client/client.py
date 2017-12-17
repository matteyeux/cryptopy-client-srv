#!/usr/bin/python3
import sys
import os
import socket
from random import randint
# on va chercher le module cesar avec l'algo cesar implémenté
sys.path.insert(0, "../server")
import cesar

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 2345

# envoie et reçoit les données du serveur
# return : le resultat de la chaine envoyée par le serveur
# on precise comme argument l'ip du srv, le port, le msg a envoyer puis la clé pour dechiffrer
def send_and_recv(srv_ip, srv_port, msg2srv, key):
	sock.connect((srv_ip, srv_port))

	key_and_msg = str(key) + ":" + msg2srv
	print("[i] key and message : " + key_and_msg)
	sock.send(key_and_msg.encode())

	srv_reply = sock.recv(255).decode()
	print(srv_reply)

	decrypted = sock.recv(255).decode()
	print("[x] decrypted msg : " + decrypted)

	sock.close()
	return decrypted

def usage(python_file):
    print("usage:", python_file, "[message] <key>")


if __name__ == '__main__':
	argc = len(sys.argv)
	if argc <= 1:
		usage(sys.argv[0])
		sys.exit()
	if argc == 3:
		crypto_key = int(sys.argv[2])
	else :
		crypto_key = randint(1,10000)
	message = sys.argv[1]
	# on appelle la fonction cesar_crypt(string, key) depuis le module cesar
	crypted_msg = cesar.cesar_crypt(message, crypto_key)
	print("[i] crypted message : " + crypted_msg)

    # la variable check aura la valeur de la chaine dechiffrée
	check = send_and_recv(host, port, crypted_msg, crypto_key)
	if check == message:
		print("[+] server successfully decrytped string")
	else :
		print("[e] string is wrong")
