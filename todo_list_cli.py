todo = []

while True:
    aksi = input("Tambah (t), Lihat (l), Hapus (h), Keluar (k): ")
    if aksi == 't':
        todo.append(input("Tugas: "))
    elif aksi == 'l':
        for i, t in enumerate(todo): print(f"{i+1}. {t}")
    elif aksi == 'h':
        del todo[int(input("Nomor tugas: ")) - 1]
    elif aksi == 'k':
        break
