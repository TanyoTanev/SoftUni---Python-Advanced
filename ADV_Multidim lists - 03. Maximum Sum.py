'''3. Maximal Sum
Write a program that reads a rectangular integer matrix of size N x M and finds in it the square 3 x 3 that has
maximal sum of its elements.
Input
 On the first line, you will receive the rows N and columns M. On the next N lines you will receive each row
with its columns
Output
 Print the elements of the 3 x 3 square as a matrix, along with their sum
'''

def matrix_create():
  matrix = []
  string = input().split(' ')
  if string[0].isdigit() and string[1].isdigit():
     (rows, cols) = map(int, string)

     for row in range(rows):
        string_list = input().split(' ')
        matrix.append([])
        for i in range(len(string_list)):
            if string_list[i].isdigit():

                matrix[-1].append(int(string_list[i]))
        #matrix.append(list(map(int, input().split(' '))))
  #print(matrix)
  return matrix

def matrix_find_max_sum(matrix):
 if len(matrix) > 2 and len(matrix[0]) > 2:
  max_sum = matrix[0][0] + matrix[0][1] + matrix[0][2] + matrix[1][0] + matrix[1][1] + matrix[1][2] + matrix[2][0] + matrix[2][1] + matrix[2][2]
  #print(max_sum)
  row_max = 0
  column_max = 0
  #if len(matrix) > 2 and len(matrix[0]) > 2:
  for row in range(len(matrix)-2):
      for column in range(len(matrix[row])-2):
          if row + 2 < len(matrix) and column + 2 < len(matrix[row]):
             next_sum = matrix[row][column] + matrix[row][column+1] + matrix[row][column+2] + matrix[row+1][column] + matrix[row+1][column+1] + matrix[row+1][column+2] + matrix[row+2][column] + matrix[row+2][column+1] + matrix[row+2][column+2]
             if next_sum > max_sum:
               max_sum = next_sum
               row_max = row
               column_max = column
 #else:
 # return None


  print(f"Sum = {max_sum}")
  for row in range(3):
      print(f"{matrix[row_max+row][column_max]} {matrix[row_max+row][column_max+1]} {matrix[row_max+row][column_max+2]}")


matrix = matrix_create()
matrix_find_max_sum(matrix)
