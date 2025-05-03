"""
Berilgan x uchun quyidagi funksiyani hisoblash algoritmi va dasturiy ta'minotini tuzing.
x^2 + 2x -4 agar x>=2
1/(x^4-16) agar x<2
"""


def result(x: int) -> float:
    if x >=2:
        return x**2+2*x-4
    else:
        return 1/(x**4-16)

print(result(4))
