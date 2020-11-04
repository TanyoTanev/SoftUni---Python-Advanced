'''8. *Miner
We get as input the size of the field in which our miner moves. The field is always a square. After that we will
receive the commands which represent the directions in which the miner should move. The miner starts from
position - &#39;s&#39;. The commands will be: left, right, up and down. If the miner has reached a side edge of the field and
the next command indicates that he has to get out of the field, he must remain on his current possition and ignore
the current command. The possible characters that may appear on the screen are:
 * - a regular position on the field.
 e - the end of the route.
 c - coal
 s - the place where the miner starts
Each time when the miner finds a coal, he collects it and replaces it with &#39;*&#39;. Keep track of the count of the
collected coals. If the miner collects all of the coals in the field, the program stops and you have to print the
following message: &quot;You collected all coals! ({rowIndex}, {colIndex})&quot;.
If the miner steps at &#39;e&#39; the game is over (the program stops) and you have to print the following message:
&quot;Game over! ({rowIndex}, {colIndex})&quot;.
If there are no more commands and none of the above cases had happened, you have to print the following
message: &quot;{remainingCoals} coals left. ({rowIndex}, {colIndex})&quot;.
Input
 Field size - an integer number.
 Commands to move the miner - an array of strings separated by &quot; &quot;.
 The field: some of the following characters (*, e, c, s), separated by whitespace (&quot; &quot;);
Output
 There are three types of output:
o If all the coals have been collected, print the following output: &quot;You collected all coals!
({rowIndex}, {colIndex})&quot;
o If you have reached the end, you have to stop moving and print the following line: &quot;Game over!
({rowIndex}, {colIndex})&quot;
o If there are no more commands and none of the above cases had happened, you have to print the
following message: &quot;{totalCoals} coals left. ({rowIndex}, {colIndex})&quot;
'''

def matrix_create():
  matrix = []
  number_rows = int(input())
  commands_to_move = input().split(' ')
  #print(commands_to_move)
  row_start = 0
  col_start = 0
  coals_max = 0


  for row in range(number_rows):
    string = input().split(' ')
    matrix.append(string)
    for column in range(len(string)):
          if matrix[row][column] == 's':
              row_start = row
              col_start = column
          elif matrix[row][column] == 'c':
              coals_max += 1

  #print('the matrix')
  #for row in range(len(matrix)):
  #    print(matrix[row])

  return matrix, commands_to_move, row_start, col_start, coals_max

def find_start(matrix):
    row_start = 0
    col_start = 0
    coals_max = 0

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 's':
                row_start = row
                col_start = column
            elif matrix[row][column] == 'c':
                coals_max +=1

    return row_start, col_start, coals_max



def mining(matrix, commands_to_move, row_start, col_start, coals_max):

    #row_start, col_start, coals_max = find_start(matrix)
    row_currrent = row_start
    col_current = col_start
    coals = 0

    for i in range(len(commands_to_move)):
       command = commands_to_move[i]
       if command == 'up' and row_currrent -1 >= 0:
           row_currrent -=1
       elif command == 'right' and col_current + 1 < len(matrix[0]):
           col_current +=1
       elif command == 'left' and col_current - 1 >= 0:
           col_current -=1
       elif command == 'down' and row_currrent + 1 < len(matrix):
           row_currrent +=1

       symbol = matrix[row_currrent][col_current]

       if symbol == 'c':
           coals +=1
           matrix[row_currrent][col_current] = '*'
           if coals == coals_max:
            print(f"You collected all coals! ({row_currrent}, {col_current})")
            break
       elif symbol == 'e':
           print(f"Game over! ({row_currrent}, {col_current})")
           break
       elif i == len(commands_to_move) - 1 and coals < coals_max:
           print(f"{coals_max - coals} coals left. ({row_currrent}, {col_current})")


    #print('new matrix')
    #for row in range(len(matrix)):
     #  print(matrix[row])
    #print(coals)

matrix, commands_to_move, row_start, col_start, coals_max = matrix_create()
mining(matrix, commands_to_move, row_start, col_start, coals_max)

