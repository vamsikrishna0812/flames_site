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
    f = { 1 : "F",
          2 : "L",
          3 : "A",
          4 : "M",
          5 : "E",
          6 : "S"
        }
    if c <= 6:
        return f[c]
    else:
        return f[(c % 6)]
    