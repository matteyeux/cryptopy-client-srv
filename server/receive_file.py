#!/usr/bin/python3
import socket # attention -> cela peut être from socket import *
import sys
socketClient = socket.socket()
#connecter au serveur
socketClient.connect(("127.0.0.1",2000))
file_receive=open ("fileReceive.txt", "wb") # le fichier à recevoir. On renomme le fichier reçu
data_receive = socketClient.recv(65536)
file_receive.write(data_receive)       
# fermeture
file_receive.close()
socketClient.close()
