############################################################################################
########################################## Part 2 ##########################################
############################################################################################



######################################## Functions #########################################
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



########################################## MAIN ############################################
with open("C:/Python Projects/AdventOfCode/2024/Day4/input.txt", 'r') as file:
    lines = file.readlines()
word_list = [line.strip() for line in lines] # Clean up any trailing newlines


# Get positions to check for, we want to check for all As
pos = get_positions(wordList=word_list, letter="A")


# Build first func
def check_X(word_list:list, x, y):
    # Get all corners if index error it is not possible to creat an x
    err = False
    check = False
    try:
        UL = word_list[y-1][x-1] # Upper left corner
        UR = word_list[y-1][x+1] # Upper right corner
        LL = word_list[y+1][x-1] # Lower left corner
        LR = word_list[y+1][x+1] # Lower right corner
    except IndexError:
        check = False
        err = True
        
    if not err:
        if UL == "M" and LR == "S":
            if UR == "M" and LL == "S":
                check = True
            elif UR == "S" and LL == "M":
                check = True
        elif UL == "S" and LR == "M":
            if UR == "M" and LL == "S":
                check = True
            elif UR == "S" and LL == "M":
                check = True
        else:
            check = False
    return check

count = 0
for x, y in pos:
    if check_X(word_list=word_list, x=x, y=y):
        count = count+1

print(count)
