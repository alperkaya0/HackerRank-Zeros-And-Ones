import numpy as np

inp = input()

inp = inp.split(" ")

temp = []

for x in range(len(inp)):
    inp[x] = int(inp[x])
    temp.append(inp[x])    

print(np.zeros(temp,dtype = np.int))
print(np.ones(temp,dtype = np.int))
