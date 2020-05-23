#How to calculate the dot product
def addDotProd(arr1, arr2):
    resList = []
    total = 0
    for i in range(0, len(arr1)):
        resList.append(arr1[i] * arr2[i])
    for i in resList:
        total += i
    return total

print(addDotProd([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, -3, 0, -5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] , [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, -3, 0, -5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] )) 