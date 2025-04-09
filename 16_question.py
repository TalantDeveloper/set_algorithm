"""
Berilgan uchta nuqta A(x1; y1), B(x2; y2), C(x3; y3) uchburchakning uchlarini tashkil qilish yoki
tashkil qilmasligini aniqlash algoritmi va dasturiy ta'minotini tuzing.
"""
# def uchburchak_bormi(x1, y1, x2, y2, x3, y3):
#     # Vektorlar determinantini hisoblaymiz
#     determinant = (x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)
#     if determinant == 0:
#         return "Bu nuqtalar uchburchak hosil qilmaydi (bir to‘g‘ri chiziqda yotadi)."
#     else:
#         return "Bu nuqtalar uchburchak hosil qiladi."
#
# # Foydalanuvchidan nuqtalar koordinatalarini olish
# x1, y1 = map(int, input("A nuqtaning (x1 y1) koordinatalarini kiriting: ").split())
# x2, y2 = map(int, input("B nuqtaning (x2 y2) koordinatalarini kiriting: ").split())
# x3, y3 = map(int, input("C nuqtaning (x3 y3) koordinatalarini kiriting: ").split())
#
# natija = uchburchak_bormi(x1, y1, x2, y2, x3, y3)
# print(natija)


def triangle_have(x1, y1, x2, y2, x3, y3):
    determinant = (x2 - x1) * (y3 - y1) - (x3 - x1)*(y2 - y1)
    print(determinant)
    if determinant == 0:
        print("Uchburchak yasash mumkin emas.")
    else:
        print("Uchburchak yasash mumkin.")


x1, y1 = map(int, input("A nuqtaning (x1 y1) koordinatalarini kiriting: ").split())
x2, y2 = map(int, input("B nuqtaning (x2 y2) koordinatalarini kiriting: ").split())
x3, y3 = map(int, input("C nuqtaning (x3 y3) koordinatalarini kiriting: ").split())

triangle_have(x1, y1, x2, y2, x3, y3)
