'''9. *Radioactive Mutant Vampire Bunnies

Browsing through GitHub, you come across an old JS Basics teamwork game. It is about very nasty bunnies that
multiply extremely fast. There&#39;s also a player that has to escape from their lair. You really like the game, so you
decide to port it to Python because that&#39;s your language of choice. The last thing that is left is the algorithm that
decides if the player will escape the lair or not.
First, you will receive a line holding integers N and M, which represent the rows and columns in the lair. Then you
receive N strings that can only consist of &quot;.&quot;, &quot;B&quot;, &quot;P&quot;. The bunnies are marked with &quot;B&quot;,
the player is marked with
&quot;P&quot;, and everything else is free space, marked with a dot &quot;.&quot;. They represent the initial state of the lair. There will be
only one player. Then you will receive a string with commands such as LLRRUUDD - where each letter represents
the next move of the player (Left, Right, Up, Down).
After each step of the player, each of the bunnies spread to the up, down, left and right (neighboring cells marked as
&quot;.&quot; changes their value to B). If the player moves to a bunny cell or a bunny reaches the player, the player has died.
If the player goes out of the lair without encountering a bunny, the player has won.
When the player dies or wins, the game ends. All the activities for this turn continue (e.g. all the bunnies spread
normally), but there are no more turns. There will be no stalemates where the moves of the player end before he
dies or escapes.

© SoftUni – https://softuni.org. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
Follow us: Page 4 of 8
Finally, print the final state of the lair with every row on a separate line. On the last line, print either &quot;dead: {row}
{col}&quot; or &quot;won: {row} {col}&quot;. Row and col are the coordinates of the cell where the player has died or the
last cell he has been in before escaping the lair.
Input
 On the first line of input, the numbers N and M are received - the number of rows and columns in the lair
 On the next N lines, each row is received in the form of a string. The string will contain only &quot;.&quot;, &quot;B&quot;, &quot;P&quot;. All
strings will be the same length. There will be only one &quot;P&quot; for all the input
 On the last line, the directions are received in the form of a string, containing &quot;R&quot;, &quot;L&quot;, &quot;U&quot;, &quot;D&quot;
Output
 On the first N lines, print the final state of the bunny lair
 On the last line, print the outcome - &quot;won:&quot; or &quot;dead:&quot; + {row} {col}
Constraints
 The dimensions of the lair are in range [3…20]
 The directions string length is in range [1…20]

5 8
.......B435
...B....345
....B..B345
........234
...P1234567
ULLLD


'''
def matrix_create():
  matrix = []
  col_start = 0
  row_start = 0
  rows, columns = list(map(int, input().split(' ')))
  #print(f"row{rows}, columns {columns}")

  for row in range(rows):
     string = input()
     matrix.append([])
     for column in range(columns):
       matrix[row].append(string[column])
       if matrix[row][column] == 'P':
            row_start = row
            col_start = column
            matrix[row][column] = '.'

  commands_to_move = input()
  #print('the matrix')
 # print(f"len of matrix {len(matrix)}, len na colonite {len(matrix[3])}")
  #print(f"startovi koord {row_start}{col_start}")
  #for row in range(len(matrix)):
      #print(matrix[row])
  #print(matrix)
  return matrix, commands_to_move, row_start, col_start



def escape_from_lair(matrix):

    won_or_dead = 0 # 1 - dead; 2 - won
    dead_from_bunnies = 0 # 1 - dead; 2 - won

    row_current = row_start
    col_current = col_start

    row_dead = 0
    col_dead = 0

    for i in range(len(commands_to_move)):
      command = commands_to_move[i]
      if won_or_dead:
          break
      else:
        if command == 'L' and col_current - 1 >= 0:
           if matrix[row_current][col_current - 1] != 'B':
            #matrix[]
            col_current -=1
           elif matrix[row_current][col_current - 1] == 'B':
            #print(f"dead: {row_current} {col_current-1}")
            won_or_dead = 1
            row_dead = row_current
            col_dead = col_current-1
        elif command == 'L' and col_current == 0:
            won_or_dead = 2

        elif command == 'R' and col_current + 1 < len(matrix[0]) - 1:
            if matrix[row_current][col_current + 1] != 'B':
                col_current += 1
            else:
                #print(f"dead: {row_current} {col_current + 1}")
                won_or_dead = 1
                row_dead = row_current
                col_dead = col_current + 1
        elif command == 'R' and col_current == len(matrix[0]) - 1:
             won_or_dead = 2


        elif command == 'U' and row_current - 1 >= 0:
            if matrix[row_current][col_current] != 'B':
                row_current -= 1
            else:
                #print(f"dead: {row_current - 1} {col_current}")
                won_or_dead = 1
                row_dead = row_current  - 1
                col_dead = col_current
        elif command == 'U' and row_current == 0:
                won_or_dead = 2

        elif command == 'D' and row_current + 1 < len(matrix):
            if matrix[row_current][col_current] != 'B':
                row_current += 1
            else:
                #print(f"dead: {row_current + 1} {col_current}")
                won_or_dead = 1
                row_dead = row_current + 1
                col_dead = col_current
        elif command == 'D' and row_current ==  len(matrix) - 1:
                won_or_dead = 2

        matrix, dead_from_bunnies, row_dead_from_bunnies, col_dead_from_bunnies = bunnies_spread(matrix, row_current, col_current, won_or_dead)

        if dead_from_bunnies:
             won_or_dead =1
             row_dead = row_dead_from_bunnies
             col_dead = col_dead_from_bunnies
        if won_or_dead:
            #print('the matrix')
            for row in range(len(matrix)):
                #for col in range(len(matrix[row])):
                  print(''.join(matrix[row]))
            if won_or_dead == 2:
              print(f"won: {row_current} {col_current}")
            elif won_or_dead == 1:
                print(f"dead: {row_dead} {col_dead}")

    print('the matrix')
    for row in range(len(matrix)):
        print(matrix[row])

def bunnies_spread(matrix, row_current, col_current, won_or_dead ):
    matrix_new = matrix
    dead_from_bunnies = 0
    row_dead = 0
    col_dead = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
             if matrix[row][col] == 'B':
                if row - 1 >= 0 and row -1 == row_current and col == col_current and won_or_dead == 0:
                    #print(f"dead: {row_current} {col_current}")
                    dead_from_bunnies = 1
                    row_dead = row - 1
                    col_dead = col
                    matrix_new[row - 1][col] = 'B1'
                    #break
                elif row - 1 >= 0 and matrix[row - 1][col] != 'B':
                    matrix_new[row - 1][col] = 'B1'

                if col - 1 >= 0 and col - 1 == col_current and row == row_current and won_or_dead == 0:
                    #print(f"dead: {row_current} {col_current}")
                    dead_from_bunnies = 1
                    row_dead = row
                    col_dead = col - 1
                    matrix_new[row][col - 1] = 'B1'
                    #break
                elif col - 1 >= 0 and matrix[row][col - 1] != 'B':
                    matrix_new[row][col - 1] = 'B1'

                if row + 1 < len(matrix) and row + 1 == row_current and col == col_current and won_or_dead == 0:
                    #print(f"dead: {row_current} {col_current}")
                    dead_from_bunnies = 1
                    row_dead = row + 1
                    col_dead = col_current
                    matrix_new[row + 1][col] = 'B1'
                    #break
                elif row + 1 < len(matrix) and matrix[row + 1] [col] != 'B':
                    matrix_new[row + 1] [col] = 'B1'

                if col + 1 < len(matrix[0]) and col +1 == col_current and row == row_current and won_or_dead == 0:
                    #print(f"dead: {row_current} {col_current}")
                    #break
                    dead_from_bunnies = 1
                    row_dead = row
                    col_dead = col + 1
                    matrix_new[row][col + 1] = 'B1'

                elif col + 1 < len(matrix[0]) and matrix[row][col + 1] != 'B':
                    matrix_new[row][col + 1] = 'B1'
    print('the matrix')

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix_new[row][col] == 'B1':
                matrix_new[row][col] = 'B'
    for row in range(len(matrix)):
        print(matrix_new[row])
    return matrix_new, dead_from_bunnies, row_dead, col_dead




matrix, commands_to_move, row_start, col_start = matrix_create()
#print("transfered")
#for row in range(len(matrix)):
 #   print(matrix[row])
escape_from_lair(matrix)


