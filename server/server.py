#!/usr/bin/python3
import socket
import _thread

# socket serveur
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
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
                        print("Connexion perdue")
                        conn.close()
                print(data)
        conn.close()

if __name__ == '__main__':
    print("server is running")
    try:
        while True:
            c, addr = sock.accept()
            _thread.start_new_thread(client_thread, (c,))
        sock.close()
        print("jo")
    except Exception :
        import traceback
        print("hi")
        #print(traceback.format.exc())
