a = [8, 2, 6, 4, 5, 9, 7, 1, 3, 0, 'f', 'q', 'y', 'a', 'e', 'm', 'o', 'p', 's', 'w']
numbers = []
letters = []
for item in a:
    if type(item) is str:
        letters.append(item)
    elif type(item) is int:
        numbers.append(item)

numbers.sort()
letters.sort()

fin_list = numbers + letters

two = []
for item in numbers:
    if item % 2 == 0:
        two.append(item)

caps = []
for item in letters:
    caps.append(item.upper())

print('Відсортований список:', fin_list)
print('Список парних чисел:', two)
print('Список літер написаних капсом:', caps)