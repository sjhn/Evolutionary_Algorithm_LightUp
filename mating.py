import numpy as np
def mate (parent_a, parent_b):

    #print(parent_a[0][0])
    x=parent_a[0].shape[0]
    #print('shape',parent_a[0].shape)
    y=parent_a[0].shape[1]
    #print('1', parent_a)
    #print('2',parent_b)
    #print(type(parent_a))
    ar1=np.array(parent_a)[0][:][:x//2].astype(int)
    ar2=np.array(parent_b)[0][x//2:].astype(int)

    #print(x,y)
    #print(ar1.astype(int))
    #print(type(ar1))
    #print(ar1,ar2)
    child = np.concatenate((ar1,ar2),axis=0)
    #print('child')
    #print(child)
    return child