import numpy as np

n, m = list(map(int, input().split()))
j = np.array([list(map(int, input().split())) for _ in range (n)])

print(np.mean(j, axis = 1))
print(np.var(j, axis = 0))
print(round(np.std(j, axis = None), 11))
