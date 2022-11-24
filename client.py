import socket as sc
import os

so = sc.socket()

host = input("log in host number: ")
port = 60000
FORMAT = "utf-8"
SIZE = 102400

so.connect((host, port))

rec = so.recv(SIZE)
ab = rec.decode("utf-8")
print("first input : ", ab)
rec = so.recv(SIZE)
fa = rec.decode("utf-8")

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

