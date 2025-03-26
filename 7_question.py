def palindrom(number):
    """Berilgan ixtiyoriy sonning Palindromligini aniqlash."""
    num_str = str(number)
    length = len(num_str)
    half = length // 2
    for i in range(half):
        if num_str[i] != num_str[length - i - 1]:
            return f"{number} palindrom son emas."
    return f"{number} palindrom son."


print(palindrom(65456))
