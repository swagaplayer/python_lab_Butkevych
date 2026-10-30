#task 1
l = [12, 3, 4, 14, -12, 5, 10, 16, -4]
p = []  
m = []  
e = []  
d = []  
for x in l:
    if x > 0: p.append(x)
    if x < 0: m.append(x)
    if x % 2 == 0: e.append(x)
    if x % 3 == 0: d.append(x)
mn = min(l)
mx = max(l)
s = sum(l)
a = s / len(l)
print("Додатні:", p)
print("Від’ємні:", m)
print("Парні:", e)
print("Кратні 3:", d)
print(f"Min: {mn}; Max: {mx}; Sum: {s}; Average: {round(a, 2)}")

#task 2
g1 = {'Anna', 'Ivan', 'Olha'}
g2 = {'Ivan', 'Maksym', 'Olha'}

c_m = g1 & g2
o1 = g1 - g2
o2 = g2 - g1
al = g1 | g2

print("Спільні:", ", ".join(c_m))
print("Тільки group1:", ", ".join(o1))
print("Тільки group2:", ", ".join(o2))
print("Усі:", ", ".join(al))

#task 3
d = {
    "mouse": 35,
    "keyboard": 48,
    "monitor": 120,
    "ram": 75
}
d["mouse"] = 38
d["ssd"] = 65
q = "keyboard"
r = d.get(q, "Товар не знайдено")
print(f"Пошук товару '{q}': {r} грн") 
print("Товари в діапазоні 40..100 грн:")
for k, v in d.items():
    if 40 <= v <= 100:
        print(f"{k} - {v} грн")

#task 4
g = ('10-IT', '2026/2027')
d = {
    "Anna": [10, 11, 12, 11, 10],
    "Ivan": [8, 9, 10, 11, 9]
}
n = "Olha"
m = [11, 12, 12, 10, 11]

if len(m) == 5 and all(1 <= x <= 12 for x in m):
    d[n] = m
print(f"{g[0]} — {g[1]}")
b_n = "" 
h_m = 0   
for k, v in d.items():
    a = sum(v) / len(v)
    print(f"{k} — {round(a, 1)}")
    
    if a > h_m:
        h_m = a
        b_n = k

print(f"Найкращий результат: {b_n} — {round(h_m, 1)}")

