import socket


target_host = "adelio.toco.works"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# connect the client
client.connect((target_host, target_port))


# send some data
client.send(b"GET / HTTP/1.1\r\nHost: adelio.toco.works\r\n\r\n")


# recive some data
response = client.recv(4096)

print(response.decode())
client.close