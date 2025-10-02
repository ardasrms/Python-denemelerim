import random

# 1 ile 10 arasında rastgele sayı tut
sayi = random.randint(1, 10)

tahmin = int(input("1 ile 10 arasında bir sayı tahmin et: "))

if tahmin == sayi:
    print("Tebrikler, doğru bildin! 🎉")
else:
    print(f"Üzgünüm, doğru sayı {sayi} idi.")
