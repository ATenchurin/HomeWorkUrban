first = int(input('Введите первое произвольное число: '))
second = int(input('Введите второе произвольное число: '))
third = int(input('Введите третье произвольное число: '))
if first == second and first == third and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)