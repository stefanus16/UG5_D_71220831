asal_mobil=input("masukan asal mobil: ")
def hitung_mobil():

    # inisialisasi variabel awal
    jumlahSol = 0
    jumlahSur = 0
    jumlahJog = 0
    jumlahMag = 0
    
    while True:
        asalMobil = input("Masukkan asal mobil (Solo, Surabaya, Jogja, Magelang) atau ketik 'done' untuk keluar: ")
        if asalMobil.lower() == "done":
            break
        elif asalMobil.lower() == "solo":
            jumlahSol += 1
        elif asalMobil.lower() == "surabaya":
            jumlahSur += 1
        elif asalMobil.lower() == "jogja":
            jumlahJog += 1
        elif asalMobil.lower() == "magelang":
            jumlahMag += 1
        else:
            print("Asal mobil tidak valid.")
    
    # output jumlah mobil dari masing-masing kota
    print("Jumlah mobil dari Solo: ", jumlahSol)
    print("Jumlah mobil dari Surabaya: ", jumlahSur)
    print("Jumlah mobil dari Jogja: ", jumlahJog)
    print("Jumlah mobil dari Magelang: ", jumlahMag)
