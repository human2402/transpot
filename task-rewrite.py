def godPleaseWork(c, A, B):
    def getEmptyStringWithSameLength(stringie):
        new_string = ""
        for i in range(0, len(str(stringie))):
            new_string += "⠀"

        return new_string


    result_dict = {"starting_array": c, "price_A": A, "price_B": B}

    # Ensure supplies and demands are balanced
    balanced = 0
    if sum(A) != sum(B):
        if sum(A) < sum(B):
            newNum = sum(B) - sum(A)
            balanced = newNum
            A.append(newNum)
            c.append([0] * len(B))
        else:
            newNum = sum(A) - sum(B)
            balanced = newNum
            B.append(newNum)
            for row in c:
                row.append(0)
        
    
    print ("A:", A)
    print ("B:", B)
    for i in c:
        print (i)
    print ("supply, demand difference  = ", balanced)

    # Initialize variables
    supply = A[:]
    demand = B[:]
    allocation = [["X" for _ in row] for row in c]


    # Start at the top-left (North-West corner) of the cost matrix
    i, j = 0, 0

    while i < len(supply) and j < len(demand):
        # Allocate shipments from the current cell as much as possible
        if supply[i] != demand[j]:
            quantity = min(supply[i], demand[j])
            allocation[i][j] = quantity
            supply[i] -= quantity
            demand[j] -= quantity


            print (i, j)
            print (getEmptyStringWithSameLength(supply[-1]),demand)
            for ii in range(len(allocation)):
                print (supply[ii], allocation[ii])

            # Move horizontally or vertically to the next unallocated cell
            if supply[i] == 0:
                i += 1
            else:
                j += 1
        else:
            quantity = supply[i]
            allocation[i][j] = quantity
            supply[i] -= quantity
            demand[j] -= quantity
            if j+1 != len (allocation[i]):
                allocation[i][j+1] = 0

            j+=1            
    print (i, j)
    print (getEmptyStringWithSameLength(supply[-1]),demand)
    for ii in range(len(allocation)):
        print (supply[ii], allocation[ii])



    isSupported = False
    usedCellsCount = 0
    supposedCellsCount = len(A) + len (B) - 1
    for row in allocation:
        for item in row:
            if item != 'X':
                usedCellsCount += 1
    if usedCellsCount == supposedCellsCount:
        isSupported = True
    print("used cells: ", usedCellsCount, "m+n-1: ", usedCellsCount)
    if isSupported:
        print ("continue pls")
    else:
        print("plan failed")
        
    # result_dict["initial_allocation"] = allocation
    






c = [[12, 15, 21, 14],
     [14, 8, 15, 11],
     [19, 16, 26, 12]]

A = [200, 150, 160]
B = [100, 100, 160, 140]

result = godPleaseWork(c, A, B)
