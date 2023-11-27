import tkinter as tk
from tkinter import *

class balok_ilhamFix:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
    
        nama = Label(mainFrame, text="MUHAMMAD ILHAM RAMDHANI")
        nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        #Label input
        panjang = Label(mainFrame, text="Panjang:")
        panjang.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        lebar = Label(mainFrame, text="Lebar:")
        lebar.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        tinggi = Label(mainFrame, text="Tinggi:")
        tinggi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        # Textbox input
        self.txtpanjang = Entry(mainFrame)
        self.txtpanjang.grid(row=1, column=1)
        self.txtlebar = Entry(mainFrame)
        self.txtlebar.grid(row=2, column=1)
        self.txttinggi = Entry(mainFrame)
        self.txttinggi.grid(row=3, column=1)

        #Button
        self.hitung_button = Button(mainFrame, text="Hitung", command=self.onHitung)
        self.hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        #Output label Luas
        self.luas = Label(mainFrame, text="Luas :")
        self.luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        #Output label Volume
        self.volume = Label(mainFrame, text="volume :")
        self.volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        #Output Textbox Luas
        self.txtLuas= Entry(mainFrame)
        self.txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        #output Textbox Volume
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self):
        panjang = float(self.txtpanjang.get())
        lebar = float(self.txtlebar.get())
        tinggi = float(self.txttinggi.get())
        L = round(((2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)),2)
        V = round((panjang*lebar*tinggi),2)
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,V)
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,L)

    def onKeluar(self):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = balok_ilhamFix(root, "Program Bola")
    root.mainloop() 