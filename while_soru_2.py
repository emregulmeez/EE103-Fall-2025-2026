alt_sınır=100.00
üst_sınır=200.00
f=float(input("Bir frekans değeri giriniz:"))
while f<alt_sınır or f>üst_sınır:
    print(f"Girdiğiiz frekans değeri {f:.2f} kHZ güvenli aralık olan 100.0-200.00 kHz aralığında değil.\nTAŞIYICI FREKANSI REDDEDİLDİ")
    f=float(input("Lütfen yeni bir frekans değeri giriniz:"))
print(f"Girdiğiniz frekans değeri {f:.2f}kHZ güvenli aralık olan 100.00-200.00 kHz aralığında.\nTAŞIYICI FREKANSI KABUL EDİLDİ\n!!!TEBRİKLER!!!")