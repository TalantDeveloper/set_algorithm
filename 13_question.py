"""
Berilgan massivda manfiy elementlarini o'sish hamda musbat elementlarini kamayish tartibida
saralash algoritmi va dasturiy ta'minotini tuzing.
"""


def sort_list(nums: list) -> list:
    list_1 = [x for x in nums if x < 0]
    list_2 = [x for x in nums if x >= 0]
    print(list_1, list_2)
    for i in range(1, len(list_1)):
        for j in range(len(list_1) - 1):
            if list_1[i] > list_1[j]:
                list_1[i], list_1[j] = list_1[j], list_1[i]
    for i in range(1, len(list_2)):
        for j in range(len(list_2) - 1):
            if list_2[i] < list_2[j]:
                list_2[i], list_2[j] = list_2[j], list_2[i]
    return list_1 + list_2


numbers = [5, -1, -7, 2, 9, -4, -9]
print(sort_list(numbers))
