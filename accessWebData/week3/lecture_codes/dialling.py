# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:54:59 2020

@author: Harvey
# Make a socket connection like dialing a phone
"""

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# socket.SOCK_STREAM - creates an endpoint thats ready to connect but not yet 
#                        connected, connection point
# socket.AF_INET - hock a thing to the internet

# 'data.pr4e.org' - host
# 80 - port number