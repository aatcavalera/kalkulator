import qrcode

data = input("Masukkan teks/link: ")
img = qrcode.make(data)
img.save("qrcode.png")
print("QR Code disimpan.")
