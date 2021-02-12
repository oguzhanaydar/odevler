def sıfırıoynat=(array):
    new = []
    zeros = []
    
    for i in range(len(array)):
        if array[i] == 0 or array[i] == 0.0:
            if type(array[i]) == int or type(array[i]) == float:
                zeros.append(array[i])
            else: new.append(array[i])
        else:
            new.append(array[i])
    
    return new + zeros
print(sıfırıoynat([1,2,0,1,0,1,0,3,0,1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
print(sıfırıoynat([0,1,None,2,False,1,0]), [1, None, 2, False, 1, 0, 0])