def solveTrans(c, A, B):
    result_dict = {"starting_array": c, "price_A": A, "price_B": B}

    # Ensure supplies and demands are balanced
    if sum(A) != sum(B):
        if sum(A) < sum(B):
            A.append(sum(B) - sum(A))
            c.append([0] * len(B))
        else:
            B.append(sum(A) - sum(B))
            for row in c:
                row.append(0)

    print("\nA:", A)
    print("B:", B)
    print("Starting array:")
    for row in c:
        print(row)
    print("")

    # Initialize variables
    supply = A[:]
    demand = B[:]
    allocation = [["X" for _ in row] for row in c]

    # Start at the top-left (North-West corner) of the cost matrix
    i, j = 0, 0

    while i < len(supply) and j < len(demand):
        # Allocate shipments from the current cell as much as possible
        quantity = min(supply[i], demand[j])
        allocation[i][j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity

        # Move horizontally or vertically to the next unallocated cell
        if supply[i] == 0:
            i += 1
        else:
            j += 1

    result_dict["initial_allocation"] = allocation

    # Fix initial allocation by replacing 'X' with 0 where needed
    for i in range(len(A)):
        for j in range(len(B)):
            if allocation[i][j] == 'X':
                allocation[i][j] = 0
                break

    # Print initial allocation
    print("Initial allocation:")
    for row in allocation:
        print(row)

    # Calculate potentials
    pot_A = [0] * len(A)
    pot_B = [0] * len(B)
    pot_A[0] = 0  # Arbitrarily set one potential to zero

    for i in range(len(A)):
        for j in range(len(B)):
            if allocation[i][j] != 0:
                pot_B[j] = c[i][j] - pot_A[i]

    # Update potentials to satisfy the balance equations
    for i in range(len(A)):
        for j in range(len(B)):
            if allocation[i][j] == 0:
                pot_A[i] = c[i][j] - pot_B[j]

    result_dict["potentials"] = {"A": pot_A, "B": pot_B}

    # Print potentials
    print("Potentials for A:", pot_A)
    print("Potentials for B:", pot_B)

    return result_dict


# Example usage
c = [[12, 15, 21, 14],
     [14, 8, 15, 11],
     [19, 16, 26, 12]]

A = [200, 150, 160]
B = [100, 100, 160, 140]

result = solveTrans(c, A, B)
