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
    print("used cells:", usedCellsCount, "| m+n-1:", usedCellsCount)
    
    
    if isSupported:
        priceF = 0
        for i in range(len(allocation)):
            for j in range(len(allocation[i])):
                if allocation[i][j] != 'X':
                    priceF += allocation[i][j]*c[i][j]
                    
        print ("F:", priceF)

        # Calculate potentials
        pot_A = ["X"] * len(A)
        pot_B = ["X"] * len(B)
        pot_A[0] = 0  # Arbitrarily set one potential to zero

        # i, j = 0, 0
        # while i <= len(pot_A)-1 and j <= len(pot_B)-1:
        #     if allocation[i][j]  != "X":
        #         pot_B[j] = c[i][j] - pot_A[i]
        #     j+=1
        #     if j==len(pot_B):
                
        #         i+=1
        #     print (i, j, pot_A, pot_B)
            
            
        #     if j>len(pot_B): break

        for i in range(len(pot_A)):
            for j in range(len(pot_B)):
                if allocation[i][j]  != "X":
                    if pot_A[i] != "X":
                        pot_B[j] = c[i][j] - pot_A[i]
                    else:
                        pot_A[i] = c[i][j] - pot_B[j]
        
                print (i, j, pot_A, pot_B)
            
            
        #     if j>len(pot_B): break

        result_dict["potentials"] = {"A": pot_A, "B": pot_B}

        # Print potentials
        print("Potentials for A:", pot_A)
        print("Potentials for B:", pot_B)





    else:
        print("plan failed")
        
    # result_dict["initial_allocation"] = allocation
    






c = [[12, 15, 21, 14],
     [14, 8, 15, 11],
     [19, 16, 26, 12]]

A = [200, 150, 160]
B = [100, 100, 160, 140]

result = godPleaseWork(c, A, B)
