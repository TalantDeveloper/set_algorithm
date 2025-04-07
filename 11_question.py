def sorted_array(numbers: list) -> list:
    lenth = len(numbers)
    for i in range(lenth):
        if numbers[i] < 0:
            numbers[i] = -numbers[i]
    for i in range(lenth):
        for j in range(lenth):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


numbers = [1, 9, 3, -8, 4, 5, 2, 7]
print(numbers)
print(sorted_array(numbers))
