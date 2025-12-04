############################################################################################
########################################## Part 1 ##########################################
############################################################################################

start = 50
import os

base = os.path.dirname(__file__)   # folder where this script lives
path = os.path.join(base, "input.txt")

# Read input file into a list
with open(path, 'r') as file:
    data = [line.strip() for line in file.readlines()]


def dial(start, input):
    direction = input[0]
    turns = int(input[1:])
    
    if direction == "L":
         turns = -turns
    elif direction == "R":
        pass
    else:
        print("Faulty input, must start with either 'R' or 'L'")      
    
    return (start + turns) % 100


#dial_pos = [dial(start, input) for input in data]
# Always start at 50
dial_pos = []
for input in data:
    start = dial(start, input)
    dial_pos.append(start)

n_zeros = dial_pos.count(0)

print("Answer to part one is is: ", n_zeros)

############################################################################################
########################################## Part 2 ##########################################
############################################################################################
# Func to make turns sign based
 #TODO Could be done with list comprehension but w/o error message
def numeric_turns(input):
    direction = input[0]
    turns = int(input[1:])
    
    if direction == "L":
         turns = -turns
    elif direction == "R":
        pass
    else:
        print("Faulty input, must start with either 'R' or 'L'")  
    
    return turns

# Init
laps = 0
pos_new = 50
turns_list = [numeric_turns(turn) for turn in data]

# Loop and count
for turn in turns_list:
    pos_start = pos_new
    pos_new = (pos_start + turn) % 100
    
    # Count laps past 0
    laps += abs((pos_start + turn) // 100)
    
    # If starting position was 0 and we turn left, one lap should be deducted.
    if pos_start == 0 and turn <0:
        laps -= 1
    
    # If we turn left and end up exactly at 0 one lap should be added.
    if pos_new == 0 and turn < 0:
        laps += 1
            
print("Answer to part two is is: ",laps)



