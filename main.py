from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10,0,1,2,3,4,5])
y = np.array([2,3,4,5,6,7,8,9,10,11,1,2,3,4,5,6])

distance, path = fastdtw(x, y, dist=euclidean)

print(distance)
print(path)
