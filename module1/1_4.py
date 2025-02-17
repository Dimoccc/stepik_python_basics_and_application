# put your python code here

n = int(input()) # amount of iterations

parent = {"global": None} #dict of parents: nested namespaces (who is inclosed in whom)
variables = {"global": set()} #dic with namespaces and all variables in it

data = [] #data to collect all inputs, the list of lists

for i in range(n):
    str_of_data = input().split()

    data.append(str_of_data)

for value in data:
    do = value[0]
    belongs_to = value[1]
    var_or_space = value[2]
    if do == "create":
        parent[belongs_to] = var_or_space
        variables[belongs_to] = set()
        print('parent ', parent)
        print('variables ', variables)
        print("+++++++++++++++++++++++++++++++++++")
    elif do == "add":
        variables[belongs_to].add(var_or_space)
        print("+++++++++++++++++++++++++++++++++++")
        print('variables ', variables)
    elif do == "get":
        while belongs_to is not None:
            if var_or_space in variables[belongs_to]:
                print("+++++++++++++++++++++++++++++++++++")
                print('belongs_to ',belongs_to)
                break
            belongs_to = parent[belongs_to]
        print('belongs_to ',belongs_to)