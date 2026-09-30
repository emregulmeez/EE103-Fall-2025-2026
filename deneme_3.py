def voltaj_hesaplama(i,r):
    v=i*r
    return v
hesaplanan_voltaj=voltaj_hesaplama(3.42,8.64)
print(f"Hesaplanan voltaj değeri:{hesaplanan_voltaj:5.2f}Volt")
if hesaplanan_voltaj<20:
    print(f"Hesaplanan voltaj değeri:{hesaplanan_voltaj:5.2f}Volt\nKullanıcının istediği değerden düşük bir voltaj değeri.")
else:
    print(f"Hesaplanan voltaj değeri:{hesaplanan_voltaj:5.2f}Volt\nKullanıcının istediği değerden yüksek bir voltaj değeri.")
    