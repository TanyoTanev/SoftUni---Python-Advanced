'''2.2x2 Squares in Matrix
Find the count of 2 x 2 squares of equal chars in a matrix.
Input
 On the first line, you are given the integers rows and cols - the matrix's dimensions
 Matrix characters come at the next rows lines (space separated)
'''
#matrix = [

#['A', 'B', 'B', 'D'],
#['E', 'B', 'B', 'B'],
#['I', 'J', 'B', 'B']

#]
#print(matrix)

def matrix_create():
    (rows, cols) = map(int, input().split(' '))
    matrix = []
    for row in range(rows):
        matrix.append([])
        matrix[-1] = list(input().split(' '))
    #print(matrix)
    return matrix





def matrix_find_eq_chars(matrix):
    equals_count = 0
    for row in range(len(matrix)-1):
        for column in range(len(matrix[row])):
            if column+1 < len(matrix[row]) and row+1 < len(matrix):
              if matrix[row][column] == matrix[row][column+1] == matrix[row+1][column] == matrix[row+1][column+1]:
                equals_count +=1
    #if equals_count == 0:
        #print('No 2 x 2 squares of equal cells exist.')
    #else:
    print(equals_count)


matrix = matrix_create()
matrix_find_eq_chars(matrix)

