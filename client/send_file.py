#!/usr/bin/python3
import socket
import sys
import os
sys.path.insert(0, "../server")
import cesar

def read_and_crypt(file_to_touch):
	f = open(file_to_touch, "r")
	file2read = f.read()
	print(file2read)
	file2crypt = cesar.cesar_crypt(file2read, 1)
	print(file2crypt)
	f.close()
	crypted_file = file_to_touch + ".crypt" 
	f = open(crypted_file, "w")
	f.write(file2crypt)
	f.close()

def send_crypted_file(crypted_file): #theo was here

	socketServeur = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	socketServeur.bind(("127.0.0.1",2000))
	socketServeur.listen(1)
	socketClient, address = socketServeur.accept()
	crypted_file = crypted_file + ".crypt"
	file2send = open(crypted_file,"rb") #open in binary
	while True:
	    chunk = file2send.read(65536) #lire donnee dans le fichier
	    if not chunk: 
                break  # EOF
            socketClient.sendall(chunk) # envoie à la socket
	file2send.close()
	socketClient.close()
	socketServeur.close()

def usage(python_file):
    print("usage:", python_file, "[file]")

if __name__ == '__main__':
	
	if len(sys.argv) != 2:
		usage(sys.argv[0])
		sys.exit(1)

	arg_file = sys.argv[1]
	if os.path.exists(arg_file) != True:
		print("[error] " + arg_file + ": no such file or directory")
		sys.exist(1)
	
	read_and_crypt(arg_file)
        send_crypted_file(arg_file)
