##Створіть програму, яка запитує користувача ціле число і виводить всі його дільники.

num = int(input("Введіть число: "))

for i in range(1, num):
    if num%i == 0:
        print(str(i) + " -- це дільник")

