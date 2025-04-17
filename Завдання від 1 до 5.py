# Завдання 1. «Фільтрація чисел»
filtered_numbers = [x for x in range(1, 101) if x % 3 == 0 and x % 5 != 0]
print("Завдання 1 — Числа, кратні 3, але не кратні 5:")
print(filtered_numbers)

# Завдання 2. «Перетворення температури»
celsius = [0, 10, 20, 30, 40, 100]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print("\nЗавдання 2 — Температури у Фаренгейтах:")
print(fahrenheit)

# Завдання 3. «Квадрати парних чисел»
even_squares = [x**2 for x in range(1, 51) if x % 2 == 0]
print("\nЗавдання 3 — Квадрати парних чисел:")
print(even_squares)

# Завдання 4. «Аналіз тексту»
text = "Python is amazing and powerful language"
word_lengths = [len(word) for word in text.split()]
print("\nЗавдання 4 — Довжини слів у тексті:")
print(word_lengths)

# Завдання 5. «Складні числа»
# Число є складним, якщо має більше 2 дільників
composite_numbers = [
    x for x in range(2, 101)
    if len([d for d in range(1, x + 1) if x % d == 0]) > 2
]
print("\nЗавдання 5 — Складні числа від 1 до 100:")
print(composite_numbers)
