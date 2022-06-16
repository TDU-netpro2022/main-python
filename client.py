
import socket

print('start client')

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
# host = socket.gethostname()
host = "localhost"
port = 9999

print("大文字にしたい文字列を入力してください")
message = input()

# connection to hostname on the port.
s.connect((host, port))
s.send(message.encode("ascii"))

# Receive no more than 1024 bytes
msg = s.recv(1024)

s.close()

print(msg.decode('ascii'))
