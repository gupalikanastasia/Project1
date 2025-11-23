from type_checker import type_checker

@type_checker(a=int, b=str)
def greet_person(a, b="Default"):
    print(f"Привіт, {b}! Твоє щасливе число: {a}")
    return a + 1

@type_checker(x=float, z=list)
def calculate_sum(x, y, z):
    total = x + y + sum(z)
    print(f"Обчислена сума: {total}")
    return total

print("Тестування Успішних Викликів")
result1 = greet_person(10, "Анастасія")
print(f"Результат greet_person: {result1}")

result2 = calculate_sum(x=5.5, y=2, z=[1, 2, 3])
print(f"Результат calculate_sum: {result2}")

print("\nТестування Помилок Типу")
try:
    greet_person("twenty", "Іван")
except TypeError as e:
    print(f"Перехоплено очікувану помилку: {e}")

try:
    calculate_sum(5.5, 2, z=(1, 2, 3))
except TypeError as e:
    print(f"Перехоплено очікувану помилку: {e}")
