import socket

server = "timeeeee.no-ip.org"
port = 53421

print "connect to server"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server, port))
print "send some text"
bytes_sent = sock.send("some text")
print "send some other text"
bytes_sent = sock.send("some other text")
print "get response"
response = sock.recv(1024)
print "response: {}".format(response)
sock.close()
