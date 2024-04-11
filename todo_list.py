# Yapılacaklar listesi için bir liste tanımlayalım
yapilacaklar_listesi = []

# Bir öğeyi yapılacaklar listesine eklemek için bir fonksiyon tanımlayalım
def ogelere_ekle(oge):
    yapilacaklar_listesi.append(oge)
    print(f"'{oge}' öğesi yapılacaklar listesine eklendi.")

# Mevcut yapılacaklar listesini görüntülemek için bir fonksiyon tanımlayalım
def listeyi_goster():
    print("\nMevcut Yapılacaklar Listesi:")
    for i, oge in enumerate(yapilacaklar_listesi, start=1):
        print(f"{i}. {oge}")

# Örnek kullanım
ogelere_ekle("Market alışverişi yap")
ogelere_ekle("Ödevi bitir")
ogelere_ekle("Annemi ara")
ogelere_ekle("ev isi yapma")  #
listeyi_goster()
