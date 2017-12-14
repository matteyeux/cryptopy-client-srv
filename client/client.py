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
    sock.close()

def crypt_string(msg2crypt, key):
    result = ''
    for i in range(len(msg2crypt)):
        result = result + chr((ord(msg2crypt[i]) + key - ord('A')) % 26 + ord('A'))
    return result

def usage(python_file):
    print("usage:", python_file, "[message] <key>")

if __name__ == '__main__':
    #print(crypt_string("aaaa", 12))
    argc = len(sys.argv)
    if argc <= 1:
        usage(sys.argv[0])
        sys.exit()
    if argc == 3:
        crypto_key = int(sys.argv[2])
    else :
        crypto_key = 4
    message = sys.argv[1]
    crypted_msg = crypt_string(message, crypto_key)
    print(crypted_msg)
    serv_function("127.0.0.1", 2345, crypted_msg)
