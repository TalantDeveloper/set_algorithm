"""
Berilgan x uchun quyidagi funksiyan hisoblash algoritmi va dasturiy ta'minotini tuzing.
x^3-9  agar x>10
-(2x)/(x^2-29) agar x<=10
"""

def result(x: int) -> float:
    if x > 10:
        return x**3-9
    else:
        return -(2*x)/(x**2-29)

print(result(11))
