'''5. Snake Moves
You are walking in the park and you encounter a snake! You are terrified, and you start running zigzag, so the snake
starts following you.
You have a task to visualize the snake&#39;s path in a square form. A snake is represented by a string. The isle is a
rectangular matrix of size NxM. A snake starts going down from the top-left corner and slithers its way down. The
first cell is filled with the first symbol of the snake, the second cell is filled with the second symbol, etc. The snake is
as long as it takes in order to fill the stairs completely - if you reach the end of the string representing the snake,
start again at the beginning. After you fill the matrix with the snake&#39;s path, you should print it.

Input
 The input data should be read from the console. It consists of exactly two lines
 On the first line, you&#39;ll receive the dimensions of the stairs in format: &quot;N M&quot;, where N is the number of
rows, and M is the number of columns. They&#39;ll be separated by a single space
 On the second line you&#39;ll receive the string representing the snake

Output
 The output should be printed on the console. It should consist of N lines
 Each line should contain a string representing the respective row of the matrix

Constraints
 The dimensions N and M of the matrix will be integers in the range [1 … 12]
 The snake will be a string with length in the range [1 … 20] and will not contain any whitespace
characters
'''

def matrix_create():
  matrix = []
  string = input().split(' ')
  if string[0].isdigit() and string[1].isdigit() and 0 < int(string[0]) <= 12 and 0 < int(string[1]) <= 12:
     (rows, cols) = map(int, string)

     for row in range(rows):
        string_list = [0 for i in range(cols)]
        matrix.append(string_list)
  #print(matrix)
  return matrix



def snake_string(matrix):
    row = 0
    column = 0
    snake_full = ''

    snake = input()
    on_right = 1
    on_left = 0

    remain = len(matrix)*len(matrix[0]) % len(snake)
    times = len(matrix)*len(matrix[0]) // len(snake)
    #print(times)


    for i in range(times):
     snake_full = snake_full + snake
    for i in range(remain):
        snake_full = snake_full + snake[i]
    #print(remain)
    #print(snake_full)
    #print(len(snake_full))
    #print(len(matrix)*len(matrix[0]))

    for i in range(len(matrix)*len(matrix[0])):
         if on_right:
           matrix[row][column] = snake_full[i]
           if column + 1 < len(matrix[0]):
             column +=1
           else:
               row +=1
               on_right = 0
               on_left = 1

         elif on_left:

             matrix[row][column] = snake_full[i]
             if column - 1 >= 0:
                 column -= 1
             else:
                 row +=1
                 on_right = 1
                 on_left = 0
    #print(matrix)
    for row in range(len(matrix)):
        # for column in range(len(matrix[row])):
        print(''.join(matrix[row]))



matrix = matrix_create()
snake_string(matrix)

