def find_cycle(mat: list, pos: tuple, dir_row: bool = True, path: list = None, visited: set = None) -> list:
    """ Построение цикла опорного плана транспортной задачи.
        При условии, что цикл существует и он единственный.
    """
    if not path:
        path = [pos]
    if not visited:
        visited = set()
    ii, jj = pos
    print("Current position:", pos)
    # Собираем сначала соседей по строке, потом через раз на повороте.
    if dir_row:
        neighbors = [(ii, k) for k in range(len(mat[0])) if k != jj and mat[ii][k] != 'X']
    # Собираем соседей по столбцу на каждом втором повороте.
    else:
        neighbors = [(k, jj) for k in range(len(mat)) if k != ii and mat[k][jj] != 'X']
    print("Neighbors:", neighbors)
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
                    print("Exploring neighbor:", neighbor)
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



# Corrected example matrix representing transportation costs with a cycle
# example_matrix_with_cycle = [
#     [0, 10, 20],
#     [15, 5, 25],  # Changed 0 to 5 to ensure a valid cycle
#     [25, 30, 0]
# ]

example_matrix_with_cycle = [
    [100, 100, 0, 'X', 'X'],
    ['X', 'X', 150, 'X', 'X'],
    ['X', 0, 10, 140, 10]
]

# Choose a starting position (for example, (0, 1))
start_position_with_cycle = (2, 1)

# Initialize global flag
# FLAG_END = False

# Find the cycle in the corrected example matrix with a cycle
cycle_with_cycle = find_cycle(example_matrix_with_cycle, start_position_with_cycle)

# Print the resulting cycle
print("Cycle:", cycle_with_cycle)



# # Corrected example matrix representing transportation costs with a cycle
# example_matrix_with_cycle = [
#     [0, 10, 20],
#     [15, 5, 25],  # Changed 0 to 5 to ensure a valid cycle
#     [25, 30, 0]
# ]

# # Choose a starting position (for example, (0, 1))
# start_position_with_cycle = (0, 1)

# # Initialize global flag
# FLAG_END = False

# # Find the cycle in the corrected example matrix with a cycle
# cycle_with_cycle = find_cycle(example_matrix_with_cycle, start_position_with_cycle)

# # Print the resulting cycle
# print("Cycle:", cycle_with_cycle)

# def find_cycle(mat: list, pos: tuple, dir_row: bool = True, path: list = None, visited: set = None) -> list:
#     if not path:
#         path = [pos]
#     if not visited:
#         visited = set()
#     ii, jj = pos
#     print("Current position:", pos)
#     if dir_row:
#         neighbors = [(ii, k) for k in range(len(mat[0])) if k != jj and mat[ii][k] != 'X']
#     else:
#         neighbors = [(k, jj) for k in range(len(mat)) if k != ii and mat[k][jj] != 'X']
#     print("Neighbors:", neighbors)
#     if neighbors:
#         if path[0] in neighbors and len(path) > 2:
#             path.append(path[0])  # Add the starting position to the end of the path to complete the cycle
#             return path
#         else:
#             for neighbor in neighbors:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     print("Exploring neighbor:", neighbor)
#                     path.append(neighbor)
#                     result = find_cycle(mat, neighbor, not dir_row, path, visited)
#                     if result:
#                         return result
#                     else:
#                         path.pop()
#                         visited.remove(neighbor)
#     return None



# Define a matrix
# matrix = [
#     [0, 1, 1, 0],
#     [1, 0, 1, 0],
#     [1, 1, 0, 0],
#     [0, 0, 0, 0]
# ]

# matrix = [
#     [100, 100, 0, 'X', 'X'],
#     ['X', 'X', 150, 'X', 'X'],
#     ['X', 'X', 10, 140, 10]
# ]

# # Call the function and print the result
# cycle = find_cycle(matrix, (2, 1))
# print("Cycle:", cycle)
