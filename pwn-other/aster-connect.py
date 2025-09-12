import socket
import sys
import time

#Asterisk Call Manager connection script
HOST = "[TARGET IP]"
PORT = 5038
USER = "[USERNAME]"
SECRET = "[PASSWORD]"

def send(sock, text):
    # ensure CRLF endings for AMI
    if not text.endswith("\r\n"):
        text = text.replace("\n", "\r\n")
        if not text.endswith("\r\n"):
            text += "\r\n"
    sock.sendall(text.encode())

def recv_all(sock, timeout=1.0):
    sock.settimeout(timeout)
    data = b""
    try:
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
            # short pause to aggregate data
            time.sleep(0.01)
    except socket.timeout:
        pass
    return data.decode(errors="ignore")

def main():
    s = socket.socket()
    s.connect((HOST, PORT))

    # read banner
    banner = recv_all(s, timeout=0.5)
    print("BANNER:\n", banner)

    # Login action - note CRLF and blank line at end
    login = (
        "Action: Login\r\n"
        f"Username: {USER}\r\n"
        f"Secret: {SECRET}\r\n"
        "Events: off\r\n"
        "\r\n"
    )
    send(s, login)
    print("Sent LOGIN, awaiting response...")
    print(recv_all(s, timeout=1.0))

    # If login succeeded, you can send a Command action
    # Example: run 'core show version' on asterisk CLI
    cmd = (
        "Action: Command\r\n"
        "Command: core show help\r\n"
        "\r\n"
    )
    send(s, cmd)
    print("Sent COMMAND, awaiting response...")
    print(recv_all(s, timeout=1.0))

    # Keep the socket open and read for a short while (or loop forever)
    try:
        for _ in range(10):
            data = recv_all(s, timeout=2.0)
            if data:
                print("EVENTS/RESPONSE:\n", data)
            else:
                print(".", end="", flush=True)
    except KeyboardInterrupt:
        pass

    # Properly logoff
    send(s, "Action: Logoff\r\n\r\n")
    print("\nSent LOGOFF")
    s.close()

if __name__ == "__main__":
    main()
