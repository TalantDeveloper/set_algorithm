"""
Berilgan x uchun quyidagi funksiyani hisoblash algoritmi va dasturiy ta'minotini tuzing.
x+19 agar x>=5
1/(x^2-14) agar x<5
"""

def result(x: int) -> float:
    if x>=5:
        return x+19
    else:
        return 1/(x**2-14)

print(result(4))
