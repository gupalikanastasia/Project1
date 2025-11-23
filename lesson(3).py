student_grades = {}
excellent_students = []# 10-12
good_students = []     # 7-9
lagging_students = []  # 4-6
failed_students = []   # 1-3
total_score = 0

print("Вводьте ім'я студента та його оцінку. Для завершення введіть 'stop'.")

while True:
    name = input("Введіть ім'я (або 'stop' для виходу): ")
    if name == 'stop':
        break
    try:
        grade = int(input(f"Введіть оцінку для {name}: "))

        if 1 <= grade <= 12:
            student_grades[name] = grade
            total_score += grade

            if 10 <= grade <= 12:
                excellent_students.append(name)
            elif 7 <= grade <= 9:
                good_students.append(name)
            elif 4 <= grade <= 6:
                lagging_students.append(name)
            elif 1 <= grade <= 3:
                failed_students.append(name)
        else:
            print("Оцінка має бути від 1 до 12!")

    except ValueError:
        print("Будь ласка, введіть число!")

if student_grades:
    print(f"Всі студенти та оцінки: {student_grades}")

    average = total_score / len(student_grades)
    print(f"Середній бал: {average:.2f}")

    print(f"Відмінники (10-12): {len(excellent_students)} - {', '.join(excellent_students)}")
    print(f"Хорошисти (7-9): {len(good_students)}")
    print(f"Відстаючі (4-6): {len(lagging_students)}")
    print(f"Не здали (1-3): {len(failed_students)}")
else:
    print("\nСписок студентів порожній.")





