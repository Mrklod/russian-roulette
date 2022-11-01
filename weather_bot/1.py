def convert_number_2_word(number):
    if number == 0:
        return "ноль"
    elif number == 1:
        return "один"
    elif number == 2:
        return "два"
    elif number == 3:
        return "три"
    elif number == 4:
        return "четыре"
    elif number == 5:
        return "пять"
    elif number == 6:
        return "шесть"
    elif number == 7:
        return "семь"
    elif number == 8:
        return "восемь"
    elif number == 9:
        return "девять"


def calculate_scores(string):
    b = [0,0,0]

    if "A" in string:
        b[0] += 1
    if "B" in string:
        b[1] += 1
    if "C" in string:
        b[2] += 1
    return b

"""def rec(s):
    if len(s)== 1 or len(s) == 2:
        return s
    return s[0] + "(" + rec(s[1:-1]) + ")" + s[-1]
s = input()
print(rec(s))

def rec(s):
    if len(s)==0:
        return s
    return s[0] + rec(s[2:-1]) + "*"+s[1]

s = input()

print(rec(s))"""


def power(x, n):
    if n == 0:
        return 1
    if n%2==0:
        return power(x, n//2)*power(x, n//2)
    else:
        power(x, n-1)*x



