# Berilgan bir xil o'lchamli ikkita massivning skalyar ko'paytmasini
# hisoblash algoritmi va dasturiy ta'minotini tuzing.

def add_elements(nums_1, nums_2):
    if len(nums_1) != len(nums_2):
        return f"Massivlar o'lchami teng emas {len(nums_1)} != {len(nums_2)}"
    result = 0
    for i in range(len(nums_1)):
        result += nums_1[i] * nums_2[i]
    return result


numbers1 = [1, 4, 5, 2, 7, 9, 3, -8]
numbers2 = [1, 9, 3, 8, 4, 5, 2, 7]
print(add_elements(numbers1, numbers2))
