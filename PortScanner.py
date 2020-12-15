import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.settimeout(5)

host = input("Please enter the IP you wnat to scan: ")
port = int(input("Please enter the you wnat to scan: "))

def portScanner(port):
    if soc.connect_ex((host, port)):
        print('the port is closed')
    else:
        print('port is open')

portScanner(port)
