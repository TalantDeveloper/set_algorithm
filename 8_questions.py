def quelity(numbers: list) -> int:
    result = 1
    x = len(numbers)
    for i in range(x):
        for j in range(x):
            if i > j:
                print(numbers[i][j])
                result *= numbers[i][j]
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
