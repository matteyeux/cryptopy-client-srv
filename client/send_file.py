#!/usr/bin/python3
import socket
import sys
# création de socket
socketServeur = socket.socket()
# écoute sur tous les interfaces, port 20 
socketServeur.bind(("127.0.0.1",2000))
# attente & acceptation de client
socketServeur.listen(1)
socketClient, address = socketServeur.accept()
# transfert ce fichier
chemin_file=r"a.txt" ##le r"..." permet de ne pas interpréter les '\'
file_send = open(chemin_file,"rb") #open in binary
# "envoyer" le fichier sur la socket
while True:
    chunk = file_send.read(65536) #lire donnee dans le fichier
    if not chunk: 
        break  # EOF
    socketClient.sendall(chunk) # evoie à la socket
#fermeture
file_send.close()
socketClient.close()
socketServeur.close()
