import functools as ft
import operator as op

FIO = [
    ("Guido","van","Rosum"),
    ("Hsakell","Curry"),
    ("John","Backus")
]

x = int("1101", base = 2)
print(x)

int_2 = ft.partial(int, base = 2)
x = int_2("1101")
print(x)

sort_by_last = ft.partial(list.sort, key = op.itemgetter(-1))
print(FIO)
sort_by_last(FIO)
print(FIO)

y = ["abc","cba","abb"]
sort_by_last(y)
print(y)

