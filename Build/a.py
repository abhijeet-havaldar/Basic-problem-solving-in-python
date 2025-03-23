# Import the HTTPConnection class from the http.client module.
from http.client import HTTPConnection

# Create an HTTPConnection object for the "example.com" host.
conn = HTTPConnection("example.com")

# Send a GET request to the root path ("/") of the host.
conn.request("GET", "/")

# Get the response from the server.
result = conn.getresponse()

# Retrieve the entire contents of the response.
contents = result.read()

# Print the contents of the response.
print(contents)
