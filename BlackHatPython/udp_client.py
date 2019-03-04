import socket

target_host = "127.0.0.1"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
message = "AAABBBCCC".encode()
client.sendto(message, (target_host, target_port))

# recieve some data
data = client.recvfrom(4096)

# print data and close
print(data)

client.close()