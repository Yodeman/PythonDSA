def find_boyer_moore(T, P):
    """Return the lowest index of T at hich substring P begins else -1.."""
    n,m = len(T), len(P)
    if m == 0:
        # empty string
        return 0
    last = {}
    for k in range(m):
        # last occurrence of a letter
        last[P[k]]=k
    # start from the back - Looking glass heuristic
    i = m-1
    k = m-1
    while i < n:
        if T[i]==P[k]:
            # matching character
            if k==0:
                # pattern begins at index i of text
                return i
            else:
                # examine previous character
                i -= 1
                k -= 1
        else:
            # character jump heuristic
            j = last.get(T[i], -1)
            i += m - min(k, j+1)
            k = m-1
    return -1