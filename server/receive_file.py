#!/usr/bin/python3
import socket # attention -> cela peut être from socket import *
import sys
import sys

import cesar

# ducnm81@gmail.com

def recv_file(crypted_filename):
	socketClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#connecter au serveur
	socketClient.connect(("127.0.0.1",2000))
	file_receive = open (crypted_filename, "wb") # le fichier à recevoir. On renomme le fichier reçu
	data_receive = socketClient.recv(65536)
	file_receive.write(data_receive)       
	# fermeture
	file_receive.close()
	socketClient.close()

def decrypt_file(crypted_filename):
	f = open(crypted_filename, "r")
	readfile = f.read()
	print(readfile)
	
	decrytped_file = open(crypted_filename + ".dec", "w")
	decrypt = decrytped_file.write(cesar.cesar_decrypt(readfile, 1))
	#print(cesar.cesar_decrypt(readfile, 1))
	
if __name__ == '__main__':
	recv_file("crypted_file")
	decrypt_file("crypted_file")
