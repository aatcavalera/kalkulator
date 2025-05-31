while True:
    teks = input("Kamu: ")
    if "halo" in teks.lower():
        print("Bot: Hai juga!")
    elif "bye" in teks.lower():
        print("Bot: Sampai jumpa!")
        break
    else:
        print("Bot: Aku tidak mengerti.")
