def find_cycle(mat: list, pos: tuple, dir_row: bool = True, path: list = None, visited: set = None) -> list:
    """ Построение цикла опорного плана транспортной задачи.
        При условии, что цикл существует и он единственный.
    """
    if not path:
        path = [pos]
    if not visited:
        visited = set()
    ii, jj = pos
    # print("Current position:", pos)
    # Собираем сначала соседей по строке, потом через раз на повороте.
    if dir_row:
        neighbors = [(ii, k) for k in range(len(mat[0])) if k != jj and mat[ii][k] != 'X']
    # Собираем соседей по столбцу на каждом втором повороте.
    else:
        neighbors = [(k, jj) for k in range(len(mat)) if k != ii and mat[k][jj] != 'X']
    # print("Neighbors:", neighbors)
    # Если есть соседи:
    if neighbors:
        # Если стартовая точка есть в списке соседей - путь найден!
        if path[0] in neighbors and len(path) > 2:
            return path
        else:
            # Перебираем всех соседей.
            for neighbor in neighbors:
                if neighbor not in visited:  # Check if neighbor has not been visited
                    visited.add(neighbor)  # Mark neighbor as visited
                    # print("Exploring neighbor:", neighbor)
                    # Кладем очередную вершину в список пути.
                    path.append(neighbor)
                    # Запускаем рекурсию по ненулевым соседям.
                    result = find_cycle(mat, neighbor, not dir_row, path, visited)  # Flip direction for next exploration
                    # Если нашли путь дальше не перебираем.
                    if result:
                        return result
                    # Если путь не найден, то удаляем вершину из списка пути и помечаем как непосещенную.
                    else:
                        path.pop()
                        visited.remove(neighbor)
    return None

def getEmptyStringWithSameLength(stringie):
        new_string = ""
        for i in range(0, len(str(stringie))):
            new_string += "⠀"

        return new_string

def getLocalElement(arr):
    loc_al = []
    for row in arr:
        newLine = []
        for item in row:
            newLine.append(item)
        loc_al.append(newLine)
    return loc_al

def solveTask(c, A, B):


    # c = [[12, 15, 21, 14],
    #  [14, 8, 15, 11],
    #  [19, 6, 26, 12]]

    # A = [200, 150, 160]
    # B = [100, 100, 160, 140]
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

    result_dict = {
                "is_there_error": False,
                "starting_array": c,
                "price_A": A,
                "price_B": B,
                "ab_difference": balanced
                };
        
    
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

    print("used cells:", usedCellsCount, "| m+n-1:", supposedCellsCount)

    loc_al = getLocalElement(allocation)
    result_dict["first_plan"] = {
                "type": "base_plan",
                "array": loc_al,
                "a": A,
                "b": B,
                "busy_cells": usedCellsCount, 
                "m+n-1": supposedCellsCount
            }
    
    
    if isSupported:
        iterationCounter = 1
        isFine = False
        while isFine == False and iterationCounter < 10:
            

            print (" ")
            print (" ")
            print ("ITERATION:", iterationCounter)
            priceF = 0
            for i in range(len(allocation)):
                for j in range(len(allocation[i])):
                    if allocation[i][j] != 'X':
                        priceF += allocation[i][j]*c[i][j]
                        
            print (" ")
            print ("F:", priceF)
            print (" ")

            

            # Calculate potentials
            pot_A = ["X"] * len(A)
            pot_B = ["X"] * len(B)
            pot_A[0] = 0  # Arbitrarily set one potential to zero

            # потанцевалы
            for att in range(2):
                for i in range(0,len(pot_A)):
                    for j in range(0, len(pot_B)):
                        if allocation[i][j]  != "X":
                            if pot_A[i] != "X":
                                pot_B[j] = c[i][j] - pot_A[i]
                            else:
                                if pot_B[j] != "X":
                                    pot_A[i] = c[i][j] - pot_B[j]
                    print (i, j,c[i][j], pot_A, pot_B)
                
            result_dict["potentials"] = {"A": pot_A, "B": pot_B}

            loc_al = getLocalElement(allocation)
            result_dict["iteration_"+str(iterationCounter)] = {
                "type": "new_plan",
                "array": loc_al,
                "a": pot_A,
                "b": pot_B,
            }

            # Print potentials
            print("Potentials for A:", pot_A)
            print("Potentials for B:", pot_B)
            print (" ")

            # переплаты века
            overPrices = []
        
            for i in range(len(pot_A)):
                newLine = []
                for j in range(len(pot_B)):
                    if allocation[i][j] == "X":
                        overing = (pot_A[i] + pot_B[j]) - c[i][j]
                        # print (i, j, pot_A[i], pot_B[j], c[i][j], overing)
                        newLine.append(overing)
                    else:
                        newLine.append("X")
                overPrices.append(newLine)

            for row in overPrices:
                print (row)

            #ищем самую большую переплату
            greatest_pos = (0,0)
            greatest_overprice = -100

            for i in range(len(pot_A)):
                for j in range(len(pot_B)):
                    item = overPrices[i][j]
                    if item != "X":
                        if  item >= greatest_overprice:
                            greatest_pos = (i, j)
                            greatest_overprice = item
            
            print ("Max imbalance: ", greatest_overprice,"| its postion - ", greatest_pos)
            
            if greatest_overprice <= 0:
                isFine = True
            print (" ")
            print ("Is it final: ", isFine) 
            print (" ")
            
            result_dict["iteration_"+str(iterationCounter)]["_overprice"] = {
                "array": overPrices,
                "is_fine": isFine,
                "greatest_overprice": greatest_overprice,
                "greatest_pos": greatest_pos
            }

            #let us find the cycle
            if not isFine:
                localAlocation = allocation
                localAlocation[greatest_pos[0]][greatest_pos[1]] = 0
                cycle_with_cycle = find_cycle(localAlocation, greatest_pos)

                min_minus = 999999
                for i in range(1,len(cycle_with_cycle), 2):
                    elem = cycle_with_cycle[i]
                    if allocation[elem[0]][elem[1]] < min_minus:
                        min_minus = allocation[elem[0]][elem[1]]
                print("Cycle:", cycle_with_cycle)
                print ("Min element:", min_minus)

                result_dict["iteration_"+str(iterationCounter)]["_cycle"] = {
                    "cycle": cycle_with_cycle,
                    "min_element": min_minus
                }
            

                # let us have the allocation calculated
                for i in range(0,len(cycle_with_cycle)):
                    elem = cycle_with_cycle[i]
                    
                    if i%2 == 0:
                        if allocation[elem[0]][elem[1]] != "X":
                            allocation[elem[0]][elem[1]] += min_minus
                        else:
                            allocation[elem[0]][elem[1]] = min_minus
                    else:
                        allocation[elem[0]][elem[1]] -= min_minus
                        if (allocation[elem[0]][elem[1]]) <= 0:
                            allocation[elem[0]][elem[1]] = "X"

                print (" " )
                print ("New matrix: ")

                for i in allocation:
                    print (i) 
                iterationCounter += 1
                
                    
            else:
                result_dict["iteration_count"] = iterationCounter
                return result_dict            




    else:
        
        result_dict["is_there_error"] = True
        result_dict["error_message"] = "plan failed"
        return result_dict  
        
    # result_dict["initial_allocation"] = allocation
        






c = [[12, 15, 21, 14],
     [14, 8, 15, 11],
     [19, 6, 26, 12]]

A = [200, 150, 160]
B = [100, 100, 160, 140]

# print( solveTask(c, A, B))
