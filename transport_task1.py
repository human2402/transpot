FLAG_END = False
"""def find_cycle(mat: list, pos: tuple, dir_row: bool = True, path: list = None) -> list:
    # Построение цикла опорного плана транспортной задачи.
    # При условии, что цикл существует и он единственный.
    
    global FLAG_END

    if not path:
        path = [pos]
    ii, jj = pos
    if dir_row:
        neighbors = [(ii, k) for k in range(len(mat[0])) if k != jj and mat[ii][k]]
    else:
        neighbors = [(k, jj) for k in range(len(mat)) if k != ii and mat[k][jj]]
    if neighbors:
        if start_point in neighbors:
            FLAG_END = True
            return path
        else:
            dir_row = not dir_row
            for neighbor in neighbors:
                path.append(neighbor)
                find_cycle(mat, neighbor, dir_row, path)
                if FLAG_END:
                    break
                else:
                    path.pop()
    return path """


c = [[7, 3, 6],
    [4, 8, 3],
    [2, 5, 9]]

A = [75, 40, 35]
B = [55, 45, 50]

#уравниваем поставщиков и покупателей
if not(sum(A) == sum(B)):
    if sum(A) < sum(B):
        A.append(sum(B)- sum(A))
        nl = []
        for i in B:
            nl.append(0)
        c.append(nl)
    else:
        B.append(sum(A)- sum(B))
        for i in c:
            i.append(0)

# print (sum(A) , sum(B))

# print ('a' != 'a')
# \print (a, b)
for i in c:
    print (i)

isNotOk = True
while isNotOk:
    local_a, local_b = [], []
    for i in A:
        local_a.append(i)
    for i in B:
        local_b.append(i)
    sol_list = []
    # for line in local_a:
    #     new_line = []
    #     for col in local_b:
    #         new_cel = min (col, line)
    #         print (line, col, new_cel)
    #         new_line.append(new_cel)
    #         col = col - new_cel
    #         line = line - new_cel
            
    #         # if line <= 0:
    #         #     break
    #     sol_list.append(new_line)

    #считаем по северу
    ZERO_FLAG = False
    for line in range (len(local_a)):
        new_line = []
        for col in range (len(local_b)):
            # if local_a[line] == 0 or local_b[col] == 0:
            #     if new_line[-1] == 0:
            #         pass
            #     else:
            #         new_line.append("x")\
            
            if local_a[line] == 0 :
                if new_line[-1] == 0 and ZERO_FLAG:
                    pass
                    ZERO_FLAG = False
                else:
                    new_line.append("x")
                    
            elif local_b[col] == 0:
                new_line.append("x")
            
            else:
                new_cel = min (local_a[line], local_b[col])
                #print (local_a[line], local_b[col], new_cel)
            # print (A, B)
                new_line.append(new_cel)
                if local_a[line] == local_b[col] and col != len(local_b)-1:
                    new_line.append(0)  
                    ZERO_FLAG = True
                    local_b[col-1] = local_b[col-1] - new_cel
                    local_a[line] = local_a[line] - new_cel
                else:
                    local_b[col] = local_b[col] - new_cel
                    local_a[line] = local_a[line] - new_cel
                
                # if line <= 0:
                #     break
        sol_list.append(new_line) 

        print ("kek k", B)
        print ("kek k", local_b)
        for i in range(len(sol_list)):
            print (A[i], local_a[i], sol_list[i], )

    
    #вводим потанцевалы
    potencial_a,potencial_b = [], []
    for i in A:
        potencial_a.append('x')
    for i in B:
        potencial_b.append('x')
    
    for line in range (len(local_a)):
        if line == 0:
            potencial_a[line] = 0
        
        for col in range (len(local_b)):
            
            if sol_list[line][col] != 'x':
                if potencial_b[col] != 'x':
                    potencial_a[line] = (c[line][col]-potencial_b[col] )
                #dprint (sol_list[line][col],potencial_a[line] , c[line][col])
                
                new_pot = ( c[line][col]- potencial_a[line])
                potencial_b[col]=new_pot

                # print ("kek k", B)
                # print ("kek k", local_b)
                # for i in range(len(sol_list)):
                #     print (A[i], local_a[i], sol_list[i], potencial_a[i])

                # print ("kek k", potencial_b)

                
    #считаем несходление
    dif = []
    gratest_pos = (0,0)
    gratest_dif = 0
    for i in A:
        nl = []
        for i in B:
            nl.append('x')
        dif.append(nl)

    for line in range (len(local_a)):
        for col in range (len(local_b)):
            #print (potencial_a[line][col] , potencial_b[line][col], c[line][col])
            dif_pot = (potencial_a[line] + potencial_b[col]) - c[line][col]
            if dif_pot > 0:
                dif[line][col] = dif_pot
                if dif_pot>gratest_dif:
                    gratest_dif = dif_pot
                    gratest_pos = (line, col)

    for i in dif:
        print (i)

    # i, j = gratest_pos
    # sol_list[i][j] = -1
    # way = find_cycle(sol_list, gratest_pos)
    # sol_list[i][j] = 0
    # FLAG_END = False

    isNotOk = False
    
    print ("kek k", B)
    print ("kek k", local_b)
    for i in range(len(sol_list)):
        print (A[i], local_a[i], sol_list[i], potencial_a[i])

    print ("kek k", potencial_b)

# print (a, b)


    
