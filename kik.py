matrix = [
    [100, 100, 0, 0] ,
    [0, 0, 150, 0],
    [0, 0, 10, 140]
]
start_points = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 3), (2, 4)]


FLAG_END = False


def find_cycle(mat: list, pos: tuple, dir_row: bool = True, path: list = None) -> list:
    """ Построение цикла опорного плана транспортной задачи.
        При условии, что цикл существует и он единственный.
    """
    global FLAG_END

    if not path:
        path = [pos]
    ii, jj = pos
    # Собираем сначала соседей по строке, потом через раз на повороте.
    if dir_row:
        neighbors = [(ii, k) for k in range(len(mat[0])) if k != jj and mat[ii][k]]
    # Собираем соседей по столбцу на каждом втором повороте.
    else:
        neighbors = [(k, jj) for k in range(len(mat)) if k != ii and mat[k][jj]]
    # Если есть соседи:
    if neighbors:
        # Если стартовая точка есть в списке соседей - путь найден!
        if start_point in neighbors:
            FLAG_END = True
            return path
        else:
            # Меняем направление для поворота.
            dir_row = not dir_row
            # Перебираем всех соседей.
            for neighbor in neighbors:
                # Кладем очередную вершину в список пути.
                path.append(neighbor)
                # Запускаем рекурсию по ненулевым соседям.
                find_cycle(mat, neighbor, dir_row, path)
                # Если нашли путь дальше не перебираем.
                if FLAG_END:
                    break
                # Если путь не найден, то удаляем вершину из списка пути.
                else:
                    path.pop()
    return path

# for start_point in start_points:
start_point  = (2, 1)
i, j = (2,1)
matrix[i][j] = -1
way = find_cycle(matrix, (2,1))
matrix[i][j] = 0
FLAG_END = False
print(way)

# --------------------------------------

#  [(0, 1), (0, 0), (2, 0), (2, 1)]
# [(0, 2), (0, 0), (2, 0), (2, 2)]
# [(0, 3), (0, 0), (2, 0), (2, 3)]
# [(0, 4), (0, 0), (2, 0), (2, 1), (1, 1), (1, 4)]
# [(1, 0), (1, 1), (2, 1), (2, 0)]
# [(1, 2), (1, 1), (2, 1), (2, 2)]
# [(1, 3), (1, 1), (2, 1), (2, 3)]
# [(2, 4), (2, 1), (1, 1), (1, 4)]