##Напишіть програму, яка перевіряє, чи є введене користувачем число простим чи складовим.

num = int(input("Введіть число: "))

is_simple = True
if num >= 4:
    for i in range(2, num-1):
        if num%i == 0:
            is_simple = False
            break

if is_simple:
    print("Число " + str(num) + " " + "просте")
else:
    print("Число " + str(num) + " " + "складене")