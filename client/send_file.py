#!/usr/bin/python3
import socket
import sys
sys.path.insert(0, "../server")
import cesar
socketServeur = socket.socket()
socketServeur.bind(("127.0.0.1",2000))
socketServeur.listen(1)
socketClient, address = socketServeur.accept()

chemin_file="a.txt"
f = open("a.txt", "r")
file2read = f.read()
print(file2read)
file2crypt = cesar.cesar_crypt(file2read, 1)
print(file2crypt)
f.close()

f = open("crypt.txt", "w")
f.write(file2crypt)
f.close()


file_send = open("crypt.txt","rb") #open in binary
while True:
    chunk = file_send.read(65536) #lire donnee dans le fichier
    if not chunk: 
        break  # EOF
    socketClient.sendall(chunk) # evoie à la socket

file_send.close()
socketClient.close()
socketServeur.close()
