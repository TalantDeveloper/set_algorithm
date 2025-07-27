"""
Berilgan 3*3 o'lchamli matritsaning determinantini hisoblash algoritmi va dasturiy ta'minotini tuzing.
"""

nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def determinant(nums: list) -> int:
    result = nums[0][0] * nums[1][1] * nums[2][2] - nums[2][0] * nums[1][1] * nums[0][2]
    result += nums[0][1] * nums[1][2] * nums[2][0] - nums[0][0] * nums[2][1] * nums[1][2]
    result += nums[0][2] * nums[1][0] * nums[2][1] - nums[1][0] * nums[0][1] * nums[2][2]
    return result


print(determinant(nums))
