#task1
import math

radius = float(input("Радіус: "))
a = float(input("Перший катет: "))
b = float(input("Другий катет: "))
n = int(input("Предметів: "))
k = int(input("В упаковці: "))

if radius < 0 or a < 0 or b < 0 or n < 0 or k <= 0:
    print("Помилка: перевірте введені значення.")
else:
    area = math.pi * radius ** 2
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    packages = math.ceil(n / k)

    print(f"Площа круга: {area:.2f}")
    print(f"Гіпотенуза: {hypotenuse:.2f}")
    print(f"Потрібно упаковок: {packages}")

    #task2
import random
import statistics

value = input("Кількість оцінок N: ").strip()

if not value.isdecimal() or int(value) <= 0:
    print("Помилка: N має бути додатним цілим числом.")
else:
    n = int(value)
    grades = [random.randint(1, 12) for _ in range(n)]

    print("Оцінки:", grades)
    print("Min:", min(grades))
    print("Max:", max(grades))
    print("Середнє:", round(statistics.mean(grades), 2))
    print("Медіана:", statistics.median(grades))
    print("Оцінок 10–12:", sum(grade >= 10 for grade in grades))

#task3
from datetime import date

try:
    year = int(input("Рік події: "))
    month = int(input("Місяць події: "))
    day = int(input("День події: "))

    event_date = date(year, month, day)
    today = date.today()

    if event_date > today:
        print(f"До події залишилося: {(event_date - today).days} днів")
    elif event_date < today:
        print(f"Після події минуло: {(today - event_date).days} днів")
    else:
        print("Подія відбувається сьогодні!")

except ValueError:
    print("Помилка: введіть правильну дату.")
