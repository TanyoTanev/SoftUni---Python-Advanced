'''3. Diagonals
Using nested list comprehension write a program that reads NxN matrix, finds its diagonals, prints them and their
sum as shown below.
'''

'''N = int(input())
matrix = []
diagonal_main = []
diagonal_second = []

def matrix_diagonals(matrix):# diagonal_main, diagonal_second ):
    

    for row in range(len(matrix)):
        
            diagonal_main.append(matrix[row][row])
            diagonal_second.append(matrix[row][len(matrix)-row-1])

    return diagonal_main, diagonal_second

for _ in range(N):
    matrix.append(list(map(int, input().split(', '))))

diagonals = matrix_diagonals(matrix)
print(sum(diagonals[0]))
print(diagonals[1])'''

N = int(input())
matrix = []
diagonal_main = []
diagonal_second = []

matrix = [list(map(int, input().split(', '))) for _ in range(N)]


diagonal_main = [ matrix[row][row] for row in range(len(matrix))]
diagonal_second = [(matrix[row][len(matrix) - row - 1]) for row in range(len(matrix))]

print(f"First diagonal: {', '.join([str(x) for x in diagonal_main])}. Sum: {sum(diagonal_main)}")
print(f"Second diagonal: {', '.join([str(x) for x in diagonal_second])}. Sum: {sum(diagonal_second)}")