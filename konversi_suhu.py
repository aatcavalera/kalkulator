def konversi(c):
    return (c * 9/5) + 32

celsius = float(input("Masukkan suhu (°C): "))
print(f"{celsius}°C = {konversi(celsius):.2f}°F")
