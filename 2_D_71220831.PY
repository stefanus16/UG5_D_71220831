def hitung_mobil():
    jumlah_mobil = {k: 0 for k in ['Solo', 'Surabaya', 'Jogja', 'Magelang']}
    
    while True:
        asal = input("Masukkan asal mobil (ketik 'done' untuk keluar): ").capitalize()
        
        if asal in jumlah_mobil:
            jumlah_mobil[asal] += 1
        if asal == 'Done':
            break
    
    for kota, jumlah in jumlah_mobil.items():
        print("Jumlah mobil dari {}: {}".format(kota, jumlah))

hitung_mobil()