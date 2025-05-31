import re

email = input("Masukkan email: ")
pola = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pola, email):
    print("Email valid.")
else:
    print("Email tidak valid.")
