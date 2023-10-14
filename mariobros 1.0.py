from turtle import *
import turtle
from tkinter import *
from tkinter import messagebox

"""value awal dari masing-masing variabel input"""
bangunan=0
jarak_tower=0
perbedaan_lapisan=0
panjang=0
lebar=0
layer_pertama=0
layer_utama=0

"""meminta input untuk membuat tower"""
while True: #menggunakan while loop agar sistem terus meminta input hingga input bernilai true
    bangunan = turtle.numinput("Tower To Build", "Enter the amount of tower \
you want to build (integer)", minval=1)
    if bangunan.is_integer() == False: #menggunakan .is_integer untuk mengetahui jika input yang diberikan valid(integer)
        messagebox.showinfo("Input Error", "Your input is not integer")
        continue
    else:
        if bangunan > 1: #jika input > 1 maka diminta input jarak tower dan perbedaan lapisan antar tower
            while True:
                jarak_tower = turtle.numinput("Distance between Towers", "Enter the distance \
between tower (integer)", minval=2, maxval=5)
                if jarak_tower.is_integer() == False: #menggunakan .is_integer untuk mengetahui jika input yang diberikan valid(integer)
                    messagebox.showinfo("Input Error",  "Your input is not integer")
                    continue
                else:
                    break
            while True:
                perbedaan_lapisan = turtle.numinput("Towers Layer Difference", "Enter the number \
of layer differences between each tower (integer)", minval=2, maxval=5)
                if perbedaan_lapisan.is_integer() == False: #menggunakan .is_integer untuk mengetahui jika input yang diberikan valid(integer)
                    messagebox.showinfo("Input Error",  "Your input is not integer")
                    continue
                else:
                    break
            break
        else:
            break
while True:
    panjang = turtle.numinput("Brick Lenght", "Enter the lenght of the \
brick (integer)", minval=1, maxval=35)
    if panjang.is_integer() == False: #menggunakan .is_integer untuk mengetahui jika input yang diberikan valid(integer)
        messagebox.showinfo("Input Error", "Your input is not integer")
        continue
    else:
        break
while True:
    lebar = turtle.numinput("Brick Widht", "Enter the widht of the \
brick (integer)", minval=1, maxval=25)
    if lebar.is_integer() == False: #menggunakan .is_integer untuk mengetahui jika input yang diberikan valid(integer)
        messagebox.showinfo("Input Error", "Value that you're input is not integer")
        continue
    else:
        break
while True:
    panjang_layer_tower = turtle.numinput("First Tower Layer Amount", "Enter the amount \
of layer for the first tower (integer)", minval=1, maxval=25)
    if panjang_layer_tower.is_integer() == False: #menggunakan .is_integer untuk mengetahui jika input yang diberikan valid(integer)
        messagebox.showinfo("Input Error", "Value that you're input is not integer")
        continue
    else:
        break
while True:
    lebar_layer_tower = turtle.numinput("Layer Lenght", "Enter the lenght \
of the layer (integer)", minval=1, maxval=10)
    if lebar_layer_tower.is_integer() == False: #menggunakan .is_integer untuk mengetahui jika input yang diberikan valid(integer)
        messagebox.showinfo("Input Error", "Value that you're input is not integer")
        continue
    else:
        break

panjang_tower = (bangunan*panjang*panjang_layer_tower) + (jarak_tower*panjang*(bangunan-1)) #menghitung total panjang semua tower
lebar_tower = (lebar_layer_tower*bangunan+(perbedaan_lapisan*(bangunan-1))) #menghitung total lebar semua tower

turtle.screensize(canvwidth=panjang_tower+100,canvheight=lebar_tower+100)

jumlah_balok=0 #value awal untuk jumlah balok
setpos(0,0)
turtle.speed(10000)
turtle.hideturtle()

"""main program"""
while True :
    for y in range(int(bangunan)): #loop untuk banyaknya bangunan yang akan dibuat
        x_coordinate = -(panjang_tower/2) + (panjang*(panjang_layer_tower+jarak_tower))*y         
        """untuk koordinat awal masing-masing tower, setiap mengiterasi loop, koordinat x akan berubah 
        dengan ditamba panjang tower dan jarak antar towernya"""
        y_coordinate = -250
        penup()
        goto(x_coordinate, y_coordinate) 
        pendown()        
        for a in range(0, int(lebar_layer_tower+perbedaan_lapisan*y)): 
            """loop untuk membuat layer tower keatas, apabila y > 0 maka 
            layer tower akan bertambah sesuai input perbedaan lapisan"""
            for b in range(int(panjang_layer_tower)): #
                for c in range(2): #loop untuk membuat sebuah balok
                    fillcolor("#ca7f65")
                    begin_fill()
                    forward(panjang)
                    left(90)
                    forward(lebar)
                    left(90)
                    end_fill()
                jumlah_balok += 1 #setiap menyelesaikan satu iterasi jumlah balok akan bertambah
                penup()
                forward(panjang) #pen akan berpindah ke titik baru untuk membuat balok baru sejauh panjang dari 1 balok
                pendown()
            penup()
            y_coordinate = -250 + lebar+(lebar*a) #untuk menghitung koordinat y ketika layer sebelumnya selesai
            goto(x_coordinate, y_coordinate) #berpindah posisi ke titik awal layer berikutnya
            pendown()
        x_coordinate = x_coordinate - (panjang/2) 
        """untuk menghitung posisi koordinat x dari atap yang jumlah 
        baloknya lebih banyak 1 daripada balok pada badan tower"""
        y_coordinate = -250 + (lebar*(lebar_layer_tower+perbedaan_lapisan*y))
        """untuk menghitung posisi koordinat y dari atap"""
        penup()
        goto(x_coordinate, y_coordinate)
        pendown()
        for d in range(int(panjang_layer_tower+1)): 
            """loop untuk membuat atap, jumlah balok pada atap ditambah 1 
            dari jumlah balok pada badan towe"""
            for f in range(2): #loop untuk membuat sebuah balok
                fillcolor("#693424")
                begin_fill()
                forward(panjang)
                left(90)
                forward(lebar)
                left(90)
                end_fill()
            jumlah_balok += 1 #setiap menyelesaikan satu iterasi jumlah balok akan bertambah
            penup()
            forward(panjang) #pen akan berpindah ke titik baru untuk membuat balok sejauh panjang dari 1 balok
            pendown()
        continue
    penup()
    goto(0, -300) #memindahkan posisi pen untuk menulis pesan
    pendown()
    pesan = f"{int(bangunan)} Super Mario have been built with a total of {jumlah_balok} bricks"
    turtle.write(pesan, move=False, align='center', font=('Futura', 15, 'normal')) #mencetak pesan berisi jumlah bangunan dan banyaknya balok    
    exitonclick()
    break
