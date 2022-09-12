import socket as sc
import os

hostname = sc.gethostname()
host = sc.gethostbyname(hostname)
port = 60000
FORMAT = "utf-8"
SIZE = 102400
print("Client should connect ip: ", host)

so = sc.socket()
so.bind((host, port))

so.listen(4)

print("oldu bu")

while True:
    a, rece = so.accept()
    fn = input("write file name for send: ")
    a.send(fn.encode(FORMAT))

    with open(fn, "rb") as al:
        la = os.path.getsize(fn)
        m = al.read(la)
    a.sendall(m)

    print("Done sending...")


    a.close()


