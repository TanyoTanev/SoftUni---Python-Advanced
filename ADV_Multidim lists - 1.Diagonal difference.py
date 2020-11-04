'''1.Diagonal Difference
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).

On the first line, you are given the integer N - the size of the square matrix
 The next N lines hold the values for every row - N numbers separated by a space
'''

def matrix_create():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split(' '))))

    #print(matrix)
    return matrix

#n = 3
    #matrix = [

     # [11, 2, 4],
     # [4, 5, 6],`
     # [10, 8, -12]

      #     ]



def matrix_solve(matrix):
    prime_diagonal = 0
    second_diagonal = 0
    n=len(matrix)
    for i in range(len(matrix)):
        prime_diagonal +=matrix[i][i]
        second_diagonal = second_diagonal + matrix[n-1-i][i]
    return print(abs(prime_diagonal-second_diagonal))
    #print(prime_diagonal)
    #print(second_diagonal)

matrix_solve(matrix_create())
