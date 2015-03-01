import os
import sys
import time
from socket import socket
from ServerSocket import ServerSocket

try:
    sock = ServerSocket()
    sock.readUDP()
finally:
    print('done')
