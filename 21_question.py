"""
Berilgan x uchun quyidagi funksiyani hisoblash algoritmi va dasturiy ta'minotini tuzing.
-2x^2+9  agar x<=-1
x/(x^3+9)  agar x> -1
"""

def result(x: int) -> float:
    if x <= -1:
        return -2*x**2+9
    else:
        return x/(x**3+9)

print(result(0))
