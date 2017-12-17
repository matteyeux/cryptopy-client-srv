#!/usr/bin/python3
import tkinter as tk
import socket
import threading
import sys
sys.path.insert(0, "../server")
import cesar
class Msn(tk.Frame):
	def __init__(self, fenetre, **kwargs):
		tk.Frame.__init__(self, fenetre)
		self.pack(fill=tk.BOTH)
		# self.lblTitre = Label(self, text="CHAT SERVER", anchor = "w")
		# self.lblTitre.pack(side=TOP)
		# self.lblTexte = Label(self, text="", anchor = "w")
		# self.lblTexte.pack(side=BOTTOM)
		self.hist=tk.Text(self,width=20,height=15,wrap=tk.WORD)
		self.hist.pack()
		self.saisie = tk.Entry(self)
		self.saisie.pack()
		self.butenvoyer = tk.Button(self, text="Send", command=self.send2client)
		self.butenvoyer.pack()
		self.butQuit = tk.Button(self, text="Quit", command=self.leave)
		self.butQuit.pack()
		self.saisie.bind("<Return>", self.callback)
		self.a = threading.Thread(None, self.connect, None)
		self.a.start()
		self.b = threading.Thread(None, self.recv_from_srv, None)


	def callback(self, event):
		self.send2client()

	def leave(self):
		self.quit()

	def recv_from_srv(self):
		while 1:
			self.data_receive = self.client.recv(2048).decode()
			
			self.key = self.data_receive.split(":",1)[0]
			self.data2dec = self.data_receive.split(":",1)[1]
			
			self.data_decrypt = cesar.cesar_decrypt(self.data2dec, int(self.key))
			self.hist.insert(tk.END,'client:  '  + self.data_decrypt + "\n")

	def connect(self):
		self.Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.Sock.bind(('127.0.0.1',2345))
		self.Sock.listen(10)
		self.client, self.adresse = self.Sock.accept()
		self.b.start()

	def send2client(self):
		data_send = self.saisie.get()
		data_send+='\n'
		self.client.send(data_send.encode())
		self.hist.insert(tk.END,'moi:  ' + data_send)
        
if __name__ == '__main__':	
	fenetre = tk.Tk()
	fenetre.resizable(width=False,height=False)
	fenetre.title("Chat server")
	fenetre.geometry("300x400")
	Msn = Msn(fenetre)
	 
	Msn.mainloop()
	fenetre.destroy()
