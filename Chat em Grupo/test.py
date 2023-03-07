import socket

HOST = 'localhost'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

mensagem = client.recv(1024)
print(mensagem)

if mensagem == b'SALA':
    client.send(b'Games')
    client.send(b'Marcelo')
