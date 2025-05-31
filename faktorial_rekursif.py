def faktorial(n):
    return 1 if n == 0 else n * faktorial(n-1)

angka = int(input("Masukkan angka: "))
print(f"{angka}! = {faktorial(angka)}")
