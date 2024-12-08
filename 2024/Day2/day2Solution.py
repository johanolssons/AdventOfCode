############################################################################################
######################################### PACKAGES #########################################
############################################################################################

# Generic
import pandas as pd

############################################################################################
########################################## Part 1 ##########################################
############################################################################################

# Import Data
df = pd.read_csv('C:/Python Projects/AdventOfCode/2024/Day2/input.txt', delimiter=" ",header=None)
print(df.head())

# Sample data
dfSample = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

dfSample = pd.DataFrame(dfSample)

# Rule 1
def is_decreasing(list):
    """
    Checks if items in list is decreasing but not more than 3

    Parameters:
    list (pandas.core.series.Series): The list to check

    Returns:
    boolean: True if list ís decrase but not by more than 3, false otherwise
    """
    cleaned_list = list.dropna()
    return all(0 < cleaned_list[i]  - cleaned_list[i + 1] <= 3 for i in range(len(cleaned_list) - 1))
# Rule 2
def is_increasing(list):
    """
    Checks if items in list is increasing but not more than 3

    Parameters:
    list (pandas.core.series.Series): The list to check

    Returns:
    boolean: True if list ís increasing but not by more than 3, false otherwise
    """
    cleaned_list = list.dropna()
    return all(-3 <= cleaned_list[i]  - cleaned_list[i + 1] < 0 for i in range(len(cleaned_list) - 1))

# Rule 1 & 2
def is_safe(list):
    """
    Checks if items in list is increasing/decreasing but not more than 3

    Parameters:
    list (pandas.core.series.Series): The list to check

    Returns:
    boolean: True if list ís increasing/decreasing but not by more than 3, false otherwise
    """
    return is_increasing(list) or is_decreasing(list)

# Check
numSafeReports = 0
for index, row in df.iterrows():
    if is_safe(row):
        numSafeReports = numSafeReports + 1

numSafeReports

############################################################################################
########################################## Part 2 ##########################################
############################################################################################
"""
First idea is to apply the Problem Dampner on only unsafe repoerts to see if they can be made
safe to save time. An ad hos solution would be to iteratively remove a number from the
list/repoet one by one then fetching it through the check. If it becomes safe then stop and
return as true. 
"""

def problem_damper(list):
    """
    Takes a list and excludes element per element then checks that list using "is_safe()".
    If the report becomes safe at any point the function breaks and returns tre


    Parameters:
    list (pandas.core.series.Series): The list to check

    Returns:
    boolean: True if if report can become safe through problem dampner
    """
    for i in range(len(list)):
        tempList = pd.Series([list[idx] for idx in range(len(list)) if idx != i])
        if is_safe(tempList):
            return(True)
    return(False)

numSafeReports2 = 0
for index, row in df.iterrows():
    if is_safe(row):
        numSafeReports2 = numSafeReports2 + 1
    elif problem_damper(row):
        numSafeReports2 = numSafeReports2 + 1
numSafeReports2

#cleaned_list = list.dropna()
#tempList = 