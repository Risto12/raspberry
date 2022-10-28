import socket
import subprocess

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
serversocket.bind(('localhost', 8089)) # Fix
serversocket.listen(1)
connection, address = serversocket.accept()

output = subprocess.run(["shutdown"], capture_output=True)

print(output)

if output.returncode == 0:
    response = """HTTP/1.1 200 OK
    Content-Type: text/html

    <html><body>200</body></html>
    """
else:
    response = """HTTP/1.1 200 OK
    Content-Type: text/html

    <html><body>418</body></html>
    """

connection.send(response.encode())
connection.close()
