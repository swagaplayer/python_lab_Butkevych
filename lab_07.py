from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def task1():
    with (BASE_DIR / "text.txt").open("r", encoding="utf-8") as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    print(f"Рядків: {line_count}")
    print(f"Слів: {word_count}")
    print(f"Символів: {char_count}")

    if not lines:
        print("Файл порожній: найдовшого рядка немає.")
        return

    clean_lines = [line.rstrip("\r\n") for line in lines]
    number, longest = max(enumerate(clean_lines, start=1), key=lambda item: len(item[1]))
    print(f"Найдовший рядок: №{number}, {len(longest)} символів")
    print(f"Текст: {longest}")


def task2():
    fragment = input("Фрагмент для пошуку: ").strip()
    if not fragment:
        print("Помилка: фрагмент не може бути порожнім.")
        return

    found = False
    with (BASE_DIR / "text.txt").open("r", encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            line = line.rstrip("\r\n")
            if fragment.casefold() in line.casefold():
                print(f"{number}: {line}")
                found = True

    if not found:
        print("Збігів не знайдено.")



def read_students(path):
    students = []
    with path.open("r", encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(";")
            if len(parts) != 2 or not parts[0].strip():
                raise ValueError(f"students.txt, рядок {number}: неправильний формат")
            name = parts[0].strip()
            try:
                score = int(parts[1].strip())
            except ValueError as exc:
                raise ValueError(f"students.txt, рядок {number}: бал має бути цілим числом") from exc
            students.append((name, score))
    return students


def task3():
    students = read_students(BASE_DIR / "students.txt")
    selected = sorted((student for student in students if student[1] > 80),
                      key=lambda student: student[1], reverse=True)
    output = BASE_DIR / "result.txt"
    with output.open("w", encoding="utf-8") as file:
        for name, score in selected:
            file.write(f"{name};{score}\n")

    print("Результати студентів з балом понад 80:")
    if selected:
        for name, score in selected:
            print(f"{name};{score}")
    else:
        print("Таких студентів немає.")
    print(f"Результат збережено у {output.name}")



def read_grades(path):
    data = {}
    with path.open("r", encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(";")
            if len(parts) != 3 or not parts[0].strip() or not parts[1].strip():
                raise ValueError(f"grades.csv, рядок {number}: потрібен формат name;subject;grade")
            name, subject, value = (part.strip() for part in parts)
            try:
                grade = int(value)
            except ValueError as exc:
                raise ValueError(f"grades.csv, рядок {number}: оцінка має бути цілим числом") from exc
            if not 1 <= grade <= 12:
                raise ValueError(f"grades.csv, рядок {number}: оцінка має бути від 1 до 12")
            data.setdefault(name, []).append(grade)
    return data


def make_report(data):
    if not data:
        return "Немає даних про оцінки.\n"

    results = [(name, len(grades), sum(grades) / len(grades))
               for name, grades in data.items()]
    results.sort(key=lambda item: item[2], reverse=True)

    lines = [f"{name} — оцінок: {count} — середній: {avg:.2f}"
             for name, count, avg in results]
    best_average = results[0][2]
    best_names = [name for name, _, avg in results if abs(avg - best_average) < 1e-9]
    lines.extend(["Найкращий результат:",
                  f"{' та '.join(best_names)} — {best_average:.2f}"])
    return "\n".join(lines) + "\n"


def task4():
    data = read_grades(BASE_DIR / "grades.csv")
    report = make_report(data)
    with (BASE_DIR / "report.txt").open("w", encoding="utf-8") as file:
        file.write(report)
    print(report, end="")
    print("Звіт збережено у report.txt")


def main():
    tasks = {"1": task1, "2": task2, "3": task3, "4": task4}
    while True:
        print("\nОберіть завдання: 1, 2, 3, 4 (або 0 для виходу)")
        try:
            choice = input("Ваш вибір: ").strip()
        except EOFError:
            print("Введення недоступне. Запустіть файл у терміналі VS Code.")
            break
        if choice == "0":
            print("Роботу завершено.")
            break
        if choice not in tasks:
            print("Помилка: оберіть 1, 2, 3, 4 або 0.")
            continue
        try:
            tasks[choice]()
        except FileNotFoundError as exc:
            print(f"Помилка: не знайдено файл {Path(exc.filename).name}. "
                  "Перевірте, чи він знаходиться поруч із lab06.py.")
        except (UnicodeError, ValueError, PermissionError) as exc:
            print(f"Помилка обробки файлу: {exc}")


if __name__ == "__main__":
    main()
