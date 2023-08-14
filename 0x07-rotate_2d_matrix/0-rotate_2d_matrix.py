#!/usr/bin/python3

''' Rotation of n X n 2D Matrix(90 degrees clockwise) '''

def rotate_2d_matrix (matrix):
    ''' Rotates in place '''
    a = len(matrix)
    arrange = []

    for b in range(a):
        for c in range(a-1,-1,-1):
            arrange.append(matrix[c][b])

        for b in range(a):
            for c in range (a):
                matrix[b][c] = arrange.pop(0)
