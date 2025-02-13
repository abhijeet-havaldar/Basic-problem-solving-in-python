#Q:Write a Python program to find local IP addresses using Python's stdlib.

import socket

local_hostname = socket.gethostname()
ip_addresses = socket.gethostbyname_ex(local_hostname)[2]

filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]
first_ip = filtered_ips[ :1]
print(first_ip[0])