v_kond=9.0
v_güvenli=1.0
adım=0.0
while v_kond>=v_güvenli:
    v_kond*=0.88
    adım+=1
    print(f"Kondansatör yükü:{v_kond:.2f} Adım Sayısı:{adım:.2f}\nKondansatör yükü güvenli aralıkta")
print(f"Kondansatör Yükü:{v_kond:.2f} Adım Sayısı:{adım:.2f}\nKondansatör yükü güvenli aralıkta değil.\nLütfen kondansatörü şarj ediniz")