####################################
# Nergiz Ablamın Kontrol Paneli    #
# /bin/python                      #
####################################

import os
from time import sleep, time

os.system('cls')

while True:

    yol = "C:\\Benim Web Sitem" # İnstagram Yol.

    islem = input("""
        Nergiz ablamın kontrol paneline hoş geldiniz.

        ~ İşlem seçmek için 2 tür sayı girmeniz gerekiyor.

        1-) Giriş Yap
        2-) Çıkış Yap
    
    """)

    if(islem == '1'): # İşlem NO
        peğswöğd = str(input('Giriş İçin Şifre Gir: ')) # Soru
        e = "peğswöğd doğrulandı, giriş yapıyorum bekle 1 saniye" # Output Yazı
        if peğswöğd == "tosbik": # Şifre
            print(e) # Output

            os.chdir(yol) # Belirtilen Yolun Dosyasına Giriş
            print('İnstagramı Açıyorum Bekle Kardeşim.') # Output
            sleep(3) # Bekle
            os.system("start index.html") # İnstagram

        else:
            sleep(2) # Bekle
            print('peğswöğd yanlış.') # Yanlış Şifre
            os.system('cls') # Temizle
            sleep(2) # Bekle
    elif(islem == '2'): # İşlem NO
        print('Çıkış Yapıldı.') # Output
        sleep(2) # Bekle
        exit() # Çıkış