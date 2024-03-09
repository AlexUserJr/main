##Розробте програму, яка запитує у користувача число та виводить його факторіал.

num = int(input("Введіть число: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Факторіал числа", num, ":", factorial)