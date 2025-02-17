dict = {} 

def find_cls(A, B):
    if A == B: 
        return True
    elif A in dict[B]:
        return True
    else:
        for C in dict[B]:
            if find_cls(A, C): 
                return True
        return False

for _ in range(int(input())): 
    inp = str(input()).split()
    dict.update({inp[0]: set(inp[2:])})

for _ in range(int(input())): 
    inp = str(input()).split()
    cls1, cls2 = inp[0], inp[1]
    if find_cls(cls1, cls2):
        print("Yes")
    else: print("No")