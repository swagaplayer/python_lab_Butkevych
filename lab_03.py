# task 1 
text = input("Введіть текст: ")
total_chars = len(text)
letters = 0
digits = 0
spaces = 0
vowels = 0
vowel_set = set("aeiouyаеєиіїоуюя")
for char in text:
    if char.isalpha():
        letters += 1
        if char.lower() in vowel_set:
            vowels += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
words = len(text.split())
print(f"Символів: {total_chars}")
print(f"Літер: {letters}")
print(f"Цифр: {digits}")
print(f"Пробілів: {spaces}")
print(f"Голосних: {vowels}")
print(f"Слів: {words}")

# task 2
input = "кОмАРОВ  іВАН  пЕТРОВИЧ"
parts = input.split()
if len(parts) == 3:
    last_name = parts[0].capitalize()
    first_name = parts[1].capitalize()
    patronymic = parts[2].capitalize()
    result = f"{last_name} {first_name[0]}.{patronymic[0]}."
    
    print("Результат:", result)
else:
    print("Помилка: Вхідний рядок повинен містити рівно три слова (Прізвище, Ім'я, По батькові).")

    #task 3 
    text1 = input("Перший рядок: ")
    text2 = input("Другий рядок: ")
a = text1.lower().replace(" ", "")
b = text2.lower().replace(" ", "")
if sorted(a) == sorted(b):
    print("Рядки є анаграмами.")
else:
    print("Рядки не є анаграмами.")

#taskk 4
s = input("Введіть речення: ")
words = s.split()
if not words:
    print("Речення порожнє.")
else:
    mx = max(len(w) for w in words)
    mn = min(len(w) for w in words)
    longest = list(dict.fromkeys(w for w in words if len(w) == mx))
    shortest = list(dict.fromkeys(w for w in words if len(w) == mn))
    uniq_cnt = len(set(w.lower() for w in words))
    print(f"Найдовші: {', '.join(longest)}")
    print(f"Найкоротші: {', '.join(shortest)}")
    print(f"Унікальних слів: {uniq_cnt}")
    old = input("Введіть слово для заміни: ")
    new = input("Введіть нове слово: ")
    res_words = [new if w == old else w for w in words]
    print(f"Після заміни: {' '.join(res_words)}")
