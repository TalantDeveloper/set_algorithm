

def quelity(numbers: list) -> int:
    result = 1
    length = len(numbers)
    for i in range(length):
        for j in range(length - 1 - i):
            print(numbers[i][j], end=" ")
            result *= numbers[i][j]
        print()
    return result


nums = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]
]
print(quelity(nums))
