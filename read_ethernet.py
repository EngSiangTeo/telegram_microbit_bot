import socket

UDP_IP = "0.0.0.0" # listen to everything
UDP_PORT = 12345 # port

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
  data, addr = sock.recvfrom(512) # random buffer size, doesn't matter here..
  data = data.decode('utf-8')
  print("received message:", data)
  #simplest way to react.. of course, a better parser should be used, and add GPIO code, etc..
  if data==b'LED=1\n':
    print("LED ON")
  elif data==b'LED=0\n':
    print("LED OFF")
