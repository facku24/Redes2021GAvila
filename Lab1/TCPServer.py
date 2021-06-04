from socket import *


serverName = '127.0.0.1'
serverPort = 12000

def create_socket(addr,port):
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.bind((serverName,serverPort))
	serverSocket.listen(1)
	return serverSocket
def recibir_msj(connectionSocket):
	sentence = connectionSocket.recv(1024)#recibir mensaje
	return sentence

def modificar_msj(msj):
	capitalizedSentence = msj.decode().upper()#modificar mensaje
	return capitalizedSentence

def enviar_msj(connectionSocket,msj):
	connectionSocket.send(msj.encode())#enviar mensaje
def cerrar_socket(connectionSocket):
	connectionSocket.close() #cerra coneccion
def main ():
	serverSocket= create_socket(serverName,serverPort)
	print('el  servidor esta escuchando en el puerto: ' + str(serverPort))
	while 1:
		connectionSocket, addr = serverSocket.accept()
		mensaje=recibir_msj(connectionSocket)
		mensaje=modificar_msj(mensaje)
		enviar_msj(connectionSocket,mensaje)
		cerrar_socket(connectionSocket)
	

if __name__ == '__main__':
	main()