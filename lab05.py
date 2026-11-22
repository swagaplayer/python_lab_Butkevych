
# Завдання 1

def circle_area(radius):
    return 3.14159 * radius ** 2


def rectangle_area(width, height):
    return width * height


def triangle_area(base, height):
    return base * height / 2


def task1():
    shape = input('Фігура (круг, прямокутник, трикутник): ').strip().lower()
    try:
        if shape == 'круг':
            radius = float(input('Радіус: '))
            if radius <= 0:
                print('Помилка: радіус має бути додатним.')
                return
            print(f'Площа круга: {circle_area(radius):g}')
        elif shape == 'прямокутник':
            width = float(input('Ширина: '))
            height = float(input('Висота: '))
            if width <= 0 or height <= 0:
                print('Помилка: сторони мають бути додатними.')
                return
            print(f'Площа прямокутника: {rectangle_area(width, height):g}')
        elif shape == 'трикутник':
            base = float(input('Основа: '))
            height = float(input('Висота: '))
            if base <= 0 or height <= 0:
                print('Помилка: основа й висота мають бути додатними.')
                return
            print(f'Площа трикутника: {triangle_area(base, height):g}')
        else:
            print('Помилка: невідома фігура.')
    except ValueError:
        print('Помилка: введіть числові параметри.')


# Завдання 2

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def digit_sum(n):
    return sum(int(digit) for digit in str(n))


def task2():
    value = input('Натуральне число N: ').strip()
    if not value.isdecimal() or int(value) < 1:
        print('Помилка: введіть натуральне число.')
        return
    n = int(value)
    print('Просте число:', 'так' if is_prime(n) else 'ні')
    print('Дільники:', divisors(n))
    print('Сума цифр:', digit_sum(n))


# Завдання 3

def average(grades):
    return sum(grades) / len(grades)


def minimum(grades):
    return min(grades)


def maximum(grades):
    return max(grades)


def count_above(grades, value):
    return sum(grade > value for grade in grades)


def task3():
    grades = [10, 8, 12, 9, 11]
    threshold = 9
    print('Оцінки:', grades)
    print('Поріг:', threshold)
    print('Середній бал:', average(grades))
    print('Мінімальна:', minimum(grades))
    print('Максимальна:', maximum(grades))
    print(f'Вище {threshold}:', count_above(grades, threshold))


# Завдання 4

def has_min_length(password):
    return len(password) >= 8


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_lowercase(password):
    return any(char.islower() for char in password)


def has_special(password):
    return any(not char.isalnum() for char in password)


def validate_password(password):
    errors = []
    if not has_min_length(password):
        errors.append('довжина менше 8 символів')
    if not has_digit(password):
        errors.append('немає цифри')
    if not has_uppercase(password):
        errors.append('немає великої літери')
    if not has_lowercase(password):
        errors.append('немає малої літери')
    if not has_special(password):
        errors.append('немає спеціального символу')
    return len(errors) == 0, errors


def task4():
    password = input('Password: ')
    valid, errors = validate_password(password)
    if valid:
        print('Пароль надійний.')
    else:
        print('Пароль не відповідає вимогам.')
        print('Не виконано:', '; '.join(errors))


# головне меню

def main():
    actions = {'1': task1, '2': task2, '3': task3, '4': task4}
    while True:
        print('\nОберіть завдання: 1, 2, 3, 4 (або 0 для виходу)')
        choice = input('Ваш вибір: ').strip()
        if choice == '0':
            break
        if choice in actions:
            actions[choice]()
        else:
            print('Помилка: оберіть число від 1 до 4 або 0.')


if __name__ == '__main__':
    main()
