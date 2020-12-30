def fact(n, m={}):
    if n == 0 or n == 1:
        m[n] = 1
        return m[n]
    if n not in m:
        m[n] = n*fact(n-1)
    return m[n]
