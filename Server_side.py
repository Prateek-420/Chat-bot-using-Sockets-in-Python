import socket
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4444
new_socket.bind(("0.0.0.0", port))
print("Binding successful" )
name = input('Enter name: ')
new_socket.listen(1)
conn, add = new_socket.accept()
print("Received connection from ", add[0])
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
conn.send(name.encode())
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
    if message == "quit":
        print("Ending Connection now")
        conn.send("Ending the connection now".encode())  # sending message to the client.
        break

new_socket.close()
