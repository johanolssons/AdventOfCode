############################################################################################
######################################### PACKAGES #########################################
############################################################################################

# Generic
import re


############################################################################################
########################################## Part 1 ##########################################
############################################################################################
#TODO
    # 

with open("C:/Python Projects/AdventOfCode/2024/Day3/input.txt", 'r') as file:
    text = file.read()

pattern = r'mul\((\d{1,3}),\s*(\d{1,3})\)'
matches = re.findall(pattern, text)
res1 = sum([(int(x) * int(y)) for x, y in matches])
res1

############################################################################################
########################################## Part 2 ##########################################
############################################################################################


# Step 1: Find all 'don't()' and 'do()' positions
dont_indices = [m.start() for m in re.finditer(r'don\'t\(\)', text)]
do_indices = [m.start() for m in re.finditer(r'do\(\)', text)]

# Step 2: Initialize the list to store valid matches
valid_matches = []

# Step 3: Process the text to find matches outside of the don't-do range
offset = 0  # To track the position in the text as we process
for start_dont in dont_indices:
    # Find matches before this 'don't()'
    part_after_last_dont = text[offset:start_dont]
    matches_in_part = re.findall(pattern, part_after_last_dont)
    valid_matches.extend(matches_in_part)

    # Now we need to exclude the range between this 'don't()' and the next 'do()' if it exists
    if do_indices:  # If there are any 'do()' found
        # Find the index of the first 'do()' after this 'don't()'
        for start_do in do_indices:
            if start_do > start_dont:
                break
        else:
            # If no do() found after this don't(), we process until the end
            start_do = len(text)
        
        # Skip everything in between
        offset = start_do
    else:
        # If no do() found, we process until the end of the text
        offset = len(text)

# After processing all dont() occurrences, look for matches in any remaining text
part_after_last_dont = text[offset:]
matches_in_part_end = re.findall(pattern, part_after_last_dont)
valid_matches.extend(matches_in_part_end)

# Convert matches to tuples of integers
res2 = sum([(int(x) * int(y)) for x, y in valid_matches])
res2

# Display the results

