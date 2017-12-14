#!/usr/bin/python3
import sys
import os
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 2345

def serv_function(srv_ip, srv_port, msg2srv):
    sock.connect((srv_ip, srv_port))
    sock.send(msg2srv.encode())

def usage(python_file):
    print("usage:", python_file, "[message]")

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc != 2:
        usage(sys.argv[0])
        sys.exit()
    message = sys.argv[1]
    serv_function("127.0.0.1", 2345, message)
