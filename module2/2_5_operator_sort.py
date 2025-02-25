import operator as op

print(op.add(4,5))
print(op.mul(4,5))
print(op.contains([1,2,3,4],5))

x = [1,2,3]
f = op.itemgetter(1)
print(f(x))

y = {"123":3}
fa =op.itemgetter("123")
print(fa(y))

FIO = [
    ("Guido","van","Rosum"),
    ("Hsakell","Curry"),
    ("John","Backus")
]

FIO.sort(key=op.itemgetter(-1))
print(FIO)