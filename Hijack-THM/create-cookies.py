import hashlib
import base64

# Open the file and read its lines
with open('passwords.txt', 'r') as f:
    lines = f.readlines()

# Loop through the lines and modify each one
for line in lines:
    # Strip the line of leading/trailing whitespace
    stripped_line = line.strip()
    
    # Hash the stripped line using MD5
    hashed_line = hashlib.md5(stripped_line.encode('utf-8')).hexdigest()
    
    # Add "admin:" to the beginning of the hash
    modified_hash = 'admin:' + hashed_line
    
    # Encode the modified hash to base64
    encoded_hash = base64.b64encode(modified_hash.encode('utf-8'))
    
    # Print the encoded hash
    print(encoded_hash.decode('utf-8'))
