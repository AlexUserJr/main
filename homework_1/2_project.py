##Створіть програму, яка запитує у користувача число та виводить усі числа від 1 до цього числа включно.

n = int(input("Введіть число: "))

for i in range(1, n + 1):
    print(i)