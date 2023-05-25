"""
Script for displaying crime results

This script uses the functions defined in toolbox to solve the crime, printing
out the result on the console.

Developed by Al Palanuwech (ap689) and Professor Bracy for CS1110SP A1.

Author: Kene Chukwuma (ebc68) and Monalisa Almeida (mca74)
Date:   02/20/23
"""

from toolbox import *
import sys

#############################################################################
# Students DO NOT MODIFY the code below
#############################################################################

suspects = {}
time_of_crime = '4:39'
DEFAULT_FILE = "case1.txt"
if __name__ == "__main__":
    args = sys.argv[1:]
    if args != []:
        DEFAULT_FILE = args[0]


def start_case():
    """
    Initiates court case and modifies dictionary 'suspects' with the the
    potential suspects sets them all to 'None'
    """
    suspects['al palanuwech'] = None
    suspects['lenhard thomas'] = None
    suspects['anne bracy'] = None


def provide_evidence(name, time):
    """
    provide evidence to the court, given a name and a time
    Precondition name: a string
    Precondition time: a string in the international time format ie. hh:mm
    """
    assert name in suspects, (name + "not found in the suspect list," +
                              " have you decrypted the name yet?")
    suspects[name] = time_helper(time, time_of_crime)


def time_helper(time1, time2):
    """Returns true if time1 and time 2 are close enough
    Precondition time1: a string in the international time format ie. hh:mm
    Precondition time2: a string in the international time format ie. hh:mm
    """
    threshhold = 10
    ind1 = time1.index(':')
    time1_min = int(time1[:ind1])*60 + int(time1[ind1+1:])
    ind2 = time2.index(':')
    time2_min = int(time2[:ind2])*60 + int(time2[ind2+1:])
    return abs(time2_min - time1_min) < threshhold


def report_case():
    """ Given the current information from startcase() and provide_evidence(),
    print out the results.
    """
    print("The court will now announce the results:")
    for key in suspects:
        if suspects[key] is None:
            print("No evidence found for "+key+'.')
        elif suspects[key]:
            print(key+" has been found guilty!")
        else:
            print(key+" is innocent.")
    # reset dictionary
    suspects.clear()


start_case()

###########################################################################
# STUDENTS INSERT SCRIPT CODE HERE
# Use functions from toolbox to extract information, then call
# provide_evidence(...) with the correct arguments.

# read the file case1.txt, then use functions from toolbox to extract
# 'name' and 'time' for each suspect (theres 2 suspects present), then call
# provide_evidence(...) for each pair

# Read file, file_str contains the contents of case1.txt as a string, what next?

file_str = file_to_string(DEFAULT_FILE)
#suspect 1
suspect1 = get_line(file_str, 1)
name1 = get_value(suspect1, 'name')
actual_name1 = decrypt(name1)
time1 = get_value(suspect1, 'time')
provide_evidence(actual_name1, time1)

#suspect 2
suspect2 = get_line(file_str, 2)
name2 = get_value(suspect2, 'name')
actual_name2 = decrypt(name2)
time2 = get_value(suspect2, 'time')
provide_evidence(actual_name2, time2)

# END OF STUDENT CODE
report_case()
