import time

detik = int(input("Hitung mundur berapa detik? "))
while detik > 0:
    print(detik)
    time.sleep(1)
    detik -= 1
print("Waktu Habis!")
