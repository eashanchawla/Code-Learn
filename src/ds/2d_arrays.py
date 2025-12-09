matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

import numpy as np
from collections import defaultdict

def transpose(matrix):
    # return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    return np.array([list(col) for col in zip(*matrix)])


def rotate_90(matrix, clockwise=True):
    if clockwise:
        return np.array([list(reversed(col)) for col in zip(*matrix)])
    else:
        return np.array([list(col) for col in zip(*matrix)][::-1])

def spiral_traversal(matrix):
    top=0
    bottom=len(matrix)-1
    left=0
    right=len(matrix[0])-1
    traversal_list = []
    while top<=bottom and left<=right:
        # left to right move first
        for i in range(left, right+1):
            traversal_list.append(matrix[top][i])
        top+=1
        for i in range(top, bottom+1):
            traversal_list.append(matrix[i][right])
        right-=1
        if left <= right and top <= bottom:
            for i in range(right, left-1, -1):
                traversal_list.append(matrix[bottom][i])
            bottom-=1 

        if top <= bottom and left<=right:
            for i in range(bottom, top-1, -1):
                traversal_list.append(matrix[i][left])
            left+=1
    return [traversal_list]

expected_diagonal_answer = [[1,2,4,7,5,3,6,8,9]]

def diagonal_traverse(matrix):
    # identifying lines where the sum of x,y co-ords is the same. they are all on the same diagonal

    sum_dict = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum_dict[i+j].append(matrix[i][j])
                
    final_list = []
    for i in sum_dict.keys():
        final_list.extend(sum_dict[i][::-1]) if i%2==0 else final_list.extend(sum_dict[i])
    return [final_list]      

def display_matrix(matrix, title):
    print(f"{title}:\n{'-' * len(title)}")
    for row in matrix:
        print(" ".join(map(str, row)))
    print()


matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

display_matrix(matrix, "Original Matrix")
display_matrix(transpose(matrix), "Transpose")
display_matrix(rotate_90(matrix), "Rotate Clockwise")
display_matrix(rotate_90(matrix, False), "Rotate Anti-clockwise")
display_matrix(spiral_traversal(matrix), "Spiral Traversal")
display_matrix(diagonal_traverse(matrix), "Diagonal Traversal")

def pascals_triangle(num_rows=5):
    pascal_list = [[1]]
    for current_row in range(1, num_rows):
        starting_list = [0] + pascal_list[current_row-1] + [0]
        generated_list = [a+b for a, b in zip(starting_list, starting_list[1:])]
        # generated_list = [starting_list[i]+starting_list[i-1] for i in range(1, len(starting_list))]
        pascal_list.append(generated_list)
    print(pascal_list)

pascals_triangle(5)