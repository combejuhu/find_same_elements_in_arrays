import numpy as np

array_one = np.array([5, 10, 6, 28, 19])

array_two = np.array( [19,28, 30])

for i in array_one:
  for j in array_two:
    if j == i:
        print (j)
