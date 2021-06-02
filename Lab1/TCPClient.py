from socket import *
def create_socket(addr,port):
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((addr,port))
	return clientSocket


def enviar_msj(clientSocket,msj):
	clientSocket.send(msj.encode())

def recibir_msj(clientSocket):
	modifiedSentence = clientSocket.recv(1024)
	return modifiedSentence

def cerrar_socket(clientSocket):
	clientSocket.close()

def main():
	serverName = '127.0.0.1'
	serverPort = 12000
	clientSocket=create_socket(serverName,serverPort)
	sentence = input('ingrese un mensaje: ')
	enviar_msj(clientSocket,sentence)
	mensaje=recibir_msj(clientSocket)
	print('devolucion del Server: ' + mensaje.decode())
	cerrar_socket(clientSocket)

if __name__ == "__main__":
	main()