# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:07:00 2023

@author: USER
"""
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Stuff about my IP
hostname = socket.gethostname()
localhost = socket.gethostbyname(hostname)
print('my computer ip: ', localhost)
                               
server_socket.bind((localhost, 3000))

server_socket.listen(5)

conn, addr = server_socket.accept()
print('Connected by', addr)

data = conn.recv(1024)
print('Received message:', data.decode())

conn.close()

server_socket.close()


