# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a



numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 10
print(numbers)

summ = 0
for num in numbers :
    if num > a:
        summ += num


print(summ)
