from socket import *

serverName = '127.0.0.1'
serverPort = 12000

# AF_INET establece como protocolo de red a IP
# SOCK_STREAM establece como protocolo de transporte a TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((serverName,serverPort))

serverSocket.listen(1)

print('The server is ready to receive')

while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.decode().upper()
	connectionSocket.send(capitalizedSentence.encode())
	connectionSocket.close()