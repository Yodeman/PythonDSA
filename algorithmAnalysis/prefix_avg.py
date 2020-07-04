# Quadratic time algorithm.
# O(n**2)
def prefix_average1(S):
    """Return list such tha, for all j, A[j] equals average of S[0],...,S[j]."""
    n = len(S)  # O(1)
    A = [0]*n   # O(n)
    for j in range(n):      # O(n) - executes n times.
        total = 0
        for i in range(j+1):     # O(n**2) - since running depends on the outter loop.
            total += S[i]
        A[j] = total/(j+1)
    return A

# though shotter code but has same time complexity "O(n**2)"" as prefix_average1
def prefix_average2(S):
    n = len(S)
    A = [0]*n
    for j in range(n):
        A[j] = sum(S[0:j+1])/(j+1)
    return A

# Linear time algorithm.
def prefix_average3(S):
    n = len(S)  # O(1)
    A = [0]*n   # O(n)
    total = 0
    for j in range(n):      # O(n) - executes n times.
        total += S[j]
        A[j] = total/(j+1)
    return A

if __name__ == "__main__":
    from time import perf_counter
    import numpy as np

    S = list(np.array(np.random.randint(1,100,(1,1000)))[0])
    #print(S[:5])
    start_time = perf_counter()
    prefix_average2(S)
    print("Time: %f" %(perf_counter()-start_time))