v=12
r1=1000
for r2 in range (200,1100,100):
    v_out=v*(r2/(r1+r2))
    print(f"Çıkış gerilimi:{v_out:.2f}Volt. Giriş gerilim:{v:.2f}Volt R1 direnci:{r1:.2f}ohm R2 direnci:{r2:.2f}ohm")