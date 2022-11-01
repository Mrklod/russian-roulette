# Калькулятор для дебилов v1

import numexpr

expr = input("Введите пример: ")

resultat = numexpr.evaluate(expr)

print(resultat)