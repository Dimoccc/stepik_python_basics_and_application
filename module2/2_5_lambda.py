x = [
    ("Guido","van","Rosum"),
    ("Hsakell","Curry"),
    ("John","Backus")
]

# def length(name):
#     return len(" ".join(name))

# name_lengths = [length(name) for name in x]
# print(name_lengths)

# x.sort(key=length)
# print(x)

x.sort(key = lambda name: len(" ".join(name)))
print(x)