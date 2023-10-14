#Method untuk mengubah hexadecimal ke string
def ubah_hexadecimal_ke_string(input_pesan_kelompok_zog):
    pesan_kelompok_zog_bytes_string = bytes.fromhex(input_pesan_kelompok_zog)
    pesan_kelompok_zog_ascii_string = pesan_kelompok_zog_bytes_string.decode("ASCII")
    return pesan_kelompok_zog_ascii_string

#Method untuk mengubah interger ke biner
def ubah_interger_ke_biner(input_angka_satu, input_angka_dua):
    password_int = (input_angka_satu*input_angka_dua)*13
    password_biner = bin(password_int)
    return password_biner

"""Fungsi utama untuk menjalankan program"""
input_pesan_kelompok_zog = input("Pesan Kelompok Zog: ") #meminta input dari pesan kelompok zog
input_angka_satu = int(input("Angka 1: ")) #meminta input angka pertama password
input_angka_dua = int(input("Angka 2: ")) #meminta input angka kedua password

"""meminta value dari function"""
pesan_kelompok_zog_string = ubah_hexadecimal_ke_string(input_pesan_kelompok_zog) 
password_kelompok_zog_string = ubah_interger_ke_biner(input_angka_satu, input_angka_dua)

"""mencetak hasil dari terjemahan pesan dan password"""
print(f'Hasil terjemahan pesan: {pesan_kelompok_zog_string}\
      \nPassword: {password_kelompok_zog_string}\
      \n\nPesan "{pesan_kelompok_zog_string}" telah diterima dengan password\
      "{password_kelompok_zog_string}".')