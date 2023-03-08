kalimat = input("Masukkan kalimat: ")
cari = input("Masukkan kata yang ingin diganti: ")
ganti = input("Masukkan kata pengganti: ")

def ganti_kata(kalimat, cari, ganti):
    baru = ''
    kata = ''
    for i in range(len(kalimat)):
        if kalimat[i] == ' ':
            if kata == cari:
                baru += ganti
            else:
                baru += kata
            baru += ' '
            kata = ''
        else:
            kata += kalimat[i]
    if kata == cari:
        baru += ganti
    else:
        baru += kata
    return baru


baru = ganti_kata(kalimat, cari, ganti)
print("Kalimat baru: ",baru)