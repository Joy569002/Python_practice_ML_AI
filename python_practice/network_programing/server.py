import socket

s = socket.socket()
s.bind(('', 8080))
s.listen()
conn, addr = s.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if data.lower() == "exit":
        break
    print("Client:", data)
    message = input("Enter your message: ")
    conn.send(message.encode())

conn.close()