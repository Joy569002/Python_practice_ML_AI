import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.connect((host, port))

while True:
    message = input("Enter your message: ")
    s.send(message.encode())
    if message.lower() == "exit":
        break
    response = s.recv(1024).decode()
    print("Server:", response)

s.close()