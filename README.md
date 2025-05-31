## Hari 1: Kalkulator Sederhana

**Deskripsi:**  
Kalkulator terminal yang menjumlahkan, mengurangi, mengalikan, dan membagi dua angka.

```python
def kalkulator():
    print("Kalkulator Sederhana")
    while True:
        a = float(input("Angka pertama: "))
        b = float(input("Angka kedua: "))
        op = input("Operasi (+ - * /): ")

        if op == '+':
            print(f"Hasil: {a + b}")
        elif op == '-':
            print(f"Hasil: {a - b}")
        elif op == '*':
            print(f"Hasil: {a * b}")
        elif op == '/':
            print(f"Hasil: {a / b if b != 0 else 'Error: Tidak bisa bagi 0'}")
        else:
            print("Operasi tidak valid.")

        if input("Hitung lagi? (y/n): ") != 'y':
            break

kalkulator()
```
