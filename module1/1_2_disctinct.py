objects = [1, 2, 1, 2, 3]

lst=[]
for i in objects:
    if not i in lst:
        lst.append(i)
print(len(lst))