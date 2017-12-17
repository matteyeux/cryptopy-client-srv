#!/usr/bin/python3
import tkinter as tk
import socket
import threading
import sys
from random import randint
sys.path.insert(0, "../server")
import cesar
class Msn(tk.Frame):
	def __init__(self, window, **kwargs):
		tk.Frame.__init__(self, window)
		self.pack(fill=tk.BOTH)
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_socket.connect(('127.0.0.1', 2345))
		self.hist=tk.Text(self,width=20,height=15,wrap=tk.WORD)
		self.hist.pack()
		self.lblTexte = tk.Label(self, text="", anchor = "w")
		self.lblTexte.pack()
		self.saisie = tk.Entry(self)
		self.saisie.pack()
		self.send = tk.Button(self, text="send", command=self.send2srv)
		self.send.pack()      
		self.butQuit = tk.Button(self, text="Quit", command=self.leave)
		self.butQuit.pack()
		self.saisie.bind("<Return>", self.callback)
		b = threading.Thread(None, self.recv_from_srv, None)
		b.start()
              

	def callback(self, event):
		self.send2srv()
	
	def leave(self):
		self.client_socket.close()
		self.quit()

	def send2srv(self):
		key = randint(1,10000)
		data_input = self.saisie.get()
		data2crypt = cesar.cesar_crypt(data_input, key)
		key_and_msg = str(key) + ":" + data2crypt
		self.client_socket.send(key_and_msg.encode())
		self.hist.insert(tk.END,'msg:  ' + data_input + "\n")

	def recv_from_srv(self):
		while 1:
			self.data_receive = self.client_socket.recv(2048).decode()
			self.hist.insert(tk.END,'serveur: '+ self.data_receive)


if __name__ == '__main__':
	window = tk.Tk()
	window.resizable(width=False,height=False)
	window.title("Chat client")
	window.geometry("300x400")
	Msn = Msn(window)
 
	Msn.mainloop()
	window.destroy()



