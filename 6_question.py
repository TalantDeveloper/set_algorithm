def matritsani_tozalash(matritsa):
    n = len(matritsa)
    m = len(matritsa[0])

    # Musbat element mavjud bo‘lgan satr va ustunlarni aniqlash
    musbat_satrlar = set()
    musbat_ustunlar = set()

    for i in range(n):
        for j in range(m):
            if matritsa[i][j] > 0:
                musbat_satrlar.add(i)
                musbat_ustunlar.add(j)

    # Filtrlash (musbat element mavjud bo‘lgan satr va ustunlarni o‘chirish)
    yangi_matritsa = []
    for i in range(n):
        if i not in musbat_satrlar:
            yangi_satr = []
            for j in range(m):
                if j not in musbat_ustunlar:
                    yangi_satr.append(matritsa[i][j])
            if yangi_satr:  # agar satr bo‘sh bo‘lib qolmasa
                yangi_matritsa.append(yangi_satr)

    return yangi_matritsa

# Misol uchun
# n = int(input("Matritsa satrlar soni (n): "))
# m = int(input("Matritsa ustunlar soni (m): "))

matritsa = [
    [-1, -2, -4, -6, -7, 9],
    [-5, -4, -3, -2, -1, -2],
    [2, -5, 6, -4, -6, -3]
]
# print("Matritsa elementlarini kiriting:")
# for i in range(n):
#     satr = list(map(int, input(f"{i+1}-satr elementlari: ").split()))
#     matritsa.append(satr)

natija = matritsani_tozalash(matritsa)

print("\nTozalangan matritsa:")
for row in natija:
    print(row)
