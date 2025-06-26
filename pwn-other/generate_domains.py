# generate_domains.py

with open("domains.txt", "w") as f:
    for i in range(256):  # 0x00 to 0xFF
        subdomain = f"0x{i:02x}.a.hackycorp.com"
        f.write(subdomain + "\n")

print("domains.txt created with 256 subdomains!")
