import socket

import datetime

HOST, PORT = '', 8888

socket.AF_INET

socket.SOCK_STREAM

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listen_socket.bind((HOST, PORT))

listen_socket.listen(1)

print 'Serving HTTP on port %s ...' % PORT

while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	print request

	http_responce = """\
HTTP/1.1 200 OK

Hello, World!

The time is

""" + str(datetime.datetime.now()) + """ so it is """

	client_connection.sendall(http_responce)
	client_connection.close()



	