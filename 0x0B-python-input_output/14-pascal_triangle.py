#!/usr/bin/python3
def pascal_triangle(n):
    """
        function that returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    my_list = []
    if n <= 0:
        return my_list
    elif n == 1:
        return my_list[[1]]
    else:
        my_list = [[1], [1, 1]]
        for i in range(1, n - 1):
            tmp = [1]
            for j in range(0, len(my_list[i]) - 1):
                tmp.extend([my_list[i][j] + my_list[i][j + 1]])
            my_list.append(tmp)
            tmp += [1]
    return my_list
