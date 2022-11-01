"""def abbrev_name(name=str):
    a,b = name.split(sep=" ")
    c = str(a[0] + "." + b[0])
    return c.upper()


def bool_to_word(boolean):
    if boolean == "True":
        return "Yes"
    return "No"

def quarter_of(month):
    if month == 1 or 2 or 3:
        return 1
    if month == 4 or 5 or 6:
        return 2
    if month == 7 or 8 or 9:
        return 3
    if month == 10 or 11 or 12:
        return 4

def summation(num):
    c = 0
    for i in range(num+3):
        c = c + i
    return c

def greet(name):
    return (f"Hello,{name} how are you doing today?")

def update_light(current):
    if current == "green":
        return "yellow"
    if current == "yellow":
        return "red"
    if current == "red":
        return "green"

#def distinct(seq):
    #c = set(seq)
    #return list(c)
    new_seq = []
    #for i in seq:
        #if i not in new_seq:
            #seq.append(i)
    #return new_seq

def distinct(seq):
    return sorted(set(seq), key=seq.index)

def find_smallest_int(arr):
    c = 0
    for i in range(len(arr)):
        if arr[i] < c:
            c = i
    return c

def find_smallest_int(arr):
    return min(arr)


def sort_trade():
    mas = [51,16,77,11,2]
    n = len(mas)
    p = n - 1
    while p > 0:
        for i in range(p):
            if mas[i] > mas[i + 1]:
                mas[i],mas[i+1]=mas[i+1],mas[i]
        p-=1
    for i in range(n):
        print(mas[i])

def mas_masiv():
    a = [[1,2,3],[1,2,3],[1,2,3]]
    n = 3
    m = 3
    s = 0
    for i in range(n):
        for j in range(m):
            s = s + a[i][j]
    print(s)
    print(s/(n*m))

def max_min_mas():
    a = [[-1,2,3],[1,2,3],[1,2,4]]
    max = a[0][0]
    min = a[0][0]
    for i in range(3):
        for j in range(3):
            if a[i][j]>max:
                max=a[i][j]
            if a[i][j]<min:
                min = a[i][j]
    return max,min

def count_max():
    a = [[-1, 2, 3], [1, 2, 3], [1, 2, 4]]
    c = int(input("c = "))
    k = 0
    p = False
    for i in range(3):
        for j in range(3):
            if c == a[i][j]:
                k +=1
                p= True
    if p == True:
        return f"Таких чисел {k}"
    return "Nety"

def better_than_average(class_points=[], your_points=int):
    c = len(class_points)
    b = (sum(class_points) /len(class_points)
    if int(b)<your_points:
        return True
    return False

def basic_op(operator, value1, value2):
    if operator == +:
        return value1 + value2
    if operator == -:
        return value1 - value2
    if operator == *:
        return value1 * value2
    if operator == /:
        return value1 / value2


def solution(string, ending):
    if ending[-1]!=string[-1]:
        return False
    if ending in string[1:]:
        return True
    if ending == string:
        return True
    if ending not in string[1:]:
        return False

def solution(string, ending):
    return string.endswith(ending)

def high_and_low(numbers):
    c = f"{max(numbers)} {min(numbers)}"
    return c

def get_sum(a,b):
    if a == b:
        return a
    c = 0
    for i in range(a,b):
        c = c + i
    return c

def positive_sum(arr):
    sum_num = 0
    for i in arr:
        if i >=0:
            sum_num = sum_num + i
    return sum_num


def invert(lst):
    num = []
    for i in lst:
        i = i * -1
        num.append(i)
    return num

def are_you_playing_banjo(name):
    if name[0]=="R" or name[0]=="r":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"

def filter_list(l):
    mas=[]
    for i in l:
        if i == int:
            mas.append(i)
    return mas

def friend(x):
    c = []
    for i in x:
        if len(i)==4:
            c.append(i)
    return c

def find_short(s):
    return min(len(x) for x in s.split())

def no_space(x=str):
    b = x.split()
    b = ''.join(b)
    return b

def make_negative( number ):
    if number == 0:
        return 0
    if number>0:
        return number*-1
    return number

def paperwork(n, m):
    if n<=0 or m <= 0:
        return 0
    return n * m

def hero(bullets, dragons):
    if bullets*0.5>=dragons:
        return True
    return False

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))"""

# def litres(time):
#     return time // 2
#
# def lovefunc( flower1, flower2 ):
#     if flower1 % 2 ==0 and flower2 % !=0 or flower1 %2 !=0 and flower2 % 2 ==0:
#         return True
#     return False
#
# def find_needle(haystack=list):
#     if "needle" in haystack:
#         c = haystack.index("needle")
#         return f"found the needle at position {c}"
#     return c
#
# def odd_or_even(arr=[]):
#     if sum(arr)%2==0:
#         return "even"
#     return "odd"
#
# def rps(p1, p2):
#     a = {
#         "rock": "scissors",
#         "scissors": "paper",
#         "paper": "rock"
#     }
#     if p1 == p2:
#         return "Draw!"
#     for i,j in a.items():
#         if p1 == i and p2 == j:
#             return "Player 1 won!"
#         if p2 == i and p1 == j:
#             return "Player 2 won!"
#
#
# def format_duration(seconds):
#     sec = 0
#     minut = 0
#     hour = 0
#     days = 0
#     if seconds == 0:
#         return "now"
#     sec = seconds
#     sec = sec%60
#     minut = sec//60
#     minut = sec%60
#     hour = minut//60
#     hour = minut%60
#     days = hour//60
#     if sec != 0 and minut != 0 and hour !=0 and days !=0:
#         return f'{days} days, {hour} hour, {minut} minutes and {sec} seconds'




