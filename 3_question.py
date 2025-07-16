#  Berilgan n natural sondagi turli raqamlar miqdori aniqlansin.

n = int(input("Son kiriting= "))

nums = []
while n > 0:
    k = n % 10
    if k not in nums:
        nums.append(k)
    n = n // 10

print(f"Turli raqamlar soni = {len(nums)}")

