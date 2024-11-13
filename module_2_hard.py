def gen_password(number):
    result = ""
    for i in range(1, number):
        for j in range(i+1, number+1):
            if (i + j) % number == 0:
                result += str(i) + str(j)
    return result

number= int(input("Введите число от 3 до 20: "))
if 3 <= number <= 20:
    print(gen_password(number))
else:
    print("Введите число в пределах от 3 до 20.")