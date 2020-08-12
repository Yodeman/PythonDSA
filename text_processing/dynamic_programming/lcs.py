def LCS(X, Y):
    """Return table such that L[j][k] is length of LCS for X[0:j] and Y[0:k]."""
    n,m = len(X), len(Y)
    L = [[0]*(m+1) for k in range(n+1)]
    for j in range(n):
        for k in range(m):
            if X[j]==Y[k]:
                L[j+1][k+1]=L[j][k]+1
            else:
                L[j+1][k+1]=max(L[j][k+1], L[j+1][k])
    return L

def LCS_Solution(X, Y, L):
    """Return the longest common substring of X and Y, given LCS table."""
    solution = []
    j, k = len(X), len(Y)
    while L[j][k] > 0:
        if X[j-1]==Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] >= L[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ' '.join(reversed(solution))

if __name__ == "__main__":
    X = "skullandbones"
    Y = "lullabybabies"
    L = LCS(X, Y)
    print(L)
    lcs = LCS_Solution(X, Y, L)
    print(lcs)