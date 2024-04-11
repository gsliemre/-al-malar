import tkinter as tk
from tkinter import messagebox

def hesapla():
    try:
        uzunluk = float(uzunluk_entry.get())
        genislik = float(genislik_entry.get())
        alan = uzunluk * genislik
        sonuc_label.config(text=f"Alan: {alan:.3f} birim kare")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayısal değerler girin.")

# Ana pencere oluşturma
pencere = tk.Tk()
pencere.title("Alan Hesaplama Makinesi")
pencere.geometry("300x150")

# Giriş alanları ve etiketleri
uzunluk_label = tk.Label(pencere, text="Uzunluk:")
uzunluk_label.pack()
uzunluk_entry = tk.Entry(pencere)
uzunluk_entry.pack()

genislik_label = tk.Label(pencere, text="Genişlik:")
genislik_label.pack()
genislik_entry = tk.Entry(pencere)
genislik_entry.pack()

# Hesapla butonu
hesapla_button = tk.Button(pencere, text="Hesapla", command=hesapla)
hesapla_button.pack()

# Sonuç etiketi
sonuc_label = tk.Label(pencere, text="")
sonuc_label.pack()

pencere.mainloop()
