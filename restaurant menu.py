welcome = """Selamat datang! Masukkan dua nama file yang berisi daftar
makanan yang kamu miliki"""
program = True
while program :
    print(welcome)
    try :
        """meminta input nama file"""
        input_file_input = input("Masukkan nama file input daftar makanan: ")
        input_file_output = input("Masukkan nama file output: ")
        file_input = open(input_file_input, 'r') #method membuka file input
        file_output = open(input_file_output, 'a') #method membuka file output
        program = False
    except :
        print("Maaf, file input tidak ada")
menu = """
Apa yang ingin kamu lakukan?
================================================
1. Tampilkan daftar makanan pertama
2. Tampilkan daftar makanan kedua
3. Tampilkan gabungan makanan dari dua daftar
4. Tampilkan makanan yang sama dari dua daftar
5. Keluar
================================================"""
"""menu subprogram"""
subprogram = True
while subprogram :
    print(menu)
    aksi = int(input("Masukkan aksi yang ingin dilakukan: "))
    daftar1 = file_input.readline()
    daftar2 = file_input.readline()
    print(daftar2)
    if aksi == 1 :
        daftar1 = daftar1[18:].lower()
        pesan_daftar1 = f"\nDaftar makanan pertama:\n{daftar1}"
        file_output.write(f"{pesan_daftar1}\n")
        print(pesan_daftar1)    
    elif aksi == 2: 
        print(daftar2)
        daftar2 = daftar2[18:].lower()
        pesan_daftar2 = f"\nDaftar makanan kedua:\n{daftar2}"
        file_output.write(f"{pesan_daftar2}\n")
        print(pesan_daftar2)   
    elif aksi == 3 :
        daftar1 = daftar1[18:].lower()
        daftar2 = daftar2[18:].lower()
        daftar3 = daftar1.replace("\n"," ",1) +","+ daftar2.replace("/n"," ",1) + ","
        print(daftar3)
        index_awal = 0
        daftar_gabungan = ""
        for char in daftar3 :
                i = daftar3.find(',',index_awal)
                nama_makanan = daftar3[index_awal:i]
                if nama_makanan not in daftar_gabungan:
                    daftar_gabungan += "," + nama_makanan
                index_awal = i + 1
        daftar_gabungan = daftar_gabungan.replace(","," ",1)
        pesan_daftar_gabungan = f"\nGabungan makanan favorit dari kedua daftar:\n{daftar_gabungan}"
        file_output.write(pesan_daftar_gabungan)
        print(pesan_daftar_gabungan)
    elif aksi == 4 :
        daftar1 = file_input.readline()
        daftar2 = file_input.readline()
        daftar1 = daftar1[18:-1].lower()
        daftar2 = daftar2[18:].lower()
        #daftar3 = daftar1 +","+ daftar2 + ","
        index_awal = 0
        daftar_makanan_sama = ""
        for char in daftar1 :
                i = daftar1.find(',',index_awal)
                nama_makanan = daftar1[index_awal:i]
                if nama_makanan in daftar2 :
                    if nama_makanan not in daftar_makanan_sama :
                        daftar_makanan_sama += nama_makanan + ","
                index_awal = i + 1
        daftar_irisan = f"\nMakanan yang sama dari kedua daftar:\n{daftar_makanan_sama.replace(',','',1)}"
        file_output.write(daftar_irisan)
        print(daftar_irisan)            
    else :
        print(f'Terima kasih telah menggunakan program ini! \
            /nSemua keluaran telah disimpan pada file {input_file_output}')
        subprogram = False