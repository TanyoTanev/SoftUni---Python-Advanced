'''7. *Bombs
You will be given a square matrix of integers, each integer separated by a single space, and each row on a new line.
Then on the last line of input you will receive indexes - coordinates to several cells separated by a single space, in
the following format: row1,column1 row2,column2 row3,column3…
On those cells there are bombs. You must detonate every bomb, one by one in the order they were given. When a
bomb explodes it deals damage equal to its own integer value, to all the cells around it (in every direction and in all
diagonals). One bomb can't explode more than once and after it does, its value becomes 0. When a cell&#39;s value
reaches 0 or below, it dies. Dead cells can't explode.
You must print the count of all alive cells and their sum. Afterwards, print the matrix with all its cells (including the
dead ones).
Input
 On the first line, you are given the integer N - the size of the square matrix.
 The next N lines holds the values for every row - N numbers separated by a space.
 On the last line you will receive the coordinates of the cells with the bombs in the format described
above.
Output
 On the first line you need to print the count of all alive cells in the format:
&quot;Alive cells: {aliveCells}&quot;
 On the second line you need to print the sum of all alive cell in the format:
&quot;Sum: {sumOfCells}&quot;
 In the end print the matrix. The cells must be separated by a single space.

Constraints
 The size of the matrix will be between [0…1000].
 The bomb coordinates will always be in the matrix.
 The bomb&#39;s values will always be greater than 0.
 The integers of the matrix will be in range [1…10000].
'''

def matrix_create():
  matrix = []
  number_rows = int(input())

  for row in range(number_rows):
    string = list(map(int,input().split(' ')))
    matrix.append(string)
  #print('the matrix')
  #for row in range(len(matrix)):
      #print(matrix[row])

  return matrix

def bombs_coordinates_read():
   bombs_coordinates = input().split(' ')
   for i in range(len(bombs_coordinates)):
       bombs_coordinates[i] = bombs_coordinates[i].split(',')
       bombs_coordinates[i][0] = int(bombs_coordinates[i][0])
       bombs_coordinates[i][1] = int(bombs_coordinates[i][1])

   return bombs_coordinates#, bombs_damage


def bombs_detonate(matrix, bombs_coordinates):#, boms_damage):
   explosion_value = 0
   cell_value = 0
   bomb_row = 0
   bomb_col = 0

   for i in range(len(bombs_coordinates)):
      bomb_row = bombs_coordinates[i][0]
      bomb_col = bombs_coordinates[i][1]
      damage = 0
      if matrix[bomb_row][bomb_col] > 0:

          explosion_value = matrix[bomb_row][bomb_col]#bombs_damage[i] #matrix[bomb_row][bomb_col]
          matrix[bomb_row][bomb_col] = 0



       #print(f"explosion value {explosion_value} number of bomb{i}")
          if bomb_row - 1 >= 0 and bomb_col - 1 >= 0 and int(matrix[bomb_row - 1][bomb_col - 1]) > 0:
           #damage = matrix[bomb_row - 1][bomb_col -1] - explosion_value
           matrix[bomb_row - 1][bomb_col - 1] = matrix[bomb_row - 1][bomb_col -1] - explosion_value
           #print(matrix[bomb_row - 1][bomb_col - 1])

          if bomb_col - 1 >= 0 and int(matrix[bomb_row][bomb_col - 1]):
           #damage   = matrix[bomb_row][bomb_col -1] - explosion_value
           matrix[bomb_row][bomb_col - 1] = matrix[bomb_row][bomb_col -1] - explosion_value
           #print(matrix[bomb_row][bomb_col - 1])

          if bomb_row + 1 < len(matrix) and bomb_col - 1 >= 0 and int(matrix[bomb_row + 1][bomb_col - 1]) > 0:
           #damage = matrix[bomb_row + 1][bomb_col - 1] - explosion_value
           matrix[bomb_row + 1][bomb_col - 1] = matrix[bomb_row + 1][bomb_col - 1] - explosion_value
           #print(matrix[bomb_row + 1][bomb_col - 1])

          if bomb_row + 1 < len(matrix) and int(matrix[bomb_row + 1][bomb_col]) > 0:
           #damage = matrix[bomb_row + 1][bomb_col] - explosion_value
           matrix[bomb_row + 1][bomb_col] = matrix[bomb_row + 1][bomb_col] - explosion_value
           #print(matrix[bomb_row + 1][bomb_col])

          if bomb_row - 1 >= 0 and int(matrix[bomb_row - 1][bomb_col]) > 0:
           #damage = matrix[bomb_row - 1][bomb_col] - explosion_value
           matrix[bomb_row - 1][bomb_col] = matrix[bomb_row - 1][bomb_col] - explosion_value
           #print(matrix[bomb_row - 1][bomb_col])

          if bomb_row - 1 >= 0 and bomb_col + 1 < len(matrix) and int(matrix[bomb_row - 1][bomb_col + 1]) > 0:
           #damage = matrix[bomb_row - 1][bomb_col + 1] - explosion_value
           matrix[bomb_row - 1][bomb_col + 1] = matrix[bomb_row - 1][bomb_col + 1] - explosion_value
           #print(matrix[bomb_row - 1][bomb_col + 1])

          if bomb_col + 1 < len(matrix) and int(matrix[bomb_row][bomb_col + 1]) > 0:
           #damage = matrix[bomb_row][bomb_col + 1] - explosion_value
           matrix[bomb_row][bomb_col + 1] = matrix[bomb_row][bomb_col + 1] - explosion_value
           #print(matrix[bomb_row][bomb_col + 1])

          if bomb_row + 1 <len(matrix) and bomb_col + 1 < len(matrix) and int(matrix[bomb_row + 1][bomb_col + 1]) > 0:
           #damage = matrix[bomb_row+1][bomb_col + 1] - explosion_value
           matrix[bomb_row + 1][bomb_col + 1] = matrix[bomb_row+1][bomb_col + 1] - explosion_value
           #print(matrix[bomb_row + 1][bomb_col + 1])
      else:
           pass

   count_cells_sums(matrix)

   for row in range(len(matrix)):
       for col in range(len(matrix[row])):
         #print(matrix[row])
         matrix[row][col] = str(matrix[row][col])
   for row in range(len(matrix)):
       print(' '.join(matrix[row]))
   return matrix


def count_cells_sums(matrix):
    cells_alive = 0
    cells_sums = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] > 0:
                cells_alive +=1
                cells_sums += matrix[row][column]
    print(f"Alive cells: {cells_alive}")
    print(f"Sum: {cells_sums}")

matrix = matrix_create()
bomb_coordinates = bombs_coordinates_read()
bombs_detonate(matrix, bomb_coordinates)#, bombs_damage)