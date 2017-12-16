#!/usr/bin/python3
import socket
import _thread
import sys

import cesar

# socket serveur
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# https://stackoverflow.com/questions/337115/setting-time-wait-tcp
# https://stackoverflow.com/questions/4465959/python-errno-98-address-already-in-use?lq=1
# On change le comportement de la socket pour reutiliser l'addr
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = '127.0.0.1'  # l'ip locale de l'ordinateur
port = 2345         # choix d'un port

# on bind notre socket
sock.bind((host,port))

# On est pret à accueillir 10 clients max
sock.listen(10)

# une fonction pour accueillir un client
# parametre: conn : socket correspondante au client
# pour chaque client, on recoit une donnée et l'affiche
def client_thread(conn):
	while True:
		data = conn.recv(255).decode()
		if not data:
			print("[-] connection lost\n")
			conn.close()
			sys.exit(-1)
			print(data)

		print("[i] data received : " + data)
		print("[i] data to decrypt : " + data[2:])

		key = data.split(":",1)[0] # data[:1] is bad when key is > 9 better use split
		print("[i] key : " + key)

		cool = "[x] reply from serv : " + data
		client.send(cool.encode())

		data2dec = data.split(":",1)[1]
		dec_data = cesar.cesar_decrypt(data2dec, int(key))
		print("[i] decrypted string : " + dec_data)
		client.send(dec_data.encode())
	conn.close()

if __name__ == '__main__':
	print("server is running")
	while True:
		client, addr = sock.accept()
		print("[+] client : " + str(addr[0])) # if print addr -> ('127.0.0.1', 37010)
		print("[+] port : " + str(addr[1]))
		_thread.start_new_thread(client_thread, (client,))
	sock.close()