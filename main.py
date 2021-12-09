from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Müzik Galerisi")
pencere.geometry("800x600")
# pencere.wm_iconbitmap("ico/sarki.ico")

baslik = Label(pencere, text="2021 Yılında Başa Sarıp Dinlediklerin!")
baslik.grid(row=0, column=0, padx=12, pady=12)
baslik.config(font=("Arial", 33))

sayfalar = ["img/sarki_01.jpg", "img/sarki_02.jpg", "img/sarki_03.jpg", "img/sarki_04.jpg", "img/sarki_05.jpg","img/sarki_06.jpg","img/sarki_07.jpg"]

sayfa = 1


def goster():
   gorsel = ImageTk.PhotoImage(Image.open(sayfalar[sayfa]))
   cerceve = Label(image=gorsel)
   cerceve.image = gorsel
   cerceve.grid(row=2, column=0, padx=12, pady=12)
   goster()

def sonraki():
   global sayfa
   if sayfa < len(sayfalar) - 1:
       sayfa += 1
   else:
       sayfa = 0
   print(sayfa)
   sonraki()


buton = Button(text="Diğer Şarkın", command=sonraki)
buton.grid(row=2, column=0, padx=12, pady=12)
buton.config(font=("Arial", 24))

pencere.mainloop()

