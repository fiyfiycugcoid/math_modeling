import numpy as np
N = 4
M = 6

dlya_osobo_odaryennyx = np.zeros ((N, M))

for i in range(N):
    for j in range(M):
        if j>0 and i>0:
            dlya_osobo_odaryennyx [i, j] = np.sin(N * i + M * j)
        else:
            dlya_osobo_odaryennyx [i, j] = np.sin(N * (i+1) + M * (j + 1))

for i in range(N):
    for j in range(M):
        if dlya_osobo_odaryennyx [i, j] < 0:
            dlya_osobo_odaryennyx[i, j] = 0

print(dlya_osobo_odaryennyx)