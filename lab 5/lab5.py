try:
    import requests
    import numpy
    import pandas
    import matplotlib
    from PIL import Image
    import flask
    from bs4 import BeautifulSoup
    import scipy
    import tqdm
    import pycowsay
    print("Успішно імпортовано всі 10 бібліотек.\n")

except ImportError as e:
    print(f"Помилка імпорту: {e}")
    print("Будь ласка, переконайтеся, що ви встановили всі бібліотеки з requirements.txt")
    print("Використайте команду: pip install -r requirements.txt")
    exit()

try:
    print("Блок 1: requests")
    response = requests.get("https://google.com")

    if response.status_code == 200:
        print(f"requests: Отримано успішну відповідь від google.com, статус: {response.status_code}")
    else:
        print(f"requests: Отримано дивний статус: {response.status_code}")

except Exception as e:
    print(f"requests: Помилка під час виконання запиту: {e}")

try:
    print("\nБлок 2: numpy")
    arr = numpy.array([10, 20, 30, 40, 50])
    mean_value = arr.mean()
    print(f"numpy: Створено масив. Середнє значення: {mean_value}")

except Exception as e:
    print(f"numpy: Помилка: {e}")

try:
    print("\nБлок 3: pandas")
    data = {'Ім\'я': ['Анна', 'Богдан', 'Віктор'], 'Вік': [25, 30, 22]}
    df = pandas.DataFrame(data)
    print("pandas: Створено DataFrame:")
    print(df.to_string())

except Exception as e:
    print(f"pandas: Помилка: {e}")
try:
    print("\nБлок 4: Pillow")
    img = Image.new('RGB', (100, 50), color='red')
    img.show()
    print(f"Pillow: Створено нове зображення розміром {img.size} та режимом {img.mode}")

except Exception as e:
    print(f"Pillow: Помилка: {e}")

try:
    print("\nБлок 5: tqdm")
    print("tqdm: Запуск демонстрації прогрес-бару...")
    for i in tqdm.tqdm(range(1000000), desc="Завантаження"):
        pass

    print("tqdm: Прогрес-бар завершено!")

except Exception as e:
    print(f"tqdm: Помилка: {e}")

print("\nЗавершення програми")