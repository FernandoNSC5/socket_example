import socket

print("Starting var")
ip = '192.168.56.1'
port = 3000
blen = 128

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Criado socket, criando conexao")
soc.connect((ip, port))
print("Connected")

while True:

	s = input("O que enviar? ->")
	print("Sending")
	soc.send(s.encode())
	print("Aguardando resposta")
	r = soc.recv(blen).decode()
	print("Resposta: " + str(r))

	sel = int(input("Responder? 1-s 0-n "))

	if not sel:
		break