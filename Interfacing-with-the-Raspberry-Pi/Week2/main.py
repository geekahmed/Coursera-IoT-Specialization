import socket
import sys

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    host = socket.gethostname()
    port = 12345
    mySocket.bind((host, port))
except socket.error:
    print("Failed to bind")
    sys.exit()
mySocket.listen(5)
while True:
    conn, addr = mySocket.accept()
    data = conn.recv(1000)
    if not data:
        break
    print("Got a request!")

conn.close()
mySocket.close()
