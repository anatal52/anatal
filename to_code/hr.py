arr2d = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

# 0,0 0,1 0,2
# 1,1
# 2,0 2,1 2,2


def hg(arr2d):
    hg = {}
    for i in range(4):
        for j in range(4):
            hg[(i,j)] = arr2d[i][j]+arr2d[i][j+1]+arr2d[i][j+2]+arr2d[i+1][j+1]+arr2d[i+2][j]+arr2d[i+2][j+1]+arr2d[i+2][j+2]

    return max(hg.values())


hg(arr2d)
