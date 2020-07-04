class Vector:
    """Represents a vector in a multidimensional space."""

    def __init__(self, d):
        self._coords = [0]*d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError ('dimension must agree')
        return [self[j]+other[j] for j in range(len(self))]

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '(' + str(self._coords)[1:-1] + ')'

if __name__ == "__main__":
    v = Vector(5)
    u = Vector(5)
    w = Vector(3)
    for i in range(5):
        v[i] = i+1
    for i in range(5):
        u[i] = i+5
    for i in range(3):
        w[i] = i+3
    z = v + u
    print('u=', u)
    print('v=', v)
    print('w=', w)
    print('z=', z)
    try:
        y = v + w
        print('y=', y)
    except Exception as e:
        print('cannot perform y=v+w,', end='  ')
        print(e)