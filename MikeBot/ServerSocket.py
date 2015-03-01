import sys
import os
import socket

class ServerSocket:
        PORT = 8080
        
	def __init__(self, sock=None):
		if sock is None:
                        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		else:
			self.sock = sock

	def readUDP(self, recv_buffer=4096, delim='\n'):
                self.sock.bind(("", self.PORT))
		while 1:
			data = self.sock.recv(recv_buffer)
			print(data)
			
			#while(buffer.find(delim)!= -1):
			#	line, buffer= buffer.split('\n',1)
			#	yield line
		return
