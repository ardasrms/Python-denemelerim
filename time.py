import time

# Kullanıcıdan alarm saati al
alarm_saati = input("Alarm saatini gir (HH:MM): ")

print("Alarm ayarlandı:", alarm_saati)

while True:
    # Şimdiki zamanı al
    simdi = time.strftime("%H:%M")
    
    # Saat eşleşirse alarmı çaldır
    if simdi == alarm_saati:
        print("🔔 Alarm Çalıyor! 🔔")
        break
    
    # 1 saniye bekle
    time.sleep(1)
