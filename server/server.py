#!/usr/bin/python3
import socket
import _thread

## socket serveur
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = '127.0.0.1' # l'ip locale de l'ordinateur
Port = 2345         # choix d'un port 
# on bind notre socket
Sock.bind((Host,Port))
# On est pret à accueillir 10 clients
Sock.listen(10)

# une fonction pour accueillir un client
# parametre: conn : socket correspondante au client
# pour chaque client, on recoit une donnée et l'affiche

def client_thread(conn):
        while True:
                data = conn.recv(255).decode()
                if not data:
                        print("Connexion perdue")
                        conn.close()
                print(data)
        conn.close()

def CesarCrypt(ch,n):
    result = ''
    for i in range(len(ch)):
        result = result + chr((ord(ch[i]) + n-ord('A')) % 26 + ord('A'))
    return result

str_origin = input("Entrer un message : ")
int_cle = int(input("Entrer la clé : "))
str_cryp=CesarCrypt(str_origin,int_cle)
print(str_cryp)


#le serveur accueille des clients
while True:
       c, addr = Sock.accept()     # Establish connection with client.
       _thread.start_new_thread(client_thread, (c,))
Sock.close()
print("server")
