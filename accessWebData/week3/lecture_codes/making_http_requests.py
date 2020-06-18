# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 20:53:41 2020

@author: Harvey
Making an HTTP Request in Python
"""

import socket
# making a doorway
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to host if existing with port number, otherwise, will fail if not exists
mysock.connect(('data.pr4e.org', 80))
# make a request commmand
# \r\n\r\n - enter two times i guess \r carriage return is needed in windows os while in linux its not
# encode converts unicode to UTF-8
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# send the request command
mysock.send(cmd)

while True:
    data = mysock.recv(512) # received up to 512 characters
    if (len(data) < 1): # if we get no data, EOF, or EO transmission
        break
    print(data.decode()) # decode, interpret and decode data, converts UTF-8 to unicode
mysock.close()

# steps
# 1. make a connection to port 80
# 2. send a get request with blank line
# 3. wait and read data then print