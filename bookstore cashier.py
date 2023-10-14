"""Fungsi yang mencetak menu yang tersedia"""
def print_menu():
    print("Selamat Datang di Toko Buku Place Anak Chill")
    print("="*44)
    print("1. Pinjam buku \n2. Keluar")
    print("="*44)

"""Fungsi untuk mengecek saldo mencukupi"""
def cek_saldo(saldo, biaya):
    if saldo >= biaya:
        print("Berhasil meminjam buku", pilihan_buku, "selama", waktu, "hari")    
        saldo -= biaya
        print("Saldo anda saat ini Rp"+str(float(saldo)))
    else:
        kurang_saldo = biaya - saldo
        print("tidak berhasil meminjam! Saldo anda kurang", kurang_saldo)


#main program
running = True
while running:
    print_menu()
    choice = int(input("Apa yang ingin anda lakukan: "))
    if choice == 1:
        nama_pelanggan = input("Masukkan nama anda: ")
        saldo = int(input("Masukkan saldo anda (Rp): "))
        membership = input("Apakah anda member? [Y/N]: ").casefold()
        """mengecek input membership yang diberikan"""
        if membership == "y":
            counter = 0
            while counter < 3: #mengulang input sampai 3 kali apabila id tidak valid
                id_pelanggan = input("Masukkan ID anda: ")
                sum_digit = sum(int(digit) for digit in str(id_pelanggan)) #Menjumlahkan digit dari id yang diberikan
                if sum_digit == 23 and len(id_pelanggan) == 5: #memeriksa jumlah digit dari id pelanggan
                    print("Login member berhasil!")
                    break
                else:
                    counter += 1 #apabila id salah, counter akan terus bertambah
            else:
                print("Program akan kembali ke menu utama\n")
                continue
        else:
            print("Login non-member berhasil!")
    
        while True:
            #mencetak katalog
            print("\n"+"="*44)
            print("X-Man (Rp 7.000/hari)\nDoraemoh (Rp 5.500/hari)\nNartoh (Rp 4.000/hari)")
            print("="*44)
            print("Exit")
            print("="*44)

            pilihan_buku = input("Buku yang dipilih: ").casefold()
            """"Memeriksa input yang diberikan di pilihan buku"""
            if pilihan_buku == "x-man":
                waktu = int(input("Ingin melakukan peminjaman untuk berapa hari: ")) 
                if membership == "y": #apabila pelanggan memiliki membership mendapat diskon
                    biaya = waktu*7000*0.8
                else:
                    biaya = waktu*7000
                cek_saldo(saldo, biaya)
            elif pilihan_buku == "doraemoh":
                waktu = int(input("Ingin melakukan peminjaman untuk berapa hari: "))
                if membership == "y": #apabila pelanggan memiliki membership mendapat diskon
                    biaya = waktu*5500*0.
                else:
                    biaya = waktu*5500
                biaya = waktu*5500
                cek_saldo(saldo, biaya)
            elif pilihan_buku == "nartoh":
                waktu = int(input("Ingin melakukan peminjaman untuk berapa hari: "))
                if membership == "y": #apabila pelanggan memiliki membership mendapat diskon
                    biaya = waktu*4000*0.8
                else:
                    biaya = waktu*4000
                cek_saldo(saldo, biaya)
            elif pilihan_buku == "exit":
                break
            else:
                print("Komik tidak ditemukan. Masukkan kembali judul komik sesuai katalog!")
                continue
            
            saldo -= biaya

    if choice == 2:
        print("Terima kasih telah mengunjungi Toko Buku Place Anak Chill!")
        exit()    
               
