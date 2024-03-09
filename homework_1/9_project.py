##Напишіть програму, яка знаходить середнє арифметичне всіх чисел у списку.

numbers = [1, 2, 3, 4, 5]
sum = 0

for number in numbers:
    sum = sum + number

average = sum/len(numbers)

print("Середнє арифметичне:", average)