#100% taken from this stackoverflowpost:
#http://stackoverflow.com/questions/8663079/maximum-rectangle-algorithm-implementation


from collections import namedtuple

Point = namedtuple('Point', ('X', 'Y'))

#Y      0  1  2      X
arr = [[0, 0, 0, ], #0
       [1, 0, 0, ], #1
       [0, 0, 1, ], #2
       ]

def area(ll, ur):
    if (ll.X < 0) or (ll.Y < 0) or (ur.X < 0) or (ur.Y < 0):
        return 0.
    return ((ur.X - ll.X) + 1) * ((ur.Y - ll.Y) + 1)

def update_cache(a, c, x):
    M = len(a[0])
    N = len(a)
    for y in range(M):
        if a[x][y] == 0:
            c[y] = c[y] + 1
        else:
            c[y] = 0

def mrp(a):
    best_ll = Point(-1, -1)
    best_ur = Point(-1, -1)
    M = len(a[0]) 
    N = len(a)
    c = [0 for x in range(M + 1)]
    stack = []
    for x in range(N-1, -1, -1):

        update_cache(a, c, x)        
        width = 0
        for y in range(M + 1):
            if c[y] > width:
                stack.append((y, width))                
                width = c[y]
            if c[y] < width:
                while stack:
                    y0, w0 = stack.pop()
                    if (width * (y - y0)) > area(best_ll, best_ur):
                        best_ll = Point(x, y0)
                        best_ur = Point(x + width - 1, y - 1)
                    width = w0
                    if (c[y] >= width):
                        break
                width = c[y] 
                if width == 0:
                    stack.append((y0, w0))
    return best_ll, best_ur
