def find_kmp(T, P):
    """
    Return the lowest index of T at which substring P begins else -1,
    using knuth-morris-pratt algorithm
    """
    n, m = len(T), len(P)
    if m == 0:
        return 0
    fail = compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j]==P[k]:
            if k==m-1:
                return j-m+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1

def compute_kmp_fail(P):
    """Utility that computes and return KMP 'fail' list."""
    m = len(P)
    fail = [0]*m
    j = 1
    k = 0
    while j < m:
        if P[j]==P[k]:
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail