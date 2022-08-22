def solution(A):
    count = 0
    myDict = {}
    myDict[1] = True
    myDict[0] = False

    next = None
    # first element value
    val = myDict[A[0]]
    if val == True:
        next = False
    else:
        next = True

    for element in A[1:]:
        if next != myDict[element]:
            count += 1
            # do something to update element
            myDict[element] = next
        if myDict[element] == True:
            next = False
        else:
            next = True

    print(count)
    return count

C = 1,1,1,1,1,1
solution(C)