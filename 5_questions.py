# def sonlarni_almashtirish(x, y, z):
#     summa = x + y + z
#     sonlar = [x, y, z]
#     if x == y == z:
#         return f"Sonlar o'zaro teng!"
#
#     eng_katta = max(sonlar)
#     eng_kichik = min(sonlar)
#
#     if summa > 9:
#         sonlar.remove(eng_katta)
#         yangi_qiymat = (sonlar[0] + sonlar[1]) / 2
#         sonlar.append(yangi_qiymat)
#     else:
#         sonlar.remove(eng_kichik)
#         yangi_qiymat = (sonlar[0] + sonlar[1]) / 2
#         sonlar.append(yangi_qiymat)
#
#     return sonlar
#
#
# x = int(input("x ni kiriting: "))
# y = int(input("y ni kiriting: "))
# z = int(input("z ni kiriting: "))
#
# natija = sonlarni_almashtirish(x, y, z)
# print("Natija:", natija)


# Agar uchta haqiqiy, o'zaro teng bo'lmagan x, y va z sonlar yig'indisi 1 dan kichik bo'lsa, u holda
# uchta sonnin eng kichigi qolganlari yig'indisining yarmisi bilan almashtirish, aks holda x va y lardan
# kichigi qolganlari yig'indisining yarmi bilan almashtirish algoritmi va dasturiy ta'minotini tuzing.


x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

if x == y == z:
    print("Sonlar o'zaro teng")

min_num = min(x, y, z)
max_num = max(x, y, z)
sum = x + y + z


