NO_OF_CHARS = 128
def shift_table(pat):
    m = len(pat)
    tbl = [m]*NO_OF_CHARS

    for i in range(m-1):
        tbl[ord(pat[i])] = m-1-i

    return tbl
def search_horspool(T, P):
    m = len(P)
    n = len(t)
    t = shift_table(P)
    i = m-1
    while(i <= n-1):
        k = 0
        while k <= m-1 and P[m-1-k]==T[i-k]:
            k +=1
            if k == m:
                return i-m+1
            else :
                tc = t[ord(T[i-k])]
                i += (tc-k)
    return -1

NO_OF_CHARS = 128
def shift_table(pat):
    m = len(pat)
    tbl = [m]*NO_OF_CHARS

    for i in range(m-1):
        tbl[ord(pat[i])] = m-1-i

    return tbl
print("패턴의 위치:", search_horspool("APPLEMANGOBANANAGRAPE", "BANANA"))