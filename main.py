#  1. Berilgan n ta haqiqiy sonlar orasida qo'shnilaridan (oldingi va keyingi sonlardan)
#  katta bo'lgan sonlar miqdorini topish algoritmi va dasturi tuzilsin.

def greater_between():
    n = int(input("n ="))

    nums = []
    for i in range(n):
        num = float(input(f"{i + 1}-element="))
        nums.append(num)

    t = 0
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            t += 1

    return f"Natija: {t}"


print(greater_between())
