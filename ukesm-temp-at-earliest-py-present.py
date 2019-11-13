import iris
import numpy as np

suites = np.array(['bc179','bc292','bc370','bb075','az513','az515','az524','bb277','bc470','bd288','bd416','bd483','bf647','bf656','bf703','bh162'])

base = '/nesi/project/niwa00013/williamsjh/afterburner/u-bm722/model_monitor2/nc/awmean/'


arr = []

for i in range(len(suites)):
    cubes = iris.load(base+suites[i]+'*')
    print('the global mean temperature of u-'+suites[i]+' is '+str(cubes[0].data[0]))
    arr.append(cubes[0].data[0])        


arr = np.array(arr)

inds = arr.argsort()


print('from low to high, the order of suite IDs is...')
print(suites[inds])

print('and their temperatures are...')
print(arr[inds])
