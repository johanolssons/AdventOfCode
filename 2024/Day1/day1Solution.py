############################################################################################
######################################### PACKAGES #########################################
############################################################################################

# Generic
import pandas as pd


############################################################################################
########################################### MAIN ###########################################
############################################################################################

#Import data
df = pd.read_csv('C:/Python Projects/AdventOfCode/2024/Day1/input.txt', delimiter="  ",header=None, names=["Left", "Right"])

# Left and right ascending list
leftAsc = df['Left'].sort_values().reset_index(drop=True)
RightAsc = df['Right'].sort_values().reset_index(drop=True)

# Result for part 1
res1 = sum(abs(leftAsc - RightAsc))

# Part2
res2 = 0
for index, row in df.iterrows():
    simScore = row['Left'] * (df['Right'] == row['Left']).sum()
    res2 = res2 + simScore

print(res2)