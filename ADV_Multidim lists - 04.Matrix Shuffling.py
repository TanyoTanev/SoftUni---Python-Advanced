'''4.Matrix Shuffling
Write a program which reads a string matrix from the console and performs certain operations with its elements.
User input is provided in a similar way like in the problems above - first you read the dimensions and then the data.
Your program should then receive commands in format: &quot;swap row1 col1 row2c col2&quot; where row1, row2, col1, col2
are coordinates in the matrix. For a command to be valid, it should start with the &quot;swap&quot; keyword along with four
valid coordinates (no more, no less). You should swap the values at the given coordinates (cell [row1, col1] with cell
[row2, col2]) and print the matrix at each step (thus you&#39;ll be able to check if the operation was performed
correctly).
If the command is not valid (doesn&#39;t contain the keyword &quot;swap&quot;, has fewer or more coordinates entered or the
given coordinates do not exist), print &quot;Invalid input!&quot; and move on to the next command. Your program
should finish when the string 'END' is entered.

'''

def matrix_create():
  matrix = []
  string = input().split(' ')
  if string[0].isdigit() and string[1].isdigit():
     (rows, cols) = map(int, string)

     for row in range(rows):
        string_list = input().split(' ')
        #matrix.append([])
        matrix.append(string_list)
  #print(matrix)
  return matrix

def command_check(command):
    pass


def matrix_shuffle(matrix):


    while True:
     command = input()

     if command == 'END':
            break

     else:
       command = command.split(' ')

       if  command[0] == 'swap' and len(command) == 5 and 0 <= int(command[1]) <= len(matrix) and 0 <= int(command[2]) <= len(matrix[0]) and 0 <= int(command[3]) <= len(matrix) and 0 <= int(command[4]) <= len(matrix[0]):

            row1 = int(command[1])
            col1 = int(command[2])
            row2c = int(command[3])
            col2 = int(command[4])

            transition_value = matrix[row1][col1]
            matrix[row1][col1] = matrix[row2c][col2]
            matrix[row2c][col2] = transition_value

            #print(matrix)
            for row in range(len(matrix)):
                #for column in range(len(matrix[row])):
                    print(' '.join(matrix[row]))

        #else:
           # print("Invalid input!")
       else:
         print("Invalid input!")



matrix = matrix_create()
matrix_shuffle(matrix)


