n = int(input())
namespaces = {
    'global': {'parent': None, 'vars': set()}
}

for _ in range(n):
    print(namespaces)
    parts = input().split()
    cmd = parts[0]
    
    if cmd == 'create':
        namespace, parent = parts[1], parts[2]
        namespaces[namespace] = {'parent': parent, 'vars': set()}
    elif cmd == 'add':
        namespace, var = parts[1], parts[2]
        if namespace in namespaces:
            namespaces[namespace]['vars'].add(var)
    elif cmd == 'get':
        namespace, var = parts[1], parts[2]
       # current = namespace
        result = None
        while namespace in namespaces:
            if var in namespaces[namespace]['vars']:
                result = namespace
                break
            namespace = namespaces[namespace]['parent']
        print(result if result is not None else 'None')