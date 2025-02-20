import itertools

def primes():
    x = 2
    while True:
        if not [i for i in range(2,x) if x % i==  0]:
            yield x
        x+=1

print(list(itertools.takewhile(lambda x : x <= 31, primes())))