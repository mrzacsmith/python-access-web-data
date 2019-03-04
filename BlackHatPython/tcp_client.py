import socket

target_host = 'www.google.com'
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

# Must encode
cmd = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode()
client.send(cmd)

response = client.recv(4096)

print(response)

# Close connection
client.close()