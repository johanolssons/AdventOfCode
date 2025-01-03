############################################################################################
######################################### PACKAGES #########################################
############################################################################################

# Generic
import matplotlib.pyplot as plt
import numpy as np

############################################################################################
########################################## Part 1 ##########################################
############################################################################################
# TODO: Too many "XMAS" found, implement conktrol in results to confirm that the right word is found

"""
I got thre more occurances of "XMAS" than chat GPT which had the correct ammoutnt (2534). I have tried
to debug the code for too long now and might get back to it later. In the directory i have a file 
"XMAS_coordinates.csv" which is GPTs coordinates of all starting "X"es where the upper left corner is (0,0)
"""

######################################## Functions #########################################
# List of all positions to check
def get_positions(wordList:list, letter:str): 
    """
    Returns the xy positions of a certain letter in a list of strings.

    Parameters:
    wordList (list): The list to check.
    letter (str): The letter to search for.

    Returns:
    list: A list of touples containing the xy positions. 
    """
    
    return [(col_idx, row_idx) 
           for row_idx, row in enumerate(wordList) 
           for col_idx, char in enumerate(row) 
           if char == letter]

# Functions to check for "XMAS"
def check_right(wordList:list, word: str, x:int = 0, y:int = 0):
    """
    Checks if a certain word exist in a on a specified position (x,y) in a specified
    list of text (wordList), assuming the word is written in "right" orientation.

    TODO: Error handling

    Parameters:
    wordList (list): The list to check.
    word (str): The word to check for.
    x (int): The x starting position, dafaults to 0.
    y (int): The y starting position, dafaults to 0. 

    Returns:
    boolean: True if word is found, False otherwise. 
    """
    res = ""
    control = ""
    for i in range(len(word)):
        if wordList[y][x+i] == word[i]:
            check = True
            control = control + word[i]
            res = res + wordList[y][x+i] #Control to spell word
        else:
            check = False
            break
    return check, control, res

def check_left(wordList:list, word: str, x:int = 0, y:int = 0):
    """
    Checks if a certain word exist in a on a specified position (x,y) in a specified
    list of text (wordList), assuming the word is written in "left" orientation.

    TODO: Error handling

    Parameters:
    wordList (list): The list to check.
    word (str): The word to check for.
    x (int): The x starting position, dafaults to 0.
    y (int): The y starting position, dafaults to 0. 

    Returns:
    boolean: True if word is found, False otherwise.
    """
    res = ""
    control = ""
    for i in range(len(word)):
        # TODO: Remove first if statement checking for negative indexing if relevant positions are checked.
        if x-i < 0:
            check = False
            break
        elif wordList[y][x-i] == word[i]:
            check = True
            res = res + wordList[y][x-i] #Control to spell word
            control = control + word[i] #Control to spell word
        else:
            check = False
            break
    return check, control, res

def check_up(wordList:list, word: str, x:int = 0, y:int = 0):
    """
    Checks if a certain word exist in a on a specified position (x,y) in a specified
    list of text (wordList), assuming the word is written in "upward" orientation.

    TODO: Error handling

    Parameters:
    wordList (list): The list to check.
    word (str): The word to check for.
    x (int): The x starting position, dafaults to 0.
    y (int): The y starting position, dafaults to 0. 

    Returns:
    boolean: True if word is found, False otherwise. 
    """
    res = ""
    control = ""
    for i in range(len(word)):
        # TODO: Remove first if statement checking for negative indexing if relevant positions are checked.
        if y-i < 0:
            check = False
            break
        elif wordList[y-i][x] == word[i]:
            check = True
            res = res + wordList[y-i][x] #Control to spell word
            control = control + word[i]
        else:
            check = False
            break
    return check, control, res

def check_down(wordList:list, word: str, x:int = 0, y:int = 0):
    """
    Checks if a certain word exist in a on a specified position (x,y) in a specified
    list of text (wordList), assuming the word is written in "downward" orientation.

    TODO: Error handling

    Parameters:
    wordList (list): The list to check.
    word (str): The word to check for.
    x (int): The x starting position, dafaults to 0.
    y (int): The y starting position, dafaults to 0. 

    Returns:
    boolean: True if word is found, False otherwise. 
    """
    res = ""
    control = ""
    for i in range(len(word)):

        if wordList[y+i][x] == word[i]:
            check = True
            res = res + wordList[y+i][x] #Control to spell word
            control = control + word[i]
        else:
            check = False
            break
    return check, control, res

def check_right_up(wordList:list, word: str, x:int = 0, y:int = 0):
    """
    Checks if a certain word exist in a on a specified position (x,y) in a specified
    list of text (wordList), assuming the word is written in "right upward" orientation.

    TODO: Error handling

    Parameters:
    wordList (list): The list to check.
    word (str): The word to check for.
    x (int): The x starting position, dafaults to 0.
    y (int): The y starting position, dafaults to 0. 

    Returns:
    boolean: True if word is found, False otherwise. 
    """
    res = ""
    control = ""
    for i in range(len(word)):
         # TODO: Remove first if statement checking for negative indexing if relevant positions are checked.
        if y-i < 0:
            check = False
            break
        elif wordList[y-i][x+i] == word[i]:
            check = True
            res = res + wordList[y-i][x+i] #Control to spell word
            control = control + word[i]
        else:
            check = False
            break
    return check, control, res

def check_right_down(wordList:list, word: str, x:int = 0, y:int = 0):
    """
    Checks if a certain word exist in a on a specified position (x,y) in a specified
    list of text (wordList), assuming the word is written in "right downward" orientation.

    TODO: Error handling

    Parameters:
    wordList (list): The list to check.
    word (str): The word to check for.
    x (int): The x starting position, dafaults to 0.
    y (int): The y starting position, dafaults to 0. 

    Returns:
    boolean: True if word is found, False otherwise. 
    """
    res = ""
    control = ""
    for i in range(len(word)):

        if wordList[y+i][x+i] == word[i]:
            check = True
            res = res + wordList[y+i][x+i] #Control to spell word
            control = control + word[i]
        else:
            check = False
            break
    return check, control, res

def check_left_up(wordList:list, word: str, x:int = 0, y:int = 0):
    """
    Checks if a certain word exist in a on a specified position (x,y) in a specified
    list of text (wordList), assuming the word is written in "left upward" orientation.

    TODO: Error handling

    Parameters:
    wordList (list): The list to check.
    word (str): The word to check for.
    x (int): The x starting position, dafaults to 0.
    y (int): The y starting position, dafaults to 0. 

    Returns:
    boolean: True if word is found, False otherwise. 
    """
    res = ""
    control = ""
    for i in range(len(word)):
         # TODO: Remove first if statement checking for negative indexing if relevant positions are checked.
        if x-i < 0 or y-i < 0:
            check = False
            break
        elif wordList[y-i][x-i] == word[i]:
            check = True
            res = res + wordList[y-i][x-i] #Control to spell word
            control = control + word[i]
        else:
            check = False
            break
    return check, control, res

def check_left_down(wordList:list, word: str, x:int = 0, y:int = 0):
    """
    Checks if a certain word exist in a on a specified position (x,y) in a specified
    list of text (wordList), assuming the word is written in "left downward" orientation.

    TODO: Error handling

    Parameters:
    wordList (list): The list to check.
    word (str): The word to check for.
    x (int): The x starting position, dafaults to 0.
    y (int): The y starting position, dafaults to 0. 

    Returns:
    boolean: True if word is found, False otherwise. 
    """
    res = ""
    control = ""
    for i in range(len(word)):

        if wordList[y+i][x-i] == word[i]:
            check = True
            res = res + wordList[y+i][x-i]#Control to spell word
            control = control + word[i]
        else:
            check = False
            break
    return check, control, res

########################################### Code ###########################################

# Read file 
with open("C:/Python Projects/AdventOfCode/2024/Day4/input.txt", 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines] # Clean up any trailing newlines

# Sample text
with open("C:/Python Projects/AdventOfCode/2024/Day4/input.txt", 'r') as file:
    linesSample = file.readlines()
linesSample = [line.strip() for line in linesSample] # Clean up any trailing newlines

# Iterate through positions and peform checks
## TODO: Create function
## TODO: Do not check for infeasible out of bound positions
## FIXME: Cacks past baundries through negative indexing.. 
### TODO: Change temporary solution where only negative indices are avoided in check funtions.
word = "XMAS"
wordList = linesSample
count = 0
result1 = []

# Get positions to check for
pos = get_positions(wordList=wordList, letter="X")

for x, y in pos:
    # Check to the right
    try:
        check, control, res = check_right(wordList=wordList, word=word, x=x, y=y)
        if check:
            count = count + 1
            result1.append((x,y,"R", control, res))
    except IndexError:
        pass
    
    # Check to the left
    try:
        check, control, res = check_left(wordList=wordList, word=word, x=x, y=y)
        if check:
            count = count + 1
            result1.append((x,y,"L", control, res))
    except IndexError:
        pass

    # Check upward
    try:
        check, control, res = check_up(wordList=wordList, word=word, x=x, y=y)
        if check:
            count = count + 1
            result1.append((x,y,"U", control, res))
    except IndexError:
        pass

    # Check to the downward
    try:
        check, control, res = check_down(wordList=wordList, word=word, x=x, y=y)
        if check:
            count = count + 1
            result1.append((x,y,"D", control, res))
    except IndexError:
        pass

    # Check to the right and up (diag)
    try:
        check, control, res = check_right_up(wordList=wordList, word=word, x=x, y=y)
        if check:
            count = count + 1
            result1.append((x,y,"RU", control, res))
    except IndexError:
        pass

    # Check to the right and down (diag)
    try:
        check, control, res = check_right_down(wordList=wordList, word=word, x=x, y=y)
        if check:
            count = count + 1
            result1.append((x,y,"RD", control, res))
    except IndexError:
        pass

    # Check to the left and up (diag)
    try:
        check, control, res = check_left_up(wordList=wordList, word=word, x=x, y=y)
        if check:
            count = count + 1
            result1.append((x,y,"LU", control, res))
    except IndexError:
        pass

    # Check to the left and down (diag)
    try:
        check, control, res = check_left_down(wordList=wordList, word=word, x=x, y=y)
        if check:
            count = count + 1
            result1.append((x,y,"LD", control, res))
    except IndexError:
        pass

print(count)


############################################################################################
##################################### Plot the results #####################################
############################################################################################

"""
import matplotlib.pyplot as plt
import numpy as np

# Example grid
grid = np.array([
    ['M', 'M', 'M', 'X', 'M', 'A', 'S'],
    ['X', 'M', 'A', 'S', 'M', 'X', 'M'],
    ['A', 'M', 'X', 'M', 'A', 'M', 'M'],
    ['S', 'M', 'X', 'M', 'A', 'S', 'M'],
])

# List of starting "X" coordinates (from your earlier task)
coordinates = [(0, 3), (1, 0), (2, 2), (3, 2)]  # Replace with your actual coordinates

# Create a visual representation
plt.figure(figsize=(6, 6))
ax = plt.gca()

# Draw the grid
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        color = 'red' if (i, j) in coordinates else 'black'
        ax.text(j, i, grid[i, j], va='center', ha='center', fontsize=12, color=color)

# Set grid lines
ax.set_xticks(np.arange(-0.5, grid.shape[1], 1), minor=True)
ax.set_yticks(np.arange(-0.5, grid.shape[0], 1), minor=True)
ax.grid(which='minor', color='gray', linestyle='-', linewidth=1)

# Turn off axes
ax.set_xticks([])
ax.set_yticks([])
plt.show()
"""
############################################################################################
########################################## Part 2 ##########################################
############################################################################################
