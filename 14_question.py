"""
Berilgan massivning o'zidan oldingi va keyingi elementlaridan katta bo'lgan musbat elementlaridan
yangi massiv hosil qilish algoritmi va dasturit ta'minotini tuzing.
"""


def more_elements(nums: list) -> list:
    arrays = []
    for i in range(1, len(nums) - 1):
        if nums[i - 1] < nums[i] > nums[i + 1] and nums[i] > 0:
            arrays.append(nums[i])
    return arrays


numbers = [1, 9, 3, 8, 4, 5, 2, 7]
print(more_elements(numbers))
