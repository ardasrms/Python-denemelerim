# Basit Hesap Makinesi

# Kullanıcıdan sayı alıyoruz
sayi1 = float(input("Birinci sayıyı gir: "))
sayi2 = float(input("İkinci sayıyı gir: "))

print("\nİşlem Seç:")
print("1 - Toplama")
print("2 - Çıkarma")
print("3 - Çarpma")
print("4 - Bölme")

secim = input("Seçimin: ")

if secim == "1":
    print("Sonuç:", sayi1 + sayi2)
elif secim == "2":
    print("Sonuç:", sayi1 - sayi2)
elif secim == "3":
    print("Sonuç:", sayi1 * sayi2)
elif secim == "4":
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Hata! Sıfıra bölünemez.")
else:
    print("Geçersiz seçim!")
