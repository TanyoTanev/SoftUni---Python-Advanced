'''6. Knight Game

Chess is the oldest game, but it is still popular these days. For this task we will use only one chess piece - the Knight.
The knight moves to the nearest square but not on the same row, column, or diagonal. (This can be thought of as
moving two squares horizontally, then one square vertically, or moving one square horizontally then two squares
vertically - i.e. in an &quot;L&quot; pattern.) 
The knight game is played on a board with dimensions N x N and a lot of chess knights 0 &lt;= K &lt;= N 2 .
You will receive a board with K for knights and &#39;0&#39; for empty cells. Your task is to remove a minimum of the knights,
so there will be no knights left that can attack another knight.
Input
- On the first line, you will receive the N size of the board
- On the next N lines, you will receive strings with Ks and 0s.
Output
Print a single integer with the minimum number of knights that needs to be removed
Constraints
 Size of the board will be 0 &lt; N &lt; 30
 Time limit: 0.3 sec. Memory limit: 16 MB.
'''

def matrix_create():
  matrix = []
  number_rows = int(input())
  #print(number_rows)
  for row in range(number_rows):
    #matrix.append(input())
    string= input().split(' ')
    string_repared =''
    for i in range(len(string)):
          string_repared +=string[i]
    matrix.append(string_repared)

  #print(len(matrix[3]))
  #for row in range(len(matrix)):
   #print(matrix[row])
  return matrix

def check_knights_attack(matrix):
    knights_attack = 0
    checked_matrix = 0

    while True:
        if knights_attack or checked_matrix:
            break

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == 'K':
                   if row-2 >= 0 and column - 1 >= 0 and matrix[row-2][column-1] == 'K':
                       knights_attack = 1
                       break
                   elif row-2 >= 0 and column+1 < len(matrix[row]) and matrix[row-2][column+1] == 'K':
                       knights_attack =1
                       break
                   elif row+2 < len(matrix) and column-1 >= 0 and matrix[row+2][column-1] == 'K':
                       knights_attack = 1
                       break
                   elif row+2 < len(matrix) and column+1 < len(matrix[row]) and matrix[row+2][column+1] == 'K':
                       knights_attack = 1
                       break
                   elif row - 1 >= 0 and column - 2 >= 0 and matrix[row - 1][column - 2] == 'K':
                       knights_attack = 1
                       break
                   elif row - 1 >= 0 and column + 2 < len(matrix[row]) and matrix[row - 1][column + 2] == 'K':
                       knights_attack = 1
                       break
                   elif row + 1 < len(matrix) and column - 2 >= 0 and matrix[row + 1][column - 2] == 'K':
                       knights_attack = 1
                       break
                   elif row + 1 < len(matrix) and column + 2 < len(matrix[row]) and matrix[row + 1][column + 2] == 'K':
                       knights_attack = 1
                       break
                if row == len(matrix)-1 and column == len(matrix[row])-1:
                       checked_matrix = 1

    if knights_attack:
     return True
    else:
     return False


def find_max_knights_attack(matrix):
    max_knights_attack = 0
    knights_attack = 0
    checked_matrix = 0
    col_max_attack = 0
    row_max_attack = 0

    while True:
        if checked_matrix:
            break

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
               # row_len = len(matrix[row])
                #print(row_len)
                knights_attack = 0
                if matrix[row][column] == 'K':
                   if row-2 >= 0 and column - 1 >= 0 and matrix[row-2][column-1] == 'K':
                       knights_attack += 1
                   if row - 2 >= 0 and column + 1 < len(matrix[row]) and matrix[row - 2][column + 1] == 'K':
                       knights_attack += 1

                   if row+2 < len(matrix) and column-1 >= 0 and matrix[row+2][column-1] == 'K':
                       knights_attack += 1

                   if row+2 < len(matrix) and column+1 < len(matrix[row]) and matrix[row+2][column+1] == 'K':
                       knights_attack += 1

                   if row - 1 >= 0 and column - 2 >= 0 and matrix[row - 1][column - 2] == 'K':
                       knights_attack += 1

                   if row - 1 >= 0 and column + 2 < len(matrix[row]) and matrix[row - 1][column + 2] == 'K':
                       knights_attack += 1

                   if row + 1 < len(matrix) and column - 2 >= 0 and matrix[row + 1][column - 2] == 'K':
                       knights_attack += 1

                   if row + 1 < len(matrix) and column + 2 < len(matrix[row]) and matrix[row + 1][column + 2] == 'K':
                       knights_attack += 1

                   if knights_attack > max_knights_attack:
                       row_max_attack = row
                       col_max_attack = column
                       max_knights_attack = knights_attack
                       knights_attack = 0
                if row == len(matrix)-1 and column == len(matrix[row])-1:
                       checked_matrix = 1


    #print(row_max_attack)
    #print(col_max_attack)
    #print(max_knights_attack)
    #print(matrix[row_max_attack][col_max_attack])
    return int(row_max_attack), int(col_max_attack)





def remove_min_knights(matrix):
   removed_knights = 0
   if check_knights_attack(matrix):
        pass #print('There ARE attacking knights')
   elif check_knights_attack(matrix) == False:
        pass #print('There are NO attacking knights')
   if check_knights_attack(matrix):
    while check_knights_attack(matrix):
       row,col = find_max_knights_attack(matrix)
       #print(row)
       #print(col)
       #print(matrix[row])#.replace('K','0')
       string = matrix[row]
       string = string[:col] + '0' + string[col+1:]
       matrix[row] = string
       removed_knights +=1
       #print('new matrix')
       #for row in range(len(matrix)):
        #print(matrix[row])

   print(removed_knights)

matrix = matrix_create()
#print(check_knights_attack(matrix))
remove_min_knights(matrix)
#find_max_knights_attack(matrix)