def flames_analyzer(n1, n2):
    n = list(n1) + list(n2)
    a = set(n1)
    b = set(n2)
    s = list(a & b)
    for i in s:
        if  i in n1 and n2 :
            for j in range (2):
                n.remove(i)
    c = len(n)
    f = ['F', 'L', 'A', 'M', 'E', 'S']
    
    while len(f) != 1 :
        if c % len(f) == 0:
            f.remove(f[-1])
        else:
            f.remove(f[(c % len(f) - 1)])
    return f[0]
    
