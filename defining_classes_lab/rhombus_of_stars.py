def print_rhombus(number):
    res = ''
    offset_counter = 1
    row = 0
    for i in range(number):
        offset = " " * (number - 2 + offset_counter)
        res += f'{offset}*' + f' *' * row + f'\n'
        offset_counter -= 1
        row += 1
    row = number - 2
    for j in range(number - 1):
        offset = " " * (number + offset_counter)
        res += f'{offset}*' + f' *' * row + f'\n'
        offset_counter += 1
        row -= 1
    return res


n = int(input())
print(print_rhombus(n))