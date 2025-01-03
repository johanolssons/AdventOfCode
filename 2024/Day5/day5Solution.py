############################################################################################
######################################### PACKAGES #########################################
############################################################################################

# Generic
import pandas as pd

############################################################################################
##################################### Part 1 Functions #####################################
############################################################################################

def file_split(path_in:str, path_out1:str, path_out2:str):
    with open(path_in, 'r') as file:
        content = file.read()

    # Split the content where there are blank rows
    split_content = content.split('\n\n')

    # Save the split parts into separate files
    if len(split_content) == 2:
        with open(path_out1, 'w') as file1:
            file1.write(split_content[0])
        with open(path_out2, 'w') as file2:
            file2.write(split_content[1])
        print(f"Files saved as {path_out1} and {path_out2}")
    elif len(split_content) > 2:
        print("The file contains too many sections.")
    else:
        print("The file does not contain enough sections to split.")


############################################################################################
########################################## Part 1 ##########################################
############################################################################################

# First we we split the input file into ordering rules and updates
file_split("C:/Python Projects/AdventOfCode/2024/Day5/input.txt", 
           "C:/Python Projects/AdventOfCode/2024/Day5/order_rules.txt", 
           "C:/Python Projects/AdventOfCode/2024/Day5/updates.txt")


# Now we read the two different files per line as lists
# Order rules
#with open("C:/Python Projects/AdventOfCode/2024/Day5/order_rules.txt", 'r') as file:
#    lines = file.readlines()
#order_rules = [line.strip() for line in lines] # Clean up any trailing newlines
df_order = pd.read_csv("C:/Python Projects/AdventOfCode/2024/Day5/order_rules.txt", sep="|",names=["before", "after"])

# Updates
with open("C:/Python Projects/AdventOfCode/2024/Day5/updates.txt", 'r') as file:
    updates = [list(map(int, line.strip().split(","))) for line in file]

#Walk thorugh each update and verify the order
correct_updates = []
for update in updates:
    break_roule = False
    for i in range(len(update)):
        # Get pages before and after
        pages_after = update[i+1:]
        pages_before = update[:i]

        # Check if any pages after should be before
        if set(pages_after) & set(df_order[df_order["after"] == update[i]]["before"]):
            break_roule = True
            break
        # Check if any pages before should be after
        elif set(pages_before) & set(df_order[df_order["before"] == update[i]]["after"]):
            break_roule = True
            break
    if not break_roule:
        correct_updates.append(update)


# SUM the middle numbers
middle_sum = sum(update[len(update) // 2] for update in correct_updates)






