# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions
def Composition_and_sum():
    print('введите первую дробь a/b')
    fraction_1 = fractions.Fraction(input())
    print('введите вторую дробь a/b')
    fraction_2 = fractions.Fraction(input())
    composition = fraction_1 * fraction_2
    sum = fraction_1 + fraction_2
    print(f'произведение = {composition} \nсумма {sum}')
    return composition, sum

Composition_and_sum()
