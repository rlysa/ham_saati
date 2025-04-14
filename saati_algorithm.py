def check_amount(n):
    if not n.isdigit():
        return False
    if int(n) < 2:
        return False
    return int(n)


def check_names(n, str1, str2):
    names = []
    for i in range(n):
        print(f'Введите название {str1} {i + 1}')
        name = input()
        while name in names or name == '':
            print(f'Такой {str2} уже существует или введена пустая строка. Введите другое название {str1} {i + 1}')
            name = input()
        names.append(name)
    return names


def fill_matrix(n, names, str1, str2):
    matrix = [[1.0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        for j in range(1, n - i):
            print(f'Сравните {str1} "{names[i]}" и {str1} "{names[i + j]}" {str2}')
            k = input()
            while k.isalpha():
                print(f'Введите целое или дробное число. Сравните {str1} "{names[i]}" и {str1} "{names[i + j]}"')
                k = input()
            matrix[i + j][i] = float(k)
            matrix[i][i + j] = 1 / float(k)
    return matrix


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(round(j, 2), end=f'{" " * (5 - len(str(round(j, 2))))}')
        print()
