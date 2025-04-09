"""
Massivning [-5, 6] intervalga tegishli elementlarini o'sish tartibida saralash va qolgan
elementlarini o'z o'rnida qoldirish algoritmi va dastruriy ta'minotini tuzing.
"""


def innterval(nums: list) -> list:
    arrays = []
    for num in nums:
        if -5 <= num <= 6:
            arrays.append(num)
    for i in range(1, len(arrays)):
        for j in range(len(arrays) - 1):
            if arrays[i] <= arrays[j]:
                num = arrays[j]
                arrays[j] = arrays[i]
                arrays[i] = num
    k = 0
    for i in range(len(nums)):
        if nums[i] in arrays:
            nums[i] = arrays[k]
            k +=1
    return nums


numbers = [-4, 5, 4, -2, -8, 9, 2]
print(innterval(numbers))
