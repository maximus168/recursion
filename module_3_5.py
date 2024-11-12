# Рекурсия
number = input( ' Введите число: ', )
def get_multiplied_digits (number):
    str_number = str(number)
    first = int(str_number [0])
    if len (str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else: return first
# number = 5408 # c этим без input тоже работает
result = get_multiplied_digits (number)
print(f'результат умножения цифр в числе {number} : {result}')