#!usr/bin/python3

import socket
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.settimeout(5)

host = input('Please enter the IP you want to scan: ')
port = int(input("Please enter the port you want to scan: "))


def portScanner(port):
    if clientsocket.connect_ex((host,port)):
        print('This port is closed!')
    else:
        print('The port is open')
        
        
portScanner(port)