# Ixtiyoriy sonning raqamlar yig'indisini hisoblash algoritmi va dasturiy ta'minotini tuzing.

n = int(input("Son kiriting= "))

sum = 0
while n > 0:
    sum += n % 10
    n = n // 10

print(sum)
