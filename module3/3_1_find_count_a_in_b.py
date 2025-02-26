a,b = input(), input()
counter = 0
for i in range(len(a)):
    if a.find(b,i,i+ len(b))>=0:
        counter +=1
print(counter)