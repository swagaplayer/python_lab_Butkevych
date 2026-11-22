
import tkinter as tk
import student_utils

students = ["Anna", "Ivan", "Olha"]


def make_report():
    value = count_entry.get().strip()
    report_text.delete("1.0", tk.END)

    if not value.isdecimal() or not 1 <= int(value) <= 20:
        report_text.insert(
            tk.END,
            "Помилка: введіть ціле число від 1 до 20."
        )
        return

    count = int(value)
    lines = []

    for student in students:
        grades = student_utils.generate_grades(count)
        average = student_utils.average_grade(grades)
        level = student_utils.get_level(average)

        lines.append(
            f"{student}: {grades} → {average:.2f} → {level}"
        )

    report = "\n".join(lines)
    print(report)
    report_text.insert(tk.END, report)


window = tk.Tk()
window.title("Статистика учнів")
window.geometry("660x300")

tk.Label(
    window,
    text="Введіть кількість оцінок (1–20):"
).pack(pady=8)

count_entry = tk.Entry(window)
count_entry.pack(pady=4)

tk.Button(
    window,
    text="Сформувати звіт",
    command=make_report
).pack(pady=8)

report_text = tk.Text(
    window,
    height=8,
    width=75,
    wrap="word"
)
report_text.pack(padx=12, pady=8)

window.mainloop()
