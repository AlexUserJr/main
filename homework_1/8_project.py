##Створіть програму, яка перевіряє, чи є введений користувачем рядок паліндромом.

text = input("Введіть фразу: ")
reversed_text = ""

for i in range(len(text)-1, -1, -1):
    reversed_text += text[i]

if text == reversed_text:
    print("Фраза є паліндромом")
else: print("Фраза не є паліндромом")