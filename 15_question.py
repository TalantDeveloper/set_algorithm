"""
Berilgan 3*3 o'lchamli matritsaning determinantini hisoblash algoritmi va dasturiy ta'minotini tuzing.
"""

nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def determinant(nums: list):
    lenth = len(nums)
    for i in range(len(nums)):
        nums[i] = nums[i] + nums[i][:lenth - 1]
    print(nums)
    print(nums[2][4])
    result = nums[0][0]*nums[1][1]*nums[2][2]-nums[2][2]*nums[1][1]*nums[0][2]
    print(result)
    result += nums[0][1]*nums[1][2]*nums[2][3]-nums[2][1]*nums[1][2]*nums[0][3]
    print(result)
    result += nums[0][2]*nums[1][3]*nums[2][4]-nums[2][2]*nums[1][3]*nums[0][4]
    return result


print(determinant(nums))
