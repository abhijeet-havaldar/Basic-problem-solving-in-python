#Q:Write a Python program to validate an IP address.

import socket

addr = '122.0.0.25.61'

try:
    socket.inet_aton(addr)

    print("valid IP")

except socket.error:
    print("Invalid IP")