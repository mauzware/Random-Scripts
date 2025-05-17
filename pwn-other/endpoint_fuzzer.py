import socket

def fuzz_endpoints(ip, port, endpoints):
    for endpoint in endpoints:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, port))

            print(f"Testing: {endpoint}")
            client_socket.sendall(endpoint.encode() + b'\n')

            response = client_socket.recv(1024)
            print(f"Response from {endpoint}: {response.decode()}\n")

            client_socket.close()
        except Exception as e:
            print(f"Error with {endpoint}: {e}")

# List of potential endpoints to fuzz
endpoint_list = ["some_endpoint", "shell", "admin", "backup", "reset", "login", "help", "root", "register", "old"]

# Target IP and port (replace with actual values)
target_ip = "10.10.23.85"
target_port = 8000

# Fuzz the endpoints
fuzz_endpoints(target_ip, target_port, endpoint_list)
