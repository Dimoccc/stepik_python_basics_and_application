def mod_checker(x, mod=0):
    return lambda y, x=x, mod=mod: y % x == mod

# def mod_checker(x, mod=0):
#     def mod_n(y, x=x, mod=mod):  # Фиксируем x и mod через аргументы по умолчанию
#         return y % x == mod
#     return mod_n

mod_3 = mod_checker(3)
print(mod_3(3))  # True
print(mod_3(4))  # False