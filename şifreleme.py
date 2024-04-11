import random
import string

def generate_password(length=12):
    # Küçük harf, büyük harf, rakam ve özel karakterleri birleştir
    characters = string.ascii_letters + string.digits + string.punctuation
    # Rastgele bir şifre oluştur
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Varsayılan uzunlukta (12 karakter) bir şifre oluştur
default_password = generate_password()
print(f"Varsayılan şifre: {default_password}")

# Özel uzunlukta (örneğin 16 karakter) bir şifre oluştur
ozel_uzunluk_sifre = generate_password(length=16)
print(f"Özel uzunlukta şifre: {ozel_uzunluk_sifre}")
