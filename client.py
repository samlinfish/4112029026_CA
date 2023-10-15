# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:06:36 2023

@author: USER
"""
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('140.120.248.113', 3000))

message = input("Enter a message: ")
client_socket.sendall(message.encode())

client_socket.close()


