import random # Random fonksiyonunu ekler

# Gereksinimler:
# 1. Kullanıcının parolasının içerebileceği tüm karakterleri içeren bir değişken oluşturun

#      Örneğin: "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# 2. Bir değişken oluşturun ve kullanıcıdan parolanın uzunluğunu girmesini isteyin

# 3.  Programın oluşturulan parolayı saklayacağı bir değişken oluşturun

# 4. Karakter değişkeninden rastgele bir karakter seçmek ve bunu oluşturulan parolanın bulunduğu değişkene eklemek için bir döngü ve random kütüphanesi kullanın

# 5. Parolayı konsola yazdırın


Parolalar = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" # Harf ile sembol değişkeni
Uzunluk = int(input("Lütfen parolanın uzunluğunu giriniz: ")) # Kullanıcıdan parolanın uzunluğunu alıyor
Parola = "" # Kullanıcının parolasının olduğu değişken

for i in range(Uzunluk):    # Parolayı oluşturmak için döngü
    Parola += random.choice(Parolalar)   # Parolayı oluşturuyor

print(Parola) # Parolayı konsola yazıyor





# Bu kadar kolay yaptım.
