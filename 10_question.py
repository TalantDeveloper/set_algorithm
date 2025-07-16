# Berilgan a, b va c sonlar uchun EKUB(a,b,c) va EKUK(a,b,c)larni hisoblash
# algoritmi va dasturiy ta'minotini tuzing

def ekub(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def ekuk(a, b):
    return (a * b) // ekub(a, b)


def ekub_ekuk(a, b, c):
    print(f"EKUB({a}, {b}, {c}) =>", ekub(ekub(a, b), c))
    print(f"EKUK({a}, {b}, {c}) =>", ekuk(ekuk(a, b), c))


ekub_ekuk(12, 6, 26)
print(ekub(12, 36))
