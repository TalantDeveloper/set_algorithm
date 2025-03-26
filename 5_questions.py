def sonlarni_almashtirish(x, y, z):
    summa = x + y + z
    sonlar = [x, y, z]
    if x == y == z:
        return f"Sonlar o'zaro teng!"

    eng_katta = max(sonlar)
    eng_kichik = min(sonlar)

    if summa > 9:
        sonlar.remove(eng_katta)
        yangi_qiymat = (sonlar[0] + sonlar[1]) / 2
        sonlar.append(yangi_qiymat)
    else:
        sonlar.remove(eng_kichik)
        yangi_qiymat = (sonlar[0] + sonlar[1]) / 2
        sonlar.append(yangi_qiymat)

    return sonlar


x = int(input("x ni kiriting: "))
y = int(input("y ni kiriting: "))
z = int(input("z ni kiriting: "))

natija = sonlarni_almashtirish(x, y, z)
print("Natija:", natija)
