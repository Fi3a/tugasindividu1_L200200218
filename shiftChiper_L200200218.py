#--------------------------[ FUNGSI PROSES ENKRIPSI SHIFT CHIPER ]-------------------------
def enkripsi(pesan, kunci):
    chiper = '' 
    for char in pesan:
        if char.isupper(): 
            chiper += chr((ord(char) - 65 + kunci) % 26 + 65)     
        elif char.islower():
            chiper += chr((ord(char) - 97 + kunci) % 26 + 97)  
        else:  
            chiper += char   
    return chiper

#-------------------------[ FUNGSI PROSES DEKRIPSI  SHIFT CHIPER ]-------------------------
def dekripsi(chiper, kunci):
    pesan = '' 
    for char in chiper:
        if char.isupper():  
            pesan += chr((ord(char) - 65 - kunci) % 26 + 65) 
        elif char.islower(): 
            pesan += chr((ord(char) - 97 - kunci) % 26 + 97)  
        else:  
            pesan += char 
    return pesan

#---------------[ FUNGSI MENJALANKAN PROSES ENKRIPSI DEKRIPSI SHIFT CHIPER ]---------------
def main():
    print("------------------------------------------------------")
    print("====== [ PROSES ENKRIPSI DEKRIPSI SHIFT CHIPER ] =====")
    print("------------------------------------------------------")
    pesan = input('Isi Pesan      : ')
    print("======================================================")
    kunci = 18 #NIM L200200218 (2 angka terakhir)
    chiper = enkripsi(pesan, kunci)
    
    print('Hasil enkripsi :', chiper)
    print('Hasil dekripsi :', dekripsi(chiper, kunci))
    print("======================================================")

if __name__ == '__main__': 
    main()