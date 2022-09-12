import socket as sc
import os

so = sc.socket()

host = input("log in host number: ")
port = 60000
FORMAT = "utf-8"
SIZE = 102400

so.connect((host, port))

yanit = so.recv(SIZE)
ab = yanit.decode("utf-8")
print("ilk input : ", ab)
yanit = so.recv(SIZE)
fa = yanit.decode("utf-8")

print("receive filename: ", fa)
try:
    os.remove(fa)
except:
    pass

with open(fa, "wb") as al:
    print("file opened and closed")

data = so.recv(SIZE)

with open(fa, "wb") as ok:

    ok.write(data)

print("Done receiving")

