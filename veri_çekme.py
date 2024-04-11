import pandas as pd
import numpy as np

# Veri toplama işlemi için bir web sayfasından veri çekelim
url = 'https://yandex.com'  # Web sayfasının URL'sini buraya girin

# Veriyi çekmek için pandas kütüphanesini kullanalım
try:
    veri = pd.read_html(url)  # Web sayfasındaki tabloları çekelim
    # Eğer birden fazla tablo varsa, istediğiniz tabloyu seçebilirsiniz
    # Örneğin: veri_tablosu = veri[0] (ilk tablo)
    # veya: veri_tablosu = veri[1] (ikinci tablo)
    # ...

    # Veriyi inceleyelim
    print(veri_tablosu.head())  # type: ignore # İlk birkaç satırı gösterelim

except Exception as e:
    print(f"Hata: {e}")
