import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sport = 4444

server_host = "<server_ip"
name = input('Enter your name: ')
socket_server.connect((server_host, sport))
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()
print(server_name, ' has joined...')
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    socket_server.send(message.encode())
    if message == 'quit':
   
        break
socket_server.close()
