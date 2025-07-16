#  Haqiqiy sonlardan iborat ketma-ketlikning manfiy elementlari orasidan eng
#  kattasini aniqlash algoritmi va dasturiy ta'minotini tuzing.

n = int(input("n = "))
min_num = None
nums = []
for i in range(n):
    num = float(input(f"{i + 1}-element="))
    if num < 0:
        if min_num is None or num > min_num:
            min_num = num

print(f"Natija: {min_num}")
