angka = int(input("Masukkan angka (0–9): "))
kata = ["nol", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]

print(kata[angka] if 0 <= angka <= 9 else "Di luar jangkauan.")
