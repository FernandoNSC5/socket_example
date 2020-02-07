import socket

print("Setting var")
port = 3000
buffer_ = 128
host = ''
times = 100
listened = 0

try:
	print("Creating connection status")
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soc.bind((host, port))
	soc.listen(times)

	while True:
		listened += 1
		print("Trying to accept conn")
		conn, addr = soc.accept()
		print("Request from " + str(addr))

		while True:
			rc = conn.recv(buffer_).decode()
			print("This is the message: " + str(rc))

			sel = int(input("Responder? 1-s 0-n "))

			if sel:
				resp = input("O que responder?")
				conn.send(resp.encode())
			else:
				conn.send(''.encode())

except Exception as e:
	print("Falha")
	print(str(e))